from enum import Enum

class state(Enum):
    active = 1
    inactive = 0

print(state['active'].value)
print(list(state))
print(len(state))