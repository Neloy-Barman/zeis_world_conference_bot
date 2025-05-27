from data.constants import all_buttons
from helpers.lex_response import nextIntentWithResponseCard

def handle_main_menu(event):

    # Intent Name
    intent_name = event["sessionState"]["intent"]["name"]

    # Session Attributes
    session_attributes = event["sessionState"]["sessionAttributes"] if event["sessionState"]["sessionAttributes"] is not None else {}

    # Message
    message = "Kindly explore the buttons below to learn more about the events or ZIES."
    
    # Buttons
    button_elems = all_buttons
    buttons = [{'text': f'{button}', 'value': f'{button}'} for button in button_elems]
    
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