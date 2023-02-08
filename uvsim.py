
class Machine:
    def __init__(self, init_mem):
        self._accumulator = 0000
        self._program_counter = 0
        self._memory = [0000] * 100
        for i, value in enumerate(init_mem):
            self._memory[i] = value
        print(self._memory)

    def tick(pc_value = None):
        # 
        pass
    
    def interpret_instruction(instruction):
        # 
        pass
    
    def debug_get_accumulator(self):
        '''Returns current value of the machine accumulator for debuging and
        testing puposes.'''
        return self._accumulator

    def read(self, memory_index):
        # Read takes user input and stores that in a location in memory
        new_word = input("Enter a new four-digit word. Ex: +2156, -4328: ")
        self.memory[memory_index] = self._accumulator

    def store(self, memory_index):
        # Store what is in the accumulator into a location in memory
        self.memory[memory_index] = self._accumulator
    
    def add(self, memory_index):
        # Add word from memory to word in accumulator
        self._accumulator += self.memory[memory_index]
        
    def subtract(self, memory_index):
        # Subtract word from memory from the word in accumulator
        self._accumulator += self.memory[memory_index]
        
    def divide(self, memory_index):
        # Divide word in accumulator by word in a memory index
        # NOTE: This function does floor division, which removes any decimal values
        self._accumulator //= self.memory[memory_index]
        
    def multiply(self, memory_index):
        # Multiply word in accumulator by word in a memory index
        self._accumultaor *= self.memory[memory_index]

