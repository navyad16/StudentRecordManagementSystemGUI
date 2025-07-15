from DB_Config import get_connection

def fetch_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def insert_student(name, roll, branch, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, roll_no, branch, phone) VALUES (%s, %s, %s, %s)",
                (name, roll, branch, phone))
    conn.commit()
    conn.close()

def update_student(student_id, name, roll, branch, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE students SET name=%s, roll_no=%s, branch=%s, phone=%s WHERE id=%s",
                (name, roll, branch, phone, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    conn.close()
