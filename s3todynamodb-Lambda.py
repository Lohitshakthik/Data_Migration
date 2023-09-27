import json
import boto3
import ast
s3_client=boto3.client('s3')
dynamodb=boto3.resource('dynamodb')
def lambda_handler(event, context):
   bucket=event['Records'][0]['s3']['bucket']['name'] #Fetching bucket name 
   print("Bucket name is =" + bucket)
   json_file_name = event['Records'][0]['s3']['object']['key']   #Fetch file which is uploaded in s3
   print("File name =" + json_file_name)
   json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
   print(str(json_object))
   file_reader = json_object ['Body'].read().decode('utf-8') #Fetching the details in the json fie 
   print(file_reader)
   print(str(file_reader))
   file_reader = json.loads(file_reader)   #Converting json file into dict
   print(str(file_reader))
   response = boto3.resource('dynamodb').Table('jsons3proj').put_item(Item=file_reader) #Uploads into DynamoDb
   return "Success"
