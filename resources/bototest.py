import boto3
import uuid

def create_name(prefix):
    return ''.join([prefix, str(uuid.uuid4())])

def create_bucket(prefix, s3_connection):
        session = boto3.session.Session()
        region = session.region_name
        name = create_name(prefix)
        if region == 'us-east-1':
            response = s3_connection.create_bucket(Bucket=name)
        else:
            response = s3_connection.create_bucket(Bucket=name, CreateBucketConfiguration={'LocationConstraint': region})
        print(name, region)
        return name, response

# Create new bucket
# s3_resource = boto3.resource('s3')
# bucket_name, response = create_bucket(prefix='diabetes', s3_connection=s3_resource)

# Upload file to bucket
# filename = 'diabetes.csv'
# s3_resource.Object(bucket_name, filename).upload_file(Filename=filename)

# Delete file & bucket
# s3_resource.Object(bucket_name, filename).delete()
# s3_resource.Bucket(bucket_name).delete()