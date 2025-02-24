from helpers.generic import get_slot_category
from helpers.lex_response import nextIntentWithResponseCard

def handle_speaker(event):

    # Session Attributes
    session_attributes = event["sessionAttributes"] if event["sessionAttributes"] is not None else {}

    # Fetching slot value
    speaker = event['currentIntent']['slots']['Speaker']
    print(f"Speaker Name: {speaker}")

    # Response Message
    message = "The Keynote Speakers for the AI 360 Advanced Powered Learning Conference are"

    # Options
    speaker_options = [
        {'text': 'Dr. Ashwini Kumar Sharma', 'value': 'Dr. Ashwini Kumar Sharma'},
        {'text': 'Mr. Aarsh Srivastava', 'value': 'Mr. Aarsh Srivastava'},
        {'text': 'Mr. Ashish Gupta', 'value': 'Mr. Ashish Gupta'},
        {'text': 'Dr. Neeraj Saxena', 'value': 'Dr. Neeraj Saxena'},
        {'text': 'Prof. Prabhat Ranjan', 'value': 'Prof. Prabhat Ranjan'},
        {'text': 'Prof. Rajasekharan Pillai VN', 'value': 'Prof. Rajasekharan Pillai VN'},
        {'text': 'Dr. Rakesh Kumar Jain', 'value': 'Dr. Rakesh Kumar Jain'},
        {'text': 'Dr. Poonam Kashyap', 'value': 'Dr. Poonam Kashyap'},
        {'text': 'Dr. Dharmesh J. Shah', 'value': 'Dr. Dharmesh J. Shah'},
        {'text': 'Dr. Prasad D. Khandekar', 'value': 'Dr. Prasad D. Khandekar'},
        {'text': 'Dr. Sohan Chitlange', 'value': 'Dr. Sohan Chitlange'},
        {'text': 'Prof. (Dr.) Siddharth Jabade', 'value': 'Prof. (Dr.) Siddharth Jabade'},
        {'text': 'Dr. Rajesh Dixit', 'value': 'Dr. Rajesh Dixit'},
        {'text': 'Dr. Kuldeep Raina', 'value': 'Dr. Kuldeep Raina'},
        {'text': 'Dr. Sayalee Gankar', 'value': 'Dr. Sayalee Gankar'},
        {'text': 'Prof. (Dr.) Sundeep Mishra', 'value': 'Prof. (Dr.) Sundeep Mishra'},
        {'text': 'Prof. Sanjeev Sonawane', 'value': 'Prof. Sanjeev Sonawane'},
        {'text': 'Prof. Ankur Kulkarni', 'value': 'Prof. Ankur Kulkarni'},
        {'text': 'Prof. N.J. Pawar', 'value': 'Prof. N.J. Pawar'},
        {'text': 'Prof. (Dr.) B.P. Singh', 'value': 'Prof. (Dr.) B.P. Singh'},
        {'text': 'Prof. (Dr.) Ajay Bhushan', 'value': 'Prof. (Dr.) Ajay Bhushan'},
        {'text': 'Prof. Gopalkrishna Joshi', 'value': 'Prof. Gopalkrishna Joshi'},
        {'text': 'Prof. (Dr.) G.K. Shirude', 'value': 'Prof. (Dr.) G.K. Shirude'},
        {'text': 'Dr. Shrihari (Prakash) Honwad', 'value': 'Dr. Shrihari (Prakash) Honwad'},
        {'text': 'Dr. Atul Kumar', 'value': 'Dr. Atul Kumar'},
        {'text': 'Prof. (Dr.) Tabrez Ahmad', 'value': 'Prof. (Dr.) Tabrez Ahmad'},
        {'text': 'Prof. Adit Gupta', 'value': 'Prof. Adit Gupta'},
        {'text': 'Dr. Devender Pathak', 'value': 'Dr. Devender Pathak'},
        {'text': 'Dr. Subodh Agnihotri', 'value': 'Dr. Subodh Agnihotri'},
        {'text': 'Dr. R. Ganesan', 'value': 'Dr. R. Ganesan'},
        {'text': 'Dr. Rajesh Khanna', 'value': 'Dr. Rajesh Khanna'},
        {'text': 'Dr. Shrirang Altekar', 'value': 'Dr. Shrirang Altekar'},
        {'text': 'Dr. Girish Kumar Chaudhari', 'value': 'Dr. Girish Kumar Chaudhari'},
        {'text': 'Dr. Prashant Dave', 'value': 'Dr. Prashant Dave'},
        {'text': 'Dr. N.B. Bhalerao', 'value': 'Dr. N.B. Bhalerao'},
        {'text': 'Dr. Mahesh Chitnis', 'value': 'Dr. Mahesh Chitnis'},
        {'text': 'Dr. Deepak D. Patil', 'value': 'Dr. Deepak D. Patil'},
        {'text': 'Dr. Pawan Sharma', 'value': 'Dr. Pawan Sharma'}
    ]

    # Slot Type values
    ASHWINI_KUMAR_SHARMA = [ "dr. ashwini kumar sharma", "dr. ashwini", "dr. kumar", "dr. sharma", "ashwini kumar sharma", "ashwini sharma", "kumar sharma", "dr. ashwini k. sharma", "dr. a.k. sharma", "ashwini k. sharma", "a.k. sharma", "dr. ashwani", "dr. ashwani sharma", "dr. ashwin", "dr. ashwin sharma" ]
    AARSH_SRIVASTAVA = [ "mr. aarsh srivastava", "mr. aarsh", "mr. srivastava", "aarsh srivastava", "mr. aarsh s.", "mr. a. srivastava", "aarsh s.", "a. srivastava", "mr. arsh", "mr. arsh srivastava", "mr. aarsh srivasta", "mr. aarsh srivastav" ]
    ASHISH_GUPTA = [ "mr. ashish gupta", "mr. ashish", "mr. gupta", "ashish gupta", "mr. ashish g.", "mr. a. gupta", "ashish g.", "a. gupta", "mr. ashis", "mr. ashis gupta", "mr. ashish guptaa" ]
    NEERAJ_SAXENA = [ "dr. neeraj saxena", "dr. neeraj", "dr. saxena", "neeraj saxena", "dr. neeraj s.", "dr. n. saxena", "neeraj s.", "n. saxena", "dr. neeeraj", "dr. neeeraj saxena", "dr. neeraj saxana", "dr. neeraj saaxena" ]
    PRABHAT_RANJAN = [ "prof. prabhat ranjan", "prof. prabhat", "prof. ranjan", "prabhat ranjan", "prof. prabhat r.", "prof. p. ranjan", "prabhat r.", "p. ranjan", "prof. prabhath", "prof. prabhath ranjan", "prof. prabhat rajan", "prof. prabat", "prof. prabat ranjan" ]
    RAJASEKHARAN_PILLAI_VN = [ "prof. rajasekharan pillai vn", "prof. rajasekharan", "prof. pillai", "rajasekharan pillai vn", "prof. rajasekharan pillai", "prof. r. pillai vn", "rajasekharan pillai", "r. pillai vn", "prof. rajasekaran", "prof. rajasekaran pillai", "prof. rajasekharan pilla", "prof. rajasekharan v.n." ]
    RAKESH_KUMAR_JAIN = [ "dr. rakesh kumar jain", "dr. rakesh", "dr. kumar", "dr. jain", "rakesh kumar jain", "rakesh jain", "kumar jain", "dr. rakesh k. jain", "dr. r.k. jain", "rakesh k. jain", "r.k. jain", "dr. rakesh", "dr. rakesh jain", "dr. rakesh j.", "dr. r. jain" ]
    POONAM_KASHYAP = [ "dr. poonam kashyap", "dr. poonam", "dr. kashyap", "poonam kashyap", "dr. poonam k.", "dr. p. kashyap", "poonam k.", "p. kashyap", "dr. poonaam", "dr. poonaam kashyap", "dr. poonam kashyaap" ]
    DHARMESH_J_SHAH = [ "dr. dharmesh j. shah", "dr. dharmesh", "dr. shah", "dharmesh j. shah", "dr. dharmesh shah", "dr. d.j. shah", "dharmesh shah", "d.j. shah", "dr. dharmish", "dr. dharmish shah", "dr. dharmesh s.", "dr. d. shah" ]
    PRASAD_D_KHANDEKAR = [ "dr. prasad d. khandekar", "dr. prasad", "dr. khandekar", "prasad d. khandekar", "dr. prasad khandekar", "dr. p.d. khandekar", "prasad khandekar", "p.d. khandekar", "dr. prasadd", "dr. prasadd khandekar", "dr. prasad khadekar" ]
    SOHAN_CHITLANGE = [ "dr. sohan chitlange", "dr. sohan", "dr. chitlange", "sohan chitlange", "dr. sohan c.", "dr. s. chitlange", "sohan c.", "s. chitlange", "dr. sohaan", "dr. sohaan chitlange", "dr. sohan chitlangi" ]
    SIDDHARTH_JABADE = [ "prof. (dr.) siddharth jabade", "prof. siddharth", "dr. jabade", "siddharth jabade", "prof. (dr.) siddharth j.", "prof. (dr.) s. jabade", "siddharth j.", "s. jabade", "prof. sidharth", "dr. sidharth jabade", "prof. siddharth jabaade" ]
    RAJESH_DIXIT = [ "dr. rajesh dixit", "dr. rajesh", "dr. dixit", "rajesh dixit", "dr. rajesh d.", "dr. r. dixit", "rajesh d.", "r. dixit", "dr. rajesh dixit", "dr. rajesh dikshit", "dr. rajesh dixit ji" ]
    KULDEEP_RAINA = [ "dr. kuldeep raina", "dr. kuldeep", "dr. raina", "kuldeep raina", "dr. kuldeep r.", "dr. k. raina", "kuldeep r.", "k. raina", "dr. kuldip", "dr. kuldip raina", "dr. kuldeep rainaa" ]
    SAYALEE_GANKAR = [ "dr. sayalee gankar", "dr. sayalee", "dr. gankar", "sayalee gankar", "dr. sayalee g.", "dr. s. gankar", "sayalee g.", "s. gankar", "dr. sayale", "dr. sayale gankar", "dr. sayalee gankaa" ]
    SUNDEEP_MISHRA = [ "prof. (dr.) sundeep mishra", "prof. (dr.) sundeep", "prof. (dr.) mishra", "sundeep mishra", "prof. sundeep mishra", "prof. (dr.) sundeep m.", "prof. (dr.) s. mishra", "sundeep m.", "s. mishra", "prof. sundip", "prof. sundip mishra" ]
    SANJEEV_SONAWANE = [ "prof. sanjeev sonawane", "prof. sanjeev", "prof. sonawane", "sanjeev sonawane", "prof. sanjeev s.", "prof. s. sonawane", "sanjeev s.", "s. sonawane", "prof. sanjiv", "prof. sanjiv sonawane", "prof. sanjeev sonavane" ]
    ANKUR_KULKARNI = [ "prof. ankur kulkarni", "prof. ankur", "prof. kulkarni", "ankur kulkarni", "prof. ankur k.", "prof. a. kulkarni", "ankur k.", "a. kulkarni", "prof. anku", "prof. anku kulkarni", "prof. ankur kulkarnii" ]
    NJ_PAWAR = [ "prof. n.j. pawar", "prof. n.j. pawar", "prof. nj pawar", "n.j. pawar", "nj pawar", "prof. n. j. pawar", "prof. n. pawar", "n. j. pawar", "n. pawar", "prof. nj paawar", "prof. n.j. paawar" ]
    BP_SINGH = [ "prof. (dr.) b.p. singh", "prof. (dr.) b.p. singh", "prof. (dr.) bp singh", "b.p. singh", "bp singh", "prof. b. p. singh", "prof. b. singh", "b. p. singh", "b. singh", "prof. (dr.) bp sing", "prof. (dr.) b.p. sing" ]
    AJAY_BHUSHAN = [ "prof. (dr.) ajay bhushan", "prof. (dr.) ajay", "prof. (dr.) bhushan", "ajay bhushan", "prof. ajay bhushan", "prof. (dr.) ajay b.", "prof. (dr.) a. bhushan", "ajay b.", "a. bhushan", "prof. (dr.) ajai", "prof. (dr.) ajai bhushan" ]
    GOPALKRISHNA_JOSHI = [ "prof. gopalkrishna joshi", "prof. gopalkrishna", "prof. joshi", "gopalkrishna joshi", "prof. gopalkrishna j.", "prof. g. joshi", "gopalkrishna j.", "g. joshi", "prof. gopalkrishna", "prof. gopalkrishna joshi", "prof. gopalkrishn joshi" ]
    GK_SHIRUDE = [ "prof. (dr.) g.k. shirude", "prof. (dr.) g.k. shirude", "prof. (dr.) gk shirude", "g.k. shirude", "gk shirude", "prof. g. k. shirude", "prof. g. shirude", "g. k. shirude", "g. shirude", "prof. (dr.) gk shrud", "prof. (dr.) g.k. shrud" ]
    SHRIHARI_HONWAD = [ "dr. shrihari (prakash) honwad", "dr. shrihari", "dr. honwad", "shrihari honwad", "dr. shrihari h.", "dr. s. honwad", "shrihari h.", "s. honwad", "dr. shrihari (prakash)", "dr. shrihari prakash honwad", "dr. shrihari honwaad" ]
    ATUL_KUMAR = [ "dr. atul kumar", "dr. atul", "dr. kumar", "atul kumar", "dr. atul k.", "dr. a. kumar", "atul k.", "a. kumar", "dr. atul kumarr", "dr. atull kumar", "dr. atul kumaar" ]
    TABREZ_AHMAD = [ "prof. (dr.) tabrez ahmad", "prof. (dr.) tabrez", "prof. (dr.) ahmad", "tabrez ahmad", "prof. tabrez ahmad", "prof. (dr.) tabrez a.", "prof. (dr.) t. ahmad", "tabrez a.", "t. ahmad", "prof. (dr.) tabrej", "prof. (dr.) tabrej ahmad" ]
    ADIT_GUPTA = [ "prof. adit gupta", "prof. adit", "prof. gupta", "adit gupta", "prof. adit g.", "prof. a. gupta", "adit g.", "a. gupta", "prof. aditt", "prof. aditt gupta", "prof. adit guptaa" ]
    DEVENDER_PATHAK = [ "dr. devender pathak", "dr. devender", "dr. pathak", "devender pathak", "dr. devender p.", "dr. d. pathak", "devender p.", "d. pathak", "dr. devndar", "dr. devndar pathak", "dr. devender pathakk" ]
    SUBODH_AGNIHOTRI = [ "dr. subodh agnihotri", "dr. subodh", "dr. agnihotri", "subodh agnihotri", "dr. subodh a.", "dr. s. agnihotri", "subodh a.", "s. agnihotri", "dr. subbdh", "dr. subbdh agnihotri", "dr. subodh agnihotrii" ]
    R_GANESAN = [ "dr. r. ganesan", "dr. r. ganesan", "dr. ganesan", "r. ganesan", "dr. r ganesan", "dr. r. ganeshan", "r ganeshan", "dr. r. ganesann", "dr. r ganesann" ]
    RAJESH_KHANNA = [ "dr. rajesh khanna", "dr. rajesh", "dr. khanna", "rajesh khanna", "dr. rajesh k.", "dr. r. khanna", "rajesh k.", "r. khanna", "dr. rajesh khannaa", "dr. rajesh khana", "dr. rajesh khann" ]
    SHRIRANG_ALTEKAR = [ "dr. shrirang altekar", "dr. shrirang", "dr. altekar", "shrirang altekar", "dr. shrirang a.", "dr. s. altekar", "shrirang a.", "s. altekar", "dr. shirrang", "dr. shirrang altekar", "dr. shrirang altekarr" ]
    GIRISH_KUMAR_CHAUDHARI = [ "dr. girish kumar chaudhari", "dr. girish", "dr. kumar", "dr. chaudhari", "girish kumar chaudhari", "dr. girish k. chaudhari", "dr. g. kumar chaudhari", "girish k. chaudhari", "g. kumar chaudhari", "dr. girish chaudhari", "dr. girish chaoudhari" ]
    PRASHANT_DAVE = [ "dr. prashant dave", "dr. prashant", "dr. dave", "prashant dave", "dr. prashant d.", "dr. p. dave", "prashant d.", "p. dave", "dr. prashannt", "dr. prashannt dave", "dr. prashant dvae" ]
    NB_BHALERAO = [ "dr. n.b. bhalerao", "dr. n.b. bhalerao", "dr. nb bhalerao", "n.b. bhalerao", "nb bhalerao", "dr. n. b. bhalerao", "dr. n. bhalerao", "n. b. bhalerao", "n. bhalerao", "dr. nb bhalrao", "dr. n.b. bhalrao" ]
    MAHESH_CHITNIS = [ "dr. mahesh chitnis", "dr. mahesh", "dr. chitnis", "mahesh chitnis", "dr. mahesh c.", "dr. m. chitnis", "mahesh c.", "m. chitnis", "dr. maheesh", "dr. maheesh chitnis", "dr. mahesh chitniss" ]
    DEEPAK_PATIL = [ "dr. deepak d. patil", "dr. deepak", "dr. patil", "deepak d. patil", "dr. deepak d. p.", "dr. d. patil", "deepak d. p.", "d. patil", "dr. deepakk", "dr. deepakk patil", "dr. deepak pattil" ]
    PAWAN_SHARMA = [ "dr. pawan sharma", "dr. pawan", "dr. sharma", "pawan sharma", "dr. pawan s.", "dr. p. sharma", "pawan s.", "p. sharma", "dr. pawann", "dr. pawann sharma", "dr. pawan sharmma" ]


    # List creation with slot type values list and Category
    speakers = [
        (ASHWINI_KUMAR_SHARMA, "Dr. Ashwini Kumar Sharma"),
        (AARSH_SRIVASTAVA, "Mr. Aarsh Srivastava"),
        (ASHISH_GUPTA, "Mr. Ashish Gupta"),
        (NEERAJ_SAXENA, "Dr. Neeraj Saxena"),
        (PRABHAT_RANJAN, "Prof. Prabhat Ranjan"),
        (RAJASEKHARAN_PILLAI_VN, "Prof. Rajasekharan Pillai VN"),
        (RAKESH_KUMAR_JAIN, "Dr. Rakesh Kumar Jain"),
        (POONAM_KASHYAP, "Dr. Poonam Kashyap"),
        (DHARMESH_J_SHAH, "Dr. Dharmesh J. Shah"),
        (PRASAD_D_KHANDEKAR, "Dr. Prasad D. Khandekar"),
        (SOHAN_CHITLANGE, "Dr. Sohan Chitlange"),
        (SIDDHARTH_JABADE, "Prof. (Dr.) Siddharth Jabade"),
        (RAJESH_DIXIT, "Dr. Rajesh Dixit"),
        (KULDEEP_RAINA, "Dr. Kuldeep Raina"),
        (SAYALEE_GANKAR, "Dr. Sayalee Gankar"),
        (SUNDEEP_MISHRA, "Prof. (Dr.) Sundeep Mishra"),
        (SANJEEV_SONAWANE, "Prof. Sanjeev Sonawane"),
        (ANKUR_KULKARNI, "Prof. Ankur Kulkarni"),
        (NJ_PAWAR, "Prof. N.J. Pawar"),
        (BP_SINGH, "Prof. (Dr.) B.P. Singh"),
        (AJAY_BHUSHAN, "Prof. (Dr.) Ajay Bhushan"),
        (GOPALKRISHNA_JOSHI, "Prof. Gopalkrishna Joshi"),
        (GK_SHIRUDE, "Prof. (Dr.) G.K. Shirude"),
        (SHRIHARI_HONWAD, "Dr. Shrihari (Prakash) Honwad"),
        (ATUL_KUMAR, "Dr. Atul Kumar"),
        (TABREZ_AHMAD, "Prof. (Dr.) Tabrez Ahmad"),
        (ADIT_GUPTA, "Prof. Adit Gupta"),
        (DEVENDER_PATHAK, "Dr. Devender Pathak"),
        (SUBODH_AGNIHOTRI, "Dr. Subodh Agnihotri"),
        (R_GANESAN, "Dr. R. Ganesan"),
        (RAJESH_KHANNA, "Dr. Rajesh Khanna"),
        (SHRIRANG_ALTEKAR, "Dr. Shrirang Altekar"),
        (GIRISH_KUMAR_CHAUDHARI, "Dr. Girish Kumar Chaudhari"),
        (PRASHANT_DAVE, "Dr. Prashant Dave"),
        (NB_BHALERAO, "Dr. N.B. Bhalerao"),
        (MAHESH_CHITNIS, "Dr. Mahesh Chitnis"),
        (DEEPAK_PATIL, "Dr. Deepak D. Patil"),
        (PAWAN_SHARMA, "Dr. Pawan Sharma")
    ]

    # All the speaker info
    speakers_info = {
        "Dr. Ashwini Kumar Sharma": {
            "name": "Dr. Ashwini Kumar Sharma",
            "image_url": "",
            "designation": "Director General, NIELIT",
            "description": """
                Dr. Ashwini Kumar Sharma is the Pro Chancellor of Vijaybhoomi University and Director General of NIELIT, Govt of India.
                He leads initiatives on AI-driven education and technology-based skill development in India.
            """
        },
        "Mr. Aarsh Srivastava": {
            "name": "Mr. Aarsh Srivastava",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/MAS.jpg",
            "designation": "CEO, Gravitas AI",
            "description": """
                Mr. Aarsh Srivastava is CEO & Co- Founder of Gravitas AI.
                He is an AI strategist with more than a decade's experience in AI products & solutions. He is Industry Advisor to Manipal University for AI & Data Science.
            """
        },
        "Mr. Ashish Gupta": {
            "name": "Mr. Ashish Gupta",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/AG.jpg",
            "designation": "CEO, FretBox",
            "description": """
                Mr. Ashish Gupta is the Founder and CEO of FretBox.
            """
        },
        "Dr. Neeraj Saxena": {
            "name": "Dr. Neeraj Saxena",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/NS.jpg",
            "designation": "Chancellor, JIS University",
            "description": """
                Dr. Neeraj Saxena is the Pro Chancellor of JIS University.
                He focuses on integrating AI and innovation into higher education curricula.
            """
        },
        "Prof. Prabhat Ranjan": {
            "name": "Prof. Prabhat Ranjan",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/PR.jpg",
            "designation": "Vice Chancellor, D Y Patil International University",
            "description": """
                Prof. Prabhat Ranjan is the Vice Chancellor of D Y Patil International University, Akurdi, Pune.
                He advocates for futuristic AI-driven university programs.
            """
        },
        "Prof. Rajasekharan Pillai VN": {
            "name": "Prof. Rajasekharan Pillai VN",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/RPVN.jpg",
            "designation": "Vice Chancellor, Somaiya Vidyavihar University",
            "description": """
                Prof. Rajasekharan Pillai is the Vice Chancellor of Somaiya Vidyavihar University.
                His expertise lies in AI ethics and policy frameworks in education.
            """
        },
        "Dr. Rakesh Kumar Jain": {
            "name": "Dr. Rakesh Kumar Jain",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/RKJ.jpg",
            "designation": "Vice Chancellor, Ajeenkya D Y Patil University",
            "description": """
                Dr. Rakesh Kumar Jain is the Vice Chancellor of Ajeenkya D Y Patil University, Pune.
                He has introduced AI-based learning modules and research collaborations at the university.
            """
        },
        "Dr. Poonam Kashyap": {
            "name": "Dr. Poonam Kashyap",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/PK.jpg",
            "designation": "Vice Chancellor, Alard University",
            "description": """
                Dr. Poonam Kashyap is the Vice Chancellor of Alard University, Pune.
                She promotes AI integration in interdisciplinary studies.
            """
        },
        "Dr. Dharmesh J. Shah": {
            "name": "Dr. Dharmesh J. Shah",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/DJS.jpg",
            "designation": "Vice Chancellor, Indrashil University",
            "description": """
                Dr. Dharmesh J. Shah is the Vice Chancellor of Indrashil University, Gujarat.
                He focuses on AI-driven healthcare innovations.
            """
        },
        "Dr. Prasad D. Khandekar": {
            "name": "Dr. Prasad D. Khandekar",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/PDK.jpg",
            "designation": "Vice Chancellor, DES Pune University",
            "description": """
                Dr. Prasad D Khandekar is the Vice Chancellor of DES Pune University, Pune.
                He specializes in AI applications in engineering education.
            """
        },
        "Dr. Sohan Chitlange": {
            "name": "Dr. Sohan Chitlange",
            "image_url": "",
            "designation": "Vice Chancellor, D Y Patil Dnyan Prasad University",
            "description": """
                Dr. Sohan Chitlange is the Vice Chancellor of D Y Patil Dnyan Prasad University, Pune.
                He integrates AI research into pharmaceutical sciences.
            """
        },
        "Prof. (Dr.) Siddharth Jabade": {
            "name": "Prof. (Dr.) Siddharth Jabade",
            "image_url": "",
            "designation": "Vice Chancellor, Vishwakarma University",
            "description": """
                Prof. (Dr.) Siddharth Jabade is the Vice Chancellor of Vishwakarma University, Pune.
                He leads AI-based skill development initiatives.
            """
        },
        "Dr. Rajesh Dixit": {
            "name": "Dr. Rajesh Dixit",
            "image_url": "",
            "designation": "Vice Chancellor, Renaissance University",
            "description": """
                Dr. Rajesh Dixit is the Vice Chancellor of Renaissance University, Indore.
                He promotes AI-driven entrepreneurial education.
            """
        },
        "Dr. Kuldeep Raina": {
            "name": "Dr. Kuldeep Raina",
            "image_url": "",
            "designation": "Vice Chancellor, Ramaiah University",
            "description": """
                Dr. Kuldeep Raina is the Vice Chancellor of Ramaiah University.
                He works on AI-driven policy frameworks in higher education.
            """
        },
        "Dr. Sayalee Gankar": {
            "name": "Dr. Sayalee Gankar",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/SG.jpg",
            "designation": "Vice Chancellor, D Y Patil University",
            "description": """
                Dr. Sayalee Gankar is the Vice Chancellor of D Y Patil University Pune, Ambi Maharashtra.
                She focuses on AI-driven business strategies in management studies.
            """
        },
        "Prof. (Dr.) Sundeep Mishra": {
            "name": "Prof. (Dr.) Sundeep Mishra",
            "image_url": "",
            "designation": "Vice Chancellor, G H Raisoni University",
            "description": """
                Dr. Sudhir U. Meshram is the Vice Chancellor of G H Raisoni University, Maharashtra.
                He promotes AI-driven research in engineering and management education.
            """
        },
        "Prof. Sanjeev Sonawane": {
            "name": "Prof. Sanjeev Sonawane",
            "image_url": "",
            "designation": "Vice Chancellor, Yashwantrao Chavan Maharashtra Open University",
            "description": """  
                Prof. Sanjeev Sonawane is the Vice Chancellor of Yashwantrao Chavan Maharashtra Open University, Nashik.
            """
        },
        "Prof. Ankur Kulkarni": {
            "name": "Prof. Ankur Kulkarni",
            "image_url": "",
            "designation": "Vice Chancellor, SAGE University",
            "description": """
                Prof. Ankur Kulkarni is the Vice Chancellor of SAGE University, Indore.
            """
        },
        "Prof. N.J. Pawar": {
            "name": "Prof. N.J. Pawar",
            "image_url": "",
            "designation": "Vice Chancellor, Dr. D Y Patil Vidyapeeth",
            "description": """
                Prof. N.J. Pawar is the Vice Chancellor of Dr. D Y Patil Vidyapeeth, Pune.
            """
        },
        "Prof. (Dr.) B.P. Singh": {
            "name": "Prof. (Dr.) B.P. Singh",
            "image_url": "",
            "designation": "Vice Chancellor, Maharishi University of Information Technology",
            "description": """
                Prof. (Dr.) B.P. Singh is the Vice Chancellor of Maharishi University of Information Technology.
            """
        },
        "Prof. (Dr.) Ajay Bhushan": {
            "name": "Prof. (Dr.) Ajay Bhushan",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/AB.jpg",
            "designation": "Vice Chancellor, Scope Global Skills University",
            "description": """
                Prof. (Dr.) Ajay Bhushan is the Vice Chancellor of Scope Global Skills University, Bhopal, Madhya Pradesh.
            """
        },
        "Prof. Gopalkrishna Joshi": {
            "name": "Prof. Gopalkrishna Joshi",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/Gj.jpg",
            "designation": "Vice Chancellor, MIT Vishwaprayag University",
            "description": """
                Prof. Gopalkrishna Joshi is the Founding Vice Chancellor of MIT Vishwaprayag University, Solapur.
            """
        },
        "Prof. (Dr.) G.K. Shirude": {
            "name": "Prof. (Dr.) G.K. Shirude",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/GKS.jpg",
            "designation": "Vice Chancellor, Sri Balaji University",
            "description": """
                Prof. (Dr.) G.K. Shirude is the Vice Chancellor of Sri Balaji University, Pune.
            """
        },
        "Dr. Shrihari (Prakash) Honwad": {
            "name": "Dr. Shrihari (Prakash) Honwad",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/SPH.jpg",
            "designation": "Vice Chancellor",
            "description": """
                Dr. Shrihari (Prakash) Honwad has served as Vice Chancellor at multiple AI-level universities and is associated with the Indian Institute of Science (IISc).
            """
        },
        "Dr. Atul Kumar": {
            "name": "Dr. Atul Kumar",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/AK.jpg",
            "designation": "Dean, Dr. D Y Patil B-School",
            "description": """
                Dr. Atul Kumar is the Dean of Dr. D Y Patil B-School, Pune, Maharashtra.
            """
        },
        "Prof. (Dr.) Tabrez Ahmad": {
            "name": "Prof. (Dr.) Tabrez Ahmad",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/TA.jpg",
            "designation": "Dean, GD Goenka University",
            "description": """
                Prof. (Dr.) Tabrez Ahmad is the Dean of Manav Law School and has previously served as the Vice Chancellor of GD Goenka University.
            """
        },
        "Prof. Adit Gupta": {
            "name": "Prof. Adit Gupta",
            "image_url": "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/AGU.jpg",
            "designation": "Director, Institute of Education & Research",
            "description": """
                Prof. Adit Gupta is the Director of the Institute of Education & Research.
            """
        },
        "Dr. Devender Pathak": {
            "name": "Dr. Devender Pathak",
            "image_url": "",
            "designation": "Vice Chancellor, Oriental University",
            "description": """
                Dr. Devender Pathak is the Vice Chancellor of Oriental University, Indore.
                He works on AI-powered learning models for emerging technology fields.
            """
        },
        "Dr. Subodh Agnihotri": {
            "name": "Dr. Subodh Agnihotri",
            "image_url": "",
            "designation": "Vice Chancellor, Ajeenkya DY Patil University",
            "description": """
                Dr. Subodh Agnihotri is the Vice Chancellor of Ajeenkya DY Patil University, Pune.
                He focuses on AI in healthcare and biomedical innovations.
            """
        },
        "Dr. R. Ganesan": {
            "name": "Dr. R. Ganesan",
            "image_url": "",
            "designation": "Vice Chancellor, Noorul Islam Centre",
            "description": """
            Dr. R. Ganesan is the Vice Chancellor of Noorul Islam Centre for Higher Education.
            He integrates AI-based smart learning techniques into academic programs.
            """
        },
        "Dr. Rajesh Khanna": {
            "name": "Dr. Rajesh Khanna",
            "image_url": "",
            "designation": "Vice Chancellor, D Y Patil International University",
            "description": """
                Dr. Rajesh Khanna is the Vice Chancellor of D Y Patil International University, Akurdi, Pune.
                He promotes AI-driven business intelligence and analytics.
            """
        },
        "Dr. Shrirang Altekar": {
            "name": "Dr. Shrirang Altekar",
            "image_url": "",
            "designation": "Vice Chancellor, MIT ADT University",
            "description": """
                Dr. Shrirang Altekar is the Vice Chancellor of MIT ADT University, Pune.
                He integrates AI-based decision-making frameworks in education.
            """
        },
        "Dr. Girish Kumar Chaudhari": {
            "name": "Dr. Girish Kumar Chaudhari",
            "image_url": "",
            "designation": "Vice Chancellor, Sanjay Ghodawat University",
            "description": """
                Dr. Girish Kumar Chaudhari is the Vice Chancellor of Sanjay Ghodawat University, Maharashtra.
                He develops AI solutions for rural and agricultural development.
            """
        },
        "Dr. Prashant Dave": {
            "name": "Dr. Prashant Dave",
            "image_url": "",
            "designation": "Vice Chancellor, Indus University",
            "description": """
                Dr. Prashant Dave is the Vice Chancellor of Indus University, Gujarat.
                He emphasizes AI applications in environmental sciences and sustainability.
            """
        },
        "Dr. N.B. Bhalerao": {
            "name": "Dr. N.B. Bhalerao",
            "image_url": "",
            "designation": "Vice Chancellor, K.K. University",
            "description": """
                Dr. N.B. Bhalerao is the Vice Chancellor of K.K. University, Bihar.
                He researches AI-driven solutions for smart cities.
            """
        },
        "Dr. Mahesh Chitnis": {
            "name": "Dr. Mahesh Chitnis",
            "image_url": "",
            "designation": "Vice Chancellor, Swami Vivekanand University",
            "description": """
                Dr. Mahesh Chitnis is the Vice Chancellor of Swami Vivekanand University, Madhya Pradesh.
                He promotes AI-based security solutions for digital education.
            """
        },
        "Dr. Deepak D. Patil": {
            "name": "Dr. Deepak D. Patil",
            "image_url": "",
            "designation": "Vice Chancellor, Sandip University",
            "description": """
                Dr. Deepak D. Patil is the Vice Chancellor of Sandip University, Nashik.
                He specializes in AI for robotics and automation.
            """
        },
        "Dr. Pawan Sharma": {
            "name": "Dr. Pawan Sharma",
            "image_url": "",
            "designation": "Vice Chancellor, JJT University",
            "description": """
                Dr. Pawan Sharma is the Vice Chancellor of JJT University, Rajasthan.
                He promotes AI-based research in space technology.
            """
        },
        "Dr. Mukesh Tiwari": {
            "name": "Dr. Mukesh Tiwari",
            "image_url": "",
            "designation": "Vice Chancellor, ITM University",
            "description": """
                Dr. Mukesh Tiwari is the Vice Chancellor of ITM University, Gwalior.
                He works on AI-powered automation in industries.
            """
        }
    }

    # Fetch Category
    speaker_cat = None
    if speaker:
        speaker_cat = get_slot_category(
            slot_lists  = speakers, 
            slot = speaker.strip().lower()
        )
        print(f"Categorized speaker: {speaker_cat}")

    if speaker is None or speaker_cat is None:
        return nextIntentWithResponseCard(
            session_attributes,
            message,
            None,
            None,
            None,
            speaker_options
        )
    else:
        # Fetch speakers Info
        info = speakers_info[speaker_cat]
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