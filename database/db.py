from boto3 import resource
from os import getenv

dynamodb = resource(
    "dynamodb",
    aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
    region_name="us-east-1",
)
# creamos las tablas donde se van a guardar los datos
tables = [
    {
        "TableName": "users",
        "KeySchema": [
            {
                "AttributeName": "id",
                "KeyType": "HASH",  # la llave primaria de la tabla es el id
            },
            {
                "AttributeName": "created_at",
                "KeyType": "RANGE",  # la segunda clave secundaria del usuario sera su fecha de creacion/ tipo clasificacion
            },
        ],
        "AttributeDefinitions": [
            {
                "AttributeName": "id",
                "AttributeType": "S",  # S = string  N = numero B = binario
            },
            {"AttributeName": "created_at", 
             "AttributeType": "S"},
        ],
    }
]


def create_tables():
    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST",
            )
    except Exception as e:
        print(e)
