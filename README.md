## **AWS API-SQS-Lambda CDK Project**

This project provides a boilerplate for building an infrastructure consisting of an API Gateway, SQS queue, and Lambda function using AWS CDK with Python. 

**Key Components:**

* **API Gateway:** Acts as the entry point for your application, accepting requests and routing them to the Lambda function.
* **SQS Queue:** A message queue that decouples the API Gateway from the Lambda function. Messages are stored in the queue until the Lambda function is available to process them. 
* **Lambda Function:** The serverless compute unit that executes the desired logic in response to messages received from the SQS queue.

**Getting Started:**

1. **Prerequisites:**
    * Node.js and the AWS CDK Toolkit: Follow the official guide for installation: [https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

2. **Activate Virtual Environment (Optional):**
    This project includes a pre-configured virtual environment (`.venv`). If you prefer to use it:
      * MacOS/Linux: `source .venv/bin/activate`
      * Windows: `.venv\Scripts\activate.bat`

3. **Install Dependencies:**
    Run `pip install -r requirements.txt` to install required CDK libraries for building your specific API-SQS-Lambda infrastructure.

**Building and Deploying:**

1. **Bootstrap (Optional):**
   * Run `cdk bootstrap` to configure AWS accounts and regions for deployment (only necessary for the first deployment). 
   * If you encounter permission errors, ensure your IAM user has the necessary SSM permissions (refer to IAM policy below).

2. **Synthesize CloudFormation Template:**
   * Run `cdk synth` to generate a CloudFormation template representing your infrastructure code. This allows you to review the resources that will be created.

3. **Deploy Infrastructure:**
   * Run `cdk deploy` to deploy the infrastructure to your AWS account. This creates the API Gateway, SQS queue, and Lambda function based on your code.

4. **Additional Commands:**
    * `cdk ls`: Lists all defined stacks in your project.
    * `cdk diff`: Compares the deployed stack with your current code.
    * `cdk docs`: Opens the AWS CDK documentation for reference.
    * **`cdk destroy`**: Deletes all deployed stacks, preventing unnecessary AWS charges.

**IAM Policy for Bootstrap (if necessary):**

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
      "Resource": "arn:aws:ssm:<region>:<account-id>:parameter/cdk-bootstrap/*"
    }
  ]
}
```

**Adding Dependencies:**

To introduce additional CDK libraries or modify the existing functionalities, update your `setup.py` file and re-run `pip install -r requirements.txt`. 

**Troubleshooting cdk Installation:**

If you encounter issues installing the AWS CDK toolkit, refer to this Stack Overflow thread for troubleshooting steps and a solution provided by the community: [https://stackoverflow.com/questions/64771199/after-successful-installation-aws-cdk-cdk-command-not-found/79081237#79081237](https://stackoverflow.com/questions/64771199/after-successful-installation-aws-cdk-cdk-command-not-found/79081237#79081237)


