import pandas as pd

# New Guests Info
guests = [
    "Dr. Sunil Rai",
    "Anirban Bhattacharya",
    "Sharmila Singh",
    "Naghma Irfan",
    "Dr. Mala Mehra",
    "Brajesh Shrivastava",
    "Roli Tripathi",
    "Dr. Anupriya Dayal",
    "Farah Kazmi",
    "Dr. Rina Pathak",
    "Anurita Bakshi",
    "Geetika Kapoor",
    "Dr. Ruchi Seth",
    "Rachna Mishra",
    "Dr. Aparajita Gupta",
    "Prof. Vivek Mishra",
    "Dr. Richa Prakash",
    "Pooja Lamba"
]

designations = [
    "Chancellor, UPES",
    "Vice President, Seth Anandram Jaipuria School",
    "Principal, Pioneer Montessori Inter College",
    "Principal, Senior Secondary School Girls AMU",
    "Director, Hoerner College",
    "Director, The Oriental School",
    "Principal, Amity International School",
    "Principal, Navyug Public Schoolw",
    "Principal, Pioneer Montessori School",
    "Principal, Seth M.R Jaipuria School",
    "Founder, Armadale Education",
    "Principal, St. Teresa's College",
    "Principal, Allenhouse Public School",
    "Principal, Amity International School",
    "Principal, Lucknow Public School",
    "Dean, Sri Sharda Group of Institutions",
    "Principal, Delhi Public School",
    "Principal, Adani GEMS School of Excellence"
]

desc = [
    "Dr. Sunil Rai is the Chancellor of UPES at Dehra Dun, Uttarakhand, shaping the institution's future.",
    "Anirban Bhattacharya serves as the Vice President/Head of Franchise Schools at Seth Anandram Jaipuria School, expanding educational opportunities.",
    "Sharmila Singh is the Principal of Pioneer Montessori Inter College in Lucknow, nurturing young learners.",
    "Naghma Irfan is the Principal of Senior Secondary School Girls AMU Aligarh, empowering young women through education.",
    "Dr. Mala Mehra is the Principal/Director at Hoerner College, Lucknow, guiding the institution with her leadership.",
    "Brajesh Shrivastava is the Director of The Oriental School Bhopal, providing comprehensive education.",
    "Roli Tripathi is the Principal of Amity International School, Vrindavan Yojna Campus, Lucknow, fostering a love for learning.",
    "Dr. Anupriya Dayal is the Principal of Navyug Public School, Alambagh Lucknow, creating a positive learning environment.",
    "Farah Kazmi is the Principal of Pioneer Montessori School Jankipuram Branch Lucknow, building a strong foundation for young minds.",
    "Dr. Rina Pathak is the Principal of Seth M.R Jaipuria School GOEL Campus, Lucknow, committed to academic excellence.",
    "Anurita Bakshi is the Founder of Armadale Education and MD of Kombat Creed Championship, leading in education and sports.",
    "Geetika Kapoor is the Principal of St. Teresa's College, Lucknow, dedicated to quality education.",
    "Dr. Ruchi Seth is the Principal of Allenhouse Public School, Khalasi Lines Kanpur, creating a dynamic learning environment.",
    "Rachna Mishra is the Principal of Amity International School, Lucknow, fostering holistic development.",
    "Dr. Aparajita Gupta is the Principal of Lucknow Public School, committed to shaping future leaders.",
    "Prof. Vivek Mishra is the Founder Dean of Sri Sharda Group of Institutions Lucknow, contributing to higher education.",
    "Dr. Richa Prakash is the Principal of Delhi Public School, Kalyanpur, Kanpur, focused on academic and personal growth.",
    "Pooja Lamba is the Principal of Adani GEMS School of Excellence, Lucknow SCR, promoting excellence in education."
]

df = pd.DataFrame(
    data={
        'guest': guests,
        'designation': designations,
        'desc': desc
    }
)

file_path = "./info_retrieval_data/"

file_name = "guests"

df.to_csv(f"{file_path}{file_name}.csv", index=False)

"""
    Powershell Command: - python Script_Files/df_create.py
"""

