import sqlite3

def insert_user(username, height_ft, height_in, birthdate, gender=None, neck_circumference=None, waist_circumference=None,goal=None,start_weight=None):
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, height_ft, height_in, birthdate, gender, neck_circumference, waist_circumference, goal, start_weight)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (username, height_ft, height_in, birthdate, gender, neck_circumference, waist_circumference, goal, start_weight))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error inserting user: {e}")
    except Exception as e:
        print(f"Unexpected error inserting user: {e}")

def insert_weight(username, weight, date):
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO weight_history (username, weight, date)
                VALUES (?, ?, ?)
            ''', (username, weight, date))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error inserting weight: {e}")
    except Exception as e:
        print(f"Unexpected error inserting weight: {e}")
