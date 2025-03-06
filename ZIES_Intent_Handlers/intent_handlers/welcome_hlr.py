from data.constants import all_buttons
from helpers.lex_response import nextIntentWithResponseCard

def handle_welcome(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Message
    message = """
        Hello, I am TINA - ZIES' AI-Powered Assistant. I am here to assist you with all the information you need about the upcoming 
        <strong>AI 360 Advanced Powered Learning</strong> conference being held on 28th February, 2025 at Hinjawadi, India. 
        Whether you're looking for event details and timings, speakers, guest of honor profiles or insights into ZIES and its founder, I'm here to help!
        ~How may I assist you today?
    """

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



