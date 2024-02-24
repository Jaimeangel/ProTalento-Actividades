import requests
import csv
import pandas as pd

URL='https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'

def urlToCSV(URL):
    response = requests.get(URL)

    if response.status_code == 200:

        csv_file = 'api_data.csv'

        with open(csv_file, 'w', newline='') as file:
            file.write(response.text)

    else:
        print('Error request API')

urlToCSV(URL)

csv_api = pd.read_csv('api_data.csv')

def calcular_rango_intercuartil(columna,dataframe):
     # Calcular el rango intercuartil (IQR)
    Q1_cantidad = dataframe[columna].quantile(0.25)
    Q3_cantidad = dataframe[columna].quantile(0.75)
    IQR_cantidad = Q3_cantidad - Q1_cantidad

    # Definir los límites para detectar valores atípicos
    lower_bound_cantidad = Q1_cantidad - 1.5 * IQR_cantidad
    upper_bound_cantidad = Q3_cantidad + 1.5 * IQR_cantidad

    # Filtrar los valores atípicos
    dataframe=dataframe[(dataframe[columna] >= lower_bound_cantidad) & (dataframe[columna] <= upper_bound_cantidad)]
    return dataframe

def analyze_data(dataframe):
    # Eliminamos duplicados
    df = dataframe.drop_duplicates(keep='first')
    # Verificar valores faltantes
    numero_valores_faltantes = df.isna().sum()
    # No hay ningun valor faltante por columna

    nombre_columnas = df.columns.values.tolist()
    # filtramos el dataFrame,removiendo valores atípicos
    for columna in nombre_columnas:
        # por cada columna filtramos por valores atipicos segun el rango intercuartil
        dataframe = calcular_rango_intercuartil(columna,dataframe)

    # 
    rangos = [-float("inf"), 12, 19, 39, 59, float("inf")]
    etiquetas = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']

    dataframe['age group'] = pd.cut(df['age'], bins=rangos, labels=etiquetas, right=False)

    dataframe.to_csv('analyze_data.csv', index=False)


analyze_data(csv_api)

