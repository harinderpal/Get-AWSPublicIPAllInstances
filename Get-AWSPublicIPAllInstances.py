import boto3

ec2Resource = boto3.resource('ec2')
def lambda_handler(event, context):
        instances = ec2Resource.instances.all()
        for instance in instances:
            #print("inst.public_ip_address",inst.public_ip_address)
            if instance.public_ip_address:
                print("Instance ID: ",instance.id," , Public IP: ",instance.public_ip_address,", Instance Type:",instance.instance_type) 
                
    
    
    
