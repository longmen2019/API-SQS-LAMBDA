# Import the Construct class from the constructs module
from constructs import Construct

# Import necessary classes and modules from AWS CDK
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_source
)


# Define a new stack class that inherits from the Stack class
class PythonProject15Stack(Stack):

    # Initialize the stack with the given scope, construct ID, and any additional keyword arguments
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # example resource
        # Create an SQS queue with a visibility timeout of 300 seconds
        queue = sqs.Queue(
            self, "PythonProject15Queue",
            visibility_timeout=Duration.seconds(300),
        )

        # Creating Lambda function that will be triggered by the SQS Queue
        sqs_lambda = _lambda.Function(self, 'SQSTriggerLambda',
                                      # Create a Lambda function with the specified handler, runtime, and code from
                                      # the 'lambda' directory
                                      handler='lambda-handler.handler',
                                      runtime=_lambda.Runtime.PYTHON_3_9,
                                      code=_lambda.Code.from_asset('lambda')
                                      )

        # Create an event source for the Lambda function that triggers on messages from the SQS queue
        sqs_event_source = lambda_event_source.SqsEventSource(queue)

        # Attach the SQS event source to the Lambda function
        sqs_lambda.add_event_source(sqs_event_source)
