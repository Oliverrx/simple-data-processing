import requests
import pandas as pd
import logging

# Set up logging
logging.basicConfig(filename='data_processing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# API endpoints
POSTS_URL = 'https://jsonplaceholder.typicode.com/posts'
USERS_URL = 'https://jsonplaceholder.typicode.com/users'

def get_data(url):
    try:
        # Raise HTTPError for bad status codes
        response = requests.get(url)
        response.raise_for_status()
        print("Data acquired successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f'Error getting data from {url}: {e}')
        print("Error getting data.")
        return None

def process_data(posts, users):
    try:
        # Merge posts and users data
        merged_data = pd.merge(posts, users, how='inner', left_on='userId', right_on='id')

        # Handle missing values
        merged_data.fillna({'name': 'Unknown', 'username': 'Unknown', 'email': 'Unknown'}, inplace=True)
        merged_data.fillna(0, inplace=True)
        print("Data processed successfully.")

        return merged_data
    except Exception as e:
        logging.error(f'Error processing data: {e}')
        print("Error processing data.")
        return None

def save_data(data):
    try:
        data.to_csv('user_posts.csv', index=False)
        logging.info('Data saved to user_posts.csv successfully')
        print("Data saved to user_posts.csv successfully.")
    except Exception as e:
        logging.error(f'Error saving data to CSV file: {e}')
        print("Error saving data to CSV file.")

def main():
    # Fetch data from endpoints
    posts_data = get_data(POSTS_URL)
    users_data = get_data(USERS_URL)

    if posts_data and users_data:
        # Clean and merge data
        cleaned_data = process_data(pd.DataFrame(posts_data), pd.DataFrame(users_data))
        
        # Save data to CSV
        save_data(cleaned_data)
        print("Data job completed successfully.")
    else:
        logging.warning('Failed to get data from API endpoints')
        print("Failed to complete data job.")

if __name__ == '__main__':
    main()
