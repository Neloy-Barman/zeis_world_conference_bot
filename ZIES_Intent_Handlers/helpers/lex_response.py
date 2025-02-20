
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



def buildResponseCardResponse(title, subTitle, imageUrl, options):
    buttons = []
    genericAttachments = []
    
    j = 0
    
    data_5 = {'title': title, 'subTitle':subTitle, 'imageUrl': imageUrl, 'buttons':[]}
    data_10 = {'title': title, 'subTitle':subTitle, 'imageUrl': imageUrl, 'buttons':[]}
    
    for i in options:
        j = j+1
        if j<= 5:
            data_5['buttons'].append(i)
            if (j == 5) or (options.index(i) == (len(options)-1)):
                genericAttachments.append(data_5)
    
        if (j>5) and (j<=10):
            data_10['buttons'].append(i)
            if (j == 10) or (options.index(i) == (len(options)-1)):
                genericAttachments.append(data_10)
    return {
        'contentType': 'application/vnd.amazonaws.card.generic',
        'version': 11,
        'genericAttachments': genericAttachments,
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
                'responseCard': buildResponseCardResponse(
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
            'responseCard': buildResponseCardResponse(
                title, 
                subTitle, 
                options
            )
        }
    }