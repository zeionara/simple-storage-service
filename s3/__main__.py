import hmac
import hashlib
from os import getenv
from datetime import datetime

from click import group, argument

from requests import get
from requests_aws4auth import AWS4Auth, AWS4SigningKey, StrictAWS4Auth


TIMEOUT = 3600


@group()
def main():
    pass

@main.command()
@argument('source', type = str)
@argument('destination', type = str)
def put(source: str, destination: str):
    date = datetime.now().strftime('%Y%m%d')
    # key = getenv('CLOUD_RU_S3_KEY_SECRET')

    # print(hmac.new(key.encode('utf-8'), date.encode('utf-8'), hashlib.sha256))

    endpoint = getenv('CLOUD_RU_S3_ENDPOINT')
    # endpoint = 'https://s3.cloud.ru/'

    key = getenv('CLOUD_RU_S3_TENANT_ID') + ':' + getenv('CLOUD_RU_S3_KEY_ID')
    secret = getenv('CLOUD_RU_S3_KEY_SECRET')
    region = getenv('CLOUD_RU_S3_REGION')
    service = getenv('CLOUD_RU_S3_SERVICE')

    # print(key, secret, region, service)

    auth = AWS4Auth(key, secret, region, service)
    # sig_key = AWS4SigningKey(secret, region, service, None, False)
    # auth = StrictAWS4Auth(key.encode('utf-8'), sig_key)

    print(auth)

    response = get(endpoint, auth = auth, timeout = TIMEOUT)

    print(response.text)


    # print(f'Uploading {source} to {destination}')


if __name__ == '__main__':
    main()
