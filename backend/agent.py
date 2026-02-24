from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_groq import ChatGroq
from backend.config import DATABASE_URL
import os
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PREFIX = """
Sen O'zbekiston foydalanuvchilari ma'lumotlar bazasi bo'yicha yordam beradigan 
aqlli chatbot assistantsan. Ma'lumotlar bazasida "users" jadvali bor va u 
quyidagi ustunlarni o'z ichiga oladi:

- id: Unikal identifikator
- first_name: Ism
- last_name: Familiya
- father_name: Otasining ismi
- birth_date: Tug'ilgan sana (YYYY-MM-DD formatida)
- gender: Jins ('Erkak' yoki 'Ayol')
- email: Elektron pochta
- phone: Telefon raqami
- city: Shahar (Toshkent, Buxoro, Namangan, Andijon, Farg'ona, Jizzax, Termiz, Xiva)
- address: Manzil
- passport_series: Passport seriyasi
- jshshir: JSHSHIR raqami
- nationality: Millat (O'zbek, Tojik, Qozoq, Qirg'iz, Rus, Turkman)
- marital_status: Oilaviy holat ('Turmush qurgan', 'Uylanmagan', 'Ajrashgan')
- workplace: Ish joyi
- position: Lavozim
- education: Ta'lim darajasi (Bakalavr, Magistr, Oliy, O'rta maxsus)
- income: Daromad (so'm)
- user_type: Foydalanuvchi turi ('premium', 'oddiy', 'admin')
- registered_date: Ro'yxatdan o'tgan sana

Qoidalar:
1. Faqat SELECT so'rovlarini ishlat. INSERT, UPDATE, DELETE MUMKIN EMAS.
2. Natijalarni o'zbek tilida, aniq va tushunarli qilib tushuntir.
3. Raqamli natijalarni formatlashni unutma.
4. Har doim xushmuomalalik bilan javob ber.
"""


def create_agent():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY"),
    )

    db = SQLDatabase.from_uri(DATABASE_URL)

    agent = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools",
        prefix=SYSTEM_PREFIX,
        verbose=True,
        max_iterations=10,
        handle_parsing_errors=True,
    )

    return agent


_agent_instance = None


def get_agent():
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = create_agent()
    return _agent_instance