import cv2
import argparse
from src.PlateDetector import PlateDetector
from src.PlateReader import PlateReader
from src.utils import draw_border, draw_plate

# python main.py -i "sample.mp4"
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", help="The path of the input video")

    args = parser.parse_args()

    video_path = args.input

    detector = PlateDetector()
    reader = PlateReader()
    cap = cv2.VideoCapture(video_path)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter("output_video.mp4", fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        results = detector.find_vehicles(frame)

        for result in results:
            x_car1, y_car1, x_car2, y_car2, car_id, license_plate_image = result
            frame = draw_border(frame, (int(x_car1), int(y_car1)), (int(x_car2), int(y_car2)))

            text = reader.read_plate(license_plate_image)
            frame = draw_plate(frame, result, text)

        # Display Frames
        # cv2.imshow("Frame", frame)
        out.write(frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()