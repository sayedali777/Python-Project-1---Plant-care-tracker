plants_f = 'plants.csv'


def view_all_plants():
    try:
        with open(plants_f,mode='r',newline="") as plantfile:
            reader = csv.DictReader(plantfile)
            plants = list(reader)
            if len(plants) == 0:
                print("no plants have been added yet")
                return
            else:
                print('Number of plants found:',len(plants))
                
            

            for plant in plants:
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

    for index,plant in results.iterrows():
        print(f"Plant Name: {plant['name']}")
        print(f"Location: {plant['location']}")
        print(f"Date Acquired: {plant['date_acquired']}")
        print(f"Watering Frequency: {plant['watering_frequency']}")
        print(f"Sunlight: {plant['sunlight']}")
        print(f"Last Watered: {plant['last_watered']}")

        plant_care = care[care['plant_id'] == plant['id']]
        if len(plant_care) == 0:
            print("No care actvities were recorded.")
        else:
            print("Care History:")
            for index,activity in plant_care.iterrows():
                print(f" {activity['activity']} on {activity['date']}")