"""This module is in charge of the user interface of the program"""

def request_number():
    """Request the data to the user"""
    print("INGRESE EL NÚMERO DE DATOS QUE DESEA OBTENER ")
    return int(input())

def request_deparment():
    """Request the department to the user"""
    print("INGRESE EL NOMBRE DEL DEPARTAMENTO ")
    return input().upper()

def show_data(data):
    """"display the data"""
    renamed_df = data.rename(columns={ 
        "ciudad_municipio_nom": " Ciudad ", 
        "departamento_nom": " Departamento ", 
        "edad" : "edad", 
        "fuente_tipo_contagio": "Tipo de Contagio", 
        "estado": "Estado", 
        "recuperado": "Recuperado" })
    print(renamed_df)
