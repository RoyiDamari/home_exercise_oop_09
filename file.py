from typing import override
from component import Component


class File(Component):

    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    @override
    def add_child(self, child: Component):
        raise NotImplementedError

    @override
    def remove_file(self, child: Component):
        raise NotImplementedError

    @override
    def get_size(self):
        return self.__size

    @override
    def print(self, space):
        print(space + self.name, Component.format_size(self.__size))

    def __str__(self):
        return f"name: {self.name} size: {self.__size}"