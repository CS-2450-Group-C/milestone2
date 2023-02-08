"""These are input and output functions. They will either get
input from the user and store it in memory, or write a word
from memory to the screen."""

def read(memory_index):
    # Read takes user input and stores that in a location in memory
    new_word = input("Enter a new four-digit word. Ex: +2156, -4328: ")
    self.memory[memory_index] = accumulator

def store(memory_index):
    # Store what is in the accumulator into a location in memory

    # Psuedo code for storing in memory
    self.memory[memory_index] = accumulator

def main():
    """For testing purpose"""
    output = "+12"
    print(output.ljust(5, "0"))
    # def write(self, memory_index):
    #     # Write a word from a location in memory to the screen
    #     word = self.memory[memory_index]
    #     output = ""
    #     if word < 0:
    #         output = "-" + str(word)
    #     else:
    #         output = "+" + str(word)

    #     print(output.ljust(5, "0"))
