import aws_cdk as core
import aws_cdk.assertions as assertions

from python_project15.python_project15_stack import PythonProject15Stack


# example tests. To run these tests, uncomment this file along with the example
# resource in python_project15/python_project15_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PythonProject15Stack(app, "python-project15")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })
