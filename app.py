import streamlit as st
import pandas as pd
import uuid
from datetime import date

# ─── Page Config ───
st.set_page_config(page_title="Plant Care Tracker", layout="wide")
st.title("Plant Care Tracker")

# ─── Sidebar Menu ───
menu = st.sidebar.selectbox(
    "Choose an option",
    [
        "View All Plants",
        "Add a New Plant",
        "Record Care Activity",
        "View Plants Due for Care",
        "Search Plants",
        "Add Photo to Plant"
    ]
)

# ─── View All Plants ───
if menu == "View All Plants":
    st.header("All Plants")
    plants = pd.read_csv('./plants.csv')
    if len(plants) == 0:
        st.warning("No plants found! Please add a plant first.")
    else:
        st.dataframe(plants)

# ─── Add a New Plant ───
elif menu == "Add a New Plant":
    st.header("Add a New Plant")
    
    name = st.text_input("Plant name/species")
    location = st.text_input("Location in home")
    date_acquired = st.text_input("Date acquired (DD-MM-YYYY)")
    watering_frequency = st.text_input("Watering frequency (in days)")
    sunlight = st.selectbox("Sunlight needs", ["Low", "Medium", "High"])
    last_watered = st.text_input("Last watered date (DD-MM-YYYY)")
    
    if st.button("Add Plant"):
        if name == "":
            st.error("Plant name cannot be empty.")
        elif location == "":
            st.error("Location cannot be empty.")
        elif len(date_acquired) != 10:
            st.error("Invalid date. Please use DD-MM-YYYY format.")
        elif watering_frequency == "":
            st.error("Watering frequency cannot be empty.")
        elif len(last_watered) != 10:
            st.error("Invalid last watered date. Please use DD-MM-YYYY format.")
        else:
            plant_id = str(uuid.uuid4())
            new_plant = pd.DataFrame([{
                'id': plant_id,
                'name': name,
                'location': location,
                'date_acquired': date_acquired,
                'watering_frequency': watering_frequency,
                'sunlight': sunlight,
                'last_watered': last_watered,
                'photo_path': ''
            }])
            new_plant.to_csv('./plants.csv', mode='a', header=False, index=False)
            st.success(f"{name} has been added successfully!")

# ─── Record Care Activity ───
elif menu == "Record Care Activity":
    st.header("Record Care Activity")
    
    plants = pd.read_csv('./plants.csv')
    
    if len(plants) == 0:
        st.warning("No plants found! Please add a plant first.")
    else:
        plant_names = plants['name'].tolist()
        selected_name = st.selectbox("Select a plant", plant_names)
        activity = st.selectbox("Activity", ["Watering", "Fertilizing", "Repotting", "Pruning"])
        
        if st.button("Record Activity"):
            plant_id = plants[plants['name'] == selected_name]['id'].values[0]
            today = date.today().strftime("%d-%m-%Y")
            
            new_activity = pd.DataFrame([{
                'plant_id': plant_id,
                'activity': activity,
                'date': today
            }])
            new_activity.to_csv('./care_log.csv', mode='a', header=False, index=False)
            
            # If watering update last_watered in plants.csv
            if activity == "Watering":
                plants['last_watered'] = plants['last_watered'].astype(str)
                plants.loc[plants['id'] == plant_id, 'last_watered'] = today
                plants.to_csv('./plants.csv', index=False)
            
            st.success(f"{activity} recorded for {selected_name} on {today}!")

# ─── View Plants Due for Care ───
elif menu == "View Plants Due for Care":
    st.header("Plants Due for Care")
    
    plants = pd.read_csv('./plants.csv')
    
    if len(plants) == 0:
        st.warning("No plants found!")
    else:
        today = date.today()
        due_plants = []
        
        for i in range(len(plants)):
            plant = plants.iloc[i]
            watering_frequency = int(plant['watering_frequency'])
            last_watered = pd.to_datetime(plant['last_watered'], dayfirst=True).date()
            days_since_watered = (today - last_watered).days
            
            if days_since_watered >= watering_frequency:
                due_plants.append({
                    'Name': plant['name'],
                    'Location': plant['location'],
                    'Days Since Watered': days_since_watered,
                    'Watering Frequency': watering_frequency
                })
        
        if len(due_plants) == 0:
            st.success("All plants are up to date!")
        else:
            st.dataframe(pd.DataFrame(due_plants))

# ─── Search Plants ───
elif menu == "Search Plants":
    st.header("Search Plants")
    
    search_term = st.text_input("Enter plant name or location")
    
    if st.button("Search"):
        plants = pd.read_csv('./plants.csv')
        care = pd.read_csv('./care_log.csv')
        
        if search_term == "":
            st.error("Search term cannot be empty.")
        else:
            results = plants[
                (plants['name'].str.lower().str.contains(search_term.lower())) |
                (plants['location'].str.lower().str.contains(search_term.lower()))
            ]
            
            if len(results) == 0:
                st.warning(f"No plants found matching '{search_term}'")
            else:
                st.write(f"Found {len(results)} plant(s) matching '{search_term}':")
                st.dataframe(results)
                
                # Show care history for each result
                st.subheader("Care History")
                for i in range(len(results)):
                    plant = results.iloc[i]
                    plant_care = care[care['plant_id'] == plant['id']]
                    st.write(f"**{plant['name']}**")
                    if len(plant_care) == 0:
                        st.write("No care activities recorded yet.")
                    else:
                        st.dataframe(plant_care[['activity', 'date']])

# ─── Add Photo ───
elif menu == "Add Photo to Plant":
    st.header("Add Photo to Plant")
    
    plants = pd.read_csv('./plants.csv')
    
    if len(plants) == 0:
        st.warning("No plants found! Please add a plant first.")
    else:
        plant_names = plants['name'].tolist()
        selected_name = st.selectbox("Select a plant", plant_names)
        photo_path = st.text_input("Enter photo file path (e.g. /photos/rose.jpg)")
        
        if st.button("Add Photo"):
            if photo_path == "":
                st.error("Photo path cannot be empty.")
            else:
                plants['photo_path'] = plants['photo_path'].astype(str)
                plant_id = plants[plants['name'] == selected_name]['id'].values[0]
                plants.loc[plants['id'] == plant_id, 'photo_path'] = photo_path
                plants.to_csv('./plants.csv', index=False)
                st.success(f"Photo added for {selected_name}!")