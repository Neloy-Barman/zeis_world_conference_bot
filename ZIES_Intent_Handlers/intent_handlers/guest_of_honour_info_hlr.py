import pandas as pd
from data.constants import guided_buttons
from helpers.generic import create_buttons
from helpers.lex_response import nextIntentWithResponseCard

def handle_guest_of_honour(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Reading CSV file
    result = pd.read_csv("./data/guests.csv")
    guests = result['guest'].to_list()

    # Initial
    # Message
    message = "The Guest of Honours for the <strong>AI Revolutionizing Education - Principal Conclave 2025</strong> are"
    # Buttons
    options = create_buttons(guests)

    # Fetching slot value
    guest = event['currentIntent']['slots']['Guest']
    print(f"Guest Name: {guest}")

    # Guest is not None
    if guest:

       # Information Retrieval
        answer = perform_fuzzywuzzy(
            result = result,
            slot = guest,
            column = 'guest'
        )

        if answer is not None:
            title = answer['guest']
            subTitle = answer['designation']
            description = answer['desc']
            # imageUrl = info['image_url']

            # Message
            message = (
                # '<img src="'
                # + imageUrl
                # + '" style="width:285px;border-top-left-radius: 20px;border-top-right-radius: 20px;"><br><br> <div style="display:flex;align-items: center;flex-direction:column"> <b style="font-size: 20px;">'
                # + title
                title
                + '</b><p style="font-size: 14px;color: #e1e1e1;margin-top: 5px;">'
                + subTitle
                + "</p></div>"
                + description
                + '<br>'
            )

            # Options
            options = create_buttons(guided_buttons)
        
        else:
            message = "Do you wish to check with our honourable guests list?"
    
    else:
        message = "Click on the below buttons to find about the guest of honours"


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