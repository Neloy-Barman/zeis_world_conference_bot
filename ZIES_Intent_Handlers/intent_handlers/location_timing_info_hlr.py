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

