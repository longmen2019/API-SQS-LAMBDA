# Define the handler function that takes 'event' and 'context' as parameters
def handler(event, context):
    # Create a response string by concatenating a message with the body of the first record in the event
    response = "Received Message Body from API GW: " + event['Records'][0]['body']

    # Print the response to the console for logging purposes
    print(response)

    # Return a dictionary with a status code of 200 (HTTP OK) and the response body
    return {
        'statusCode': 200,
        'body': response
    }

