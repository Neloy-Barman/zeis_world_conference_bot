from helpers.generic import get_slot_category
from helpers.lex_response import nextIntentWithResponseCard

def handle_sponsor(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Fetching slot value
    partner = event['currentIntent']['slots']['Partner']
    print(f"Partner Name: {partner}")

    # Response Message
    message = """
        The conference has esteemed sponsors and partners, including:
        <ul>
            <li><strong>AI Partner:</strong> Gravitas AI</li>
            <li><strong>Platinum Partner:</strong> NICMAR</li>
            <li><strong>Supporting Partner:</strong> Fretbox</li>
        </ul>
    """

    # Options
    partner_options = [
        {'text': 'Gravitas AI', 'value': 'Gravitas AI'},
        {'text': 'NICMAR', 'value': 'NICMAR'},
        {'text': 'Fretbox', 'value': 'Fretbox'}
    ]

    # Slot Type values
    GRAVITAS_AI = ["gravitas ai"]
    NICMAR = ["nicmar"]
    FRETBOX = ["fretbox"]

    # List creation with slot type values list and Category
    partners = [
        (GRAVITAS_AI, "Gravitas AI"),
        (NICMAR, "NICMAR"),
        (FRETBOX, "Fretbox"),
    ]

    # All the partner info
    partners_info = {
        "Gravitas AI": {
            "name": "Gravitas AI",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Sponsors/gravitas_ai.png",
            "description": """
               Gravitas AI is a niche artificial intelligence company focused on optimizing productivity and enhancing customer experiences. 
               They specialize in Enterprise bots, Chatbots, and Virtual Assistants driven through their own IP NLP technology. 
               Find more details <a href="https://www.gravitas.ai/" target="_blank">here</a>.
            """
        },
        "NICMAR": {
            "name": "NICMAR",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Sponsors/nicmar.jpg",
            "description": """
                NICMAR is a prestigious institution specializing in construction, infrastructure, real estate, and project management education. 
                As the Platinum Partner, NICMAR plays a key role in supporting the AI 360 conference.
            """
        },
        "Fretbox": {
            "name": "Fretbox",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Sponsors/fretbox.jpg",
            "description": """
                Fretbox is a technology-driven platform offering innovative solutions for student housing and residential communities. 
                They support AI-driven advancements in facility management and security.
            """
        }
    }


    # Fetch Category
    partner_cat = None
    if partner:
        partner_cat = get_slot_category(
            slot_lists  = partners, 
            slot = partner.lower()
        )
        print(f"Categorized partner: {partner_cat}")


    if partner is None or partner_cat is None:
        return nextIntentWithResponseCard(
            session_attributes,
            message,
            None,
            None,
            None,
            partner_options
        )
    else:

        # Fetch partners Info
        info = partners_info[partner_cat]
        title = info['name']
        subTitle = None
        imageUrl = info['image_url']
        description = info['description']

        # Response Message
        if imageUrl != "":
            message = (
                '<img src="'
                + imageUrl
                + '" style="width:285px;border-top-left-radius: 20px;border-top-right-radius: 20px;"><br><br> <div style="display:flex;align-items: center;flex-direction:column"> <b style="font-size: 20px;">'
                + title
                + '</b></div><br>'
                + description
                + '<br>'
            )
        else:
            message = (
                '<div style="display:flex;align-items: center;flex-direction:column"> <b style="font-size: 20px;">'
                + title
                + '</b></div><br>'
                + description
                + '<br>'
            )

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

        return nextIntentWithResponseCard(
            session_attributes,
            message, 
            None,
            None,
            None,
            options
        )

