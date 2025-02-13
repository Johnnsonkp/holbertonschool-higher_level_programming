#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Create an abstract class (Animal) using the ABC package."""
"""class should have an abstract method called sound."""
"""Subclasses of Animal: Dog."""
"""Subclasses of Animal: Cat."""


class Animal(ABC):
    """Create an abstract class (Animal) using the ABC package."""
    @abstractmethod
    def sound(self):
        """class should have an abstract method called sound."""
        pass


class Dog(Animal):
    """Subclasses of Animal: Dog."""

    def sound(self):
        """ Implement the sound method “Bark”."""
        return "Bark"


class Cat(Animal):
    """Subclasses of Animal: Cat."""

    def sound(self):
        """ Implement the sound method “Meow”."""
        return "Meow"
