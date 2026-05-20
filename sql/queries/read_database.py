import sqlite3

def get_all_users():
    """
    Retrieves all users from the 'users' table.
    :return: List of all user records.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error getting all users: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting all users: {e}")
        return []
    
# returns all users names in a list
def get_all_user_names():
    """
    Retrieves all user names from the 'users' table.
    :return: List of all user names.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM users")
            return [row[0] for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Database error getting all user names: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting all user names: {e}")
        return []

def get_all_workout_plans():
    """
    Retrieves all workout plans from the 'workout_plans' table.
    :return: List of all workout plan records.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM workout_plans")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error getting all workout plans: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting all workout plans: {e}")
        return []

def get_all_workout_plan_details():
    """
    Retrieves all workout plan details from the 'workout_plan_details' table.
    :return: List of all workout plan detail records.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM workout_plan_details")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error getting all workout plan details: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting all workout plan details: {e}")
        return []
    
def get_all_workout_week():
    """
    Retrieves all workout week entries from the 'workout_week' table.
    :return: List of all workout week records.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM workout_week")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error getting all workout week entries: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting all workout week entries: {e}")
        return []


def get_all_workout_week():
    """
    Retrieves all workout week entries from the 'workout_week' table.
    :return: List of all workout week records.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM workout_week")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error getting all workout week entries: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting all workout week entries: {e}")
        return []

def get_user_by_name(name):
    """
    Retrieves a user by their name.
    :param name: Name of the user (must be in the 'users' table).
    :return: User record or None if not found.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
            result = cursor.fetchone()
            return result
    except sqlite3.Error as e:
        print(f"Database error getting user by name: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting user by name: {e}")
        return None

def get_workout_plan_by_name(plan_name):
    """
    Retrieves a workout plan by its name.
    :param plan_name: Name of the workout plan (must be in the 'workout_plans' table).
    :return: Workout plan record or None if not found.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM workout_plans WHERE workout_plan = ?", (plan_name,))
            result = cursor.fetchone()
            return result
    except sqlite3.Error as e:
        print(f"Database error getting workout plan by name: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting workout plan by name: {e}")
        return None
    
def get_workout_plan_details_by_plan_id(plan_id):
    """
    Retrieves workout plan details by the plan ID.
    :param plan_id: ID of the workout plan.
    :return: List of workout plan details or empty list if not found.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM workout_plan_details WHERE plan_id = ?", (plan_id,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error getting workout plan details by ID: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting workout plan details by ID: {e}")
        return []
    
def get_workout_week_by_user_and_day(name, day_of_week):
    """
    Retrieves workout week entries for a specific user and day of the week.
    :param name: Name of the user.
    :param day_of_week: Day of the week (e.g., 'Monday').
    :return: List of workout week entries for the user and day.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM workout_week
                WHERE name = ? AND day_of_week = ?
            """, (name, day_of_week))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error getting workout week by user and day: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting workout week by user and day: {e}")
        return []

def get_user_workout_plan_for_day(name, day_of_week):
    """
    Retrieves the workout plan for a specific user on a given day of the week.
    This function joins the 'workout_week' and 'workout_plans' tables.
    :param name: Name of the user.
    :param day_of_week: Day of the week (e.g., 'Monday').
    :return: List of workout plan details for the user and day.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT wp.workout_plan, wp.workouts
                FROM workout_week ww
                JOIN workout_plans wp ON ww.workout_plan = wp.workout_plan
                WHERE ww.name = ? AND ww.day_of_week = ?
            """, (name, day_of_week))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error getting user's workout plan for day: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting user's workout plan for day: {e}")
        return []
    
# get current weight for user
def get_current_weight(name):
    """
    Retrieves the most recent weight entry for a specific user.
    :param name: Name of the user.
    :return: Most recent weight entry or None if not found.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT weight FROM weight_history
                WHERE name = ?
                ORDER BY date DESC
                LIMIT 1
            """, (name,))
            result = cursor.fetchone()
            return result[0] if result else None
    except sqlite3.Error as e:
        print(f"Database error getting current weight: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting current weight: {e}")
        return None

# get weight history for user
def get_weight_history(name):
    """
    Retrieves the weight history for a specific user.
    :param name: Name of the user.
    :return: List of weight history entries or empty list if not found.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT date, weight FROM weight_history
                WHERE name = ?
                ORDER BY date ASC
            """, (name,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error getting weight history: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting weight history: {e}")
        return []