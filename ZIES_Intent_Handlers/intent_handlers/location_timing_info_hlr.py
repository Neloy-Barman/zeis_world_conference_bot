from helpers.generic import get_slot_category
from helpers.lex_response import nextIntentWithResponseCard

def handle_location_timing(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Fetching slot values
    location = event['currentIntent']['slots']['Location']
    print(f"Location value: {location}")

    time = event['currentIntent']['slots']['Time']
    print(f"Time value: {time}")

    # Options
    options = [
        { 'text': "Main Menu", 'value': "Main Menu" },
        { 'text': "About Us", 'value': "About Us" },
        { 'text': "Contact Us", 'value': "Contact Us" }
    ]

    # Response Message
    if location is None and time is None:
        message = "The conference will be held on <strong>Friday, 28th February 2025</strong>, from <strong>10:00 AM to 5:00 PM</strong> at <strong>Hyatt Place Pune, Hinjawadi, India</strong>."
    else:
        if location:
            message = "The conference is at <strong>Hyatt Place Pune, Hinjawadi, India</strong>. Attendees can use private vehicles, public transport, or book accommodations nearby if needed."
        else:
            message = "The event will run for a full day, from <strong>10:00 AM to 5:00 PM</strong>."

    return nextIntentWithResponseCard(
        session_attributes,
        message, 
        None,
        None,
        None,
        options
    )

