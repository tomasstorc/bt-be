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
        data = []
        with connection.cursor() as cursor:
            for row in cursor.execute('SELECT * FROM ADMIN.EMPLOYEES;'):
                data.append(row)
        return {
            'statusCode': 200,
            'body': json.dumps({"status": "success", "time": f"{time.time() - start}", "data": json.dumps(data,sort_keys=True, default=str)},sort_keys=True, default=str)

        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({"status": "success", "time": f"{time.time() - start}", "error": json.dumps(e,sort_keys=True, default=str)},sort_keys=True, default=str)

        }
