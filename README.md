# simple-data-processing
## Data Processing Script

### Introduction
This Python script fetches data from the JSONPlaceholder API, performs data cleaning and transformation, and saves the cleaned data into a CSV file. The script also implements robust error handling and logging practices.

### Instruction

#### Requirements
- Python 3.8 or greater
- External libraries:
  - pandas
  - requests

#### Installation
1. Clone this repository to your local machine to get the python script file or directly decompress this compressed file to get the script.
2. Install the required libraries by running `pip install -r requirements.txt`.

#### Usage
1. Run the script `data_processing.py`.

#### Approach
- Data Retrieval: The script fetches data from the JSONPlaceholder API endpoints for posts and users using the `requests` library.
- Data Cleaning and Transformation: It merges the data from both endpoints, handles null or missing values, and prepares a clean dataset using the `pandas` library.
- Data Storage: The cleaned and merged data is saved into a local CSV file named `user_posts.csv`.
- Error Handling and Logging: Robust error handling is implemented using try-except blocks to manage potential issues during API calls, data processing, or file writing. Error logs are captured and saved for debugging purposes.

### Files
- `data_processing.py`: Python script for data retrieval, cleaning, transformation, and storage.
- `requirements.txt`: List of external libraries required by the script.

