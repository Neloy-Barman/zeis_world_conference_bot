
def elicit_slot(slot_to_elicit, slot, message, session_attributes, intent_name):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slot,
            'slotToElicit': slot_to_elicit,
            'message': { 
                "contentType": "PlainText",
                "content":message
            }
        }
    }


def build_response_card(title, sub_title, imageUrl, options):

    # Limit buttons to desired value
    lim = 20
    if len(options)>lim: 
        buttons = options[:lim]
    else:
        buttons = options

    # Split buttons into chunks of 5
    response_values = [{'title': title, 'subTitle': sub_title, 'buttons': buttons[i:i + 5]} 
                       for i in range(0, len(buttons), 5)]

    return {
        'contentType': 'application/vnd.amazonaws.card.generic',
        'version': 11,
        'genericAttachments': response_values
    }




def nextIntent(session_attributes, message): 

    return {
            'sessionAttributes':session_attributes,    
            'dialogAction': {
            'type': 'ElicitIntent',
            'message': {
                'contentType': 'PlainText',
                'content': message
            }
        }
    } 



def nextIntentWithResponseCard(session_attributes, message, title, subTitle, imageUrl, options): 

    return {
            'sessionAttributes':session_attributes,    
            'dialogAction': {
            'type': 'ElicitIntent',
            'message': {
                'contentType': 'PlainText',
                'content': message
                 },
                'responseCard': build_response_card(
                    title,
                    subTitle,
                    imageUrl,
                    options
                )
            }
        }



def elicit_slot_with_response_card(slot_to_elicit, slots, message, sessionAttributes, intent_name, title, subTitle,options):

    return {
        'sessionAttributes':sessionAttributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message':{
                "contentType": "PlainText",
                "content": message
            },
            'responseCard': build_response_card(
                title, 
                subTitle, 
                options
            )
        }
    }