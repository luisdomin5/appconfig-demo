import boto3
import os

from aws_lambda_powertools.tracing import Tracer

# Setup AWS X-Ray
tracer = Tracer()
client = boto3.client('appconfig')

@tracer.capture_lambda_handler
def handler(event, context):

  # Add config info to the trace in X-Ray
  tracer.put_annotation("AppId", os.environ['AppId'])
  tracer.put_annotation("EnvId", os.environ['EnvId'])
  tracer.put_annotation("ConfigId", os.environ['ConfigId'])

  # Depending on your requirements, you could remove the get_configuration
  # to the global scope.
  config = client.get_configuration(
    Application=os.environ['AppId'],
    Environment=os.environ['EnvId'],
    Configuration=os.environ['ConfigId'],
    ClientId=context.function_name
  )

  return {
    "data": config['Content'].read().decode("utf-8") 
  }
