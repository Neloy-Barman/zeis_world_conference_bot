import pandas as pd
from data.constants import guided_buttons
from helpers.generic import create_buttons
from helpers.lex_response import nextIntentWithResponseCard
from helpers.information_retrieval import perform_fuzzywuzzy

def handle_location_timing(event):
    
    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Reading CSV file
    result = pd.read_csv("./data/location_and_timing.csv")

    # Initial
    # Message
    message = "Kindly select the event for which you want location and timing information"
    # Buttons
    events = ['AI 360 Advanced Powered Learning', 'AI Revolutionizing Education']
    buttons = [{'text': f'{item}', 'value': f'Venue and Schedule of ​{item}​'} for item in events]

    # Fetching slot value
    event = event['currentIntent']['slots']['event']
    print(f"Event Name: {event}")

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
            message = answer['location_and_timing']
            # Buttons
            buttons = create_buttons(guided_buttons)
        
        else:
            message = "Do you wish to check with our organized events?"
    else:
        message = "Click on the below buttons to find about location and timing information of our events"

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










    # Response Message
    if location is None and time is None:
        message = """
            The conference will be held on <strong>Friday, 28th February 2025</strong>, from <strong>10:00 AM to 5:00 PM</strong> at <strong>Hyatt Place Pune, Hinjawadi, India</strong>.
            ~<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3781.7333518585947!2d73.73360281131752!3d18.58605646709664!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bbe8789db675%3A0xd4fbe31a328459b1!2sHyatt%20Place%20Pune%20Hinjawadi!5e0!3m2!1sen!2sbd!4v1740394951464!5m2!1sen!2sbd" width="250" height="200" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        """
    else:
        if location:
            message = """
                The conference is at <strong>Hyatt Place Pune, Hinjawadi, India</strong>. Attendees can use private vehicles, public transport, or book accommodations nearby if needed."
                ~<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3781.7333518585947!2d73.73360281131752!3d18.58605646709664!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bbe8789db675%3A0xd4fbe31a328459b1!2sHyatt%20Place%20Pune%20Hinjawadi!5e0!3m2!1sen!2sbd!4v1740394951464!5m2!1sen!2sbd" width="250" height="200" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            """
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

