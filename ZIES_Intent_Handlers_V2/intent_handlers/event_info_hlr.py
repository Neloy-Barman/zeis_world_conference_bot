import pandas as pd
from data.constants import all_events
from data.constants import event_buttons
from data.constants import guided_buttons
from helpers.generic import create_buttons
from helpers.lex_response import nextIntentWithResponseCard
from helpers.information_retrieval import perform_fuzzywuzzy


def handle_event_info(event):

    # Intent Name
    intent_name = event["sessionState"]["intent"]["name"]
    
    # Session Attributes
    session_attributes = event["sessionState"]["sessionAttributes"] if event["sessionState"]["sessionAttributes"] is not None else {}
    
    # Reading CSV file
    result = pd.read_csv("./data/events.csv")
    events = result['event'].to_list()

    # Initial
    # Message
    message = "Kindly select the event for which you want the information"
    # Buttons
    events = all_events
    buttons = create_buttons(events)

    # Fetching slot value
    event = event["sessionState"]["intent"]["slots"]['event']
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
                event_name = "AI 360 Advanced Powered Learning"
            else:
                event_name = "AI Revolutionizing Education Principal Conclave"

            # Message
            message = f"Kindly explore the buttons below to learn more about <strong>{event_name}</strong> conference."

            # Buttons
            options = event_buttons
            buttons = [{'text': f'{item}', 'value': f'{item} of {event_name}'} for item in options]
        
        else:
            message = "Do you wish to check with our organized events?"
    
    else:
        message = "Click on the below buttons to find about the events"


    print(f"Final message: {message}")
    print(f"Final buttons: {buttons}")
        
    return nextIntentWithResponseCard(
        intent_name,
        session_attributes,
        message,
        None, 
        None,
        buttons
    )