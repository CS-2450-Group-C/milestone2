"""These functions take an index in the memory, then they set the value in the accumulator to the 
value in the accumulator added/subtracted/divided/multiplied by the value obtained by going to the memory_index.
There is temporary pseudo code that will be implemented once the specifics of the program are worked out
(i.e. if the accumulator and memory is in the machine class."""

def add(memory_index):
    # Example call: accumulator_value = arithmetic.add(memory_index)
    
    # TEMPORARY PSEUDO CODE: accumulator.value = accumulator.value + memory[memory_index]
    pass
    
def subtract(memory_index):
    # Example call: accumulator_value = arithmetic.subtract(memory_index)
    
    # TEMPORARY PSEUDO CODE: accumulator.value = accumulator.value - memory[memory_index]
    pass

def divide(memory_index):
    # Example call: accumulator_value = arithmetic.divide(memory_index)
    # NOTE: We must decide how to handle quotients that have decimal points...
    # for now we will just do floor division (//), removing any decimal values.
    
    # TEMPORARY PSEUDO CODE: accumulator.value = accumulator.value // memory[memory_index]
    pass

def multiply(memory_index):
    # Example call: accumulator_value = arithmetic.multiply(memory_index)
    
    # TEMPORARY PSEUDO CODE: accumulator.value = accumulator.value * memory[memory_index]
    pass