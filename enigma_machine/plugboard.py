from .config import ALPHABET

class PlugBoard:
    """Plugboard implementation for an Enigma Machine"""
    def __init__(self, bindings: tuple[str, str]) -> None:
        """Sets up the characters that lead to each other"""
        self.bindings = {}
        for char1, char2 in bindings:
            char1, char2 = char1.upper(), char2.upper()
            if char1 not in ALPHABET or char2 not in ALPHABET:
                raise ValueError("Character not in alphabet")
            if (self.bindings.get(char1) or self.bindings.get(char2)) and not(self.bindings.get(char1) == char2 and self.bindings.get(char2) == char1):
                raise ValueError("Character already has binding applied")
            if char1 == char2:
                raise ValueError("Characters are the same")

            self.bindings[char1] = char2
            self.bindings[char2] = char1
            
    def swap(self, char: str) -> str:
        """Swaps associated characters. If a character is not in the bindings, it gets returned as normal"""
        if char not in self.bindings:
            return char
        return self.bindings[char]