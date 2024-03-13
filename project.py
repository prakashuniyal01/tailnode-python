import requests
import mysql.connector

# MySQL configurations
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DATABASE = 'tailnode'

# App ID for the API
APP_ID = '65f1d1e82d8e5b984f534734'

# Establish MySQL connection
db_connection = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
db_cursor = db_connection.cursor()

# Function to fetch user data using GET request
def fetch_user_data(user_id):
    url = f"https://dummyapi.io/data/v1/user"
    headers = {'app-id': APP_ID}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None



# data save user
def save_user_data_to_database(user_data):
    query = "INSERT INTO User (id, title, firstName, lastName, picture) VALUES (%s, %s, %s, %s, %s)"
    for data in user_data:        
        values = ( str(data['id']), data['title'], data['firstName'], data['lastName'], data['picture'])
        db_cursor.execute(query, values)
        save_post_data_to_database(data,db_connection)
    db_connection.commit()

# save post with respact to user 
def save_post_data_to_database(post_data, db_connection):
    user_id = post_data["id"]
    url = f"https://dummyapi.io/data/v1/user/{user_id}/post"
    headers = {'app-id': APP_ID}  # Replace 'YOUR_APP_ID' with your actual app ID
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        posts = response.json()
        # print(posts)
        query = "INSERT INTO Post (id,text,image,likes,tags,owner,publishDate,) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        db_cursor.execute(query, values)
        db_connection.commit()
        # Assuming you have a function to save posts to the database
        # Example: save_posts_to_database(posts, db_connection)
        # Implement the function according to your database schema







    else:
        return None
    db_connection.commit()

# Example usage
if __name__ == "__main__":
    # Fetch user data
    user_id = 123  # Example user ID
    user_data = fetch_user_data(user_id)
    # print(user_data)
    if user_data:
        
        # Save user data to MySQL database
        save_user_data_to_database(user_data["data"])
        print("User data saved to MySQL database successfully!")
    else:
        print("Failed to fetch user data")




    #         VARCHAR(255) PRIMARY KEY,
    # ->      VARCHAR(1000),
    # ->      VARCHAR(255),
    # ->      INT DEFAULT 0,
    # ->      VARCHAR(255),
    # ->      VARCHAR(255),
    # ->      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,]