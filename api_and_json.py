# =========================================================
# Task: Python API Communication and JSON Handling
# Description: This script demonstrates fetching data from a public
# API using the requests library, parsing the JSON response, applying
# filtering/search logic, and handling API errors using try-except.
# =========================================================

import requests

# ---- STEP 1: Fetch data from the API ----
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print("Status Code:", response.status_code)

# ---- STEP 2: Parse the JSON response ----
data = response.json()
print("Name:", data[0]["name"])
print("City:", data[0]["address"]["city"])

# ---- STEP 3: Apply filtering/search logic ----
matches = [user for user in data if "view" in user["address"]["city"]]

for user in matches:
    print(user["name"], "-", user["address"]["city"])

# ---- STEP 4: Handle API errors ----
try:
    bad_url = "https://jsonplaceholder.typicode.com/wrong-endpoint"
    bad_response = requests.get(bad_url, timeout=5)
    bad_response.raise_for_status()
    bad_data = bad_response.json()

except requests.exceptions.HTTPError as e:
    print("HTTP Error occurred:", e)
except requests.exceptions.ConnectionError:
    print("Failed to connect to the internet/server.")
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.RequestException as e:
    print("Something else went wrong:", e)

print("\n---- Script finished successfully ----")
