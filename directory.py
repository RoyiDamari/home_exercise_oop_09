from component import Component
from typing import override


class Directory(Component):

    def __init__(self, name):
        super().__init__(name)
        self.__children = []

    @override
    def add_child(self, child):
        self.__children.append(child)

    @override
    def remove_child(self, child):
        self.__children.remove(child)

    @override
    def get_children(self):
        return self.__children

    @override
    def draw(self, space=""):
        print(space + f"[{self.name}]")
