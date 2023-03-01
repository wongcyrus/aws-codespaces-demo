import boto3

client = boto3.client('apigateway',region_name="us-east-1")


def list_apigateway_usage_plans(client):
    return client.get_usage_plans()

def list_all_aws_apigatway_usage_plans_paginated(client):
    response = client.get_usage_plans()
    yield response
    while 'position' in response:
        response = client.get_usage_plans(position=response['position'])
        yield response

if __name__ == "__main__":

    responses = list_all_aws_apigatway_usage_plans_paginated(client);
    for response in responses:
        print(response)