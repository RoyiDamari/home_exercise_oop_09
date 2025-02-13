from abc import ABC, abstractmethod


class Component(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add_child(self, child):
        pass

    @abstractmethod
    def remove_child(self, child):
        pass

    @abstractmethod
    def get_children(self):
        pass

    @abstractmethod
    def draw(self, space):
        pass

