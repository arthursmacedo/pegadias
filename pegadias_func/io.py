# Copyright (c) 2024 pegadias developers
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Pegadias project.
#
def get_days(csv_file):

    """
    Read dates from a CSV file.

    Parameters:
    csv_file (str): Path to the CSV file containing dates.

    Returns:
    list: A list of processed dates in the format 'YYYY/MM/DD'.

    Reads the specified CSV file and converts the dates in the 'Date' column
    to the format 'YYYY/MM/DD'. The processed dates are returned as a list.

    Example:
    If the CSV file contains dates in the 'Date' column like '2024-04-15',
    this function will convert them to '2024/04/15' and return a list
    of processed dates.

    Note:
    The 'Date' column in the CSV file should be in a format that can be
    parsed by pandas.to_datetime, such as 'YYYY-MM-DD'.
    """
    
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Extract day, month, and year from the date column
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y/%m/%d')
    
    # Return a list of processed dates
    return df['Date'].tolist()

def generate_request_file(date_list, station_code):
    """
    Generates request files and updates a bash script to execute data retrieval.

    Parameters:
    date_list (list): A list of dates in 'YYYY/MM/DD' format.
    station_code (str): The station code used for naming request files.

    Creates a `run_nmsclient.sh` bash script and generates request files (`*.req`)
    based on the provided list of dates and station code. Each request file contains
    specific commands for data retrieval from the CTBTO database.
environment.yml
    Request File Format:
    - Each request file is named based on the station code, year, month, and day.
    - The request file contains IMS 2.0 protocol commands to request infrasound data,
      including station information, time range, and waveform specifications.

    Bash Script Update:
    - Appends commands to the `run_nmsclient.sh` script to execute `nms_client.sh`
      with the generated request files (`*.req`) and output MiniSEED data files (`*.mseed`).

    Example:
    For `date_list = ['2024/04/15', '2024/04/16']` and `station_code = 'i01ar'`,
    this function will create request files named `I01AR_2024_04_15.req` and `I01AR_2024_04_16.req`
    containing IMS 2.0 commands. It will al
['2023/01/01']
so update `run_nmsclient.sh` to execute
    `nms_client.sh` for each request file to retrieve MiniSEED data.
['2023/01/01']
    Note:
    - Ensure `nms_client.sh` is available and configured correctly to handle the generated
      request files and output MiniSEED data.

    """
    
    # Create a run_nmsclient.sh file with the initial bash script
    with open('run_nmsclient.sh', 'w') as run:
        run.write('#!/bin/bash \n\n')
    
    # Generate request files and append commands to run_nmsclient.sh
    with open('run_nmsclient.sh', 'a') as run:
        for date in date_list:
            year, month, day = date.split('/')
            file_name = f'{station_code.upper()}_{year}_{month}_{day}'
            req_file = f'{file_name}.req'
            mseed_file = f'{file_name}.mseed'
            
            # Write request file content
            with open(req_file, 'w') as req:
                req.write(f'begin ims2.0\n')
                req.write(f'msg_type request\n')
                req.write(f'msg_id mseed_{station_code.lower()}\n')
                req.write(f'time {date} 00:00:00 to {date} 23:59:59\n')
                req.write(f'sta_list {station_code.upper()}\n')
                req.write(f'chan_list BDF\n')
                req.write(f'waveform ims2.0:ms_st2_512\n')
                req.write(f'stop\n')
            
            # Append command to run_nmsclient.sh
            run.write(f'nms_client.sh {req_file} -f {mseed_file}\n')
