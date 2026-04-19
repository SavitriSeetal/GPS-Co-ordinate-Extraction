import os
import exifread
import pandas as pd

def get_decimal_from_dms(dms, ref):
    degrees = float(dms[0].num) / float(dms[0].den)
    minutes = float(dms[1].num) / float(dms[1].den)
    seconds = float(dms[2].num) / float(dms[2].den)

    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def extract_gps(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)
        if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            lat = tags['GPS GPSLatitude']
            lat_ref = tags['GPS GPSLatitudeRef'].values
            lon = tags['GPS GPSLongitude']
            lon_ref = tags['GPS GPSLongitudeRef'].values
            
            lat_decimal = get_decimal_from_dms(lat.values, lat_ref)
            lon_decimal = get_decimal_from_dms(lon.values, lon_ref)
            
            return lat_decimal, lon_decimal
        else:
            return None, None

# Set path to folder with images
folder_path = #Set path
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg'))]

# Extract GPS for each image
gps_data = []
for img in image_files:
    img_path = os.path.join(folder_path, img)
    lat, lon = extract_gps(img_path)
    gps_data.append({'Image': img, 'Latitude': lat, 'Longitude': lon})

# Create DataFrame and display
df = pd.DataFrame(gps_data)
df

df.to_excel("MP_output.xlsx", index=False)

import os
import exifread
import pandas as pd

def get_decimal_from_dms(dms, ref):
    degrees = float(dms[0].num) / float(dms[0].den)
    minutes = float(dms[1].num) / float(dms[1].den)
    seconds = float(dms[2].num) / float(dms[2].den)

    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def extract_gps(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)
        if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            lat = tags['GPS GPSLatitude']
            lat_ref = tags['GPS GPSLatitudeRef'].values
            lon = tags['GPS GPSLongitude']
            lon_ref = tags['GPS GPSLongitudeRef'].values
            
            lat_decimal = get_decimal_from_dms(lat.values, lat_ref)
            lon_decimal = get_decimal_from_dms(lon.values, lon_ref)
            
            return lat_decimal, lon_decimal
        else:
            return None, None

# Set path to folder with images
folder_path = "C:/Rafiqs work/PennDOT 2025/Assignment_21/MP fieldsheet and photos/PHOTOS"  # 🔁 Replace with actual path
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg'))]
  
# Extract GPS for each image
gps_data = []
for img in image_files:
    img_path = os.path.join(folder_path, img)
    lat, lon = extract_gps(img_path)
    gps_data.append({'Image': img, 'Latitude': lat, 'Longitude': lon})

# Create DataFrame
df = pd.DataFrame(gps_data)

# Export to Excel
df.to_excel("MP_output.xlsx", index=False)

print("Exported to MP_output.xlsx'")

df.to_excel(# Set path, index=False)





