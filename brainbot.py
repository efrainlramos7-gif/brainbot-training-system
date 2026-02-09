# 🧠 BrainBot Training System

BrainBot is a Python-based mental math training and automation system.  
It helps users improve basic arithmetic skills while tracking progress, score, and level.

This project demonstrates the use of:

- Object-Oriented Programming (OOP)
- Instance Methods
- Class Methods
- Static Methods
- Control Logic
- Automation Loops
- Data Tracking

---

## 📌 Features

- Generates random addition problems
- Adjusts difficulty based on user level
- Tracks score and rounds played
- Automatically levels up users
- Stores all users in a shared database
- Displays system reports
- Includes a focus and study-time checker
- Menu-driven automated control system

---

## 🛠️ Technologies Used

- Python 3
- Standard Library (`random` module)

No external packages required.

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python brainbot.py

#========================================
# Below is the full and fun code:
#=======================================

import random


class BrainBot:

    # CLASS DATA (shared by all bots)
    all_bots = []
    total_sessions = 0

    def __init__(self, name):
        # INSTANCE DATA (belongs to one bot)
        self.name = name
        self.score = 0
        self.level = 1
        self.rounds_played = 0

        BrainBot.all_bots.append(self)

    # INSTANCE METHOD
    # One bot asks a math question
    def ask_question(self):

        max_num = self.level * 10

        a = random.randint(1, max_num)
        b = random.randint(1, max_num)

        answer = a + b

        print("\n", self.name, "Level", self.level)
        print("What is:", a, "+", b, "?")

        user = int(input("Your answer: "))

        self.rounds_played += 1
        BrainBot.total_sessions += 1

        if user == answer:
            print("Correct answer.")
            self.score += 10
            self.check_level_up()
        else:
            print("Incorrect answer. The correct answer was:", answer)
            self.score -= 3

    # INSTANCE METHOD
    # Controls leveling
    def check_level_up(self):

        if self.score >= self.level * 50:
            self.level += 1
            print("Level up. You are now level", self.level)

    # CLASS METHOD
    # Shows all bots data
    @classmethod
    def show_database(cls):

        print("\n=== BRAINBOT DATABASE ===")

        for bot in cls.all_bots:
            print(
                "Name:", bot.name,
                "| Level:", bot.level,
                "| Score:", bot.score,
                "| Rounds:", bot.rounds_played
            )

    # CLASS METHOD
    # Shows total training
    @classmethod
    def system_report(cls):

        print("\n=== SYSTEM REPORT ===")
        print("Total bots:", len(cls.all_bots))
        print("Total sessions:", cls.total_sessions)

    # STATIC METHOD
    # Brain health checker (tool)
    @staticmethod
    def focus_check(minutes):

        if minutes < 20:
            return "Keep going. Your focus is improving."
        elif minutes < 40:
            return "Good focus level."
        else:
            return "You should take a break."


# ==============================
# AUTOMATION CONTROLLER
# ==============================

def main():

    print("=== BRAINBOT TRAINING SYSTEM ===")

    name = input("Enter your name: ")

    bot = BrainBot(name)

    while True:

        print("\n--- MENU ---")
        print("1. Train Brain")
        print("2. Show My Stats")
        print("3. System Report")
        print("4. Focus Check")
        print("5. Quit")

        choice = input("Choose: ")

        if choice == "1":
            bot.ask_question()

        elif choice == "2":
            BrainBot.show_database()

        elif choice == "3":
            BrainBot.system_report()

        elif choice == "4":
            mins = int(input("How many minutes studied? "))
            print(BrainBot.focus_check(mins))

        elif choice == "5":
            print("Good job today. Training session ended.")
            break

        else:
            print("Invalid choice. Please try again.")


# START SYSTEM
main()

