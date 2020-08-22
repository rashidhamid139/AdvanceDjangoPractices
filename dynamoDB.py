import boto3


AWS_ACCESS_KEY_ID = 'AKIAZ4RUTQSV633OURNA'
AWS_SECRET_ACCESS_KEY = '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'

session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

#getData
__TableName__ = 'dynamoDemo'
Primary_Key_Column = 'lastName'
Primary_key = 'dar'
columns = ['lastName', 'firstName', 'position']

db = session.resource('dynamodb', region_name='ap-south-1')
table = db.Table(__TableName__)

response = table.get_item(
    Key={
            Primary_Key_Column:Primary_key
    }
)


#putData

# response = table.put_item(
#     Item={
#         Primary_Key_Column:'khan',
#         columns[0]: 'khan',
#         columns[1]: 'Tariq',
#         columns[2]: "Shah"
#     }
# )


#deleteData

response = table.delete_item(
    Key={
        Primary_Key_Column: '44'
    }
)

print(dir(session))
