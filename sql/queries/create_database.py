import sqlite3

def create_database():
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()

            # Create User table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    name TEXT PRIMARY KEY NOT NULL,
                    height_ft INTEGER NOT NULL,
                    height_in REAL NOT NULL,
                    birthdate DATE NOT NULL,
                    gender TEXT,
                    neck_circumference REAL,
                    waist_circumference REAL
                )
            ''')

            # Create Weight Log table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS weight_history (
                    name TEXT NOT NULL,
                    date DATE NOT NULL,
                    weight REAL NOT NULL,
                    FOREIGN KEY (name) REFERENCES users(name),
                    UNIQUE (date)
                )
            ''')

            # Create workout Log table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS workout_logs (
                    name TEXT NOT NULL,
                    date DATE NOT NULL,
                    score REAL NOT NULL,
                    FOREIGN KEY (name) REFERENCES users(name),
                    UNIQUE (date)
                )
            ''')

            # Create Workout Plans table (needed before workout_week)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS workout_plans (
                    workout_plan TEXT PRIMARY KEY NOT NULL,
                    workouts TEXT NOT NULL
                )
            ''')

            # Create Workout Plan Details table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS workout_plan_details (
                    plan_id TEXT NOT NULL,
                    workout_name TEXT NOT NULL,
                    weight REAL NOT NULL,
                    sets INTEGER NOT NULL,
                    reps INTEGER NOT NULL,
                    FOREIGN KEY (plan_id) REFERENCES workout_plans(workout_plan)
                )
            ''')

            # Create Workout Week table (after workout_plans is created)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS workout_week (
                    name TEXT NOT NULL,
                    day_of_week TEXT NOT NULL,
                    workout_plan TEXT NOT NULL,
                    FOREIGN KEY (name) REFERENCES users(name),
                    FOREIGN KEY (workout_plan) REFERENCES workout_plans(workout_plan),
                    UNIQUE (name, day_of_week)
                )
            ''')

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def wipe_database(db_path="sql/my_database.db"):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            # Drop tables in the correct order to avoid foreign key constraint errors
            cursor.execute("DROP TABLE IF EXISTS workout_plan_details")
            cursor.execute("DROP TABLE IF EXISTS weight_history")
            cursor.execute("DROP TABLE IF EXISTS weight_logs")
            cursor.execute("DROP TABLE IF EXISTS workout_week")
            cursor.execute("DROP TABLE IF EXISTS workout_plans")
            cursor.execute("DROP TABLE IF EXISTS users")

            # Commit the transaction
            conn.commit()

        print("✅ Database wiped successfully.")
    except Exception as e:
        print(f"❌ Error wiping the database: {e}")