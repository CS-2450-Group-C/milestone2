
class Machine:
    def __init__(self, init_mem):
        self.accumulator = 0000
        self._memory = [0000] * 100
        for i, value in enumerate(init_mem):
            self._memory[i] = value
        print(self._memory)
    
    # Should the functions just be class methods?\
    
    # def read(self, memory_index):
    #     # Read takes user input and stores that in a location in memory
    #     new_word = input("Enter a new four-digit word. Ex: +2156, -4328: ")
    #     self.memory[memory_index] = self.accumulator

    # def store(self, memory_index):
    #     # Store what is in the accumulator into a location in memory

    #     # Psuedo code for storing in memory
    #     self.memory[memory_index] = accumulator

