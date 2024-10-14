# This line indicates that the script should be run using the Python 3 interpreter
#!/usr/bin/env python3

# Import the os module for interacting with the operating system
import os

# Import the AWS CDK (Cloud Development Kit) module
import aws_cdk as cdk

# Import the PythonProject15Stack class from the python_project15_stack module
from python_project15.python_project15_stack import PythonProject15Stack

# Create a new CDK application
app = cdk.App()


PythonProject15Stack(app, "PythonProject15Stack",
    # Instantiate the PythonProject15Stack with the app and a stack name

    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    # env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    # Set the environment for the stack using the default AWS account and region from the CLI configuration

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to.

    # env=cdk.Environment(account='123456789012', region='us-east-1'),
    # Set the environment for the stack using a specific AWS account and region

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    # Reference to the AWS CDK documentation for more details on environments
)

# Synthesize the app into a CloudFormation template
app.synth()

