# 🤖 Foydalanuvchilar Chatbot

A chatbot that answers natural language questions about a user database powered by Groq (free AI) + FastAPI + SQLite.

---

## 💬 Example Questions
- "Toshkentda nechta premium foydalanuvchi bor?"
- "Eng yuqori daromadli 5 ta foydalanuvchini ko'rsat"
- "Dasturchilar o'rtacha daromadi qancha?"
- "2023-yilda ro'yxatdan o'tganlar soni?"
- "Magistr ta'limli ayollar nechtasi Buxoroda yashaydi?"

---

## ⚙️ Requirements

- Python 3.10 or higher
- A free Groq API key (get it at https://console.groq.com)

---

## 🚀 How to Run

### Step 1: Download the project
Download this repository as a ZIP and extract it, or clone it:
```bash
git clone https://github.com/Suyunboyev/chatbot-project.git
cd chatbot-project
```

### Step 2: Create a virtual environment
```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Still, if you have error. Then write it to you bash
```bash
pip uninstall langchain langchain-community langchain-core langchain-openai langchain-groq -y

pip install langchain==0.1.20 langchain-community==0.0.38 langchain-core==0.1.52 langchain-groq==0.1.3
```

### Step 4: Get a free Groq API key
1. Go to https://console.groq.com
2. Sign up for free
3. Click **API Keys** → **Create API Key**
4. Copy the key (starts with `gsk_...`)

### Step 5: Create the `.env` file
Create a file called `.env` in the project root folder and paste this:
```
GROQ_API_KEY=gsk_your-key-here
```
Replace `gsk_your-key-here` with your actual key.

### Step 6: Add the dataset
Make sure the file `users_table_uz_full.csv` is inside the `data/` folder:
```
data/users_table_uz_full.csv
```

### Step 7: Run the server
```bash
uvicorn backend.main:app --reload --port 8000
```

You should see:
```
✅ Loaded 5000 rows into SQLite table 'users'
✅ Agent ready!
INFO: Uvicorn running on http://127.0.0.1:8000
```

### Step 8: Open the chatbot
Open your browser and go to:
```
http://localhost:8000
```

---

## 📁 Project Structure

```
chatbot-project/
├── backend/
│   ├── main.py         ← FastAPI server
│   ├── database.py     ← Loads CSV into SQLite
│   ├── agent.py        ← AI agent (Groq + LangChain)
│   ├── models.py       ← Request/Response schemas
│   └── config.py       ← Settings
├── data/
│   └── users_table_uz_full.csv
├── frontend/
│   └── index.html      ← Chat UI
├── .env                ← Your API key (create this yourself)
├── .env.example        ← Example env file
└── requirements.txt
```

---

## ❗ Common Errors

| Error | Fix |
|---|---|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` with venv activated |
| `GROQ_API_KEY not set` | Make sure `.env` file exists with your key |
| `FileNotFoundError: CSV` | Put the CSV file inside the `data/` folder |
| `model_decommissioned` | Open `backend/agent.py` and change the model name to `llama-3.3-70b-versatile` |
| Port already in use | Change `--port 8000` to `--port 8001` and open `http://localhost:8001` |

---

## 🛑 Stop the Server

Press `Ctrl + C` in the terminal.
