import sqlite3

def insert_user(name, height_ft, height_in, birthdate, gender=None, neck_circumference=None, waist_circumference=None):
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (name, height_ft, height_in, birthdate, gender, neck_circumference, waist_circumference)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, height_ft, height_in, birthdate, gender, neck_circumference, waist_circumference))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error inserting user: {e}")
    except Exception as e:
        print(f"Unexpected error inserting user: {e}")

def insert_weight(name, weight, date):
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO weight_history (name, weight, date)
                VALUES (?, ?, ?)
            ''', (name, weight, date))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error inserting weight: {e}")
    except Exception as e:
        print(f"Unexpected error inserting weight: {e}")

def insert_workout_plan(workout_plan, workouts):
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO workout_plans (workout_plan, workouts)
                VALUES (?, ?)
            ''', (workout_plan, workouts))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error inserting workout plan: {e}")
    except Exception as e:
        print(f"Unexpected error inserting workout plan: {e}")

def insert_workout_plan_detail(plan_id, workout_name, weight, sets, reps):
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO workout_plan_details (plan_id, workout_name, weight, sets, reps)
                VALUES (?, ?, ?, ?, ?)
            ''', (plan_id, workout_name, weight, sets, reps))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error inserting workout plan detail: {e}")
    except Exception as e:
        print(f"Unexpected error inserting workout plan detail: {e}")

def insert_workout_week(name, day_of_week, workout_plan):
    """
    Inserts a workout week entry into the 'workout_week' table.
    :param name: Name of the user (required)
    :param day_of_week: Day of the week (required)
    :param workout_plan: Name of the workout plan (required)
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO workout_week (name, day_of_week, workout_plan)
                VALUES (?, ?, ?)
            ''', (name, day_of_week, workout_plan))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error inserting workout week: {e}")
    except Exception as e:
        print(f"Unexpected error inserting workout week: {e}")