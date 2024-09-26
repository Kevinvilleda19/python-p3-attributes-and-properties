#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    # List of approved dog breeds
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name="Dog", breed="Mastiff"):
        """
        Initialize the Dog instance with a default name and breed.

        Parameters:
        name (str): The name of the dog. Must be between 1 and 25 characters.
        breed (str): The breed of the dog. Must be in the list of approved breeds.
        """
        self._name = None   # Initialize with None before calling the setter
        self._breed = None  # Initialize with None before calling the setter
        self.name = name    # This will trigger the name setter for validation
        self.breed = breed  # This will trigger the breed setter for validation

    @property
    def name(self):
        """Getter for the name property."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for the name property with validation."""
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        """Getter for the breed property."""
        return self._breed

    @breed.setter
    def breed(self, value):
        """Setter for the breed property with validation."""
        if value in Dog.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

