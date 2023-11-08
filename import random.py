import random

def choose_game_mode():
    print("Выберите действие: ")
    print("1. Камень")
    print("2. Ножницы")
    print("3. Бумага")
    mode = input("Вы выбрали: ")
    if mode == "1":
        return "камень"
    elif mode == "2":
        return "ножницы"
    elif mode == "3":
        return "бумага"
    else:
        print("Ты под психоделиками?.")
        return choose_game_mode()

def check_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Ничья"
    elif player_choice == "камень" and computer_choice == "ножницы" or \
         player_choice == "ножницы" and computer_choice == "бумага" or \
         player_choice == "бумага" and computer_choice == "камень":
        return "Вы победили"
    else:
        return "Вы проиграли"

def play_game():
    player_choice = choose_game_mode()
    computer_choice = random.choice(["камень", "ножницы", "бумага"])
    print("Вы выбрали:", player_choice)
    print("Компьютер выбрал:", computer_choice)
    result = check_result(player_choice, computer_choice)
    print("Результат игры:", result)

play_game()
