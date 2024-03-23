from paddleocr import PaddleOCR


class PlateReader:
    def __init__(self):
        self.ocr_model = PaddleOCR(use_angle_cls=False, lang='en', det_model_dir="weights/det", rec_model_dir="weights/rec", cls_model_dir="weights/cls")

    def read_plate(self, image):
        result = self.ocr_model.ocr(image)[0]
        line = result[0]
        p1, p2, p3, p4 = line[0]
        text, conf = line[1]
        print(text)
        return text