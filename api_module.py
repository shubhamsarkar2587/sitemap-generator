import requests


def get_api_data(api_endpoint, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",  # Set the content type based on your API requirements
    }

    # Make a GET request to the API
    response = requests.get(api_endpoint, headers=headers)

    # Check the response status
    if response.status_code == 200:
        # Request was successful
        data = response.json()  # Get the JSON data from the response
        return data
    else:
        # Request failed
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None
