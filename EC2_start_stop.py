import boto3
import sys
from botocore.exceptions import ClientError

region = 'ap-south-1'


print('The region is: ',region)
instance_Id = 'instanceid' 
action = (input('Please enter action START or STOP: ')).upper()
print('the action selected is: ', action)

ec2 = boto3.client('ec2',region_name=region)

if action == 'START':
    try:
        response = ec2.start_instances(InstanceIds = [instance_Id])
        print(response)
    except ClientError as e:
        print(e)

else:
    try:
        response = ec2.stop_instances(InstanceIds = [instance_Id]) 
        print(response)
    except ClientError as e:
        print(e)    
