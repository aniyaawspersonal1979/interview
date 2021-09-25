#!/usr/bin/python

import boto3
import datetime
import os
from datetime import date
today = date.today()
current_date=today.strftime("%Y.%m.%d")
FILENAME="interview-"+current_date+".txt"
REGION_NAME=os.environ.get('REGION_NAME')
ACCESS_KEY=os.environ.get('ACCESS_KEY')
SECRET_KEY=os.environ.get('SECRET_KEY')
BUCKET_NAME=os.environ.get('BUCKET_NAME')
OBJ_NAME=FILENAME

# Create the file
file = open(FILENAME,"w")

s3 = boto3.resource('s3', region_name=REGION_NAME, aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
response = s3.Object(BUCKET_NAME, OBJ_NAME).put(Body=open(OBJ_NAME, 'rb'))
