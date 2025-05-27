
def elicit_slot( slot_to_elicit, intent_name, slots, session_attributes, message):
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'ElicitSlot',
                'slotToElicit': slot_to_elicit
            },
            'intent': {
                'name': intent_name,
                'slots': slots,
                'state': 'InProgress'
            },
            'sessionAttributes': session_attributes,
        },
        'messages': [
            {
                'contentType': 'PlainText',
                'content': message
            }
        ]
    }
    
    
def build_response_card(message, title, sub_title, options):

    # # Limit buttons to desired value
    # lim = 30
    # if len(options) > lim:
    #     buttons = options[:lim]
    # else:
    #     buttons = options
    
    buttons = options


    # Split buttons into chunks of 5
    response_values = [{
        'title': title,
        'subTitle': sub_title,
        'buttons': buttons[i:i + 5]
    } for i in range(0, len(buttons), 5)]

    messages = [
        {
            'contentType': 'PlainText',
            'content': message
        }
    ]

    for response in response_values:
        messages.append(
            {
                'contentType': 'ImageResponseCard', 
                'imageResponseCard': response
            }
        )
    
    return messages


def nextIntent( session_attributes, intent_name, message):
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'ElicitIntent'
            },
            'sessionAttributes': session_attributes,
            'intent': {
                'name': intent_name, 
                'state': 'Fulfilled'
            }
        },
        'messages': [
            {
                'contentType': 'PlainText',
                'content': message
            }
        ]
    }
    
    
def nextIntentWithResponseCard( intent_name, session_attributes, message, title, subTitle, options):
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'ElicitIntent',
            },
            'intent': {
                'name': intent_name,
                'state': 'Fulfilled'
            },
            'sessionAttributes': session_attributes
        },
        'messages': build_response_card(
            message, 
            title if title else 'Please select an option from below: ', 
            subTitle,
            options
        )
    }
    
    
def elicit_slot_with_response_card(slot_to_elicit, intent_name, slots, session_attributes, message, title, subTitle, options):
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'ElicitSlot',
                'slotToElicit': slot_to_elicit
            },
            'intent': {
                'name': intent_name,
                'slots': slots,
                'state': 'InProgress'
            },
            'sessionAttributes': session_attributes
        },
        'messages': build_response_card(
            message, 
            title if title else 'Please select an option from below: ', 
            subTitle,
            options
        )
    }