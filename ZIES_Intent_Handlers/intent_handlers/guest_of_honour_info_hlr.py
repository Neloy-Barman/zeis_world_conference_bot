from helpers.generic import get_slot_category
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
        {'text': 'Prof. Parag Shah', 'value': 'Prof. Parag Shah'},
        {'text': 'Dr. Madhu Chitkara', 'value': 'Dr. Madhu Chitkara'},
        {'text': 'Dr. Swati Mujumdar', 'value': 'Dr. Swati Mujumdar'},
        {'text': 'Col. Yogesh Joshi', 'value': 'Col. Yogesh Joshi'},
        
    ]

    # Slot Type values
    PANNEERSELVAM_MADANAGOPAL = ["panneerselvam (ps) madanagopal", "panneerselvam", "ps madanagopal", "madanagopal", "p. s. madanagopal", "p.s. madanagopal", "paneeerselvam", "madan gopal", "psm", "panneer selvam", "panneer"]
    PROF_ANIL_KASHYAP = ["prof. anil kashyap", "prof. anil", "prof. kashyap", "anil kashyap", "dr. anil kashyap",  "anil k.", "kashyap a.", "anil kasyap", "prof anil", "anil kashyap sir", "ak"]
    PROF_DR_SIMON_MAK = ["prof. (dr.) simon mak", "prof. simon", "dr. simon", "simon mak", "prof. mak", "dr. mak", "simon m.", "simmon mak", "simon mac", "prof simon", "dr simon", "sm"]
    DR_ASHWIN_FERNANDES = ["dr. ashwin fernandes", "dr. ashwin", "dr. fernandes", "ashwin fernandes", "ashwin f.", "ashwin fernandis", "dr ashwin", "dr fernandes", "ashwin sir", "af"]
    PROF_PARAG_SHAH = [ "prof. parag shah", "prof. parag", "prof. shah", "parag shah", "prof parag", "prof shah", "parag", "shah", "proff. parag", "proff. shah", "proff parag", "proff shah", "profesor parag", "profesor shah", "parag s.", "p. shah", "prf. parag", "prf. shah"]
    DR_MADHU_CHITKARA = [ "dr. madhu chitkara", "dr. madhu", "dr. chitkara", "madhu chitkara", "dr madhu", "dr chitkara", "madhu", "chitkara", "drr. madhu", "drr. chitkara", "drr madhu", "drr chitkara","doctor madhu", "doctor chitkara", "madhu c.", "m. chitkara", "dr. madhoo", "dr. chitkra","dr madhoo", "dr chitkra", "madhoo chitkara", "madhu chitkra"]
    DR_SWATI_MUJUMDAR = [ "dr. swati mujumdar", "dr. swati", "dr. mujumdar", "swati mujumdar", "dr swati", "dr mujumdar", "swati", "mujumdar", "drr. swati", "drr. mujumdar", "drr swati", "drr mujumdar","doctor swati", "doctor mujumdar", "swati m.", "s. mujumdar", "dr. swatee", "dr. mujmdar","dr swatee", "dr mujmdar", "swatee mujumdar", "swati mujmdar" ]
    COL_YOGESH_JOSHI = [ "col. yogesh joshi", "col. yogesh", "col. joshi", "yogesh joshi", "col yogesh", "col joshi", "yogesh", "joshi", "coll. yogesh", "coll. joshi", "coll yogesh", "coll joshi","colonel yogesh", "colonel joshi", "yogesh j.", "y. joshi", "col. yogeesh", "col. joshii","col yogeesh", "col joshii", "yogeesh joshi", "yogesh joshii"]

    # List creation with slot type values list and Category
    guests = [
        (PANNEERSELVAM_MADANAGOPAL, "Panneerselvam (PS) Madanagopal"),
        (PROF_ANIL_KASHYAP, "Prof. Anil Kashyap"),
        (PROF_DR_SIMON_MAK, "Prof. (Dr.) Simon Mak"),
        (DR_ASHWIN_FERNANDES, "Dr. Ashwin Fernandes"),
        (PROF_PARAG_SHAH, "Prof. Parag Shah"),
        (DR_MADHU_CHITKARA, "Dr. Madhu Chitkara"),
        (DR_SWATI_MUJUMDAR, "Dr. Swati Mujumdar"),
        (COL_YOGESH_JOSHI, "Col. Yogesh Joshi"),

    ]

    # All the guest info
    guests_info = {
        "Panneerselvam (PS) Madanagopal": {
            "name": "Panneerselvam (PS) Madanagopal",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/PM.jpg",
            "designation": "Chief Executive Officer, MeitY Startup Hub",
            "description": """
                Panneerselvam (PS) Madanagopal is the Chief Executive Officer of MeitY Startup Hub, under the Ministry of Electronics & Information Technology.
                He leads MeitY Startup Hub, supporting tech-driven startups and AI innovation initiatives.
            """
        },
        "Prof. Anil Kashyap": {
            "name": "Prof. Anil Kashyap",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/PAK.jpg",
            "designation": "President, NICMAR University",
            "description": """
                Prof. Anil Kashyap is the President & Chancellor of NICMAR University and also serves as the Director General of NICMAR.
                He has played a key role in advancing AI and construction management education at NICMAR University.
            """
        },
        "Prof. (Dr.) Simon Mak": {
            "name": "Prof. (Dr.) Simon Mak",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/SM.jpg",
            "designation": "Vice Chancellor, UAU",
            "description": """
                Prof. (Dr.) Simon Mak is the first American Founding Vice Chancellor in India, at Universal AI University, Bombay.
                He has pioneered AI-driven higher education programs and has contributed to global AI academic collaborations.
            """
        },
        "Dr. Ashwin Fernandes": {
            "name": "Dr. Ashwin Fernandes",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/AFR.jpg",
            "designation": "Executive Director, AMESA",
            "description": """
                Dr. Ashwin Fernandes is the Executive Director for AMESA at QS Quacquarelli Symonds, a global education ranking organization.
                He specializes in global university rankings, AI education policies, and academic excellence strategies.
            """
        },
        "Prof. Parag Shah": {
            "name": "Prof. Parag Shah",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/PS.png",
            "designation": "Director, MIDAS School of Entrepreneurship",
            "description": """
               Prof. Parag Shah is the Chief Mentor of MIDAS School of Entrepreneurship and the Founding Chairman of Flame University, Pune.
               He has mentored numerous entrepreneurs and played a vital role in fostering startup culture in India.
            """
        },
        "Dr. Madhu Chitkara": {
            "name": "Dr. Madhu Chitkara",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/MC.jpg",
            "designation": "Pro-Chancellor, Chitkara University",
            "description": """
                Dr. Madhu Chitkara is the Co-Founder and Pro Chancellor of Chitkara University, Punjab & HP.
                She has been instrumental in advancing academic excellence and industry partnerships at Chitkara University.
            """
        },
        "Dr. Swati Mujumdar": {
            "name": "Dr. Swati Mujumdar",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/SM.jpg",
            "designation": "Pro-Chancellor, Symbiosis Skill Universities",
            "description": """
                Dr. Swati Mujumdar is the Pro Chancellor of Symbiosis Skills Universities in Indore & Pune.
                She has been a pioneer in integrating AI and technology-driven skills training into education.
            """
        },
        "Col. Yogesh Joshi": {
            "name": "Col. Yogesh Joshi",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/YJ.png",
            "designation": "Director, Hinjawadi Industries Association (HIA)",
            "description": """
                Col. Yogesh Joshi is the President of the Hinjawadi Industries Association (HIA), Pune, Maharashtra.
                He has been a key figure in promoting AI adoption and industry-academia collaboration in Pune.
            """
        },
    }

    # Fetch Category
    guest_cat = None
    if guest:
        guest_cat = get_slot_category(
            slot_lists  = guests, 
            slot = guest.lower()
        )
        print(f"Categorized guest: {guest_cat}")

    if guest is None or guest_cat is None:
        return nextIntentWithResponseCard(
            session_attributes,
            message,
            None,
            None,
            None,
            guest_options
        )
    else:
        
        # Fetch guests Info
        info = guests_info[guest_cat]
        title = info['name']
        subTitle = info['designation']
        imageUrl = info['image_url']
        # imageUrl = "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Founder/Zeba_Parvin.jpg"
        description = info['description']

        # Response Message
        if imageUrl != "":
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
        else:
            message = (
                '<div style="display:flex;align-items: center;flex-direction:column"> <b style="font-size: 20px;">'
                + title
                + '</b><p style="font-size: 14px;color: #e1e1e1;margin-top: 5px;">'
                + subTitle
                + "</p></div>"
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