import sys
from parse import parse

def main():
    # Ensure file is given
    if len(sys.argv) < 2:
        print("Usage: python uvsim.py fileName.txt")
        return

    # Fill memory from given file
    memory = []
    try:
        memory = parse(sys.argv[1])
    except ValueError as ex:
        print(ex)
        return



if __name__ == "__main__":
    main()
