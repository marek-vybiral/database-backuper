# Database Backuper
Dockerized script to regularly backup a Postgres database to S3 compatible storage


## Super simple setup:

### 1) Prepere your ENV vars:

Schedule:
```
SCHEDULE=04:00,12:00
```

Database connection:
```
DB_HOST=example.com
DB_PORT=5432
DB_NAME=my_db
DB_USER=my_user
DB_PASSWORD=my_pw
```

Storage:
```
S3_ENDPOINT=https://fra1.digitaloceanspaces.com/
S3_REGION=fra1
S3_BUCKET=my_bucket
S3_KEY=xxx
S3_SECRET=xxxxxx
```

### 2) Deploy the image somewhere
I recommend using [CapRover](https://caprover.com/)


## Result
![reuslt](https://i.imgur.com/BBGkhhW.jpg)
