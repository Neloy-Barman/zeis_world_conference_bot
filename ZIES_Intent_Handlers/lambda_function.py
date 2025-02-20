import json
from intent_handlers.guest_of_honour_info_hlr import handle_guest_of_honour

def lambda_handler(event, context):

    # Current Intent Name
    intent_name = event['currentIntent']['name']
    print(f"Triggered Intent Name: {intent_name}")

    intent_to_handlers = {
        "Guest_Of_Honour_Info_ZIES" : handle_guest_of_honour
    }

    return intent_to_handlers[intent_name](event)


    # # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
