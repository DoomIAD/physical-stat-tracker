import sqlite3

def update_user(username, height_ft=None, height_in=None, birthdate=None, gender=None, 
                neck_circumference=None, waist_circumference=None, goal=None, start_weight=None):
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
    if goal is not None:
        set_clause.append("goal = ?")
        params.append(goal)
    if start_weight is not None:
        set_clause.append("goal_date = ?")
        params.append(start_weight)


    if not set_clause:
        return  # No fields to update

    query = f"UPDATE users SET {', '.join(set_clause)} WHERE username = ?"
    params.append(username)

    execute_query(query, params)

def execute_query(query, params):
    with sqlite3.connect("sql/my_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()