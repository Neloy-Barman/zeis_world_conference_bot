from helpers.generic import get_slot_category
from helpers.lex_response import nextIntentWithResponseCard

def handle_contact(event):

    # Intent Name
    intent_name = event["sessionState"]["intent"]["name"]

    # Session Attributes
    session_attributes = event["sessionState"]["sessionAttributes"] if event["sessionState"]["sessionAttributes"] is not None else {}
    
    # Fetching slot value
    contact = event["sessionState"]["intent"]["slots"]['Contact']
    print(f"Contact Name: {contact}")
    
    # Options
    options = [
        {
            'text': "Main Menu",
            'value': "Main Menu"
        },
        {
            'text': "About Us",
            'value': "About Us"
        }
    ]

    # Slot Type values
    email = ["email", "official email", "email address", "official email id", "mail address"]

    # List creation with slot type values list and Category
    contacts = [
        (email, "Email")
    ]

    # All the contacts info
    contacts_info = {
        "Email": "The official email for ZIES is <strong>zies2023@gmail.com</strong>."
    }

    # Fetch Category
    contact_cat = None
    if contact:
        contact_cat = get_slot_category(
            slot_lists  = contacts, 
            slot = contact.strip().lower()
        )
        print(f"Categorized partner: {contact_cat}")

    # Response Message 
    if contact is None or contact_cat is None:
        message = """
            Call us at: <strong>+91-96210-47786</strong> Or <strong>+91-97938-85136</strong>
            ~Email us at:</strong> <strong>zies2023@gmail.com</strong>
            ~Visit our instagram handle <strong><a href="https://www.instagram.com/zies_scholarbirds?igsh=d3pmM2VsYzlxMDZm" target="_blank">here</a></strong>
        """
    else:
        
        # Fetch contacts Info
        message = contacts_info[contact_cat]

    title = None
    subTitle = None

    return nextIntentWithResponseCard(
        intent_name,
        session_attributes,
        message, 
        title,
        subTitle,
        options
    )

