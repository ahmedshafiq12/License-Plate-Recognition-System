import cv2
import argparse
from src.PlateDetector import PlateDetector
from src.Car import Car
from src.utils import draw_border, draw_plate, find_common_numbers

# python main.py -i "sample.mp4" -d
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", help="The path of the input video")
    parser.add_argument("-d", "--display", action="store_true", help="Display output video")

    args = parser.parse_args()

    video_path = args.input
    display = args.display

    detector = PlateDetector()

    cap = cv2.VideoCapture(video_path)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter("output_video.mp4", fourcc, fps, (width, height))

    cars = {}
    while True:
        ret, frame = cap.read()
        results, all_cars_ids = detector.find_vehicles(frame)
        show_ids = []

        for result in results:
            x_car1, y_car1, x_car2, y_car2, car_id, license_plate_image = result
            if car_id in cars.keys():
                cars[car_id].update_car(result)
                text = cars[car_id].plate_number

            else:
                cars[car_id] = Car(result)
                text = cars[car_id].plate_number

        show_ids = find_common_numbers(list(cars.keys()), all_cars_ids)
        for car_id in show_ids:
            car = cars[car_id]
            if car.plate_number != -1:
                frame = draw_border(frame, (car.x_car1, car.y_car1), (car.x_car2, car.y_car2), car.plate_number, car.color)
                # frame = draw_plate(frame,
                #                    car.x_car1, car.y_car1, car.x_car2, car.y_car2,
                #                    car.images["plate_image"],
                #                    car.plate_number)

        # Write Frames
        out.write(frame)

        # Display Frames
        if display:
            frame = cv2.resize(frame, (1280, 720))
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()