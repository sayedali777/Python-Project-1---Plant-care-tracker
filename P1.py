import pandas as pd

import uuid

plants = pd.read_csv('./plants.csv')

care = pd.read_csv('./care_log.csv')

def load_plants():
    plants = pd.read_csv('./plants.csv')
    return plants

def add_plant() :
    """ This function asks the user for the plants details then adds the new plant to the csv file """

    confirm = input("Press Enter to continue or 'b' to go back: ")
    if confirm.lower() == 'b':
        return
    ## take user input
    
    name = input('Enter Plant name/species: ')
    location = input('Location in home: ')
    date_acquired = input('Date acquired "Day-Month-Year" : ')
    watering_frequency = input('Watering frequency (in days) :')
    sunlight = input('Sunlight needs (Low, Medium, High) :').capitalize()
    last_watered = input('When was the plant last watered? "Day-Month-Year":')

    
    if name == '':
        print('Please enter plant name, cannot be empty!')
    elif location == '':
        print('Check location, cannot be empty!')
    elif len(date_acquired) != 10:
        print('Please follow this format for date acquired "Day-Month-Year", should be exactly 10 char. example: 01-01-2026')
    elif watering_frequency == '':
        print('Check watering, cannot be empty!')
    elif sunlight not in ['Low','Medium','High']:
        print('Check sunlight, it must be Low, Medium or High !')
    elif len(last_watered) != 10:
        print('Please follow this format for last watered "Day-Month-Year", should be exactly 10 char. example: 01-01-2026')
    else :
        plant_id = str(uuid.uuid4())
        new_plant = pd.DataFrame([{'id': plant_id, 'name': name, 'location': location, 'date_acquired': date_acquired, 'watering_frequency': watering_frequency
                                   , 'sunlight': sunlight, 'last_watered': last_watered}])
        new_plant.to_csv('./plants.csv', mode='a', header=False, index=False)
        print(f'{name} has been added to the plants file with id: {plant_id}.')
        
    

def add_photo():
    confirm = input("Press Enter to continue or 'b' to go back: ")
    if confirm.lower() == 'b':
        return    
    plants = pd.read_csv('./plants.csv')
    
    if len(plants) == 0:
        print('No plants found! Please add a plant first.')
        return
    
    print('\nYour plants:')
    for i in range(len(plants)):
        plant = plants.iloc[i]
        print(f"{i+1}. {plant['name']} (ID: {plant['id']})")
    
    plant_id = input('\nEnter the plant ID to add a photo: ')
    
    if plant_id not in plants['id'].values:
        print(f"Plant ID '{plant_id}' not found!")
        return
    
    photo_path = input('Enter the photo file path (e.g. /photos/rose.jpg): ')
    
    if photo_path == '':
        print('Photo path cannot be empty.')
        return
    
    plants['photo_path'] = plants['photo_path'].astype(str)
    
    plants.loc[plants['id'] == plant_id, 'photo_path'] = photo_path
    plants.to_csv('./plants.csv', index=False)
    print('Photo added successfully!')
    
