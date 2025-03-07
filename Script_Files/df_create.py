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



# Previous guests
guests = [
    'Panneerselvam (PS) Madanagopal',
    'Prof. Anil Kashyap',
    'Prof. (Dr.) Simon Mak',
    'Dr. Ashwin Fernandes',
    'Prof. Parag Shah',
    'Dr. Madhu Chitkara',
    'Dr. Swati Mujumdar',
    'Col. Yogesh Joshi'
]

designation = [
    'Chief Executive Officer, MeitY Startup Hub',
    'President, NICMAR University',
    'Vice Chancellor, UAU',
    'Executive Director, AMESA',
    'Director, MIDAS School of Entrepreneurship',
    'Pro-Chancellor, Chitkara University',
    'Pro-Chancellor, Symbiosis Skill Universities',
    'Director, Hinjawadi Industries Association (HIA)'
]

desc = [
    'Panneerselvam (PS) Madanagopal is the Chief Executive Officer of MeitY Startup Hub, under the Ministry of Electronics & Information Technology. He leads MeitY Startup Hub, supporting tech-driven startups and AI innovation initiatives.',
    'Prof. Anil Kashyap is the President & Chancellor of NICMAR University and also serves as the Director General of NICMAR. He has played a key role in advancing AI and construction management education at NICMAR University.',
    'Prof. (Dr.) Simon Mak is the first American Founding Vice Chancellor in India, at Universal AI University, Bombay. He has pioneered AI-driven higher education programs and has contributed to global AI academic collaborations.',
    'Dr. Ashwin Fernandes is the Executive Director for AMESA at QS Quacquarelli Symonds, a global education ranking organization. He specializes in global university rankings, AI education policies, and academic excellence strategies.',
    'Prof. Parag Shah is the Chief Mentor of MIDAS School of Entrepreneurship and the Founding Chairman of Flame University, Pune. He has mentored numerous entrepreneurs and played a vital role in fostering startup culture in India.',
    'Dr. Madhu Chitkara is the Co-Founder and Pro Chancellor of Chitkara University, Punjab & HP. She has been instrumental in advancing academic excellence and industry partnerships at Chitkara University.',
    'Dr. Swati Mujumdar is the Pro Chancellor of Symbiosis Skills Universities in Indore & Pune. She has been a pioneer in integrating AI and technology-driven skills training into education.',
    'Col. Yogesh Joshi is the President of the Hinjawadi Industries Association (HIA), Pune, Maharashtra. He has been a key figure in promoting AI adoption and industry-academia collaboration in Pune.'
]

imageURL = [
    'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/PM.jpg',
    'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/PAK.jpg',
    'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/SM.jpg',
    'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/AFR.jpg',
    'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/PS.png',
    'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/MC.jpg',
    'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/SM.jpg',
    'https://global-upload-storage.s3.us-east-1.amazonaws.com/ZIES/Guests/YJ.png'
]



df = pd.DataFrame(
    data={
        'guest': guests,
        'designation': designation,
        'desc': desc,
        'imageURL': imageURL
    }
)

file_path = "./info_retrieval_data/"

file_name = "guests"

df.to_csv(f"{file_path}{file_name}.csv", index=False)

"""
    Powershell Command: - python Script_Files/df_create.py
"""

