
# Subir un archivo CSV a una tabla DynamoDB en AWS

Para subir un archivo CSV a una tabla de **DynamoDB** en AWS, puedes seguir estos pasos utilizando **Python** y la biblioteca **Boto3**.

## Prerrequisitos

1. **Instalar Boto3**: Necesitas tener la biblioteca `boto3` instalada en tu entorno de Python. Puedes instalarla con:
   ```bash
   pip install boto3
   ```

2. **Credenciales de AWS**: Asegúrate de tener configuradas tus credenciales de AWS (ya sea con un archivo `~/.aws/credentials` o usando variables de entorno).

## Paso 1: Crear una tabla en DynamoDB

Antes de cargar los datos, asegúrate de tener una tabla en DynamoDB. Si aún no tienes una, puedes crear una a través de la **Consola de AWS** o usando el siguiente script de Python:

```python
import boto3

dynamodb = boto3.resource('dynamodb')

# Crear tabla en DynamoDB
table = dynamodb.create_table(
    TableName='MiTabla',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Clave primaria
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'  # Tipo de dato (S = String)
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Creando tabla. Esperando a que esté disponible...")
table.meta.client.get_waiter('table_exists').wait(TableName='MiTabla')
print("Tabla creada exitosamente.")
```

Esto creará una tabla con una clave primaria llamada `id`.

## Paso 2: Leer el archivo CSV

Ahora, vamos a leer el archivo CSV y cargar los datos en la tabla DynamoDB.

```python
import csv
import boto3

# Inicializar el recurso DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MiTabla')  # Nombre de la tabla en DynamoDB

# Función para cargar datos desde el CSV a DynamoDB
def cargar_datos_a_dynamodb(csv_file):
    with open(csv_file, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)  # Leer archivo como diccionario
        for fila in lector_csv:
            # Insertar cada fila como un ítem en DynamoDB
            table.put_item(Item=fila)

    print("Datos cargados exitosamente.")

# Llamada a la función con tu archivo CSV
csv_file = 'datos.csv'  # Nombre del archivo CSV
cargar_datos_a_dynamodb(csv_file)
```

## Paso 3: Estructura del archivo CSV

Para que esto funcione, el archivo CSV debe tener los mismos nombres de columna que los atributos de la tabla en DynamoDB. Aquí hay un ejemplo de cómo debe verse el archivo `datos.csv`:

```csv
id,nombre,edad,email
1,Juan Pérez,30,juan.perez@example.com
2,Ana García,25,ana.garcia@example.com
3,Carlos López,40,carlos.lopez@example.com
```

## Paso 4: Ejecución

Una vez que hayas preparado el archivo CSV y el script de Python, simplemente ejecuta el script para cargar los datos a DynamoDB:

```bash
python cargar_datos_dynamodb.py
```

Este script leerá cada fila del archivo CSV y usará el método `put_item()` de Boto3 para subir cada fila como un ítem en la tabla DynamoDB.

## Resumen

1. Crea una tabla DynamoDB con una clave primaria.
2. Usa Python y Boto3 para leer un archivo CSV y cargar los datos en DynamoDB.
3. Asegúrate de que las columnas del CSV coincidan con los nombres de los atributos en la tabla DynamoDB.

Si tienes más columnas en tu CSV que no coinciden con la estructura de la tabla, puedes ajustar el script para mapear correctamente esos campos o incluso transformar los datos antes de insertarlos en DynamoDB.