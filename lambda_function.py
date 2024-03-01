import json
import oracledb

def lambda_handler(event, context):
    connection = oracledb.connect(user='scott', password='mypw', dsn='localhost/oraclepdb1')
    with connection.cursor() as cursor:
        for row in cursor.execute('select city from locations'):
            print(row)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!!')
    }
