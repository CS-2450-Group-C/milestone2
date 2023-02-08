from uvsim import Machine
import sys
from parse import parse

def main():
    # Ensure file is given
    if len(sys.argv) < 2:
        print("Usage: python main.py fileName.txt")
        return

    # Fill memory from given file
    memory = []
    try:
        memory = parse(sys.argv[1])
    except ValueError as ex:
        print(ex)
        return
    
    # Create new machine from parsed memory
    machine = Machine(memory)

    while (machine.is_running()):
        machine.tick()

    

if __name__ == "__main__":
    main()