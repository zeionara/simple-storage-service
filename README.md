# Simple storage service

My experiments with [simple storage service from cloud.ru](https://cloud.ru/products/evolution-object-storage).

## Set up environment

Create a clean conda environment and install dependencies from [requirements.txt](/requirements.txt):

```sh
conda create -n s3 python=3.13
conda activate s3
pip install -r requirements.txt
```

## Usage

Before using the command, set up following env variables:

- `CLOUD_RU_S3_ENDPOINT` - `endpoint` of your default `bucket`, for example: `https://bucket.s3.cloud.ru`.
- `CLOUD_RU_S3_TENANT_ID` - your tenant id (generated automatically by the platform, see [this page](https://console.cloud.ru/spa/svp/s3-storage)).
- `CLOUD_RU_S3_KEY_ID` - your key id (generated manually by creating a service account).
- `CLOUD_RU_S3_KEY_SECRET` - your key secret (generated manually by creating a service account).
- `CLOUD_RU_S3_REGION` - your region (assigned automatically upon bucket creation).
- `CLOUD_RU_S3_SERVICE` - your service name (assigned automatically upon bucket creation).

The app supports two basic operations with simple storage service:

### Create bucket

Run the following command:

```sh
python -m s3 create-bucket foo
```

If everything is successful, the will look like:

```sh
Created bucket foo
```

### Upload files

Run the following command:

```sh
python -m s3 push assets/foo.txt assets/foo.txt
```

If everything is successful, the will look like:

```sh
Upload successful. Check out your file:
wget https://bucket.s3.cloud.ru/assets/foo.txt
```
