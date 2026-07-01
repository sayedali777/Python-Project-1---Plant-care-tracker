from datetime import date, datetime

import pandas as pd

def load_care_log():
     """ 
    this will read all the activities from the care_log csv
     """
     care_log = pd.read_csv('./care_log.csv')
     return care_log 

    
def record_care_activity():
    """Records a new care activity for a plant and saves it to care_log.csv."""
    
    plants = pd.read_csv('./plants.csv')
    
    if len(plants) == 0:
        print('No plants found! Please add a plant first.')
        return
    
    # Show all plants
    print('\nYour plants:')
    print(str(plants[['id','name']]))
    
    # Take input from user
    choice = input('\nEnter the number of the plant you cared for: ')
    
    plant_id = plants.iloc[int(choice) - 1]['id']
    plants_name = plants.iloc[int(choice) - 1]['name']
    
    # Ask for activity
    print('\nActivities:')
    print('1. Watering')
    print('2. Fertilizing')
    print('3. Repotting')
    print('4. Pruning')
    
    activity_status = input('Enter the activity number (1-4): ')
    
    if activity_status == '1':
        activity = 'Watering'
    elif activity_status == '2':
        activity = 'Fertilizing'
    elif activity_status == '3':
        activity = 'Repotting'
    elif activity_status == '4':
        activity = 'Pruning'
    else:
        print('Invalid choice!')
        return
    
    # Record today's date
    today = date.today().strftime('%d-%m-%Y')
    
    # Save to care_log.csv
    new_activity = pd.DataFrame([{
        'plant_id': plant_id,
        'activity': activity,
        'date': today
    }])
    new_activity.to_csv('./care_log.csv', mode='a', header=False, index=False)
    
    # If watering, update last_watered in plants.csv
    if activity == 'Watering':
        plants['last_watered'] = plants['last_watered'].astype(str)
        plants.loc[plants['id'] == plant_id, 'last_watered'] = today
        plants.to_csv('./plants.csv', index=False)
    
    print(f'\n{activity} recorded for {plants_name} on {today}!')

def view_plants_due_for_care():
    """Shows a list of plants that are due for watering based on their watering frequency."""
    
    plants = pd.read_csv('./plants.csv')
    care_log = pd.read_csv('./care_log.csv')
    
    if len(plants) == 0:
        print('No plants found! There are no plants to check.')
        return
    
    print('\n Plants due for care:')
    print('-------------------------')
    
    today = date.today()
    due_plants = []
    
    for i in range(len(plants)):
        plant = plants.iloc[i]
        plant_name = plant['name']
        plant_id = plant['id']
        watering_frequency = int(plant['watering_frequency'])
        last_watered = pd.to_datetime(plant['last_watered'], dayfirst=True).date()
        
        days_since_watered = (today - last_watered).days
        
        if days_since_watered >= watering_frequency:
            due_plants.append(plant_name)
            print(f'{plant_name} (ID: {plant_id}) - last watered {days_since_watered} days ago (every {watering_frequency} days)')
    
    if len(due_plants) == 0:
        print('All plants are up to date!')
    
    print('-------------------------')
    
    
    