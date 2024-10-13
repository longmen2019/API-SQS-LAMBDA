from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_source

)


class PythonProject15Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        queue = sqs.Queue(
            self, "PythonProject15Queue",
            visibility_timeout=Duration.seconds(300),
        )
        # Creating Lambda function that will be triggered by the SQS Queue
        sqs_lambda = _lambda.Function(self, 'SQSTriggerLambda',
                                      handler='lambda-handler.handler',
                                      runtime=_lambda.Runtime.PYTHON_3_9,
                                      code=_lambda.Code.from_asset('lambda')
                                      )
        # Create an SQS event source for Lambda
        sqs_event_source = lambda_event_source.SqsEventSource(queue)

        # Add SQS event source to the Lambda function
        sqs_lambda.add_event_source(sqs_event_source)
