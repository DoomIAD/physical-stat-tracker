import sqlite3

def create_database():
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()

            # Create User table
            # Keeps track of basic user information to improve percentile and BMI calculations
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY NOT NULL,
                    height_ft INTEGER NOT NULL,
                    height_in REAL NOT NULL,
                    birthdate DATE NOT NULL,
                    gender TEXT,
                    neck_circumference REAL,
                    waist_circumference REAL
                )
            ''')

            # Create Weight Log table
            # Tracks weight history for line chart on Home page
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS weight_history (
                    username TEXT NOT NULL,
                    date DATE NOT NULL,
                    weight REAL NOT NULL,
                    FOREIGN KEY (username) REFERENCES users(username),
                    UNIQUE (date)
                )
            ''')

            # Create workout Log table
            # Tracks activity converted to points from steps or time working out for GitHub contribution graph on Home page
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS activity_history (
                    username TEXT NOT NULL,
                    date DATE NOT NULL,
                    score REAL NOT NULL,
                    FOREIGN KEY (username) REFERENCES users(username),
                    UNIQUE (date)
                )
            ''')

            # Create Workout Plans table
            # Stores titles of active workout plans with a distinct order for easily repeatable workouts
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS workout_plans (
                    plan_name TEXT PRIMARY KEY NOT NULL,
                    username TEXT NOT NULL,
                    workout_order INTEGER NOT NULL,
                    UNIQUE (workout_order),
                    FOREIGN KEY (username) REFERENCES users(username)
                )
            ''')

            # Create Workout Plan Details table
            # Specific plans for each exercise and which workout it is in
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS workout_plan_details (
                    plan_name TEXT NOT NULL,
                    workout_name TEXT NOT NULL,
                    weight REAL NOT NULL,
                    sets INTEGER NOT NULL,
                    reps INTEGER NOT NULL,
                    FOREIGN KEY (plan_name) REFERENCES workout_plans(plan_name)
                )
            ''')

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")