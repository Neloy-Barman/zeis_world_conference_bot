from helpers.generic import get_slot_category
from helpers.lex_response import nextIntentWithResponseCard

def handle_founder_info(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Response Message
    message = "The Guest of Honours for the AI 360 Advanced Powered Learning Conference are"

    # Options
    options = [
        {
            'text': "Main Menu",
            'value': "Main Menu"
        },
        {
            'text': "About Us",
            'value': "About Us"
        },
        {
            'text': "Contact Us",
            'value': "Contact Us"
        }
    ]

    title = "Zeba Parveen"
    subTitle = "Founder & Director, ZIES"
    imageUrl = "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Founder/Zeba_Parvin.jpg"
    description = """
        Zeba Parveen is the Founder & Director of ZIES, leading initiatives to enhance educational collaborations. 
        She is the host of the 2nd Edition of AI 360 Advanced Powered Learning conference.
    """

    # Response Message
    message = (
        '<img src="'
        + imageUrl
        + '" style="width:285px;border-top-left-radius: 20px;border-top-right-radius: 20px;"><br><br> <div style="display:flex;align-items: center;flex-direction:column"> <b style="font-size: 20px;">'
        + title
        + '</b><p style="font-size: 14px;color: #e1e1e1;margin-top: 5px;">'
        + subTitle
        + "</p></div>"
        + description
        + '<br>'
    )
    
    return nextIntentWithResponseCard(
        session_attributes,
        message, 
        None,
        None,
        None,
        options
    )