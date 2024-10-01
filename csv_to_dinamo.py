import csv
import boto3

# Inicializar el recurso DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('posiciones-table-dev')  # Nombre de la tabla en DynamoDB

# Función para cargar datos desde el CSV a DynamoDB
def cargar_datos_a_dynamodb(csv_file):
    with open(csv_file, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)  # Leer archivo como diccionario
        for fila in lector_csv:
            # Insertar cada fila como un ítem en DynamoDB
            table.put_item(Item=fila)

    print("Datos cargados exitosamente.")

# Llamada a la función con tu archivo CSV
csv_file = 'posiciones.csv'  # Nombre del archivo CSV
cargar_datos_a_dynamodb(csv_file)
