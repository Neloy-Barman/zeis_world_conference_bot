import json
import requests
from pytz import timezone 
from datetime import date
from datetime import datetime
from helpers.generic import validate_slot
from helpers.lex_response import nextIntent
from helpers.lex_response import elicit_slot
from helpers.lex_response import nextIntentWithResponseCard
from helpers.lex_response import elicit_slot_with_response_card

def handle_lead_collection(event):

    # Current Intent Name
    intent_name = event['currentIntent']['name']

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}
    print(f"Session Attributes: {session_attributes}")

    name = session_attributes.get('Name', None)
    email = session_attributes.get('Email', None)
    contact_number = session_attributes.get('ContactNumber', None)
    designation = session_attributes.get('Designation', None)

    # Button Options
    options = [
        { 'text': "Conference Info", 'value': "Conference Info" },
        { 'text': "Venue and Schedule", 'value': "Venue and Schedule" },
        { 'text': "Speakers", 'value': "Speakers" },
        { 'text': "Guests", 'value': "Guests" },
        { 'text': "Sponsors", 'value': "Sponsors" },
        { 'text': "About Us", 'value': "About Us" },
        { 'text': "Contact Us", 'value': "Contact Us" },
        { 'text': "Founder Info", 'value': "Founder Info" }
    ]

    if session_attributes.get('Name', None) is None:
        slots = event['currentIntent']['slots']
        print(f"Slots: {slots}")

        # Request for Name
        if slots["name"] is None:
            print("Name is None")

            message = """
                Hello, I am TINA - ZIES' AI-Powered Assistant. I am here to assist you with all the information you need about the upcoming 
                <strong>AI 360 Advanced Powered Learning</strong> conference being held on 28th February, 2025 at Hinjawadi, India. 
                Whether you're looking for event details and timings, speakers, guest of honor profiles or insights into ZIES and its founder, I'm here to help!
            """

            return elicit_slot(
                "name", 
                slots, 
                f"{message}~Can I have your name please?", 
                session_attributes,
                intent_name
            )
        # Validate Name
        if slots["name"] != None:
            print("Name is not None")
            # validate and update the name
            if not validate_slot("name", slots["name"]):
                return elicit_slot(
                    "name", 
                    slots, 
                    "Please enter a valid name.", 
                    session_attributes, 
                    intent_name
                )
            name = slots["name"].title()

        
        # Request for Email Address
        if slots["email"] is None:
            print("email is None")
            return elicit_slot(
                "email", 
                slots, 
                "Please enter your email address", 
                session_attributes,
                intent_name
            )
        # Validate Email Address
        if slots['email'] != None:
            print("Email is not None.")
            # # validate and update the email address
            # if not validate_slot("EmailAddress", slots['email']):
            #     return elicit_slot("email", slots, "Please enter a valid designation email address.", session_attributes, intent_name)
            email = slots['email']


        
        # Request for Contact Number
        if slots["contact_number"] == None:
            print("Contact Number is None")

            return elicit_slot(
                "contact_number", 
                slots, 
                "May I have your phone number?", 
                session_attributes,
                intent_name
            )
        # Validate Contact Number
        if slots["contact_number"] != None:
            print("Contact Number is not None")
            # # validate and update the contact Number
            # if not validate_slot("contact_number", slots["contact_number"]):
            #     return elicit_slot(
            #         "contact_number", 
            #         slots, 
            #         "Please enter a valid phone number", 
            #         session_attributes, 
            #         intent_name
            #     )
            contact_number = slots["contact_number"]


        # Request for designation Name
        if slots["designation"] is None:
            print("Designation is None")
            return elicit_slot(
                "designation", 
                slots, 
                "What's your job title?", 
                session_attributes,
                intent_name
            )
        # Validate designation Name    
        if slots["designation"] != None:
            print("Designation is not None")
            designation = slots["designation"]

        # Setting up session attributes
        session_attributes['Name'] = name
        session_attributes['Email'] = email
        session_attributes['ContactNumber'] = contact_number  
        session_attributes['Designation'] = designation    


        try:

            south_africa = timezone('Asia/Kolkata')
            sa_time = datetime.now(south_africa)
            timenow = sa_time.strftime('%H:%M')
    
            today = date.today()
            print("today", today)

            headers = {'Content-Type': 'application/json'}

            # Handle successful lead submission after all details
            data = {
                "client_id": "71",
                # "center_id": "35",
                "isEdit": "true",
                "bot_client_id": session_attributes['CleintId'],
                "fields": {
                    "job_title": designation
                },
                "contact_name": name,
                "contact_phone": contact_number,
                "country_code": "",
                "contact_email": email,
                "company_name": None,
                "lead_source": "Tina",
                "lead_type": "Hot Lead",
                "lead_date": str(today),
                "lead_time": str(timenow),
                "lead_status": "New",
                "lead_space_id": None
            }

            print(f"Data payload: {data}")

            response = requests.post(
                'https://xywfgrd3z1.execute-api.us-east-1.amazonaws.com/prod/createLeads', 
                headers=headers, 
                data=json.dumps(data)
            )
            
            print(f"Data sending response : {response}")
            
        except Exception as e:
            print("A fatal error occured.")
            print(f"This is the error: {e}")
        finally:
            # Response Message
            message = f"Thank you {name}. I am here to assist you. What would you like to explore further?"

    else:
        message = f"Hello, {name}. I am here to assist you. What would you like to explore further?"

    return nextIntentWithResponseCard(
        session_attributes, 
        message,
        None,
        None,
        None,
        options
    )