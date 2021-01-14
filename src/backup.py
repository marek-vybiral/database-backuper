import os
import subprocess
from datetime import datetime

from boto3 import session


DUMP_ARGS = [
    'DB_HOST',
    'DB_PORT',
    'DB_NAME',
    'DB_USER',
    'DB_PASSWORD',
]

UPLOAD_ARGS = [
    'S3_KEY',
    'S3_SECRET',
    'S3_ENDPOINT',
    'S3_REGION',
    'S3_BUCKET',
]


def dump(output_file_path, db_host, db_port, db_name, db_user, db_password):
    cmd = [
        'pg_dump',
        '-h',
        db_host,
        '-p',
        db_port,
        '-U',
        db_user,
        db_name,
    ]
    process = subprocess.Popen(
        cmd,
        env={'PGPASSWORD': db_password, **os.environ},
        stdout=open(output_file_path, 'w'),
    )
    process.wait()


def compress(input_file_path, output_file_path):
    cmd = ['gzip', '-9', '-c', input_file_path, ]
    process = subprocess.Popen(cmd, stdout=open(output_file_path, 'w'))
    process.wait()



def upload(file_name, s3_key, s3_secret, s3_endpoint, s3_region, s3_bucket):
    s = session.Session()
    client = s.client('s3',
        endpoint_url=s3_endpoint,
        region_name=s3_region,
        aws_access_key_id=s3_key,
        aws_secret_access_key=s3_secret,
    )

    client.upload_file(file_name, s3_bucket, file_name)


def do_backup():
    for arg in DUMP_ARGS + UPLOAD_ARGS:
        assert arg in os.environ

    datetime_str = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')

    raw_dump = f'dump_{datetime_str}.sql'
    print(f'Dumping to {raw_dump}')
    dump(raw_dump, **{k: os.environ[k] for k in DUMP_ARGS})

    compressed_dump = raw_dump + '.gz'
    print(f'Compressing')
    compress(raw_dump, compressed_dump)

    os.remove(raw_dump)

    print(f'Uploading')
    upload(compressed_dump, **{k: os.environ[k] for k in UPLOAD_ARGS})

    os.remove(compressed_dump)
    print(f'Done')


if __name__ == '__main__':
    do_backup()
