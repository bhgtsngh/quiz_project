import sqlite3
import json

highest_score_file = "highest_score.json"

def load_highest_score():
    try:
        with open(highest_score_file, 'r') as file:
            content = file.read()
            if content.strip() == "":
                return 0
            return json.loads(content).get("highest_score", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0


def save_highest_score(score):
    with open(highest_score_file, 'w') as file:
        json.dump({"highest_score": score}, file)

def get_questions(level):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT question, answer FROM questions
    WHERE level = ?
    ''', (level,))
    questions = cursor.fetchall()
    conn.close()
    return questions

def ask_question(question, answer):
    user_answer = input(question + " ")
    return user_answer.strip().lower() == answer.lower()

def play_level(level):
    questions = get_questions(level)
    score = 0
    for question, answer in questions:
        if ask_question(question, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {answer}")
    return score

def play_game():
    current_highest_score = load_highest_score()
    print(f"Welcome to the Quiz Game! The highest score is {current_highest_score}")

    total_score = 0
    for level in range(1, 6):
        print(f"\nStarting Level {level}")
        level_score = play_level(level)
        total_score += level_score
        print(f"Level {level} complete. Score: {level_score}. Total Score: {total_score}")
        if level_score < 2:
            print("You didn't score enough to pass to the next level. Game Over.")
            break
    else:
        print("Congratulations! You've completed all levels.")

    print(f"Your final score is: {total_score}")

    if total_score > current_highest_score:
        print("New highest score!")
        save_highest_score(total_score)
    else:
        print(f"Highest score remains: {current_highest_score}")

if __name__ == "__main__":
    play_game()
