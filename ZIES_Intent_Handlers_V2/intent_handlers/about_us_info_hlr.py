from helpers.generic import get_slot_category
from helpers.lex_response import nextIntentWithResponseCard

def handle_about_us_info(event):
    
    # Intent Name
    intent_name = event["sessionState"]["intent"]["name"]

    # Session Attributes
    session_attributes = event["sessionState"]["sessionAttributes"] if event["sessionState"]["sessionAttributes"] is not None else {}

    # Fetching slot values
    services = event["sessionState"]["intent"]["slots"]['Services']
    print(f"Services value: {services}")

    events = event["sessionState"]["intent"]["slots"]['Events']
    print(f"Events value: {events}")

    # Options
    options = [
        { 'text': "Our Services", 'value': "Services" },
        { 'text': "ZIES Events", 'value': "ZIES Events" },
        { 'text': "Contact Us", 'value': "Contact Us" }
    ]

    # Response Message
    if services is None and events is None:
        message = """
            <strong>Zeba International Education of Scholarbirds (ZIES)</strong> is dedicated to supporting students in their academic and career growth by 
            bridging the gap between academia and industry. Through tailored guidance, networking opportunities, and career counseling, 
            ZIES empowers students to achieve their goals.
            ~We help students with:
            <ul>
                <li>Career path counseling</li>
                <li>Connections with universities and industry leaders</li>
                <li>Access to educational events and internships</li>
            </ul>
            By organizing exclusive events, ZIES fosters direct interaction with academic and industry experts, paving the way for success in education and beyond.
        """
    else:
        if services:
            message = """
                ZIES provides a wide range of services to support academic and career growth:
                <ul>
                    <li>University connect programs and school activities</li>
                    <li>Vice Chancellor & Principal Conclave</li>
                    <li>National & International Education Fairs</li>
                    <li>School & College Seminars</li>
                    <li>Principal Meets</li>
                    <li>Internship opportunities</li>
                    <li>Assistance with abroad and domestic admissions</li>
                </ul>
            """

            # Options
            options = [
                { 'text': "ZIES Events", 'value': "ZIES Events" },
                { 'text': "Main Menu", 'value': "Main Menu" },
                { 'text': "Contact Us", 'value': "Contact Us" }
            ]

        else:
            message = """
                We organize a variety of impactful educational events, including:
                <ul>
                    <li>Education Fairs</li>
                    <li>Vice Chancellor & Principal Conclaves</li>
                    <li>School and College Seminars</li>
                    <li>Internship Programs</li>
                </ul>
            """

            # Options
            options = [
                { 'text': "Our Services", 'value': "Services" },
                { 'text': "Main Menu", 'value': "Main Menu" },
                { 'text': "Contact Us", 'value': "Contact Us" }
            ]

    return nextIntentWithResponseCard(
        intent_name,
        session_attributes,
        message, 
        None,
        None,
        options
    )

