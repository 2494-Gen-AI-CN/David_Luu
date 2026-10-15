class TurnCounter:
    def __init__(self):
        self.turn = 1
    
    def next_turn(self):
        self.turn += 1
    
    def display(self):
        print(f"===== Turn {self.turn} =====\n")