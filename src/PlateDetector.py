from ultralytics import YOLO
from src.utils import get_car


class PlateDetector:
    def __init__(self):
        self.plate_model = YOLO("weights/PlateDetectorNano.pt")
        self.plate_model.fuse()
        self.vehicles_model = YOLO("weights/yolov8n.pt")
        self.vehicles_model.fuse()

    def find_vehicles(self, frame):
        results = []
        vehicles = self.vehicles_model.track(frame,
                                             classes=[2, 3, 5, 7],
                                             tracker="bytetrack.yaml",
                                             persist=True,
                                             conf=0.5,
                                             iou=0.3)[0]
        vehicles_detections = vehicles.boxes.data.tolist()
        all_cars_ids = vehicles.boxes.id.tolist()

        license_plates = self.plate_model(frame, conf=0.3)[0]
        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate
            # assign license plate to car
            x_car1, y_car1, x_car2, y_car2, car_id = get_car(license_plate, vehicles_detections)

            if car_id != -1:
                license_plate_image = frame[int(y1):int(y2), int(x1): int(x2), :]
                results.append([x_car1, y_car1, x_car2, y_car2, car_id, license_plate_image])

        return results, all_cars_ids
