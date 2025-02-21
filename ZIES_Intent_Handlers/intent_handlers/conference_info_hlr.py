from helpers.generic import get_slot_category
from helpers.lex_response import nextIntentWithResponseCard

def handle_conference_info(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Fetching slot values
    benefits = event['currentIntent']['slots']['Benefits']
    print(f"Benefits value: {benefits}")

    audience = event['currentIntent']['slots']['Audience']
    print(f"Audience value: {audience}")

    # Options
    options = [
        { 'text': "Benefits", 'value': "Benefits" },
        { 'text': "Target Audience", 'value': "Audience" },
        { 'text': "Contact Us", 'value': "Contact Us" }
    ]

    # Response Message
    if benefits is None and audience is None:
        message = """
            The <strong>AI 360 Advanced Powered Learning</strong> conference is a premier collaborative event dedicated to exploring the transformative role of artificial 
            intelligence in higher education. Under the theme <strong>"Future Trends: AI in Higher Education"</strong>, the conference delves into the dynamic intersection 
            of academia and industry, fostering innovation and partnership. 
            ~Key discussions will revolve around AI-powered learning in education, industry-academia collaboration, and cutting-edge AI applications in higher education. 
            By bringing together leading experts, the event aims to define AI's evolving role in shaping future-ready curriculums and ensuring alignment with industry needs, 
            paving the way for a more innovative and sustainable educational landscape.
        """
    else:
        if benefits:
            message = """
                <strong>What Attendees Will Gain: -</strong>
                <ul>
                    <li><strong>Networking Opportunities:</strong> Connect with academics, industry leaders, and policymakers.</li>
                    <li><strong>AI Insights:</strong> Gain valuable knowledge on AI-powered learning and education advancements.</li>
                    <li><strong>Exclusive Benefits:</strong> Explore innovations in education and collaboration opportunities with universities and AI specialists.</li>
                </ul>
                <strong>Key Outcomes: -</strong>
                <ul>
                    <li>Access cutting-edge curriculum recommendations and industry-aligned skills frameworks.</li>
                    <li>Develop a roadmap for research collaborations and knowledge-sharing with top experts.</li>
                </ul>
            """

            # Options
            options = [
                { 'text': "Target Audience", 'value': "Audience" },
                { 'text': "Main Menu", 'value': "Main Menu" },
                { 'text': "Contact Us", 'value': "Contact Us" }
            ]

        else:
            message = """
                <strong>Who Should Attend?</strong>
                <ul>
                    <li><strong>Academia & Industry Professionals:</strong> University leaders, curriculum designers, AI experts, and HR specialists.</li>
                    <li><strong>Policymakers:</strong> Influencers in education and technology shaping the future of learning.</li>
                    <li><strong>Aspiring Minds:</strong> Students and enthusiasts passionate about AI, data, and educational innovation.</li>
                </ul>
                <strong>Students are highly encouraged to join!</strong> This is a great opportunity to explore AI's role in education and connect with industry leaders.
            """

            # Options
            options = [
                { 'text': "Benefits", 'value': "Benefits" },
                { 'text': "Main Menu", 'value': "Main Menu" },
                { 'text': "Contact Us", 'value': "Contact Us" }
            ]

    return nextIntentWithResponseCard(
        session_attributes,
        message, 
        None,
        None,
        None,
        options
    )

