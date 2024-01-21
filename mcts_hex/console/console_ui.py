from utils.menus import Menu
from console.game_manager import GameManager, Difficulty
from utils.utils import Utils

// use os.system('clear') to clear console


class ConsoleUI:
    def __init__(self):
        self.game_manager = GameManager()
        self.state = "main_menu"

    def run(self):
        while self.state != "exit":
            self.handle_state()

    def handle_state(self):
        if self.state == "main_menu":
            self.show_main_menu()
        elif self.state == "new_game_menu":
            self.show_new_game_menu()
        elif self.state == "settings_menu":
            self.show_settings_menu()

    def show_main_menu(self):
        Menu.display_main_menu()
        choice = input("Enter your choice (1-3): ")
        self.process_main_menu_choice(choice)

    def process_main_menu_choice(self, choice):
        if choice == '1':
            self.state = "new_game_menu"
        elif choice == '2':
            self.show_about()
        elif choice == '3':
            self.state = "exit"
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

    def show_new_game_menu(self):
        Menu.display_new_game_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            self.game_manager.play_vs_player()
        elif choice == '2':
            self.game_manager.play_vs_ai()
        elif choice == '3':
            self.game_manager.show_commands()
        elif choice == '4':
            self.state = "settings_menu"
        elif choice == '5':
            self.state = "main_menu"
        elif choice == '6':
            self.state = "exit"
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    def show_settings_menu(self):
        Menu.display_settings_menu(self.game_manager.board_size, self.game_manager.difficulty)
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            self.set_board_size()
        elif choice == '2':
            self.set_difficulty()
        elif choice == '3':
            self.state = "new_game_menu"
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

    def set_board_size(self):
        while True:
            try:
                size = int(input("Enter the new board size (between 5 and 10): "))
                if 5 <= size <= 10:
                    self.game_manager.set_board_size(size)
                    print("Board size set to {}.".format(size))
                    break
                else:
                    print("Please enter an integer between 5 and 10.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def set_difficulty(self):
        while True:
            print("Choose AI difficulty:")
            print("1. Easy")
            print("2. Normal")
            print("3. Hard")

            try:
                choice = int(input("Enter your choice (1-3): "))
                if 1 <= choice <= 3:
                    difficulty = Difficulty(choice)
                    self.game_manager.set_difficulty(difficulty)
                    print("Difficulty set to: {}".format(difficulty.name))
                    break
                else:
                    print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def show_about():
        print("\nDisplaying rules...")
        print(Utils.ABOUT_PAGE)


if __name__ == "__main__":
    game_ui = ConsoleUI()
    game_ui.run()
