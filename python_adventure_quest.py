import time
import random

def start_game():
    print("Welcome to Python Adventure Quest!")
    time.sleep(1)
    print("Embark on a journey to learn Python programming.")
    time.sleep(1)
    print("You will encounter challenges, solve puzzles, and defeat enemies using your coding skills.")
    time.sleep(1)
    print("Let's start with the basics.")
    time.sleep(1)
    introduction()

def introduction():
    print("\nLevel 1: The Python Forest")
    print("You are a young adventurer who stumbled upon the mystical Python Forest.")
    time.sleep(1)
    print("Learn the basics of Python to find your way through.")
    time.sleep(1)
    
    player_name = input("Enter your character's name: ")
    print(f"Welcome, {player_name}! Let's begin your quest.")
    time.sleep(1)
    
    age = 20
    health = 100
    print(f"{player_name}, you are {age} years old and have {health} health points.")
    time.sleep(1)
    
    control_flow(player_name, health)

def control_flow(player_name, health):
    print("\nLevel 2: The Forked Path")
    print("You encounter a fork in the road.")
    time.sleep(1)
    print("Learn about conditionals (if-else statements) to decide your path.")
    time.sleep(1)
    
    choice = input("Do you go left or right? (left/right): ").lower()
    
    if choice == "left":
        print("You find a treasure chest with 20 gold coins!")
        gold = 20
    else:
        print("You encounter a wild beast!")
        time.sleep(1)
        print("Prepare to use your loop skills to defeat it.")
        gold = 0
        health = battle_beast(player_name, health)
    
    functions(player_name, health, gold)

def battle_beast(player_name, health):
    print("The wild beast attacks!")
    beast_health = 30
    while beast_health > 0:
        action = input("Do you attack (a) or defend (d)? ").lower()
        if action == 'a':
            damage = random.randint(5, 15)
            beast_health -= damage
            print(f"You deal {damage} damage to the beast. Beast's health: {beast_health}")
        else:
            damage = random.randint(1, 5)
            health -= damage
            print(f"The beast attacks you! You lose {damage} health points. Your health: {health}")
        if health <= 0:
            print("You have been defeated by the beast. Game Over.")
            return False
    print("You defeated the beast!")
    return health

def functions(player_name, health, gold):
    print("\nLevel 3: The Healing Fountain")
    print("Learn how to define and call functions to heal yourself.")
    time.sleep(1)
    
    def heal(health, amount):
        return health + amount
    
    heal_amount = 20
    health = heal(health, heal_amount)
    print(f"You found a healing fountain! Your health is now {health}.")
    time.sleep(1)
    
    data_structures(player_name, health, gold)

def data_structures(player_name, health, gold):
    print("\nLevel 4: The Ancient Library")
    print("Introduction to lists, dictionaries, and tuples to solve the librarian's puzzle.")
    time.sleep(1)
    
    inventory = ["sword", "shield", "potion"]
    print("Your inventory:", inventory)
    
    stats = {"strength": 10, "agility": 8, "intelligence": 7}
    print("Your stats:", stats)
    
    position = (10, 20)
    print("Your position:", position)
    
    print("\nSolve the librarian's puzzle to proceed.")
    time.sleep(1)
    
    questions = [
        {"question": "What data structure would you use to store a collection of unique keys and values?", "answer": "dictionary"},
        {"question": "What data structure allows you to store a collection of items in an ordered sequence?", "answer": "list"},
        {"question": "Which data structure is immutable and can contain a sequence of items?", "answer": "tuple"},
        {"question": "Which Python keyword is used to define a function?", "answer": "def"},
        {"question": "What method would you use to add an item to the end of a list?", "answer": "append"},
        {"question": "What function would you use to get the length of a list?", "answer": "len"},
        {"question": "What symbol is used to denote a comment in Python?", "answer": "hash"},
        {"question": "Which keyword is used to handle exceptions in Python?", "answer": "try"},
        {"question": "What operator is used for integer division in Python?", "answer": "double slash"},
        {"question": "Which method is used to convert a string to lowercase?", "answer": "lower"},
        {"question": "What does 'print(type(variable))' return?", "answer": "type"},
        {"question": "Which built-in function can be used to get the maximum value in a list?", "answer": "max"},
        {"question": "How do you start a for loop in Python?", "answer": "for"},
        {"question": "Which method is used to remove an item from a list by index?", "answer": "pop"},
        {"question": "What keyword is used to exit a loop early?", "answer": "break"},
        {"question": "How do you start a multi-line comment in Python?", "answer": "triple quotes"}
    ]
    
    selected_questions = random.sample(questions, 5)  # Randomly select 5 questions
    score = 0
    for quiz in selected_questions:
        answer = input(quiz["question"] + " ").lower()
        if answer == quiz["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer was:", quiz["answer"])
    
    print(f"You answered {score} out of {len(selected_questions)} questions correctly.")
    object_oriented_programming(player_name, health, gold)

def object_oriented_programming(player_name, health, gold):
    print("\nLevel 5: The Cursed Castle")
    print("Learn about classes and objects to defeat the castle's guardian.")
    time.sleep(1)
    
    class Character:
        def __init__(self, name, health, gold):
            self.name = name
            self.health = health
            self.gold = gold
        
        def take_damage(self, amount):
            self.health -= amount
            return self.health
    
    player = Character(player_name, health, gold)
    print(f"{player.name} has {player.health} health points and {player.gold} gold coins.")
    
    guardian_damage = random.randint(20, 40)
    player.take_damage(guardian_damage)
    print(f"The guardian attacks! {player.name} takes {guardian_damage} damage. Health is now {player.health}.")
    
    if player.health > 0:
        print(f"Congratulations, {player.name}! You have defeated the guardian and completed the basic levels of Python Adventure Quest.")
        print("Keep practicing to become a Python master!")
    else:
        print("You have been defeated by the guardian. Game Over.")
    
    print("Thank you for playing Python Adventure Quest!")
    restart_game()

def restart_game():
    choice = input("\nWould you like to play again? (yes/no): ").lower()
    if choice == "yes":
        start_game()
    else:
        print("Thank you for playing Python Adventure Quest! Goodbye!")

# Start the game
start_game()

