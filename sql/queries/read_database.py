from datetime import timedelta
import datetime
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
    Retrieves all usernames from the 'users' table.
    :return: List of all usernames.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM users")
            return [row[0] for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Database error getting all usernames: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting all usernames: {e}")
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

def get_all_workout_week(target_date=None):
    """
    Retrieves all workout plans mapped to dates based on a repeating cycle.
    Each user's workout plans cycle through their workout_order indefinitely.
    Cycle starts from January 1st of the current year.
    
    :param target_date: Date to get workout for (default: today)
    :return: List of tuples (username, cycle_day, plan_name) for the current cycle.
    """
    if target_date is None:
        target_date = datetime.date.today()
    
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT username, plan_name, workout_order
                FROM workout_plans
                ORDER BY username, workout_order
            """)
            rows = cursor.fetchall()
            
            if not rows:
                return []
            
            # Group plans by username and find cycle length
            user_plans = {}
            for username, plan_name, workout_order in rows:
                if username not in user_plans:
                    user_plans[username] = []
                user_plans[username].append((plan_name, workout_order))
            
            # Calculate which day in cycle target_date is
            cycle_start = datetime.date(target_date.year, 1, 1)
            days_since_cycle_start = (target_date - cycle_start).days
            
            result = []
            for username, plans in user_plans.items():
                cycle_length = len(plans)
                position_in_cycle = days_since_cycle_start % cycle_length
                
                # Return all plans in the cycle with their position
                for plan_name, workout_order in plans:
                    position = (workout_order - 1) % cycle_length
                    result.append((username, position, plan_name))
            
            return result
    except sqlite3.Error as e:
        print(f"Database error getting all workout week entries: {e}")
        return []

def get_user_by_name(username):
    """
    Retrieves a user by their username.
    :param username: username of the user (must be in the 'users' table).
    :return: User record or None if not found.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            return result
    except sqlite3.Error as e:
        print(f"Database error getting user by username: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting user by username: {e}")
        return None

def get_workout_plan_by_name(plan_name):
    """
    Retrieves a workout plan by its username.
    """
    try:
        with sqlite3.connect("sql/my_database.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM workout_plans WHERE workout_plan = ?",
                (plan_name,)
            )
            return cursor.fetchone()

    except sqlite3.Error as e:
        print(f"Database error getting workout plan by username: {e}")
        return None

def get_user_workout_plan_for_day(username, target_date=None):
    """
    Retrieves the workout plan for a specific user on a given date.
    Calculates position in the repeating cycle based on target_date.
    Cycle starts from January 1st of the current year.
    
    :param username: Username of the user.
    :param target_date: Date to get workout for (default: today).
    :return: Workout plan name or None if not found.
    """
    if target_date is None:
        target_date = datetime.date.today()
    
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT plan_name, workout_order
                FROM workout_plans
                WHERE username = ?
                ORDER BY workout_order
            """, (username,))
            rows = cursor.fetchall()
            
            if not rows:
                return None
            
            cycle_length = len(rows)
            cycle_start = datetime.date(target_date.year, 1, 1)
            days_since_cycle_start = (target_date - cycle_start).days
            position_in_cycle = days_since_cycle_start % cycle_length
            
            for plan_name, workout_order in rows:
                if (workout_order - 1) % cycle_length == position_in_cycle:
                    return plan_name
            
            return None
    except sqlite3.Error as e:
        print(f"Database error getting user's workout plan for day: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting user's workout plan for day: {e}")
        return None
    
# get current weight for user
def get_current_weight(username):
    """
    Retrieves the most recent weight entry for a specific user.
    :param username: Username of the user.
    :return: Most recent weight entry or None if not found.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT weight FROM weight_history
                WHERE username = ?
                ORDER BY date DESC
                LIMIT 1
            """, (username,))
            result = cursor.fetchone()
            return result[0] if result else None
    except sqlite3.Error as e:
        print(f"Database error getting current weight: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting current weight: {e}")
        return None

# get weight history for user
def get_weight_history(username):
    """
    Retrieves the weight history for a specific user.
    :param username: username of the user.
    :return: List of weight history entries or empty list if not found.
    """
    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT date, weight FROM weight_history
                WHERE username = ?
                ORDER BY date ASC
            """, (username,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error getting weight history: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error getting weight history: {e}")
        return []
    
# get activity history for user
def get_activity_history(username):
    """
    Returns a 7x6 activity grid.
    The last item represents today/current date.
    
    Grid format:
    [
        [0,0,0,0,0,0],
        ...
        [0,0,0,0,0,0]
    ]
    """

    # Create empty 7x6 grid
    activity_data = [[0 for _ in range(6)] for _ in range(7)]

    try:
        with sqlite3.connect('sql/my_database.db') as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT date, score
                FROM activity_history
                WHERE username = ?
                ORDER BY date ASC
            """, (username,))

            rows = cursor.fetchall()

            # Build lookup dictionary
            # Expected DB date format: YYYY-MM-DD
            activity_lookup = {
                row[0]: row[1]
                for row in rows
            }

            # Fill grid with last 42 days
            # Last cell = today
            today = datetime.datetime.now().date()
            start_date = today - timedelta(days=41)

            day_index = 0

            for col in range(6):
                for row in range(7):

                    current_date = start_date + timedelta(days=day_index)
                    date_str = current_date.strftime("%Y-%m-%d")

                    score = activity_lookup.get(date_str, 0)

                    if score < 1:
                        value = 0
                    elif score < 25:
                        value = 1
                    else:
                        value = score // 25

                    activity_data[row][col] = value

                    print(
                        f"Date: {date_str}, "
                        f"Score: {score}, "
                        f"Grid Value: {value}"
                    )

                    day_index += 1

            return activity_data

    except sqlite3.Error as e:
        print(f"Database error getting activity history: {e}")
        return [[0 for _ in range(6)] for _ in range(7)]

    except Exception as e:
        print(f"Unexpected error getting activity history: {e}")
        return [[0 for _ in range(6)] for _ in range(7)]