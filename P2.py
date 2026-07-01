from datetime import date, datetime

def load_care_log():
     """ 
    this will read all the activities from the care_log csv
     """
     care_log = pd.read_csv('.care_log.csv')
     return care_log 

    
def record_care_activity():
    """
    will record new care activity
    """
    plants = pd.read_csv('./plants.csv')

    if len(plants) == 0:
        print('No plants found! Please add a plant first.')
        return

    """
    Show all plants
    """
    print('\n Your plants:')
    print(str(plants[['id','name']]))

    """
    Take the input from user
    """
    plants_name = input('\nEnter the name of the plant you cared for:')

    plant_id = plants[plants['name'] == plant_name]['id'].values[0]

    """
    checking in the plant exists
    """
    if plants_name not in plants['name'].values:
        print(f' Plant {plants_name} not found!')
        return

    """
    Asking for the plant recent activity
    """
    print('\n Activities:')
    print('1. Watering')
    print('2. Fertilizing')
    print('3. Repotting')
    print('4. Pruning')

    activity_status = input('Enter the activity number [1-4]:')

    if activity_status == '1':
        activity = 'Watering'
    elif activity_status == '2':
        activity = 'Fertilizing'
    elif activity_status == '3':
        activity = 'Repotting'
    elif activity_status == '4':
        activity = 'Pruning'
    else:
        print(' Invalid choice!')
        return

    """
    Recording today date
    """
    today = date.today().strftime('%d-%m-%Y')

    """
    save to the care_log.csv
    """
    new_activity = pd.DataFrame([
        {
            'plant_id': plants_id,
            'activity': activity,
            'date': today
        }])

    new_activity.to_csv('./care_log.csv', mode='a', header=False, index=False)

    print(f"\n {activity} recorded for {plant_name} id: {plant_id} on {today}!")


def view_plants_due_for_care():
    """
    Show the list of the plan that are due for watering based on their watering frequency
    """

    plants = pd.read_csv('./plants.csv')
    care_log = pd.read_csv('./care_log.csv')

    if len(plants) == 0:
        print('No plants found! There are no plants to check.')
        return
    """
    Display the title 
    """
    print('\n Plants due for care:')
    print('-------------------------')

    """
    get today date and create an empty list 
    """
    today = date.today()
    due_plants = []
    """
    Check for each plant and get the plant information
    """
    for i in range(len(plants)):
        plants = plants.iloc[i]
        plants_name = plants['name']
        watering_frequency = int(plants['watering_frequency'])
        last_watered = pd.to_datetime(plants['last_watered'], dayfirst=True).date()

    """
    calculating the days since last watered
    """

    days_since_watered = (today - last_watered).days

    if days_since_watered >= watering_frequency:
            due_plants.append(plants_name)
            print(f' {plants_name} - last watered {days_since_watered} days ago (every {watering_frequency} days)')

    if len(due_plants) == 0:
        print('All plants are up to date!')
        print('-------------------------')
    
    
    