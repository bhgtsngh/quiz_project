import sqlite3

def create_database():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # Create table for questions
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level INTEGER NOT NULL,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    )
    ''')

    # Add sample questions (you can add more or modify this as needed)
    sample_questions = [
        (1, "What is 2 + 2?", "4"),
        (1, "What is the capital of France?", "Paris"),
        (2, "What is 12 * 12?", "144"),
        (2, "Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
        (3, "What is the capital of Australia?", "Canberra"),
        (3, "What is 15 * 15?", "225"),
        (4, "What is the chemical symbol for gold?", "Au"),
        (4, "Who developed the theory of relativity?", "Einstein"),
        (5, "What is the derivative of x^2?", "2x"),
        (5, "What is the capital of Iceland?", "Reykjavik"),
    ]

    cursor.executemany('''
    INSERT INTO questions (level, question, answer)
    VALUES (?, ?, ?)
    ''', sample_questions)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
