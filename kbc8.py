import tkinter as tk
import random

questions = {
     "What is the capital of France?": {
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris",
        "prize": 5000
    },
    "Which planet is known as the Red Planet?": {
        "options": ["Mars", "Jupiter", "Venus", "Saturn"],
        "answer": "Mars",
        "prize": 5000
    },
    "Who composed the Indian National Song 'Vande Mataram'?": {
        "options": ["Rabindranath Tagore", "Bankim Chandra Chattopadhyay", "Sarojini Naidu", "Kavi Pradeep"],
        "answer": "Bankim Chandra Chattopadhyay",
        "prize": 5000
    },
    "Who painted the Mona Lisa?": {
        "options": ["Michelangelo", "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"],
        "answer": "Leonardo da Vinci",
        "prize": 5000
    },
    "Which country is famous for the tulip festival?": {
        "options": ["Netherlands", "Turkey", "Belgium", "India"],
        "answer": "Netherlands",
        "prize": 5000
    },
    "Which Indian physicist is known as the 'Father of the Indian Nuclear Programme'?": {
        "options": ["C. V. Raman", "Homi Bhabha", "A. P. J. Abdul Kalam", "Vikram Sarabhai"],
        "answer": "Homi Bhabha",
        "prize": 5000
    },
    "What is the largest ocean in the world?": {
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean",
        "prize": 5000
    },
    "Who wrote the famous play 'Romeo and Juliet'?": {
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare",
        "prize": 5000
    },
    "What is the capital of Japan?": {
        "options": ["Kyoto", "Tokyo", "Osaka", "Hiroshima"],
        "answer": "Tokyo",
        "prize": 5000
    },
    "Which is the longest river in the world?": {
        "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
        "answer": "Nile",
        "prize": 5000
    },
    "Who is known as the Father of the Nation in India?": {
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Subhas Chandra Bose"],
        "answer": "Mahatma Gandhi",
        "prize": 5000
    },
    "What is the national sport of India?": {
        "options": ["Cricket", "Hockey", "Football", "Badminton"],
        "answer": "Hockey",
        "prize": 5000
    },
    "What is the largest carnivorous mammal?": {
        "options": ["Lion", "Tiger", "Bear", "Wolf"],
        "answer": "Bear",
        "prize": 5000
    },
    "Who is known as the 'Father of the Indian Constitution'?": {
        "options": ["B.R. Ambedkar", "Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Vallabhbhai Patel"],
        "answer": "B.R. Ambedkar",
        "prize": 5000
    },
    "Which Indian city is known as the 'Pink City'?": {
        "options": ["Jaipur", "Mumbai", "Delhi", "Kolkata"],
        "answer": "Jaipur",
        "prize": 5000
    },
    "What is the currency of Japan?": {
        "options": ["Yuan", "Yen", "Won", "Dollar"],
        "answer": "Yen",
        "prize": 5000
    },
    "Who is known as the father of modern physics?": {
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Niels Bohr"],
        "answer": "Albert Einstein",
        "prize": 5000
    },
    "What is the national flower of India?": {
        "options": ["Rose", "Lotus", "Sunflower", "Jasmine"],
        "answer": "Lotus",
        "prize": 5000
    },
    "Which language is used for web scripting?": {
        "options": ["Python", "Java", "HTML", "C++"],
        "answer": "HTML",
        "prize": 5000
     },
    "What is the largest state by area in India?": {
        "options": ["Rajasthan", "Uttar Pradesh", "Madhya Pradesh", "Maharashtra"],
        "answer": "Rajasthan",
        "prize": 5000
    },
    "What is the traditional attire of men in Kerala called?": {
        "options": ["Dhoti", "Kurta", "Sherwani", "Pheran"],
        "answer": "Dhoti",
        "prize": 5000
    },
    "What is the largest mammal in the world?": {
        "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "answer": "Blue Whale",
        "prize": 5000
    },
    "Who composed the Indian National Anthem, 'Jana Gana Mana'?": {
        "options": ["Rabindranath Tagore", "Mahatma Gandhi", "Jawaharlal Nehru", "Subhash Chandra Bose"],
        "answer": "Rabindranath Tagore",
        "prize": 5000
    },
    "What is the national currency of India?": {
        "options": ["Rupee", "Taka", "Yen", "Dollar"],
        "answer": "Rupee",
        "prize": 5000
    },

    # Add your other questions here...
}

class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")
        self.root.geometry("500x400")
        self.root.configure(bg="#ffffff")

        self.title_label = tk.Label(root, text="Kaun Banega Crorepati", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start KBC", command=self.start_game, font=("Arial", 16) , bg = "green", fg = "white")
        self.start_button.pack(pady=20)

        self.question_label = tk.Label(root, text="", font=("Arial", 18), wraplength=450)
        self.question_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Total Money: ₹0", font=("Arial", 14))
        self.score_label.pack(pady=5)

        self.score = 0
        self.asked_questions = []
        self.question_count = 0
        self.option_buttons = []
        self.feedback_label = None

    def start_game(self):
        self.start_button.destroy()
        self.next_question()

    def next_question(self):
        self.answer = ""
        self.answer_entry = None
        self.feedback_label = None
        self.check_button = None

        self.question_label.config(text="")
        for button in self.option_buttons:
            button.destroy()
        
        remaining_questions = [q for q in questions.items() if q[0] not in self.asked_questions]
        
        if remaining_questions:
            question, data = random.choice(remaining_questions)
            self.asked_questions.append(question)
            options = data["options"]
            answer = data["answer"]
            prize = data["prize"]

            self.question_label.config(text=question)
            self.answer = answer
            self.prize = prize

            for idx, option in enumerate(options):
                button = tk.Button(self.root, text=option, command=lambda ans=option: self.check_answer(ans))
                button.pack(pady=5)
                self.option_buttons.append(button)
        else:
            self.end_game()

    def check_answer(self, user_answer):
        user_answer = user_answer.strip().lower()
        if user_answer == self.answer.lower():
            self.score += self.prize
            self.feedback_label = tk.Label(self.root, text="Correct Answer!", fg="green", font=("Arial", 14), bg="white")
            self.feedback_label.pack(pady=10)
            self.root.after(1500, self.remove_correct_feedback)
        else:
            self.feedback_label = tk.Label(self.root, text=f"Wrong Answer! Game Over. Total prize money: ₹{self.score}", fg="red", font=("Arial", 14), bg="white")
            self.feedback_label.pack(pady=10)
            self.question_count = len(questions)
            self.end_game()

        self.update_score()
        if self.question_count < len(questions):
            self.root.after(1500, self.next_question)
        else:
            self.end_game()

    def remove_correct_feedback(self):
        if self.feedback_label:
            self.feedback_label.destroy()

    def update_score(self):
        self.score_label.config(text=f"Total Money: ₹{self.score}")

    def end_game(self):
        self.question_label.config(text="Game Over! You answered all the questions.")
        for button in self.option_buttons:
            button.destroy()

def main():
    root = tk.Tk()
    kbc = KBCGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
