# Import the core module from AWS CDK
import aws_cdk as core

# Import the assertions module from AWS CDK for testing
import aws_cdk.assertions as assertions

# Import the PythonProject15Stack class from the python_project15_stack module
from python_project15.python_project15_stack import PythonProject15Stack


# example tests. To run these tests, uncomment this file along with the example
# resource in python_project15/python_project15_stack.py

def test_sqs_queue_created(): # Define a test function to verify that an SQS queue is created

    # Create a new CDK application
    app = core.App()

    # Instantiate the PythonProject15Stack with the app and a stack name
    stack = PythonProject15Stack(app, "python-project15")

    # Create a template object from the stack for assertions
    template = assertions.Template.from_stack(stack)

    # Assert that the stack contains an SQS queue with a visibility timeout of 300 seconds
    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })

