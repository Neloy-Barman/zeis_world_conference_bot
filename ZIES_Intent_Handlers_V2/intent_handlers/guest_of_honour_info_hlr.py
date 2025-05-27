import pandas as pd
from data.constants import all_events
from data.constants import guided_buttons
from helpers.generic import create_buttons
from helpers.generic import create_profile_card
from helpers.generic import create_unordered_list_elems
from helpers.lex_response import nextIntentWithResponseCard
from helpers.information_retrieval import perform_fuzzywuzzy

def handle_guest_of_honour(event):

    # Intent Name
    intent_name = event["sessionState"]["intent"]["name"]

    # Session Attributes
    session_attributes = event["sessionState"]["sessionAttributes"] if event["sessionState"]["sessionAttributes"] is not None else {}

    # Reading CSV file
    result = pd.read_csv("./data/events.csv")

    # Initial
    # Message
    message = "Kindly select the event for which you want the guest of honour information"
    # Buttons
    events = all_events
    buttons = [{'text': f'{item}', 'value': f'Guests of ​{item}​'} for item in events]

    # Fetching slot value
    slots = event["sessionState"]["intent"]["slots"]
    guest = slots['Guest']
    print(f"Guest Name: {guest}")

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
                result = pd.read_csv("./data/guests.csv")
                guest_options = result['guest'].to_list()
                # Message
                message = f"""
                    The Guest of Honours for the <strong>{event}</strong> are
                """
                # Buttons
                buttons = create_buttons(guest_options)
            else:
                # Message
                message = "Kindly visit <a href='https://ziesworld.in/' target='_blank' rel='noopener noreferrer'>here</a> to check with the guest of honours info."
                # Buttons
                buttons = create_buttons(guided_buttons)
        else:
            message = "Do you wish to check with the honourale guests information of our organized events?"
    elif guest:

        result = pd.read_csv("./data/guests.csv")

        # Information Retrieval
        _, answer = perform_fuzzywuzzy(
            result = result,
            slot = guest,
            column = 'guest'
        )

        if answer is not None:
            title = answer['guest']
            subTitle = answer['designation']
            imageUrl = answer['imageURL']
            description = answer['desc']

            # Message
            message = create_profile_card(title, subTitle, description, imageUrl)

            # Buttons
            buttons = create_buttons(guided_buttons)

        else:
            message = "Do you wish to check with the guest of honours of our organized events?"
    else:
        message = "Click on the below buttons to find about the honourable guests information of our events"


    return nextIntentWithResponseCard(
        intent_name,
        session_attributes,
        message, 
        None,
        None,
        buttons
    )

