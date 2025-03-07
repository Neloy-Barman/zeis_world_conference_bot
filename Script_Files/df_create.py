import pandas as pd

# # New Guests Info
# guests = [
#     "Dr. Sunil Rai",
#     "Anirban Bhattacharya",
#     "Sharmila Singh",
#     "Naghma Irfan",
#     "Dr. Mala Mehra",
#     "Brajesh Shrivastava",
#     "Roli Tripathi",
#     "Dr. Anupriya Dayal",
#     "Farah Kazmi",
#     "Dr. Rina Pathak",
#     "Anurita Bakshi",
#     "Geetika Kapoor",
#     "Dr. Ruchi Seth",
#     "Rachna Mishra",
#     "Dr. Aparajita Gupta",
#     "Prof. Vivek Mishra",
#     "Dr. Richa Prakash",
#     "Pooja Lamba"
# ]

# designations = [
#     "Chancellor, UPES",
#     "Vice President, Seth Anandram Jaipuria School",
#     "Principal, Pioneer Montessori Inter College",
#     "Principal, Senior Secondary School Girls AMU",
#     "Director, Hoerner College",
#     "Director, The Oriental School",
#     "Principal, Amity International School",
#     "Principal, Navyug Public Schoolw",
#     "Principal, Pioneer Montessori School",
#     "Principal, Seth M.R Jaipuria School",
#     "Founder, Armadale Education",
#     "Principal, St. Teresa's College",
#     "Principal, Allenhouse Public School",
#     "Principal, Amity International School",
#     "Principal, Lucknow Public School",
#     "Dean, Sri Sharda Group of Institutions",
#     "Principal, Delhi Public School",
#     "Principal, Adani GEMS School of Excellence"
# ]

# desc = [
#     "Dr. Sunil Rai is the Chancellor of UPES at Dehra Dun, Uttarakhand, shaping the institution's future.",
#     "Anirban Bhattacharya serves as the Vice President/Head of Franchise Schools at Seth Anandram Jaipuria School, expanding educational opportunities.",
#     "Sharmila Singh is the Principal of Pioneer Montessori Inter College in Lucknow, nurturing young learners.",
#     "Naghma Irfan is the Principal of Senior Secondary School Girls AMU Aligarh, empowering young women through education.",
#     "Dr. Mala Mehra is the Principal/Director at Hoerner College, Lucknow, guiding the institution with her leadership.",
#     "Brajesh Shrivastava is the Director of The Oriental School Bhopal, providing comprehensive education.",
#     "Roli Tripathi is the Principal of Amity International School, Vrindavan Yojna Campus, Lucknow, fostering a love for learning.",
#     "Dr. Anupriya Dayal is the Principal of Navyug Public School, Alambagh Lucknow, creating a positive learning environment.",
#     "Farah Kazmi is the Principal of Pioneer Montessori School Jankipuram Branch Lucknow, building a strong foundation for young minds.",
#     "Dr. Rina Pathak is the Principal of Seth M.R Jaipuria School GOEL Campus, Lucknow, committed to academic excellence.",
#     "Anurita Bakshi is the Founder of Armadale Education and MD of Kombat Creed Championship, leading in education and sports.",
#     "Geetika Kapoor is the Principal of St. Teresa's College, Lucknow, dedicated to quality education.",
#     "Dr. Ruchi Seth is the Principal of Allenhouse Public School, Khalasi Lines Kanpur, creating a dynamic learning environment.",
#     "Rachna Mishra is the Principal of Amity International School, Lucknow, fostering holistic development.",
#     "Dr. Aparajita Gupta is the Principal of Lucknow Public School, committed to shaping future leaders.",
#     "Prof. Vivek Mishra is the Founder Dean of Sri Sharda Group of Institutions Lucknow, contributing to higher education.",
#     "Dr. Richa Prakash is the Principal of Delhi Public School, Kalyanpur, Kanpur, focused on academic and personal growth.",
#     "Pooja Lamba is the Principal of Adani GEMS School of Excellence, Lucknow SCR, promoting excellence in education."
# ]



# # Previous guests
# guests = [
#     'Panneerselvam (PS) Madanagopal',
#     'Prof. Anil Kashyap',
#     'Prof. (Dr.) Simon Mak',
#     'Dr. Ashwin Fernandes',
#     'Prof. Parag Shah',
#     'Dr. Madhu Chitkara',
#     'Dr. Swati Mujumdar',
#     'Col. Yogesh Joshi'
# ]

# designation = [
#     'Chief Executive Officer, MeitY Startup Hub',
#     'President, NICMAR University',
#     'Vice Chancellor, UAU',
#     'Executive Director, AMESA',
#     'Director, MIDAS School of Entrepreneurship',
#     'Pro-Chancellor, Chitkara University',
#     'Pro-Chancellor, Symbiosis Skill Universities',
#     'Director, Hinjawadi Industries Association (HIA)'
# ]

# desc = [
#     'Panneerselvam (PS) Madanagopal is the Chief Executive Officer of MeitY Startup Hub, under the Ministry of Electronics & Information Technology. He leads MeitY Startup Hub, supporting tech-driven startups and AI innovation initiatives.',
#     'Prof. Anil Kashyap is the President & Chancellor of NICMAR University and also serves as the Director General of NICMAR. He has played a key role in advancing AI and construction management education at NICMAR University.',
#     'Prof. (Dr.) Simon Mak is the first American Founding Vice Chancellor in India, at Universal AI University, Bombay. He has pioneered AI-driven higher education programs and has contributed to global AI academic collaborations.',
#     'Dr. Ashwin Fernandes is the Executive Director for AMESA at QS Quacquarelli Symonds, a global education ranking organization. He specializes in global university rankings, AI education policies, and academic excellence strategies.',
#     'Prof. Parag Shah is the Chief Mentor of MIDAS School of Entrepreneurship and the Founding Chairman of Flame University, Pune. He has mentored numerous entrepreneurs and played a vital role in fostering startup culture in India.',
#     'Dr. Madhu Chitkara is the Co-Founder and Pro Chancellor of Chitkara University, Punjab & HP. She has been instrumental in advancing academic excellence and industry partnerships at Chitkara University.',
#     'Dr. Swati Mujumdar is the Pro Chancellor of Symbiosis Skills Universities in Indore & Pune. She has been a pioneer in integrating AI and technology-driven skills training into education.',
#     'Col. Yogesh Joshi is the President of the Hinjawadi Industries Association (HIA), Pune, Maharashtra. He has been a key figure in promoting AI adoption and industry-academia collaboration in Pune.'
# ]

# imageURL = [
#     'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/PM.jpg',
#     'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/PAK.jpg',
#     'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/SM.jpg',
#     'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/AFR.jpg',
#     'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/PS.png',
#     'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/MC.jpg',
#     'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/SM.jpg',
#     'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/YJ.png'
# ]


# Previous Speakers Info
speakers = [
    'Dr. Ashwini Kumar Sharma',
    'Dr. Neeraj Saxena',
    'Prof. Prabhat Ranjan',
    'Prof. Rajasekharan Pillai VN',
    'Dr. Rakesh Kumar Jain',
    'Dr. Poonam Kashyap',
    'Dr. Dharmesh J. Shah',
    'Dr. Prasad D. Khandekar',
    'Dr. Sohan Chitlange',
    'Prof. (Dr.) Siddharth Jabade',
    'Dr. Rajesh Dixit',
    'Dr. Kuldeep Raina',
    'Dr. Sayalee Gankar',
    'Mr. Aarsh Srivastava',
    'Prof. (Dr.) Sundeep Mishra',
    'Prof. Sanjeev Sonawane',
    'Prof. Ankur Kulkarni',
    'Prof. N.J. Pawar',
    'Prof. (Dr.) B.P. Singh',
    'Prof. (Dr.) Ajay Bhushan',
    'Prof. Gopalkrishna Joshi',
    'Prof. (Dr.) G.K. Shirude',
    'Dr. Shrihari (Prakash) Honwad',
    'Dr. Atul Kumar',
    'Prof. (Dr.) Tabrez Ahmad',
    'Mr. Ashish Gupta',
    'Prof. Adit Gupta'
]


designation = [
    'Director General, NIELIT',
    'Chancellor, JIS University',
    'Vice Chancellor, D Y Patil International University',
    'Vice Chancellor, Somaiya Vidyavihar University',
    'Vice Chancellor, Ajeenkya D Y Patil University',
    'Vice Chancellor, Alard University',
    'Vice Chancellor, Indrashil University',
    'Vice Chancellor, DES Pune University',
    'Vice Chancellor, D Y Patil Dnyan Prasad University',
    'Vice Chancellor, Vishwakarma University',
    'Vice Chancellor, Renaissance University',
    'Vice Chancellor, Ramaiah University',
    'Vice Chancellor, D Y Patil University',
    'CEO, Gravitas AI',
    'Vice Chancellor, NIMS University Rajasthan.',
    'Vice Chancellor, Yashwantrao Chavan Maharashtra Open University',
    'Vice Chancellor, SAGE University',
    'Vice Chancellor, Dr. D Y Patil Vidyapeeth',
    'Vice Chancellor, Maharishi University of Information Technology',
    'Vice Chancellor, Scope Global Skills University',
    'Vice Chancellor, MIT Vishwaprayag University',
    'Vice Chancellor, Sri Balaji University',
    'Vice Chancellor',
    'Dean, Dr. D Y Patil B-School',
    'Dean, GD Goenka University',
    'CEO, FretBox',
    'Director, Institute of Education & Research'
]

desc = [
    "Dr. Ashwini Kumar Sharma is the Pro Chancellor of Vijaybhoomi University and Director General of NIELIT, Govt of India. He leads initiatives on AI-driven education and technology-based skill development in India.",
    "Dr. Neeraj Saxena is the Pro Chancellor of JIS University. He focuses on integrating AI and innovation into higher education curricula.",
    "Prof. Prabhat Ranjan is the Vice Chancellor of D Y Patil International University, Akurdi, Pune. He advocates for futuristic AI-driven university programs.",
    "Prof. Rajasekharan Pillai is the Vice Chancellor of Somaiya Vidyavihar University. His expertise lies in AI ethics and policy frameworks in education.",
    "Dr. Rakesh Kumar Jain is the Vice Chancellor of Ajeenkya D Y Patil University, Pune. He has introduced AI-based learning modules and research collaborations at the university.",
    "Dr. Poonam Kashyap is the Vice Chancellor of Alard University, Pune. She promotes AI integration in interdisciplinary studies.",
    "Dr. Dharmesh J. Shah is the Vice Chancellor of Indrashil University, Gujarat. He focuses on AI-driven healthcare innovations.",
    "Dr. Prasad D Khandekar is the Vice Chancellor of DES Pune University, Pune. He specializes in AI applications in engineering education.",
    "Dr. Sohan Chitlange is the Vice Chancellor of D Y Patil Dnyan Prasad University, Pune. He integrates AI research into pharmaceutical sciences.",
    "Prof. (Dr.) Siddharth Jabade is the Vice Chancellor of Vishwakarma University, Pune. He leads AI-based skill development initiatives.",
    "Dr. Rajesh Dixit is the Vice Chancellor of Renaissance University, Indore. He promotes AI-driven entrepreneurial education.",
    "Dr. Kuldeep Raina is the Vice Chancellor of Ramaiah University. He works on AI-driven policy frameworks in higher education.",
    "Dr. Sayalee Gankar is the Vice Chancellor of D Y Patil University Pune, Ambi Maharashtra. She focuses on AI-driven business strategies in management studies.",
    "Mr. Aarsh Srivastava is CEO & Co-Founder of Gravitas AI. He is an AI strategist with more than a decade's experience in AI products & solutions. He is Industry Advisor to Manipal University for AI & Data Science.",
    "Prof. (Dr.) Sundeep Mishra is the Vice Chancellor of NIMS University Rajasthan. He is a renowned expert in AI-driven healthcare research and medical technology.",
    "Prof. Sanjeev Sonawane is the Vice Chancellor of Yashwantrao Chavan Maharashtra Open University, Nashik. He integrates AI-based learning methodologies in higher education.",
    "Prof. Ankur Kulkarni is the Vice Chancellor of SAGE University, Indore. He specializes in AI applications for optimization and control systems.",
    "Prof. N.J. Pawar is the Vice Chancellor of Dr. D Y Patil Vidyapeeth, Pune. He works on AI-driven innovations in educational technology.",
    "Prof. (Dr.) B.P. Singh is the Vice Chancellor of Maharishi University of Information Technology. He is a leader in AI-driven business intelligence and automation.",
    "Prof. (Dr.) Ajay Bhushan is the Vice Chancellor of Scope Global Skills University, Bhopal, Madhya Pradesh. He focuses on AI-powered cybersecurity and digital governance.",
    "Prof. Gopalkrishna Joshi is the Founding Vice Chancellor of MIT Vishwaprayag University, Solapur. He applies AI in rural development and smart agriculture.",
    "Prof. (Dr.) G.K. Shirude is the Vice Chancellor of Sri Balaji University, Pune. He develops AI-based models for personalized learning and smart classrooms.",
    "Dr. Shrihari (Prakash) Honwad has served as Vice Chancellor at multiple AI-level universities and is associated with the Indian Institute of Science (IISc). He is known for AI-powered solutions in smart cities and urban planning.",
    "Dr. Atul Kumar is the Dean of Dr. D Y Patil B-School, Pune, Maharashtra. He specializes in AI for automation and robotics in industrial applications.",
    "Prof. (Dr.) Tabrez Ahmad is the Dean of Manav Law School and has previously served as the Vice Chancellor of GD Goenka University. He works on AI ethics, policy-making, and responsible AI frameworks.",
    "Mr. Ashish Gupta is the Founder and CEO of FretBox. He is an AI strategist focusing on AI applications in business intelligence.",
    "Prof. Adit Gupta is the Director of the Institute of Education & Research. He integrates AI in adaptive learning systems and cognitive computing."
]

imageURL = [
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/AKS.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/NS.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/PR.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/RPVN.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/RKJ.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/PK.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/DJS.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/PDK.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/SC.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/SJ.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/RD.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/KR.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/SG.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/MAS.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/PSM.png",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/SS.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/AKNI.png",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/NJP.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/BPS.png",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/AB.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/Gj.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/GKS.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/SPH.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/AK.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/TA.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/AG.jpg",
    "https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Speakers/AGU.jpg"
]



df = pd.DataFrame(
    data={
        'speaker': speakers,
        'designation': designation,
        'desc': desc,
        'imageURL': imageURL
    }
)

file_path = "./info_retrieval_data/"

# file_name = "guests"
file_name = "speakers"

df.to_csv(f"{file_path}{file_name}.csv", index=False)

"""
    Powershell Command: - python Script_Files/df_create.py
"""

