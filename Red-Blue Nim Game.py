class RedBlueNimGame:
    def _init_(self):
        self.red_count = 10
        self.blue_count = 10
        self.current_player = 1

    def display_counts(self):
        print(f"Red: {self.red_count}, Blue: {self.blue_count}")

    def switch_player(self):
        self.current_player = 3 - self.current_player
        print(f"\nPlayer {self.current_player}'s turn!")

    def remove_objects(self, color, count):
        if color == "red":
            if count > self.red_count or count <= 0:
                print("Invalid number of red items to remove!")
                return False
            self.red_count -= count
        elif color == "blue":
            if count > self.blue_count or count <= 0:
                print("Invalid number of blue items to remove!")
                return False
            self.blue_count -= count
        return True

    def check_game_over(self):
        if self.red_count == 0 and self.blue_count == 0:
            print(f"\nPlayer {self.current_player} loses!")
            return True
        return False

    def play(self):
        while True:
            self.display_counts()
            color = input(f"Player {self.current_player}, choose a color to remove (red/blue): ").strip().lower()
            if color not in ["red", "blue"]:
                print("Invalid color choice!")
                continue
            try:
                count = int(input(f"How many {color} objects do you want to remove? "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if self.remove_objects(color, count):
                if self.check_game_over():
                    break
                self.switch_player()

if __name__ == "_main_":
    game = RedBlueNimGame()
    game.play()
