import requests
import json
from bs4 import BeautifulSoup
import re

def get_season_4_table(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the heading for Season 4
        season_4_heading = soup.find('span', {'id': 'Season_4'})
        
        # Find the table under the Season 4 heading
        season_4_table = season_4_heading.find_next('table')
        
        # Extract data from the table and convert it to a Python dictionary
        table_data = []
        header_row = season_4_table.find('tr')
        for row in season_4_table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all(['th', 'td'])
            row_data = {}
            for i, column in enumerate(columns):
                column_name = header_row.find_all(['th', 'td'])[i].text.strip()
                row_data[column_name] = column.text.strip()
            
            # Filter based on Type and GL Tracking
            type_value = row_data.get('Type', '')
            gl_tracking_value = row_data.get('GL Tracking', '')
            description_value = row_data.get('Description', '')
            
            if (
                type_value == 'U. Awakening'
                and (gl_tracking_value == '' or gl_tracking_value == 'Skipped')
                and re.search(r'NV', description_value)
            ):
                table_data.append({
                    row_data.get('Date', ''): {
                    'U. Awakening': description_value}
                })
        
        return table_data
    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

# URL of the page
url = "https://exvius.fandom.com/wiki/Update_Schedule"

# Get the filtered data from the specified URL
result = get_season_4_table(url)

# Display the result in pretty formatted JSON
if result:
    for record in result:
        print(json.dumps(record, separators=(',', ':')))
