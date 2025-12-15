from os import getenv

from click import group, argument

from requests import put
from requests_aws4auth import AWS4Auth


TIMEOUT = 3600
SUCCESS = 200


@group()
def main():
    pass


@main.command()
@argument('name', type = str)
def create_bucket(name: str):
    endpoint = 'https://s3.cloud.ru'

    key = getenv('CLOUD_RU_S3_TENANT_ID') + ':' + getenv('CLOUD_RU_S3_KEY_ID')
    secret = getenv('CLOUD_RU_S3_KEY_SECRET')
    region = getenv('CLOUD_RU_S3_REGION')
    service = getenv('CLOUD_RU_S3_SERVICE')

    auth = AWS4Auth(key, secret, region, service)

    response = put(
        f'{endpoint}/{name}',
        auth = auth,
        timeout = TIMEOUT
    )

    if response.status_code == SUCCESS:
        print(f'Created bucket {name}')
    else:
        print(f'Failed to create bucket {name}')
        print(f'Error: {response.text}')


@main.command()
@argument('source', type = str)
@argument('destination', type = str)
def push(source: str, destination: str):
    endpoint = getenv('CLOUD_RU_S3_ENDPOINT')

    key = getenv('CLOUD_RU_S3_TENANT_ID') + ':' + getenv('CLOUD_RU_S3_KEY_ID')
    secret = getenv('CLOUD_RU_S3_KEY_SECRET')
    region = getenv('CLOUD_RU_S3_REGION')
    service = getenv('CLOUD_RU_S3_SERVICE')

    auth = AWS4Auth(key, secret, region, service)

    with open(source, 'rb') as file:
        data = file.read()

    response = put(
        endpoint + '/' + destination,
        auth = auth,
        timeout = TIMEOUT,
        data = data
    )

    if response.status_code == SUCCESS:
        print('Upload successful. Check out your file:')
        print(f'wget {endpoint}/{destination}')
    else:
        print(f'Failed to upload file as {destination}')
        print(f'Error: {response.text}')


if __name__ == '__main__':
    main()
