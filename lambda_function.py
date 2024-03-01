import json
import oracledb
import time

def lambda_handler(event, context):
    start = time.time()
    try:
        connection = oracledb.connect(user='scott', password='mypw', dsn='localhost/oraclepdb1')
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
            'body': json.dumps({"status": "failed", "time": f"{time.time() - start}"})
        }
