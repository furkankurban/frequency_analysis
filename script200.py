import pandas as pd
import os

base_path = 'Z:\\2024\son\\'
result_df_all = pd.DataFrame({'time': range(24)})
result_df_cloud = pd.DataFrame({'time': range(24)})
result_df_rvr = pd.DataFrame({'time': range(24)})

for i in range(1, 32): 
    filename_cloud = f"CLOUD_ALL_{i:02d}.his"
    filename_rvr = f"RVR_1_{i:02d}.his"
    if not os.path.exists(filename_cloud) or not os.path.exists(filename_rvr):
        print(f"Dosya eksik: {filename_cloud} veya {filename_rvr} mevcut değil, Gün sayısı 31'den azsa ciddiye almayınız.")
        continue
    
    with open(filename_cloud, "r") as file:
        data_cloud = file.read().replace('"', '')
    with open("temp_file_cloud.his", "w") as file:
        file.write(data_cloud)
    df_cloud = pd.read_csv("temp_file_cloud.his", sep="\t", skiprows=1)
    df_cloud['CREATEDATE'] = pd.to_datetime(df_cloud['CREATEDATE'])
    for column in ['BASE1 (FT)', 'BASE2 (FT)', 'BASE3 (FT)', 'BASE4 (FT)']:
        df_cloud[column] = pd.to_numeric(df_cloud[column], errors='coerce')
    
    with open(filename_rvr, "r") as file:
        data_rvr = file.read().replace('"', '')
    with open("temp_file_rvr.his", "w") as file:
        file.write(data_rvr)
    df_rvr = pd.read_csv("temp_file_rvr.his", sep="\t", skiprows=1)
    df_rvr['CREATEDATE'] = pd.to_datetime(df_rvr['CREATEDATE'])
    df_rvr['RVR_1A'] = pd.to_numeric(df_rvr['RVR_1A'], errors='coerce')
    
    df_combined = pd.merge(df_cloud, df_rvr, on='CREATEDATE', suffixes=('_cloud', '_rvr'))
    
    result_df_all[f'frequency_{i:02d}'] = result_df_all['time'].apply(lambda hour: 
        df_combined[(df_combined['CREATEDATE'].dt.hour == hour) & 
                    ((df_combined['BASE1 (FT)'] < 200) | 
                     (df_combined['BASE2 (FT)'] < 200) | 
                     (df_combined['BASE3 (FT)'] < 200) | 
                     (df_combined['BASE4 (FT)'] < 200)) &
                    (df_combined['RVR_1A'] < 200)
                   ].shape[0])
    result_df_cloud[f'frequency_{i:02d}'] = result_df_cloud['time'].apply(lambda hour: 
        df_cloud[(df_cloud['CREATEDATE'].dt.hour == hour) & 
                    ((df_cloud['BASE1 (FT)'] < 200) | 
                     (df_cloud['BASE2 (FT)'] < 200) | 
                     (df_cloud['BASE3 (FT)'] < 200) | 
                     (df_cloud['BASE4 (FT)'] < 200))
                    ].shape[0])
    result_df_rvr[f'frequency_{i:02d}'] = result_df_rvr['time'].apply(lambda hour: 
        df_rvr[(df_rvr['CREATEDATE'].dt.hour == hour) &  
                    ((df_rvr['RVR_1A'] < 200))
                    ].shape[0])
    os.remove("temp_file_cloud.his")
    os.remove("temp_file_rvr.his")

result_df_all.to_excel('frequency_by_hour_cloud200_rvr200.xlsx', index=False)
result_df_cloud.to_excel('frequency_by_hour_cloud200.xlsx', index=False)
result_df_rvr.to_excel('frequency_by_hour_rvr200.xlsx', index=False)

result_df_all = pd.DataFrame({'time': range(24)})
result_df_cloud = pd.DataFrame({'time': range(24)})
result_df_rvr = pd.DataFrame({'time': range(24)})

for i in range(1, 32): 
    filename_cloud = f"CLOUD_ALL_{i:02d}.his"
    filename_rvr = f"RVR_1_{i:02d}.his"
    if not os.path.exists(filename_cloud) or not os.path.exists(filename_rvr):
        print(f"Dosya eksik: {filename_cloud} veya {filename_rvr} mevcut değil, Gün sayısı 31'den azsa ciddiye almayınız.")
        continue
     
    with open(filename_cloud, "r") as file:
        data_cloud = file.read().replace('"', '')
    with open("temp_file_cloud.his", "w") as file:
        file.write(data_cloud)
    df_cloud = pd.read_csv("temp_file_cloud.his", sep="\t", skiprows=1)
    df_cloud['CREATEDATE'] = pd.to_datetime(df_cloud['CREATEDATE'])
    for column in ['BASE1 (FT)', 'BASE2 (FT)', 'BASE3 (FT)', 'BASE4 (FT)']:
        df_cloud[column] = pd.to_numeric(df_cloud[column], errors='coerce')
    
    with open(filename_rvr, "r") as file:
        data_rvr = file.read().replace('"', '')
    with open("temp_file_rvr.his", "w") as file:
        file.write(data_rvr)
    df_rvr = pd.read_csv("temp_file_rvr.his", sep="\t", skiprows=1)
    df_rvr['CREATEDATE'] = pd.to_datetime(df_rvr['CREATEDATE'])
    df_rvr['RVR_1A'] = pd.to_numeric(df_rvr['RVR_1A'], errors='coerce')
    
    df_combined = pd.merge(df_cloud, df_rvr, on='CREATEDATE', suffixes=('_cloud', '_rvr'))
    
    result_df_all[f'frequency_{i:02d}'] = result_df_all['time'].apply(lambda hour: 
        df_combined[(df_combined['CREATEDATE'].dt.hour == hour) & 
                    ((df_combined['BASE1 (FT)'] < 500) | 
                     (df_combined['BASE2 (FT)'] < 500) | 
                     (df_combined['BASE3 (FT)'] < 500) | 
                     (df_combined['BASE4 (FT)'] < 500)) &
                    (df_combined['RVR_1A'] < 500)
                   ].shape[0])
    result_df_cloud[f'frequency_{i:02d}'] = result_df_cloud['time'].apply(lambda hour: 
        df_cloud[(df_cloud['CREATEDATE'].dt.hour == hour) & 
                    ((df_cloud['BASE1 (FT)'] < 500) | 
                     (df_cloud['BASE2 (FT)'] < 500) | 
                     (df_cloud['BASE3 (FT)'] < 500) | 
                     (df_cloud['BASE4 (FT)'] < 500))
                    ].shape[0])
    result_df_rvr[f'frequency_{i:02d}'] = result_df_rvr['time'].apply(lambda hour: 
        df_rvr[(df_rvr['CREATEDATE'].dt.hour == hour) &  
                    ((df_rvr['RVR_1A'] < 500))
                    ].shape[0])
    os.remove("temp_file_cloud.his")
    os.remove("temp_file_rvr.his")

result_df_all.to_excel('frequency_by_hour_cloud500_rvr500.xlsx', index=False)
result_df_cloud.to_excel('frequency_by_hour_cloud500.xlsx', index=False)
result_df_rvr.to_excel('frequency_by_hour_rvr500.xlsx', index=False)

result_df_all = pd.DataFrame({'time': range(24)})
result_df_cloud = pd.DataFrame({'time': range(24)})
result_df_rvr = pd.DataFrame({'time': range(24)})

for i in range(1, 32): 
    filename_cloud = f"CLOUD_ALL_{i:02d}.his"
    filename_rvr = f"RVR_1_{i:02d}.his"
    if not os.path.exists(filename_cloud) or not os.path.exists(filename_rvr):
        print(f"Dosya eksik: {filename_cloud} veya {filename_rvr} mevcut değil, Gün sayısı 31'den azsa ciddiye almayınız.")
        continue
       
    with open(filename_cloud, "r") as file:
        data_cloud = file.read().replace('"', '')
    with open("temp_file_cloud.his", "w") as file:
        file.write(data_cloud)
    df_cloud = pd.read_csv("temp_file_cloud.his", sep="\t", skiprows=1)
    df_cloud['CREATEDATE'] = pd.to_datetime(df_cloud['CREATEDATE'])
    for column in ['BASE1 (FT)', 'BASE2 (FT)', 'BASE3 (FT)', 'BASE4 (FT)']:
        df_cloud[column] = pd.to_numeric(df_cloud[column], errors='coerce')
    
    with open(filename_rvr, "r") as file:
        data_rvr = file.read().replace('"', '')
    with open("temp_file_rvr.his", "w") as file:
        file.write(data_rvr)
    df_rvr = pd.read_csv("temp_file_rvr.his", sep="\t", skiprows=1)
    df_rvr['CREATEDATE'] = pd.to_datetime(df_rvr['CREATEDATE'])
    df_rvr['RVR_1A'] = pd.to_numeric(df_rvr['RVR_1A'], errors='coerce')
    
    df_combined = pd.merge(df_cloud, df_rvr, on='CREATEDATE', suffixes=('_cloud', '_rvr'))
    
    result_df_all[f'frequency_{i:02d}'] = result_df_all['time'].apply(lambda hour: 
        df_combined[(df_combined['CREATEDATE'].dt.hour == hour) & 
                    ((df_combined['BASE1 (FT)'] < 1000) | 
                     (df_combined['BASE2 (FT)'] < 1000) | 
                     (df_combined['BASE3 (FT)'] < 1000) | 
                     (df_combined['BASE4 (FT)'] < 1000)) &
                    (df_combined['RVR_1A'] < 800)
                   ].shape[0])
    result_df_cloud[f'frequency_{i:02d}'] = result_df_cloud['time'].apply(lambda hour: 
        df_cloud[(df_cloud['CREATEDATE'].dt.hour == hour) & 
                    ((df_cloud['BASE1 (FT)'] < 1000) | 
                     (df_cloud['BASE2 (FT)'] < 1000) | 
                     (df_cloud['BASE3 (FT)'] < 1000) | 
                     (df_cloud['BASE4 (FT)'] < 1000))
                    ].shape[0])
    result_df_rvr[f'frequency_{i:02d}'] = result_df_rvr['time'].apply(lambda hour: 
        df_rvr[(df_rvr['CREATEDATE'].dt.hour == hour) &  
                    ((df_rvr['RVR_1A'] < 800))
                    ].shape[0])
    os.remove("temp_file_cloud.his")
    os.remove("temp_file_rvr.his")

result_df_all.to_excel('frequency_by_hour_cloud1000_rvr800.xlsx', index=False)
result_df_cloud.to_excel('frequency_by_hour_cloud1000.xlsx', index=False)
result_df_rvr.to_excel('frequency_by_hour_rvr800.xlsx', index=False)

result_df_all = pd.DataFrame({'time': range(24)})
result_df_cloud = pd.DataFrame({'time': range(24)})
result_df_rvr = pd.DataFrame({'time': range(24)})

for i in range(1, 32): 
    filename_cloud = f"CLOUD_ALL_{i:02d}.his"
    filename_rvr = f"RVR_1_{i:02d}.his"
    if not os.path.exists(filename_cloud) or not os.path.exists(filename_rvr):
        print(f"Dosya eksik: {filename_cloud} veya {filename_rvr} mevcut değil, Gün sayısı 31'den azsa ciddiye almayınız.")
        continue
      
    with open(filename_cloud, "r") as file:
        data_cloud = file.read().replace('"', '')
    with open("temp_file_cloud.his", "w") as file:
        file.write(data_cloud)
    df_cloud = pd.read_csv("temp_file_cloud.his", sep="\t", skiprows=1)
    df_cloud['CREATEDATE'] = pd.to_datetime(df_cloud['CREATEDATE'])
    for column in ['BASE1 (FT)', 'BASE2 (FT)', 'BASE3 (FT)', 'BASE4 (FT)']:
        df_cloud[column] = pd.to_numeric(df_cloud[column], errors='coerce')
    
    with open(filename_rvr, "r") as file:
        data_rvr = file.read().replace('"', '')
    with open("temp_file_rvr.his", "w") as file:
        file.write(data_rvr)
    df_rvr = pd.read_csv("temp_file_rvr.his", sep="\t", skiprows=1)
    df_rvr['CREATEDATE'] = pd.to_datetime(df_rvr['CREATEDATE'])
    df_rvr['RVR_1A'] = pd.to_numeric(df_rvr['RVR_1A'], errors='coerce')
    
    df_combined = pd.merge(df_cloud, df_rvr, on='CREATEDATE', suffixes=('_cloud', '_rvr'))
    
    result_df_all[f'frequency_{i:02d}'] = result_df_all['time'].apply(lambda hour: 
        df_combined[(df_combined['CREATEDATE'].dt.hour == hour) & 
                    ((df_combined['BASE1 (FT)'] < 1500) | 
                     (df_combined['BASE2 (FT)'] < 1500) | 
                     (df_combined['BASE3 (FT)'] < 1500) | 
                     (df_combined['BASE4 (FT)'] < 1500)) &
                    (df_combined['RVR_1A'] < 1000)
                   ].shape[0])
    result_df_cloud[f'frequency_{i:02d}'] = result_df_cloud['time'].apply(lambda hour: 
        df_cloud[(df_cloud['CREATEDATE'].dt.hour == hour) & 
                    ((df_cloud['BASE1 (FT)'] < 1500) | 
                     (df_cloud['BASE2 (FT)'] < 1500) | 
                     (df_cloud['BASE3 (FT)'] < 1500) | 
                     (df_cloud['BASE4 (FT)'] < 1500))
                    ].shape[0])
    result_df_rvr[f'frequency_{i:02d}'] = result_df_rvr['time'].apply(lambda hour: 
        df_rvr[(df_rvr['CREATEDATE'].dt.hour == hour) &  
                    ((df_rvr['RVR_1A'] < 1000))
                    ].shape[0])
    os.remove("temp_file_cloud.his")
    os.remove("temp_file_rvr.his")

result_df_all.to_excel('frequency_by_hour_cloud1500_rvr1000.xlsx', index=False)
result_df_cloud.to_excel('frequency_by_hour_cloud1500.xlsx', index=False)
result_df_rvr.to_excel('frequency_by_hour_rvr1000.xlsx', index=False)

result_df_all = pd.DataFrame({'time': range(24)})
result_df_cloud = pd.DataFrame({'time': range(24)})
result_df_rvr = pd.DataFrame({'time': range(24)})

for i in range(1, 32): 
    filename_cloud = f"CLOUD_ALL_{i:02d}.his"
    filename_rvr = f"RVR_1_{i:02d}.his"
    if not os.path.exists(filename_cloud) or not os.path.exists(filename_rvr):
        print(f"Dosya eksik: {filename_cloud} veya {filename_rvr} mevcut değil, Gün sayısı 31'den azsa ciddiye almayınız.")
        continue
       
    with open(filename_cloud, "r") as file:
        data_cloud = file.read().replace('"', '')
    with open("temp_file_cloud.his", "w") as file:
        file.write(data_cloud)
    df_cloud = pd.read_csv("temp_file_cloud.his", sep="\t", skiprows=1)
    df_cloud['CREATEDATE'] = pd.to_datetime(df_cloud['CREATEDATE'])
    for column in ['BASE1 (FT)', 'BASE2 (FT)', 'BASE3 (FT)', 'BASE4 (FT)']:
        df_cloud[column] = pd.to_numeric(df_cloud[column], errors='coerce')
    
    with open(filename_rvr, "r") as file:
        data_rvr = file.read().replace('"', '')
    with open("temp_file_rvr.his", "w") as file:
        file.write(data_rvr)
    df_rvr = pd.read_csv("temp_file_rvr.his", sep="\t", skiprows=1)
    df_rvr['CREATEDATE'] = pd.to_datetime(df_rvr['CREATEDATE'])
    df_rvr['RVR_10A'] = pd.to_numeric(df_rvr['RVR_10A'], errors='coerce')
    
    df_combined = pd.merge(df_cloud, df_rvr, on='CREATEDATE', suffixes=('_cloud', '_rvr'))
    
    result_df_all[f'frequency_{i:02d}'] = result_df_all['time'].apply(lambda hour: 
        df_combined[(df_combined['CREATEDATE'].dt.hour == hour) & 
                    ((df_combined['BASE1 (FT)'] < 3000) | 
                     (df_combined['BASE2 (FT)'] < 3000) | 
                     (df_combined['BASE3 (FT)'] < 3000) | 
                     (df_combined['BASE4 (FT)'] < 3000)) &
                    (df_combined['RVR_10A'] < 5000)
                   ].shape[0])
    result_df_cloud[f'frequency_{i:02d}'] = result_df_cloud['time'].apply(lambda hour: 
        df_cloud[(df_cloud['CREATEDATE'].dt.hour == hour) & 
                    ((df_cloud['BASE1 (FT)'] < 3000) | 
                     (df_cloud['BASE2 (FT)'] < 3000) | 
                     (df_cloud['BASE3 (FT)'] < 3000) | 
                     (df_cloud['BASE4 (FT)'] < 3000))
                    ].shape[0])
    result_df_rvr[f'frequency_{i:02d}'] = result_df_rvr['time'].apply(lambda hour: 
        df_rvr[(df_rvr['CREATEDATE'].dt.hour == hour) &  
                    ((df_rvr['RVR_10A'] < 5000))
                    ].shape[0])
    os.remove("temp_file_cloud.his")
    os.remove("temp_file_rvr.his")

result_df_all.to_excel('frequency_by_hour_cloud3000_rvr5000.xlsx', index=False)
result_df_cloud.to_excel('frequency_by_hour_cloud3000.xlsx', index=False)
result_df_rvr.to_excel('frequency_by_hour_rvr5000.xlsx', index=False)
