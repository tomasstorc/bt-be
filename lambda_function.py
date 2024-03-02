import json
import oracledb
import time
import os

def lambda_handler(event, context):
    start = time.time()
    try:
        user = os.environ['USER']
        pw = os.environ['PW']
        connection_string = os.environ['TNS']
        connection = oracledb.connect(user=user, password=pw, dsn=connection_string)
        with connection.cursor() as cursor:
            for row in cursor.execute('select city from locations'):
                print(row)
        return {
            'statusCode': 200,
            'body': json.dumps({"status": "success", "time": f"{time.time() - start}"})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({"status": "failed", "time": f"{time.time() - start}", "error": e})
        }
