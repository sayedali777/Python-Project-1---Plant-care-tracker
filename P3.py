from P1 import *
from P2 import *
import pandas as pd
plants_f = 'plants.csv'


def view_all_plants():
    """Displays all plants in the collection."""
    try:
        plants = pd.read_csv('./plants.csv')
        if len(plants) == 0:
            print("no plants have been added yet")
            return
        else:
            print('Number of plants found:', len(plants))
        for i in range(len(plants)):
            plant = plants.iloc[i]
            print('\n-----Plant Details-----')
            print(f"Name: {plant['name']}")
            print(f"Location: {plant['location']}")
            print(f"Date Acquired: {plant['date_acquired']}")
            print(f"Watering Frequency: {plant['watering_frequency']}")
            print(f"Sunlight: {plant['sunlight']}")
            print(f"Last Watered: {plant['last_watered']}")
    except FileNotFoundError:
        print("File not found, please add a plant")
    except Exception as error:
        print("Error add a plant", error)

def search_all():
    """Searches for plants by name or location and displays their care details."""
    plants = pd.read_csv('./plants.csv')
    care = pd.read_csv('./care_log.csv')
    
    if len(plants) == 0:
        print("No plants have been found!")
        return
    
    searchinput = input("\nEnter a plant name or location:").lower()
    
    if searchinput == "":
        print("Error! Search input cannot be empty.")
        return
    
    results = plants[(plants['name'].str.lower().str.contains(searchinput)) | (plants['location'].str.lower().str.contains(searchinput))]
    
    if len(results) == 0:
        print(f"No plant found matching {searchinput}")
        return        
    
    print(f"Number of plants matching {searchinput} is {len(results)}:")
    
    for i in range(len(results)):
        plant = results.iloc[i]
        print(f"Plant Name: {plant['name']}")
        print(f"Location: {plant['location']}")
        print(f"Date Acquired: {plant['date_acquired']}")
        print(f"Watering Frequency: {plant['watering_frequency']}")
        print(f"Sunlight: {plant['sunlight']}")
        print(f"Last Watered: {plant['last_watered']}")
        
        plant_care = care[care['plant_id'] == plant['id']]
        
        if len(plant_care) == 0:
            print("No care activities were recorded.")
        else:
            print("Care History:")
            for j in range(len(plant_care)):
                activity = plant_care.iloc[j]
                print(f" {activity['activity']} on {activity['date']}")

def main_menu():
    """ main menu for the plant care tracker application """
    print('Welcome to the Plant Care Tracker')
    print('1. Add a new plant to the collection')
    print('2. Record a plant care activity')
    print('3. View plants due for care')
    print('4. Search plants by name or location')
    print('5. View all plants')
    print('6. Exit application')
    print('7. Add photo to a plant.')

    choice = input('Please enter your choice to use the application (1-7)')

    if choice == '1':
        add_plant()
    elif choice == '2':
        record_care_activity()
    elif choice == '3':
        view_plants_due_for_care()
    elif choice == '4':
        search_all()
    elif choice == '5':
        view_all_plants()
    elif choice == '6':
        print('Thank you for using this application, Goodbye!')
    elif choice == '7':
        add_photo()
    else:
        print('Invalid choice, please chose from 1-7')