import pandas as pd
import folium
import webbrowser

# 1. Load the dataset
df = pd.read_csv("C:/Users/acer/Downloads/Lat_long_cities_TamilNadu.csv")

# 2. Pick your native place (e.g., Tirunelveli)
native_name = 'Tirunelveli'
my_native = df[df['Location'] == native_name].iloc[0]

# 3. Create map centered on the middle of Tamil Nadu (Zoom 7 shows the whole state)
tn_map = folium.Map(location=[11.1271, 78.6569], zoom_start=7)

# 4. Add the marker for your native place
folium.Marker(
    location=[my_native['LAT'], my_native['LON']],
    tooltip=f"My Native: {native_name}",
    popup=f"Welcome to {native_name}",
    icon=folium.Icon(color="red", icon="home", prefix="fa")
).add_to(tn_map)

# 5. Save and Open
tn_map.save("tamilnadu_native.html")
webbrowser.open("tamilnadu_native.html")
