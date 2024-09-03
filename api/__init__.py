""""This module contains the functions to connect to the API and get the data from it"""
import pandas as pd
from sodapy import Socrata

def create_client():
    """Create a client to connect to the API"""
    return Socrata("www.datos.gov.co", None)

def get_data(number, department, client):
    """Get the data from the API"""
    return client.get("gt2j-8ykr", limit=number, departamento_nom = department)

def convert_dataframe(data):
    """Convert the data to a DataFrame"""
    return pd.DataFrame.from_records(data)

def format_df(data):
    """Format the DataFrame"""
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    list_data = ["ciudad_municipio_nom", "departamento_nom", "edad", "sexo", "estado", "fuente_tipo_contagio"]
    return data[list_data]
