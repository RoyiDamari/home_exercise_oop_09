from typing import override
from component import Component


class Folder(Component):

    def __init__(self, name):
        super().__init__(name)
        self.__size = 0
        self.children = []

    @override
    def add_child(self, child: Component):
        self.children.append(child)

    @override
    def remove_file(self, child: Component):
        self.children.remove(child)

    @override
    def get_size(self):
        """Recursively sum up the sizes of all files and subdirectories."""
        return sum(child.get_size() for child in self.children)

    @override
    def print(self, space):
        total_size = self.get_size()
        print(space + self.name, Component.format_size(total_size))
        for file in self.children:
            file.print(space + 4 * " ")

    def __str__(self):
        return f"name: {self.name} size: {self.__size}"