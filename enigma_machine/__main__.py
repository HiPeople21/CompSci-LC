from .config import (
    ALPHABET,
    REFLECTOR_CONFIGURATIONS,
    ROTOR_CONFIGURATIONS,
)

from .plugboard import PlugBoard
from .rotor import RotorManager


def construct_table(**kwargs) -> str:
    """Constructs a table"""
    if len(kwargs) == 0:
        raise ValueError("At least 1 field must be given")
    for i in range(len(kwargs.values()) - 1):
        if len(kwargs.values()[i]) != len(kwargs.values()[i + 1]):
            raise ValueError("Number of items in fields do not match")
    index_column_width = max(len(str(len(list(kwargs.values())[0]))), 5)
    field_column_widths = [max(max(len(i) for i in v),len(k)) for k, v in kwargs.items()]
    result = f"┌{'─'*index_column_width}" + ''.join(f'┬{"─"*i}' for i in field_column_widths) + "┐\n"
    result += f"│{'Index':^{index_column_width}}" + ''.join(f"│{list(kwargs.keys())[i]: ^{field_column_widths[i]}}" for i in range(len(kwargs.items()))) + "│\n"
    result += f"├{'─'*index_column_width}" + ''.join(f'┼{"─"*field_column_widths[i]}' for i in range(len(kwargs.items()))) + "┤\n"
    for i in range(len(list(kwargs.values())[0])):
        result += f"│{f'{i}':^{index_column_width}}" + ''.join(f"│{list(kwargs.values())[j][i]: ^{field_column_widths[j]}}" for j in range(len(kwargs.values()))) + "│\n"
    result += f"└{'─'*index_column_width}" + ''.join(f'┴{"─"*i}' for i in field_column_widths) + "┘\n"
    return result

class EnigmaMachine:
    """Enigma machine implementation"""
    def __init__(self) -> None:
        """Sets up configuration"""
        print("Pick your rotors.")
        print(construct_table(rotor_configuration=ROTOR_CONFIGURATIONS))
        
        configs = []
        rotations = []
        exit_choice = False
        while not exit_choice:
            index = input("Index: ")
            if not index.isdecimal():
                print("Input must be a natural number or 0")
                continue
            index = int(index)
            if not 0 <= index <= len(ROTOR_CONFIGURATIONS):
                print("Input out of range")
                continue
            configs.append(ROTOR_CONFIGURATIONS[index])
            while True:
                rotation = input("Choose a rotation to begin with for the rotor? (1-26): ")
                if not rotation.isdecimal():
                    print("Input must be a natural number")
                    continue
                rotation = int(rotation)
                if not 1 <= rotation <= len(ROTOR_CONFIGURATIONS):
                    print("Input out of range")
                    continue
                break
            rotations.append(rotation)
            while True:
                choice = input("Do you wish to choose another rotor? (Y/N): ")
                if choice.strip().upper() == 'N':
                    exit_choice = True
                    break
                elif choice.strip().upper() == 'Y':
                    break
                else:
                    print("Please input only 'Y' or 'N'")

        print(construct_table(rotor_configuration=REFLECTOR_CONFIGURATIONS))
        while True:
            index = input("Please pick a reflector: ")
            if not index.isdecimal():
                print("Input must be a natural number or 0")
                continue
            index = int(index)
            if not 0 <= index <= len(REFLECTOR_CONFIGURATIONS):
                print("Input out of range")
                continue
            break
        self.rotor_manager = RotorManager(configs, rotations, REFLECTOR_CONFIGURATIONS[index])
        bindings = {}
        exit_choice = False
        while not exit_choice:
            letters = input("Choose two letters for your plugboard (separated with a space, empty to skip): ").strip()
            if letters == '':
                break
            letters = [letter.upper() for letter in letters.split(" ")]
            if len(letters) != 2:
                print("Please provide only 2 letters")
                continue
            if len(letters[0]) != 1 or len(letters[1]) != 1:
                print("Please only type single characters")
                continue
            if letters[0] not in ALPHABET or letters[1] not in ALPHABET:
                print("Please only input alphabetical characters")
                continue
            if (bindings.get(letters[0]) or bindings.get(letters[1])) and not(bindings[letters[0]] == letters[1] and bindings[letters[1]] == letters[0]):
                print("Characters already used in binding")
                continue
            if letters[0] == letters[1]:
                print("Please type two different letters")
                continue
            bindings[letters[0]] = letters[1]
            bindings[letters[1]] = letters[0]
            
            while True:
                choice = input("Do you wish to choose another binding? (Y/N): ")
                if choice.strip().upper() == 'N':
                    exit_choice = True
                    break
                elif choice.strip().upper() == 'Y':
                    break
                else:
                    print("Please input only 'Y' or 'N'")
                    
        self.plugboard = PlugBoard((k,v) for k, v in bindings.items())
            
    def encrypt(self, text: str) -> str:
        """Returns the scrambled message"""
        text = text.upper()
        result = ""
        for char in text:
            char = self.plugboard.swap(char)
            char = self.rotor_manager.scramble(char)
            char = self.plugboard.swap(char)
            result += char
        return result
if __name__ == "__main__":
    # machine = EnigmaMachine()
    # print(machine.encrypt(input("Message to encrypt: ")))
    a = RotorManager(ROTOR_CONFIGURATIONS[1:4], [2,3,4], REFLECTOR_CONFIGURATIONS[0])
    for i in input(""):
        print(a.scramble(i))