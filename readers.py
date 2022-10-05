import os
import pandas as pd

def read_tc_data(file_path, cols=None):
    """
    Read the thermocouple (TC) temperature data where the time values are excluded and the temperature values 
    are returned.
    
    Parameters
    ----------
    file_path : string
        Path to the thermocouple data file(s)
        
    Returns
    -------
    List of dicts
        'file': string
        'data': pandas DataFrames
    Each dict contains the temperature data from each file read.     
    
    
    """
    
    temp_data = []
    for filename in os.listdir(file_path):
        f = os.path.join(file_path, filename)
        all_data = pd.read_csv(f)
        temp_data_keys = [k for k in all_data.keys() if 'time' not in k.lower()]
        temp_data.append({
            'file': filename,
            'temperature': all_data[temp_data_keys]
        }
        )
        
    return temp_data