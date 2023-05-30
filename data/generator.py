import numpy as np
from PIL import Image, ImageDraw


class ImageGenerator:
    def __init__(self, directory, size=(64, 64), start_point=None, end_point=None):
        self.directory = directory
        self.size = size
        self.start_point = start_point
        self.end_point = end_point

        self.generate_points()

    def valid_point(self, point):
        if point is None:
            return False
        if 0 <= point[0] <= self.size[1] and 0 <= point[1] <= self.size[1]:
            return True
        return False

    def valid_points(self):
        if not self.valid_point(self.start_point) or not self.valid_point(
            self.end_point
        ):
            return False
        if (
            self.start_point[0] == self.end_point[0]
            and self.start_point[1] == self.end_point[1]
        ):
            return False
        return True

    def generate_point(self, point):
        return np.random.randint(0, self.size[0], 2)

    def generate_points(self):
        while not self.valid_points():
            self.start_point = self.generate_point(self.start_point)
            self.end_point = self.generate_point(self.end_point)

    def generate_image(self):
        image = Image.new("L", self.size, "white")
        draw = ImageDraw.Draw(image)
        draw.line([tuple(self.start_point), tuple(self.end_point)], "black")
        return image

    def save_image(self, image):
        filename_first = f"{self.directory}/{self.start_point[0]}_{self.start_point[1]}_{self.end_point[0]}_{self.end_point[1]}.png"
        filename_revert = f"{self.directory}/{self.end_point[0]}_{self.end_point[1]}_{self.start_point[0]}_{self.start_point[1]}.png"
        image.save(filename_first)
        image.save(filename_revert)

    def run(self):
        self.generate_points()
        self.save_image(self.generate_image())


if __name__ == "__main__":
    for i in range(5000):
        generator = ImageGenerator(r"data\dataset")
        generator.run()
