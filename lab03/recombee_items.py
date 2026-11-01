import os

import pandas as pd
from dotenv import load_dotenv
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import SetItemValues, Batch
from recombee_api_client.exceptions import APIException

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lab02', '.env'))
DB_NAME = os.getenv('DB_NAME')
PRIVATE_TOKEN = os.getenv('PRIVATE_TOKEN')
REGION_STR = os.getenv('REGION', 'eu-west')
REGION = Region[REGION_STR.upper().replace('-', '_')]

client = RecombeeClient(DB_NAME, PRIVATE_TOKEN, region=REGION)

# TODO 2: Incarcarea aceluiasi dataset folosit la Lab 02
PATH_DATASET = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lab02', 'books.csv')

def send_items():
    """Functie care citeste dataset-ul si trimite item-urile in Recombee"""
    df = pd.read_csv(PATH_DATASET)
    print(f"Se trimit {len(df)} item-uri in Recombee...")
    
    requests = []
    
    for index, row in df.iterrows():
        # TODO 3: Extrageti ID-ul unic al produsului din coloana corespunzatoare din CSV
        item_id = str(row['isbn13'])

        # TODO 4: Mapati proprietatile definite anterior cu valorile din randul curent
        # Celulele goale din CSV (NaN) sunt trimise ca None
        properties = {
            "title": str(row['title']),
            "authors": None if pd.isna(row['authors']) else str(row['authors']),
            "categories": None if pd.isna(row['categories']) else str(row['categories']),
            "published_year": None if pd.isna(row['published_year']) else int(row['published_year']),
            "average_rating": None if pd.isna(row['average_rating']) else float(row['average_rating']),
            "num_pages": None if pd.isna(row['num_pages']) else int(row['num_pages']),
            "ratings_count": None if pd.isna(row['ratings_count']) else int(row['ratings_count']),
        }
        
        # Adaugam request-ul de setare a valorilor pentru item
        # (SetItemValues creează automat item-ul dacă acesta nu există)
        requests.append(SetItemValues(item_id, properties, cascade_create=True))
        
        # Trimitem in loturi (batch) de cate 100 pentru eficienta
        if len(requests) == 100:
            client.send(Batch(requests))
            requests = []
            print("S-a trimis un lot de 100 item-uri...")
            
    # Trimitem si restul ramanase (daca numarul total nu e multiplu de 100)
    if requests:
        client.send(Batch(requests))
        print("S-a trimis ultimul lot de item-uri.")
        
    print("Toate item-urile au fost trimise cu succes!")

if __name__ == "__main__":
    send_items()
