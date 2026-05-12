import pandas as pd
import folium
import webbrowser
import os

# 1. Load the dataset
# Make sure 'worldcities.csv' is in your project folder
df = pd.read_csv("C:/Users/acer/Downloads/worldcities.csv")

# 2. Select a "Small Amount" (Top 100 cities by population)
# We sort by population and take the top 100 to keep the map fast
small_df = df.sort_values(by='population', ascending=False).head(20)

# 3. Create the World Map
m = folium.Map(location=[20, 0], zoom_start=2, tiles="OpenStreetMap")


for index, row in small_df.iterrows():
    # Variables for cleaner code
    city = row['city']
    lat = row['lat']
    lon = row['lng'] # Note: standard Kaggle worldcities use 'lng'
    pop = int(row['population'])

    
    popup_text = f"""
    <b>City:</b> {city}<br>
    <b>Lat:</b> {lat}<br>
    <b>Lon:</b> {lon}<br>
    <b>Population:</b> {pop:,}
    """

    folium.Marker(
        location=[lat, lon],
        tooltip=city,           # Hover effect
        popup=folium.Popup(popup_text, max_width=200), # Click effect
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 5. Save and Open automatically
file_name = "world_small_map.html"
m.save(file_name)
webbrowser.open('file://' + os.path.realpath(file_name))

print(f"Success! Map with {len(small_df)} cities created.")
