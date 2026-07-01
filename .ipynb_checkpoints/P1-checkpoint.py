import pandas as pd

plants = pd.read_csv('./plants.csv')

care = pd.read_csv('./care_log.csv')

def load_plants():
    plants = pd.read_csv('./plants.csv')
    return plants

def add_plant() :
    """ This function asks the user for the plants details then adds the new plant to the csv file """
    ## take user input
    
    name = input('Enter Plant name/species: ')
    location = input('Location in home: ')
    date_acquired = input('Date acquired "Day-Month-Year" : ')
    watering_frequency = input('Watering frequency (in days) :')
    sunlight = input('Sunlight needs (Low, Medium, High) :').capitalize()
    last_watered = input('When was the plant last watered? "Day-Month-Year":')

    ## Checking for errors
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
        new_plant = pd.DataFrame([{'name': name, 'location': location, 'date_acquired': date_acquired, 'watering_frequency': watering_frequency
                                   , 'sunlight': sunlight, 'last_watered': last_watered}])
        new_plant.to_csv('./plants.csv', mode='a', header=False, index=False)
        print(f'{name} has been added to the plants file.')

def main_menu():
    """ main menu for the plant care tracker application """
    print('Welcome to the Plant Care Tracker')
    print('1. Add a new plant to the collection')
    print('2. Record a plant care activity')
    print('3. View plants due for care')
    print('4. Search plants by name or location')
    print('5. View all plants')
    print('6. Exit application')

    choice = input('Please enter your choice to use the application (1-6)')

    if choice == '1':
        add_plant()
    elif choice == '2':
        print('Not yet done')
    elif choice == '3':
        print('Not yet done 2')
    elif choice == '4':
        print('Not yet done 3')
    elif choice == '5':
        print('Not yet done 4')
    elif choice == '6':
        print('Thank you for using this application, Goodbye!')
    else:
        print('Invalid choice, please chose from 1-6')
    
