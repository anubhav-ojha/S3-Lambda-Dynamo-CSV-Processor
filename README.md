# S3-Lambda-Dynamo-CSV-Processor
The S3-Lambda-Dynamo-CSV-Processor is a project that uses AWS services to automatically process and store data from CSV files. It uses S3 for storage, Lambda for processing, DynamoDB for data storage and API Gateway to access the data stored in S3.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* An AWS account
* AWS CLI installed and configured on your local machine
* Python3 and pip3 installed on your local machine

### Installing
1. Clone the repository to your local machine
```
git clone https://github.com/<anubhav-ojha>/S3-Lambda-Dynamo-CSV-Processor.git
```
2. Navigate to the project directory
```
cd S3-Lambda-Dynamo-CSV-Processor
```
3. Install the necessary npm packages
```
pip3 install -r requirements.txt
```
4. Deploy the project to your AWS account using the AWS CLI
```
aws cloudformation deploy --template-file template.yml --stack-name S3-Lambda-Dynamo-CSV-Processor
```
5. Once the deployment is complete, you can test the project by uploading a CSV file to the S3 bucket created by the CloudFormation template. The Lambda function will automatically trigger and process the file, and the data will be stored in the DynamoDB table.

## Build With
* [AWS S3](https://aws.amazon.com/s3/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [AWS DynamoDB](https://aws.amazon.com/dynamodb/)
* [AWS API Gateway](https://aws.amazon.com/api-gateway/)
* [Python3](https://www.python.org/) - Python Programming Language 
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS SDK for Python

## Authors
* Anubhav Ojha - [anubhav-ojha](https://github.com/anubhav-ojha)
