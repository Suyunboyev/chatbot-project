import pandas as pd
from sqlalchemy import create_engine, text
from backend.config import DATABASE_URL, CSV_PATH

# Global engine instance
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def load_csv_to_db():
    """
    Reads the CSV file and loads it into a SQLite table called 'users'.
    This runs once at startup. If the table already exists, it is replaced
    so the data always stays fresh.
    """
    df = pd.read_csv(CSV_PATH)

    # Normalize column names: strip whitespace, lowercase
    df.columns = [c.strip().lower().replace(" ", "_").replace("'", "").replace("'", "") for c in df.columns]

    # Rename the awkward Uzbek column names to clean English aliases
    column_map = {
        "id": "id",
        "ism": "first_name",
        "familiya": "last_name",
        "otasining_ismi": "father_name",
        "tugilgan_sana": "birth_date",
        "jins": "gender",
        "email": "email",
        "telefon": "phone",
        "shahar": "city",
        "manzil": "address",
        "passport_seriya": "passport_series",
        "jshshir": "jshshir",
        "millat": "nationality",
        "oilaviy_holat": "marital_status",
        "ish_joyi": "workplace",
        "lavozim": "position",
        "ta'lim_darajasi": "education",
        "daromad": "income",
        "foydalanuvchi_turi": "user_type",
        "royxatdan_otgan_sana": "registered_date",
    }

    # Some columns might have BOM or encoding artifacts — handle gracefully
    rename = {}
    for col in df.columns:
        clean = col.lstrip("\ufeff")  # strip BOM
        if clean in column_map:
            rename[col] = column_map[clean]
        elif col in column_map:
            rename[col] = column_map[col]

    df.rename(columns=rename, inplace=True)

    df.to_sql("users", engine, if_exists="replace", index=False)
    print(f"✅ Loaded {len(df)} rows into SQLite table 'users'")


def get_engine():
    return engine