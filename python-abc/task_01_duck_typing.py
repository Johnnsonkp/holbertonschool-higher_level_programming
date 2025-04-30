#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area():
    pass

  def perimeter():
    pass

class Circle(Shape):
  pass

class Rectangle(Shape):
  pass
