import requests
import json
import pandas as pd

# api sets
population_by_sex = "https://openafrica.net/api/3/action/datastore_search?resource_id=f1fca3c3-af10-4b55-b33a-95e8fbbd8dc2&q=nairobi"
household_size = "https://openafrica.net/api/3/action/datastore_search?resource_id=111a3d9d-c676-4d5a-9600-d5acb1250b87&q=nairobi"
landarea_populationdensity = "https://openafrica.net/api/3/action/datastore_search?resource_id=17b4b55a-0b2d-40c2-8e30-27a5be21f42a&q=nairobi"
population_by_age_sex = "https://openafrica.net/api/3/action/datastore_search?resource_id=b7edfdb4-2a07-4332-8796-2f00968aff0e&q=nairobi"

def nairobi_population_by_sex(url):
    response = requests.get(url)
    # Load JSON data
    data = json.loads(response.text)   
    for record in data['result']['records']:
        print(record)


# calls
nairobi_population_by_sex(landarea_populationdensity)

# def nairobi_population_by_sex(url):
#     response = requests.get(url)
#     data = response.json()  
    
#     # Extracting relevant information into a list of dictionaries
#     records = []
#     for record in data['result']['records']:
#         record_dict = {
#             'Name': record.get('name', 0),
#             'Male': record.get('Male', 0),
#             'Female': record.get('Female', 0),
#             'Intersex': record.get('Intersex', 0),
#             'Total': record.get('Total', 0)
#         }
#         records.append(record_dict)
    
#     # Create a DataFrame from the list of dictionaries
#     population_df = pd.DataFrame(records)
#     return population_df

# # Example usage:
# # Replace 'url' with the actual URL containing the JSON data
# # For example:
# # url = 'https://example.com/data.json'
# nairobi_population = nairobi_population_by_sex(population_by_sex)
# print(nairobi_population)