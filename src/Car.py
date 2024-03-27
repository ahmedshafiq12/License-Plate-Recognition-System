from src.PlateReader import PlateReader
import random
from ultralytics.utils.plotting import Colors


colors = Colors()
reader = PlateReader()


class Car:
    def __init__(self, result):
        x_car1, y_car1, x_car2, y_car2, car_id, license_plate_image = result
        self.car_id = car_id
        self.images = {"plate_image": license_plate_image.copy(),
                       "latest_plate_image": license_plate_image.copy()}
        self.x_car1 = int(x_car1)
        self.y_car1 = int(y_car1)
        self.x_car2 = int(x_car2)
        self.y_car2 = int(y_car2)
        self.plate_number = reader.read_plate(self.images["plate_image"])
        self.color = random.choice(colors.palette)

    def update_car(self, result):
        x_car1, y_car1, x_car2, y_car2, car_id, license_plate_image = result
        self.x_car1 = int(x_car1)
        self.y_car1 = int(y_car1)
        self.x_car2 = int(x_car2)
        self.y_car2 = int(y_car2)
        if self.plate_number == -1:
            self.images["plate_image"] = license_plate_image.copy()
        self.images["latest_plate_image"] = license_plate_image.copy()
        new_number = reader.read_plate(self.images["latest_plate_image"])
        if new_number != -1:
            self.plate_number = new_number
