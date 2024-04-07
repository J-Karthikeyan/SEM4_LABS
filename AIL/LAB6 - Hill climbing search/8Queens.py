# Heuristic used is: no. of queens attacking directly or indirectly
# a Queen will have 8x7 = 56 posible successors

import random

class Board:
    def __init__(self, n=8, positions=None):
        self.n = n
        if positions is None:
            positions = [random.randint(0, n-1) for _ in range(n)]
        self.positions = positions  

    def __str__(self):
        result = '-' * self.n * 3 + "\n"
        for i in range(self.n):
            for j in range(self.n):
                if self.positions[i] == j:
                    result += " Q "
                else:
                    result += " . "
            result += "\n"
        result += '-' * self.n * 3 + "\n" + f"Total cost: {self.compute_attacks()}\n"

        return result

    def compute_attacks(self):
        attacks = 0
        
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.positions[i] == self.positions[j] or abs(i - j) == abs(self.positions[i] - self.positions[j]):
                    attacks += 1
        
        return attacks
        
    def generate_neighbours(self):
        neighbours = []
        for i in range(self.n):
            for j in range(self.n):
                if j != self.positions[i]:
                    new_positions = self.positions[:]
                    new_positions[i] = j
                    neighbours.append(Board(positions=new_positions))
        return neighbours

def hill_climbing(initial_board):
    current = initial_board
    
    while True:
        neighbors = current.generate_neighbours()
        best_neighbor = min(neighbors, key=lambda x: x.compute_attacks())
        
        if best_neighbor.compute_attacks() > current.compute_attacks():
            return current
        
        current = best_neighbor

if __name__ == "__main__":
    initial_board = Board()
    print("Initial random position:\n", initial_board)

    final_board = hill_climbing(initial_board)
    print("Final Solution:\n", final_board)
