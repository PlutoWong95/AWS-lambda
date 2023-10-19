import json
import boto3

ec2 = boto3.resource('ec2', region_name='ap-east-1')
def lambda_handler(event, context):
   #type your specify tag name here, suggest use bool to identify the value (True/False)
   instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:tag_name_here','Values':['True']}])
   for instance in instances:
       id=instance.id
       ec2.instances.filter(InstanceIds=[id]).stop()
       print("Instance ID is stopped:- "+instance.id)
   return "success" 