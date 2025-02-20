from helpers.lex_response import nextIntent
from helpers.lex_response import nextIntentWithResponseCard

def handle_guest_of_honour(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Fetching slot value
    guest = event['currentIntent']['slots']['Guest']
    print(f"Guest Name: {guest}")

    # Response Message
    message = "The Guest of Honours for the AI 360 Advanced Powered Learning Conference are"

    # Options
    guest_options = [
        {'text': 'Panneerselvam (PS) Madanagopal', 'value': 'Panneerselvam (PS) Madanagopal'},
        {'text': 'Prof. Anil Kashyap', 'value': 'Prof. Anil Kashyap'},
        {'text': 'Prof. (Dr.) Simon Mak', 'value': 'Prof. (Dr.) Simon Mak'},
        {'text': 'Dr. Ashwin Fernandes', 'value': 'Dr. Ashwin Fernandes'},
        {'text': 'Dr. Sunil Shukla', 'value': 'Dr. Sunil Shukla'},
        {'text': 'Dr. Pankaj Mittal', 'value': 'Dr. Pankaj Mittal'},
        {'text': 'Dr. Raghunath Anant Mashelkar', 'value': 'Dr. Raghunath Anant Mashelkar'},
        {'text': 'Dr. Raj Nehru', 'value': 'Dr. Raj Nehru'}
    ]

    # Slot Type values
    PANNEERSELVAM_MADANAGOPAL = ["panneerselvam (ps) madanagopal", "panneerselvam", "ps madanagopal", "madanagopal", "p. s. madanagopal", "p.s. madanagopal", "paneeerselvam", "madan gopal", "psm", "panneer selvam", "panneer"]
    PROF_ANIL_KASHYAP = ["prof. anil kashyap", "prof. anil", "prof. kashyap", "anil kashyap", "dr. anil kashyap",  "anil k.", "kashyap a.", "anil kasyap", "prof anil", "anil kashyap sir", "ak"]
    PROF_DR_SIMON_MAK = ["prof. (dr.) simon mak", "prof. simon", "dr. simon", "simon mak", "prof. mak", "dr. mak", "simon m.", "simmon mak", "simon mac", "prof simon", "dr simon", "sm"]
    DR_ASHWIN_FERNANDES = ["dr. ashwin fernandes", "dr. ashwin", "dr. fernandes", "ashwin fernandes", "ashwin f.", "ashwin fernandis", "dr ashwin", "dr fernandes", "ashwin sir", "af"]
    DR_SUNIL_SHUKLA = ["dr. sunil shukla", "dr. sunil", "dr. shukla", "sunil shukla", "sunil s.", "sunil sukla", "dr sunil", "dr shukla", "sunil shukla sir", "ss"]
    DR_PANKAJ_MITTAL = ["dr. pankaj mittal", "dr. pankaj", "dr. mittal", "pankaj mittal", "pankaj m.", "pankaj mitttal", "dr pankaj", "dr mittal", "pankaj mittal sir", "pm"]
    DR_RAGHUNATH_ANANT_MASHELKAR = ["dr. raghunath anant mashelkar", "dr. raghunath", "dr. mashelkar", "raghunath mashelkar", "raghunath a. mashelkar", "raghunath anant", "dr. anant mashelkar", "raghunath m.", "raghunath maselkar", "dr raghunath", "dr mashelkar", "ram"]
    DR_RAJ_NEHRU = ["dr. raj nehru", "dr. raj", "dr. nehru", "raj nehru", "raj n.", "dr raj", "dr nehru", "raj neheru", "rn" ]


    # guests = [
    #     # (["Panneerselvam (PS) Madanagopal", "Panneerselvam", "PS Madanagopal", "Madanagopal", "P. S. Madanagopal", "P.S. Madanagopal", "Paneeerselvam", "Madan Gopal", "PSM", "Panneer Selvam", "Panneer"], "Panneerselvam (PS) Madanagopal")
    #     (PANNEERSELVAM_MADANAGOPAL, "Panneerselvam (PS) Madanagopal")
    # ]


    guests = [
        (PANNEERSELVAM_MADANAGOPAL, "Panneerselvam (PS) Madanagopal"),
        (PROF_ANIL_KASHYAP, "Prof. Anil Kashyap"),
        (PROF_DR_SIMON_MAK, "Prof. (Dr.) Simon Mak"),
        (DR_ASHWIN_FERNANDES, "Dr. Ashwin Fernandes"),
        (DR_SUNIL_SHUKLA, "Dr. Sunil Shukla"),
        (DR_PANKAJ_MITTAL, "Dr. Pankaj Mittal"),
        (DR_RAGHUNATH_ANANT_MASHELKAR, "Dr. Raghunath Anant Mashelkar"),
        (DR_RAJ_NEHRU, "Dr. Raj Nehru")
    ]

    # All the guest info
    guests_info = {
        "Panneerselvam (PS) Madanagopal": {
            "name": "Panneerselvam (PS) Madanagopal",
            "image_url": "",
            "designation": "Chief Executive Officer, MeitY Startup Hub",
            "description": """
                Panneerselvam (PS) Madanagopal is the Chief Executive Officer of MeitY Startup Hub, under the Ministry of Electronics & Information Technology.
                He leads MeitY Startup Hub, supporting tech-driven startups and AI innovation initiatives.
                """
        },
        "Prof. Anil Kashyap": {
            "name": "Prof. Anil Kashyap",
            "image_url": "",
            "designation": "President, NICMAR University",
            "description": """
                Prof. Anil Kashyap is the President & Chancellor of NICMAR University and also serves as the Director General of NICMAR.
                He has played a key role in advancing AI and construction management education at NICMAR University.
            """
        },
        "Prof. (Dr.) Simon Mak": {
            "name": "Prof. (Dr.) Simon Mak",
            "image_url": "",
            "designation": "Vice Chancellor, UAU",
            "description": """
                Prof. (Dr.) Simon Mak is the first American Founding Vice Chancellor in India, at Universal AI University, Bombay.
                He has pioneered AI-driven higher education programs and has contributed to global AI academic collaborations.
            """
        },
        "Dr. Ashwin Fernandes": {
            "name": "Dr. Ashwin Fernandes",
            "image_url": "",
            "designation": "Executive Director, AMESA",
            "description": """
                Dr. Ashwin Fernandes is the Executive Director for AMESA at QS Quacquarelli Symonds, a global education ranking organization.
                He specializes in global university rankings, AI education policies, and academic excellence strategies.
            """
        },
        "Dr. Sunil Shukla": {
            "name": "Dr. Sunil Shukla",
            "image_url": "",
            "designation": "Director General, EDII",
            "description": """
                Dr. Sunil Shukla is the Director General of the Entrepreneurship Development Institute of India (EDII).
                He has played a key role in promoting AI-driven entrepreneurial strategies and skill development.
            """
        },
        "Dr. Pankaj Mittal": {
            "name": "Dr. Pankaj Mittal",
            "image_url": "",
            "designation": "Secretary General, AIU",
            "description": """
                Dr. Pankaj Mittal is the Secretary General of the Association of Indian Universities (AIU).
                She focuses on policy reforms and the integration of AI into higher education.
            """
        },
        "Dr. Raghunath Anant Mashelkar": {
            "name": "Dr. Raghunath Anant Mashelkar",
            "image_url": "",
            "designation": "Scientist, CSIR India",
            "description": """
                Dr. Raghunath Anant Mashelkar is a renowned scientist and former Director General of CSIR India.
                He has been a strong advocate for AI-driven research and innovation in India.
            """
        },
        "Dr. Raj Nehru": {
            "name": "Dr. Raj Nehru",
            "image_url": "",
            "designation": "Vice Chancellor, SVSU",
            "description": """
                Dr. Raj Nehru is the Vice Chancellor of Shri Vishwakarma Skill University.
                He specializes in AI-powered skill development and vocational education.
            """
        }
    }


    if guest is None:
        return nextIntentWithResponseCard(
            session_attributes,
            message,
            None,
            None,
            None,
            guest_options
        )
    else:
        # Fetch Category
        guest_cat = get_guest_category(
            guests, 
            guest.lower()
        )
        print(f"Categorized guest: {guest_cat}")

        # Fetch guests Info
        info = guests_info[guest_cat]
        title = info['name']
        subTitle = info['designation']
        # imageUrl = info['image_url']
        imageUrl = "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Founder/Zeba_Parvin.jpg"
        message = info['description']

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
            title,
            subTitle,
            imageUrl,
            options
        )

        # return nextIntent(
        #     session_attributes = session_attributes,
        #     message = "This is working"
        # )

def get_guest_category(guests, guest):
    return { name: category for names, category in guests for name in names}.get(guest, None)

