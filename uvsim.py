
class Machine:
    def __init__(self, init_mem):
        self._memory = [0000] * 100
        for i, value in enumerate(init_mem):
            self._memory[i] = value
        print(self._memory)

