import pytest
from uvsim import Machine

def test_add():
    memory = [2000, 3001]
    machine = Machine(memory)
    while (machine.is_running()):
        machine.tick()
    assert machine.debug_get_accumulator() == 5001

def test_subtract():
    memory = [2000, 3001, 3100]
    machine = Machine(memory)
    while (machine.is_running()):
        machine.tick()
    assert machine.debug_get_accumulator() == 3001

def test_divide():
    memory = [2000, 3001, 3200]
    machine = Machine(memory)
    while (machine.is_running()):
        machine.tick()
    assert machine.debug_get_accumulator() == 2

def test_multiply():
    memory = [2000, 3001, 3300]
    machine = Machine(memory)
    while (machine.is_running()):
        machine.tick()
    assert machine.debug_get_accumulator() == 10002000

def test_load():
    memory = [2000, 3001, 3300, 2002]
    machine = Machine(memory)
    while (machine.is_running()):
        machine.tick()
    assert machine.debug_get_accumulator() == 3300

def test_store():
    memory = [2000, 3001, 3300, 2000, 2106]
    machine = Machine(memory)
    while (machine.is_running()):
        machine.tick()
    assert machine._memory[6] == 2000