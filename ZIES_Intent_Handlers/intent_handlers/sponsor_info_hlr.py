import pandas as pd
from data.constants import guided_buttons
from helpers.generic import create_buttons
from helpers.generic import create_unordered_list_elems
from helpers.lex_response import nextIntentWithResponseCard
from helpers.information_retrieval import perform_fuzzywuzzy

def handle_sponsor(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Reading CSV file
    result = pd.read_csv("./data/events.csv")

    # Initial
    # Message
    message = "Kindly select the event for which you want sponsor information"
    # Buttons
    events = ['AI 360 Advanced Powered Learning', 'AI Revolutionizing Education']
    buttons = [{'text': f'{item}', 'value': f'Sponsors of ​{item}​'} for item in events]

    # Fetching slot value
    slots = event['currentIntent']['slots']
    partner = slots['Partner']
    print(f"Partner Name: {partner}")

    event = slots['event']
    print(f"Event Name: {event}")

    # Event is not None
    if event:
        # Information Retrieval
        answer, _ = perform_fuzzywuzzy(
            result = result,
            slot = event,
            column = 'event'
        )

        if answer is not None:
            if answer == 0:
                result = pd.read_csv("./data/sponsors.csv")
                partner_options = result['sponsor'].to_list()
                # Message
                message = f"""
                    The conference has esteemed sponsors and partners, including:
                    {create_unordered_list_elems(partner_options)}
                """
                # Buttons
                buttons = create_buttons(partner_options)
            else:
                # Message
                message = "Kindly visit <a href='https://ziesworld.in/'>here</a> to check with the sponsors info."
                # Buttons
                buttons = create_buttons(guided_buttons)
        else:
            message = "Do you wish to check with the sponsors of our organized events?"
    elif partner:

        result = pd.read_csv("./data/sponsors.csv")

        # Information Retrieval
        _, answer = perform_fuzzywuzzy(
            result = result,
            slot = partner,
            column = 'sponsor'
        )

        if answer is not None:
            title = answer['sponsor']
            imageUrl = answer['imageUrl']
            description = answer['desc']

            # Message
            message = (
                '<div style="display:flex;align-items: center;flex-direction:column"> <b style="font-size: 20px;">'
                + title
                + '</b></div><br>'
                + description
                + '<br>'
            )

            # Buttons
            buttons = create_buttons(guided_buttons)

        else:
            message = "Do you wish to check with the sponsors of our organized events?"
    else:
        message = "Click on the below buttons to find about the sponsors information of our events"


    return nextIntentWithResponseCard(
        session_attributes,
        message, 
        None,
        None,
        None,
        buttons
    )

