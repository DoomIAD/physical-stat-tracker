import sqlite3

def update_user(name, height_ft=None, height_in=None, birthdate=None, gender=None, 
                neck_circumference=None, waist_circumference=None):
    set_clause = []
    params = []

    if height_ft is not None:
        set_clause.append("height_ft = ?")
        params.append(height_ft)
    if height_in is not None:
        set_clause.append("height_in = ?")
        params.append(height_in)
    if birthdate is not None:
        set_clause.append("birthdate = ?")
        params.append(birthdate)
    if gender is not None:
        set_clause.append("gender = ?")
        params.append(gender)
    if neck_circumference is not None:
        set_clause.append("neck_circumference = ?")
        params.append(neck_circumference)
    if waist_circumference is not None:
        set_clause.append("waist_circumference = ?")
        params.append(waist_circumference)

    if not set_clause:
        return  # No fields to update

    query = f"UPDATE users SET {', '.join(set_clause)} WHERE name = ?"
    params.append(name)

    execute_query(query, params)

def update_workout_plan(plan_name, workouts=None):
    if workouts is None:
        return

    query = "UPDATE workout_plans SET workouts = ? WHERE workout_plan = ?"
    execute_query(query, (workouts, plan_name))

def update_workout_plan_detail(plan_id, workout_name, weight=None, sets=None, reps=None):
    set_clause = []
    params = []

    if weight is not None:
        set_clause.append("weight = ?")
        params.append(weight)
    if sets is not None:
        set_clause.append("sets = ?")
        params.append(sets)
    if reps is not None:
        set_clause.append("reps = ?")
        params.append(reps)

    if not set_clause:
        return

    query = f"UPDATE workout_plan_details SET {', '.join(set_clause)} WHERE plan_id = ? AND workout_name = ?"
    params.extend([plan_id, workout_name])
    execute_query(query, params)

def update_workout_week(name, day_of_week, workout_plan=None):
    if workout_plan is None:
        return

    query = "UPDATE workout_week SET workout_plan = ? WHERE name = ? AND day_of_week = ?"
    execute_query(query, (workout_plan, name, day_of_week))

def delete_user(name):
    query = "DELETE FROM users WHERE name = ?"
    execute_query(query, (name,))

def delete_workout_plan(plan_name):
    query = "DELETE FROM workout_plans WHERE workout_plan = ?"
    execute_query(query, (plan_name,))

def delete_workout_plan_detail(plan_id, workout_name):
    query = "DELETE FROM workout_plan_details WHERE plan_id = ? AND workout_name = ?"
    execute_query(query, (plan_id, workout_name))

def delete_workout_week(name, day_of_week):
    query = "DELETE FROM workout_week WHERE name = ? AND day_of_week = ?"
    execute_query(query, (name, day_of_week))

def execute_query(query, params):
    with sqlite3.connect("your_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()