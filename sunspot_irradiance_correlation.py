import pandas as pd

def clean_sunspots_data(file_path):
    try:
        sunspots_df = pd.read_csv(file_path, delimiter=';', header=None, names=['Year', 'Month', 'Day', 'Decimal_Date', 'Sunspot_Count', 'Other_Column1', 'Other_Column2', 'Other_Column3'])
        sunspots_df = sunspots_df[sunspots_df['Sunspot_Count'] != -1]
        sunspots_df['Date'] = (sunspots_df['Year']*10000 + sunspots_df['Month']*100 + sunspots_df['Day']).astype(int)
        print("Cleaned sunspots data:")
        print(sunspots_df.head())
        return sunspots_df[['Date', 'Sunspot_Count']]
    except Exception as e:
        print(f"Error cleaning sunspots data: {e}")
        return None

def clean_irradiance_data(file_path):
    try:
        irradiance_df = pd.read_csv(file_path, sep='\s+', header=None, names=['Date_Float', 'Julian_Date', 'Decimal_Date', 'Col4', 'Total_Solar_Irradiance', 'Col6', 'Col7', 'Col8', 'Col9', 'Col10', 'Col11', 'Col12', 'Col13', 'Col14', 'Col15'])
        irradiance_df = irradiance_df[irradiance_df['Total_Solar_Irradiance'] != 0]
        irradiance_df['Date'] = irradiance_df['Date_Float'].astype(str).str.split('.').str[0].astype(int)
        print("Cleaned irradiance data:")
        print(irradiance_df.head())
        return irradiance_df[['Date', 'Total_Solar_Irradiance']]
    except Exception as e:
        print(f"Error cleaning irradiance data: {e}")
        return None

def calculate_correlation(sunspots_file, irradiance_file):
    sunspots_df = clean_sunspots_data(sunspots_file)
    irradiance_df = clean_irradiance_data(irradiance_file)
    if sunspots_df is None or irradiance_df is None:
        return None

    try:
        merged_df = pd.merge(sunspots_df, irradiance_df, on='Date')
        print("Merged data:")
        print(merged_df.head())
        correlation = merged_df['Sunspot_Count'].corr(merged_df['Total_Solar_Irradiance'])
        return correlation
    except Exception as e:
        print(f"Error merging datasets or calculating correlation: {e}")
        return None

sunspots_file = '/Users/navadeepbudda/Downloads/SN_d_tot_V2.0.csv'
irradiance_file = '/Users/navadeepbudda/Downloads/sorce_tsi_L3_c24h_latest.txt'

correlation = calculate_correlation(sunspots_file, irradiance_file)
if correlation is not None:
    print(f"The correlation between the number of sunspots and total solar irradiance is {correlation:.4f}")
else:
    print("Failed to calculate correlation due to previous errors.")

sunspots_file = '/Users/navadeepbudda/Downloads/SN_d_tot_V2.0.csv'
irradiance_file = '/Users/navadeepbudda/Downloads/sorce_tsi_L3_c24h_latest.txt'