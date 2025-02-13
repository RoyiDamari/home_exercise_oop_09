from Component import Component
from typing import override


class File(Component):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @override
    def add_child(self, child):
        raise NotImplementedError("Cannot add children to a file (Leaf)")

    @override
    def remove_child(self, child):
        raise NotImplementedError("Cannot remove children from a file (Leaf)")

    @override
    def get_children(self):
        return []

    def format_size(self):
        """✅ Convert file size from bytes to human-readable format."""
        if self.size < 1024:
            return f"{self.size} B"
        elif self.size < 1024 ** 2:
            return f"{self.size / 1024:.2f} KB"
        elif self.size < 1024 ** 3:
            return f"{self.size / (1024 ** 2):.2f} MB"
        else:
            return f"{self.size / (1024 ** 3):.2f} GB"

    @override
    def draw(self, space=""):
        """✅ Draws the file with its size."""
        print(space + f"{self.name} - {self.format_size()}")
