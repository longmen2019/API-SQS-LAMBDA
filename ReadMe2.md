
```markdown
# AWS CDK Project Setup

This project demonstrates how to set up and deploy an AWS CDK project using Python. It includes configuring permissions, installing dependencies, and running the project.

## Prerequisites

- AWS CLI installed and configured
- AWS CDK installed
- Python 3.9 or later installed

## Setup Instructions

### 1. Bootstrap the Environment

To bootstrap your AWS environment for CDK, run the following command:

```sh
cdk bootstrap
```


```

### 2. Install Dependencies

Install the necessary Python dependencies using `pip`:

```sh
pip install -r requirements.txt
```

### 3. Deploy the Stack

Deploy your CDK stack with the following command:

```sh
cdk deploy
```

## Resources Explained

### SQS Queue

```yaml
PythonProject15Queue4F1FB294:
  Type: AWS::SQS::Queue
  Properties:
    VisibilityTimeout: 300
  UpdateReplacePolicy: Delete
  DeletionPolicy: Delete
  Metadata:
    aws:cdk:path: PythonProject15Stack/PythonProject15Queue/Resource
```

This resource defines an SQS queue with a visibility timeout of 300 seconds. The queue will be deleted when the stack is deleted.

### IAM Role for Lambda

```yaml
SQSTriggerLambdaServiceRole0C427DE8:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument:
      Statement:
        - Action: sts:AssumeRole
          Effect: Allow
          Principal:
            Service: lambda.amazonaws.com
      Version: "2012-10-17"
    ManagedPolicyArns:
      - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
  Metadata:
    aws:cdk:path: PythonProject15Stack/SQSTriggerLambda/ServiceRole/Resource
```

This resource defines an IAM role that allows the Lambda function to assume the role and use the AWSLambdaBasicExecutionRole policy.

### IAM Policy for Lambda

```yaml
SQSTriggerLambdaServiceRoleDefaultPolicyB9CC6FE7:
  Type: AWS::IAM::Policy
  Properties:
    PolicyDocument:
      Statement:
        - Action:
            - sqs:ChangeMessageVisibility
            - sqs:DeleteMessage
            - sqs:GetQueueAttributes
            - sqs:GetQueueUrl
            - sqs:ReceiveMessage
          Effect: Allow
          Resource:
            Fn::GetAtt:
              - PythonProject15Queue4F1FB294
              - Arn
      Version: "2012-10-17"
    PolicyName: SQSTriggerLambdaServiceRoleDefaultPolicyB9CC6FE7
    Roles:
      - Ref: SQSTriggerLambdaServiceRole0C427DE8
  Metadata:
    aws:cdk:path: PythonProject15Stack/SQSTriggerLambda/ServiceRole/DefaultPolicy/Resource
```

This resource defines an IAM policy that grants the Lambda function permissions to interact with the SQS queue.

### Lambda Function

```yaml
SQSTriggerLambda99F71FB3:
  Type: AWS::Lambda::Function
  Properties:
    Code:
      S3Bucket:
        Fn::Sub: cdk-hnb659fds-assets-${AWS::AccountId}-${AWS::Region}
      S3Key: 8787c31033d09a9e5c023689d3a090cead09bf9f394522f7f0e5690290b53519.zip
    Handler: lambda-handler.handler
    Role:
      Fn::GetAtt:
        - SQSTriggerLambdaServiceRole0C427DE8
        - Arn
    Runtime: python3.9
  DependsOn:
    - SQSTriggerLambdaServiceRoleDefaultPolicyB9CC6FE7
    - SQSTriggerLambdaServiceRole0C427DE8
  Metadata:
    aws:cdk:path: PythonProject15Stack/SQSTriggerLambda/Resource
    aws:asset:path: asset.8787c31033d09a9e5c023689d3a090cead09bf9f394522f7f0e5690290b53519
    aws:asset:is-bundled: false
    aws:asset:property: Code
```

This resource defines a Lambda function with its code stored in an S3 bucket. The function uses the specified IAM role and runs Python 3.9.

### Event Source Mapping

```yaml
SQSTriggerLambdaSqsEventSourcePythonProject15StackPythonProject15Queue8D5624D33EB2CB7D:
  Type: AWS::Lambda::EventSourceMapping
  Properties:
    EventSourceArn:
      Fn::GetAtt:
        - PythonProject15Queue4F1FB294
        - Arn
    FunctionName:
      Ref: SQSTriggerLambda99F71FB3
  Metadata:
    aws:cdk:path: PythonProject15Stack/SQSTriggerLambda/SqsEventSource:PythonProject15StackPythonProject15Queue8D5624D3/Resource
```

This resource defines an event source mapping that triggers the Lambda function when messages are received in the SQS queue.

## Troubleshooting

If you encounter any issues, ensure that your IAM user or role has the necessary permissions and that all dependencies are correctly installed. For further assistance, refer to the AWS CDK documentation or reach out for help.

---

Feel free to modify this `README.md` to better suit your project's specific needs!
```

Let me know if you need any further adjustments or additional information!Sure! Here's a `README.md` file based on the questions and issues you encountered with AWS CDK and permissions:

```markdown
# AWS CDK Project Setup

This project demonstrates how to set up and deploy an AWS CDK project using Python. It includes configuring permissions, installing dependencies, and running the project.

## Prerequisites

- AWS CLI installed and configured
- AWS CDK installed
- Python 3.9 or later installed

## Setup Instructions

### 1. Bootstrap the Environment

To bootstrap your AWS environment for CDK, run the following command:

```sh
cdk bootstrap
```

If you encounter permission issues, ensure that your IAM user or role has the necessary permissions. For example, you might need to add the following policy to your IAM user or role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:PutParameter",
        "ssm:GetParameter",
        "ssm:GetParameters",
        "ssm:GetParameterHistory",
        "ssm:DeleteParameter",
        "ssm:DescribeParameters",
        "ssm:ListTagsForResource",
        "ssm:AddTagsToResource",
        "ssm:RemoveTagsFromResource"
      ],
      "Resource": "arn:aws:ssm:us-east-1:471112503258:parameter/cdk-bootstrap/*"
    }
  ]
}
```

### 2. Install Dependencies

Install the necessary Python dependencies using `pip`:

```sh
pip install -r requirements.txt
```

### 3. Deploy the Stack

Deploy your CDK stack with the following command:

```sh
cdk deploy
```

## Resources Explained

### SQS Queue

```yaml
PythonProject15Queue4F1FB294:
  Type: AWS::SQS::Queue
  Properties:
    VisibilityTimeout: 300
  UpdateReplacePolicy: Delete
  DeletionPolicy: Delete
  Metadata:
    aws:cdk:path: PythonProject15Stack/PythonProject15Queue/Resource
```

This resource defines an SQS queue with a visibility timeout of 300 seconds. The queue will be deleted when the stack is deleted.

### IAM Role for Lambda

```yaml
SQSTriggerLambdaServiceRole0C427DE8:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument:
      Statement:
        - Action: sts:AssumeRole
          Effect: Allow
          Principal:
            Service: lambda.amazonaws.com
      Version: "2012-10-17"
    ManagedPolicyArns:
      - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
  Metadata:
    aws:cdk:path: PythonProject15Stack/SQSTriggerLambda/ServiceRole/Resource
```

This resource defines an IAM role that allows the Lambda function to assume the role and use the AWSLambdaBasicExecutionRole policy.

### IAM Policy for Lambda

```yaml
SQSTriggerLambdaServiceRoleDefaultPolicyB9CC6FE7:
  Type: AWS::IAM::Policy
  Properties:
    PolicyDocument:
      Statement:
        - Action:
            - sqs:ChangeMessageVisibility
            - sqs:DeleteMessage
            - sqs:GetQueueAttributes
            - sqs:GetQueueUrl
            - sqs:ReceiveMessage
          Effect: Allow
          Resource:
            Fn::GetAtt:
              - PythonProject15Queue4F1FB294
              - Arn
      Version: "2012-10-17"
    PolicyName: SQSTriggerLambdaServiceRoleDefaultPolicyB9CC6FE7
    Roles:
      - Ref: SQSTriggerLambdaServiceRole0C427DE8
  Metadata:
    aws:cdk:path: PythonProject15Stack/SQSTriggerLambda/ServiceRole/DefaultPolicy/Resource
```

This resource defines an IAM policy that grants the Lambda function permissions to interact with the SQS queue.

### Lambda Function

```yaml
SQSTriggerLambda99F71FB3:
  Type: AWS::Lambda::Function
  Properties:
    Code:
      S3Bucket:
        Fn::Sub: cdk-hnb659fds-assets-${AWS::AccountId}-${AWS::Region}
      S3Key: 8787c31033d09a9e5c023689d3a090cead09bf9f394522f7f0e5690290b53519.zip
    Handler: lambda-handler.handler
    Role:
      Fn::GetAtt:
        - SQSTriggerLambdaServiceRole0C427DE8
        - Arn
    Runtime: python3.9
  DependsOn:
    - SQSTriggerLambdaServiceRoleDefaultPolicyB9CC6FE7
    - SQSTriggerLambdaServiceRole0C427DE8
  Metadata:
    aws:cdk:path: PythonProject15Stack/SQSTriggerLambda/Resource
    aws:asset:path: asset.8787c31033d09a9e5c023689d3a090cead09bf9f394522f7f0e5690290b53519
    aws:asset:is-bundled: false
    aws:asset:property: Code
```

This resource defines a Lambda function with its code stored in an S3 bucket. The function uses the specified IAM role and runs Python 3.9.

### Event Source Mapping

```yaml
SQSTriggerLambdaSqsEventSourcePythonProject15StackPythonProject15Queue8D5624D33EB2CB7D:
  Type: AWS::Lambda::EventSourceMapping
  Properties:
    EventSourceArn:
      Fn::GetAtt:
        - PythonProject15Queue4F1FB294
        - Arn
    FunctionName:
      Ref: SQSTriggerLambda99F71FB3
  Metadata:
    aws:cdk:path: PythonProject15Stack/SQSTriggerLambda/SqsEventSource:PythonProject15StackPythonProject15Queue8D5624D3/Resource
```

This resource defines an event source mapping that triggers the Lambda function when messages are received in the SQS queue.

## Troubleshooting

If you encounter any issues, ensure that your IAM user or role has the necessary permissions and that all dependencies are correctly installed. For further assistance, refer to the AWS CDK documentation or reach out for help.

---

Feel free to modify this `README.md` to better suit your project's specific needs!
```

Let me know if you need any further adjustments or additional information!