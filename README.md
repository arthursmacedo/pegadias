
![banner](https://github.com/arthursmacedo/pegadias/assets/74022263/56651b96-94d2-46ca-9585-5ca139d42a86)

Infrasound Analysis Tool

This Python program is designed to retrieve and process infrasound data from the Comprehensive Nuclear-Test-Ban Treaty Organization (CTBTO) database for analysis. The provided script run_infrasound_analysis.py allows for the creation of request files (*.req) based on specified station IDs and dates, and then executes these requests using the nms_client.sh script to obtain raw data in MiniSEED format (*.mseed).
Requirements

    Python 3.x
    Access to CTBTO API for data retrieval

Setup

    Clone the repository:

    bash

git clone https://github.com/your_username/infrasound-analysis.git
cd infrasound-analysis

Install required dependencies:

bash

    pip install requests

    Obtain an API key from the CTBTO Preparatory Commission to access their data.

Usage

    Data Retrieval Script: run_infrasound_analysis.py
        This script reads a list of dates from a CSV file (viena.csv) and generates request files (*.req) for specified infrasound stations and dates.
        Usage:

        bash

    python run_infrasound_analysis.py

Generated Requests

    Request files (*.req) will be created for each specified station and date, containing necessary information to retrieve infrasound data.

Data Retrieval

    Execute the nms_client.sh script to retrieve data based on the generated requests:

    bash

        bash run_nmsclient.sh

File Structure

    run_infrasound_analysis.py: Main script for generating request files and executing data retrieval.
    viena.csv: CSV file containing dates for data requests.
    run_nmsclient.sh: Bash script to execute nms_client.sh for each generated request.
    nms_client.sh: CTBTO client script to retrieve infrasound data.
    data/: Directory to store retrieved MiniSEED data files.

Example

    Ensure viena.csv is populated with desired dates.
    Run the script:

    bash

python run_infrasound_analysis.py

Execute the data retrieval:

bash

    bash run_nmsclient.sh

Configuration

    Update viena.csv with the required dates for infrasound data retrieval.
    Modify station IDs (estacao) and file paths in run_infrasound_analysis.py as needed.

License

This project is licensed under the MIT License.
Contact

For any inquiries or support, please contact Arthur.
