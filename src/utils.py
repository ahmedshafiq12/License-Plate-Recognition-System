import cv2


def get_car(license_plate, vehicle_track_ids):
    x1, y1, x2, y2, score, class_id = license_plate

    found_it = False
    for j in range(len(vehicle_track_ids)):
        x_car1, y_car1, x_car2, y_car2, car_id, conf, car_class = vehicle_track_ids[j]

        if x1 > x_car1 and y1 > y_car1 and x2 < x_car2 and y2 < y_car2:
            car_index = j
            found_it = True
            break

    if found_it:
        x_car1, y_car1, x_car2, y_car2, car_id, conf, car_class = vehicle_track_ids[car_index]
        return x_car1, y_car1, x_car2, y_car2, car_id

    return -1, -1, -1, -1, -1


def draw_border(img, top_left, bottom_right, color=(0, 255, 0), thickness=10, line_length_x=200, line_length_y=200):
    x1, y1 = top_left
    x2, y2 = bottom_right

    cv2.line(img, (x1, y1), (x1, y1 + line_length_y), color, thickness)
    cv2.line(img, (x1, y1), (x1 + line_length_x, y1), color, thickness)

    cv2.line(img, (x1, y2), (x1, y2 - line_length_y), color, thickness)
    cv2.line(img, (x1, y2), (x1 + line_length_x, y2), color, thickness)

    cv2.line(img, (x2, y1), (x2 - line_length_x, y1), color, thickness)
    cv2.line(img, (x2, y1), (x2, y1 + line_length_y), color, thickness)

    cv2.line(img, (x2, y2), (x2, y2 - line_length_y), color, thickness)
    cv2.line(img, (x2, y2), (x2 - line_length_x, y2), color, thickness)

    return img


def draw_plate(frame, result, text):
    x_car1, y_car1, x_car2, y_car2, car_id, license_plate_image = result

    height, width = license_plate_image.shape[:2]

    scaling_factor = 3

    license_plate_image = cv2.resize(license_plate_image, (width * scaling_factor, height * scaling_factor))
    H, W, _ = license_plate_image.shape

    frame[int(y_car1) - H - 100:int(y_car1) - 100,
    int((x_car2 + x_car1 - W) / 2):int((x_car2 + x_car1 + W) / 2), :] = license_plate_image

    frame[int(y_car1) - H - 400:int(y_car1) - H - 100,
    int((x_car2 + x_car1 - W) / 2):int((x_car2 + x_car1 + W) / 2), :] = (255, 255, 255)

    (text_width, text_height), _ = cv2.getTextSize(
        text,
        cv2.FONT_HERSHEY_SIMPLEX,
        2.5,
        10)

    cv2.putText(frame,
                text,
                (int((x_car2 + x_car1 - text_width) / 2), int(y_car1 - H - 250 + (text_height / 2))),
                cv2.FONT_HERSHEY_SIMPLEX,
                2.5,
                (0, 0, 0),
                10)

    return frame