import psycopg2
def get_connection():
    return psycopg2.connect(
        host="localhost",
        user="user",
        port=6543,
        password="Aa@12345",
        dbname="student_db"
    )

