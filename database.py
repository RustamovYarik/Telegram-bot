import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def create_tables(self):
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER AUTOINCREAMENT PRIMARY KEY,
            first_name TEXT,
            email TEXt,
            phone_number TEXT,
            card_info INTEGER,
            chat_id INTEGER
            )
            """)
            self.con.commit()
        except Exception as exc:
            print(exc)

    def delete_table(self):
        try:
            self.cur.execute(f"DROP TABLE '{table_name}'")
            self.con.commit()
        except Exception as exc:
            print(exc)

    def get_user(self, chat_id):
        try:
            return self.cur.execute(f"SELECT * FROM users WHERE chat_id='{chat_id}'").fetchone()
        except Exception as exc:
            print(exc)
        return False

    def add_user(self, data: dict):
        try:
            first_name = data.get('first_name')
            email = data.get('email')
            card_info = data.get('card_info')
            phone_number = data.get('phone_number')
            chat_id = data.get('chat_id')
            self.cur.execute("""
            INSERT INTO users (first_name, email, card_info, phone_number, chat_id) VALUES (?,?,?,?,?)
            """, (first_name, email, card_info, phone_number, chat_id))
            self.con.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def add_user_uz(self, data: dict):
        try:
            first_name = data.get('full_name')
            email = data.get('gmail')
            card_info = data.get('karta_info')
            phone_number = data.get('tel_number')
            chat_id = data.get('chat_id')
            self.cur.execute("""
            INSERT INTO users (first_name, email, card_info, phone_number, chat_id) VALUES (?,?,?,?,?)
            """, (full_name, gmail, karta_info, tel_number, chat_id))
            self.con.commit()
            return True
        except Exception as exc:
            print(exc)
            return False