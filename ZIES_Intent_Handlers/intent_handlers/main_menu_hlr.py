from data.constants import all_buttons
from helpers.lex_response import nextIntentWithResponseCard

def handle_main_menu(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Message
    message = "Kindly explore the buttons below to learn more about <strong>AI 360 Advanced Powered Learning</strong> conference or ZIES."

    # Buttons
    button_elems = all_buttons
    buttons = [{'text': f'{button}', 'value': f'{button}'} for button in button_elems]
    
    print(f"Final message: {message}")
    print(f"Final buttons: {buttons}")
        
    return nextIntentWithResponseCard(
        session_attributes,
        message,
        None, 
        None, 
        None,
        buttons
    )