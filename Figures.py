class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def print_info(self):
        print(f"Rectangle ({self.x}, {self.y}, {self.height}, {self.width})")