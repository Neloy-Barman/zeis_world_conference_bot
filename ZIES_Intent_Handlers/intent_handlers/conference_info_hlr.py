import pandas as pd
from data.constants import all_events
from data.constants import guided_buttons
from helpers.generic import create_buttons
from helpers.generic import create_unordered_list_elems
from helpers.lex_response import nextIntentWithResponseCard
from helpers.information_retrieval import perform_fuzzywuzzy

def handle_conference_info(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Initial
    # Message
    message = "Kindly select the event for which you want the conference information"
    # Buttons
    events = all_events
    buttons = [{'text': f'{item}', 'value': f'Conference Information of ​{item}​'} for item in events]

    # Fetching slot value
    slots = event['currentIntent']['slots']

    # Event
    event = slots['event']
    print(f"Event Name: {event}")

    # Benefits
    benefits = slots['Benefits']
    print(f"Benefits value: {benefits}")

    # Audience
    audience = slots['Audience']
    print(f"Audience value: {audience}")

    # Reading CSV file
    result = pd.read_csv("./data/conference_info.csv")

    # Event is not None
    if event:

        # Information Retrieval
        _, answer = perform_fuzzywuzzy(
            result = result,
            slot = event,
            column = 'event'
        )

        if answer is not None:
            # Message
            message = answer['desc']

            # # Buttons
            buttons = create_buttons(guided_buttons)
            # buttons = [
            #     { 'text': "Benefits", 'value': f"Benefits of {event}" },
            #     { 'text': "Target Audience", 'value': f"Audience of {event}" },
            #     { 'text': "Contact Us", 'value': "Contact Us" }
            # ]

        else:
            message = "Do you wish to check with the information of our organized events?"
    # elif benefits:

    #     # Information Retrieval
    #     _, answer = perform_fuzzywuzzy(
    #         result = result,
    #         slot = event,
    #         column = 'event'
    #     )

    #     if answer is not None:
            
    #         # Message
    #         message = answer['benefits']
            
    #         # Buttons
    #         buttons = [
    #             { 'text': "Target Audience", 'value': f"Audience of {event}" },
    #             { 'text': "Main Menu", 'value': "Main Menu" },
    #             { 'text': "Contact Us", 'value': "Contact Us" }
    #         ]
    #     else:
    #         message = "Do you wish to check with the information of our organized events?"

    # elif audience:

    #     # Information Retrieval
    #     _, answer = perform_fuzzywuzzy(
    #         result = result,
    #         slot = event,
    #         column = 'event'
    #     )

    #     if answer is not None:
            
    #         # Message
    #         message = answer['audience']
            
    #         # Buttons
    #         buttons = [
    #             { 'text': "Benefits", 'value': f"Benefits of {event}" },
    #             { 'text': "Main Menu", 'value': "Main Menu" },
    #             { 'text': "Contact Us", 'value': "Contact Us" }
    #         ]
    #     else:
    #         message = "Do you wish to check with the information of our organized events?"
    else:
        message = "Click on the below buttons to find about the conference information of our events"


    return nextIntentWithResponseCard(
        session_attributes,
        message, 
        None,
        None,
        None,
        buttons
    ) 

