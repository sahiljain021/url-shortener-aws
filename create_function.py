import json, boto3, string, random, time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def lambda_handler(event, context):
    body = json.loads(event['body'])
    long_url = body['url']
    short_code = generate_code()
    expires_at = int(time.time()) + 30 * 24 * 3600

    table.put_item(Item={
        'short_code': short_code,
        'long_url': long_url,
        'expires_at': expires_at
    })

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'short_code': short_code})
    }