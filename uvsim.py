
class Machine:
    def __init__(self, init_mem):
        self._accumulator = 0000
        self._program_counter = 0
        self._memory = [0000] * 100
        self._running = True
        for i, value in enumerate(init_mem):
            self._memory[i] = value
        print(self._memory)

    def tick(self):
        '''Obtains the next operation, increments the program counter, and
        passes the operation to the interpret_instruction() method for further
        processing.'''
        self._running = True
        operation_address = self._program_counter
        operation = self._memory[operation_address]
        self._program_counter += 1
        if (self.interpret_instruction(operation) < 0):
            print(f"Error: Invalid instruction \"{operation}\" at memory address {operation_address}")
            print("Halting program.")
            self._running = False
    
    def interpret_instruction(self, instruction):
        if (instruction < 0):
            return -1
        str_instruction = str(instruction)
        if str_instruction[0] == "1":
            self.op_io(str_instruction[1], int(str_instruction[2:]))
        elif str_instruction[0] == "2":
            self.op_ls(str_instruction[1], int(str_instruction[2:]))
        elif str_instruction[0] == "3":
            self.op_ar(str_instruction[1], int(str_instruction[2:]))
        elif str_instruction[0] == "4":
            self.op_br(str_instruction[1], int(str_instruction[2:]))
        else:
            return -1
        return 0

    def is_running(self):
        return self._running

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
        self._accumulator -= self.memory[memory_index]
        
    def divide(self, memory_index):
        # Divide word in accumulator by word in a memory index
        # NOTE: This function does floor division, which removes any decimal values
        self._accumulator //= self.memory[memory_index]
        
    def multiply(self, memory_index):
        # Multiply word in accumulator by word in a memory index
        self._accumulator *= self.memory[memory_index]

