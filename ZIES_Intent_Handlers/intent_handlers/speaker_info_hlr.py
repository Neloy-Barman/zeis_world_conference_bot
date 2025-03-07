import pandas as pd
from data.constants import all_events
from data.constants import guided_buttons
from helpers.generic import create_buttons
from helpers.generic import create_profile_card
from helpers.generic import create_unordered_list_elems
from helpers.lex_response import nextIntentWithResponseCard
from helpers.information_retrieval import perform_fuzzywuzzy

def handle_speaker(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Reading CSV file
    result = pd.read_csv("./data/events.csv")

    # Initial
    # Message
    message = "Kindly select the event for which you want the speakers information"
    # Buttons
    events = all_events
    buttons = [{'text': f'{item}', 'value': f'Speakers of ​{item}​'} for item in events]

    # Fetching slot value
    slots = event['currentIntent']['slots']
    speaker = slots['Speaker']
    print(f"Speaker Name: {speaker}")

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
                result = pd.read_csv("./data/speakers.csv")
                speaker_options = result['speaker'].to_list()
                # Message
                message = f"""
                    The speakers of the <strong>{event}</strong> are
                """
                # Buttons
                buttons = create_buttons(speaker_options)
            else:
                # Message
                message = "Kindly visit <a href='https://ziesworld.in/' target='_blank' rel='noopener noreferrer'>here</a> to check with the speakers info."
                # Buttons
                buttons = create_buttons(guided_buttons)
        else:
            message = "Do you wish to check with the honourale speakers information of our organized events?"
    elif speaker:

        result = pd.read_csv("./data/speakers.csv")

        # Information Retrieval
        _, answer = perform_fuzzywuzzy(
            result = result,
            slot = speaker,
            column = 'speaker'
        )

        if answer is not None:
            title = answer['speaker']
            subTitle = answer['designation']
            imageUrl = answer['imageURL']
            description = answer['desc']

            # Message
            message = create_profile_card(title, subTitle, description, imageUrl)

            # Buttons
            buttons = create_buttons(guided_buttons)

        else:
            message = "Do you wish to check with the speakers of our organized events?"
    else:
        message = "Click on the below buttons to find about the speakers information of our events"


    return nextIntentWithResponseCard(
        session_attributes,
        message, 
        None,
        None,
        None,
        buttons
    )

