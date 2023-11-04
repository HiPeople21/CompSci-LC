from .config import ALPHABET
from .plugboard import PlugBoard

class Rotor:
    """Rotor implementation"""
    def __init__(self, configuration: str, base_rotation: int) -> None:
        """Sets up the configuration for the rotors"""
        configuration = configuration.upper()
        if len(configuration) != 26:  # Checks lenght
            raise ValueError("Configuration doesn't contain the right amount of characters")
        if ''.join(sorted(configuration)) != ALPHABET:  # Checks if the configuration contains all the alphabetical characters
            raise ValueError("The characters do not match the alphabet")
        if base_rotation < 0:
            raise ValueError("Starting rotation should be positive")
        
        self.configuration = dict(
            zip(
                range(1, 27),  # zip(range(1, 27), ALPHABET), 
                (ALPHABET.index(char) + 1 for char in configuration)  # zip((ALPHABET.index(char) + 1 for char in configuration), configuration)
            )
        )
        self.rotation = (base_rotation - 1) % 26

    def forward_encrypt(self, index: int) -> int:
        """Returns the index of the characters that results from the input flowing foward into the rotors"""
        if not 1 <= index <= 26:
            raise ValueError("Index out of bounds")
        if index + self.rotation >= 26:
            return self.configuration[(index + self.rotation) % 26]
        return self.configuration[index + self.rotation]
    
    def backward_encrypt(self, index: int) -> int:
        """Returns the index of the characters that results from the input flowing away from the rotors"""
        if not 1 <= index <= 26:
            raise ValueError("Index out of bounds")
        val = index + self.rotation
        if val >= 26:
            val %= 26
        for key, value in self.configuration.items():
            if value == val:
                return key
    
    def rotate(self) -> None:
        """Rotates the rotor"""
        self.rotation = self.rotation % 26
    
class RotorManager:
    """Manages all the rotors of the Enigma Machine"""
    def __init__(self, rotor_configs: list[str], rotations: list[int], reflector_config: str) -> None:
        if len(rotor_configs) != len(rotations):
            raise ValueError("Number of rotors does not match number of rotations appled")
        self.rotors = [Rotor(configuration.upper(), rotation) for configuration, rotation in zip(rotor_configs, rotations)]
        self.reflector = PlugBoard(zip(ALPHABET, reflector_config.upper()))
        self.characters = 0
        
    def scramble(self, char:str) -> str:
        """Gets scrambled character"""
        char = char.upper()
        if char not in ALPHABET:
            return char
        index = ALPHABET.index(char) + 1
        for rotor in self.rotors:
            index = rotor.forward_encrypt(index)
        index = ALPHABET.index(self.reflector.swap(ALPHABET[index - 1])) + 1
        for rotor in self.rotors[::-1]:
            index = rotor.backward_encrypt(index)
        self.characters += 1
        self.rotate_rotors()
        return ALPHABET[index - 1]
    
    def rotate_rotors(self) -> None:
        """Rotates the rotors"""
        for i in range(len(self.rotors)):
            if self.characters % (26 ** i) == 0:
                self.rotors[i].rotate()
            else:
                break