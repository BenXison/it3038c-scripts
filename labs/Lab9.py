import requests
import json

api_url = 'http://localhost:3000'

try:
    
    response = requests.get(api_url)

    if response.status_code == 200:
        widget_data = response.json()

        widget_list = []
        for widget in widget_data:
            widget_name = widget.get('name', 'N/A')
            widget_color = widget.get('color', 'N/A')
            widget_list.append(f"{widget_name} is {widget_color}")

        print("\n".join(widget_list))
    else:
        print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the API request: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
