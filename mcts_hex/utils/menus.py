class Menu:
    @staticmethod
    def display_main_menu():
        print("\n=====================")
        print("   Welcome to Your Game")
        print("=====================")
        print("1. Start new game")
        print("2. About")
        print("3. Quit")

    @staticmethod
    def display_new_game_menu():
        print("\n=====================")
        print("      New Game Menu")
        print("=====================")
        print("1. Play Vs Friend")
        print("2. Play vs AI")
        print("3. Commands")
        print("4. Settings")
        print("5. Back")
        print("6. Exit")

    @staticmethod
    def display_settings_menu(board_size, difficulty):
        print("\n=====================")
        print("     Settings Menu")
        print("=====================")
        print("1. Set Board Size (Current: {})".format(board_size))
        print("2. Set Difficulty (Current: {})".format(str(difficulty).split(".")[1]))
        print("3. Back")