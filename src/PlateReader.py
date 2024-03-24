from paddleocr import PaddleOCR
import string


class PlateReader:
    def __init__(self):
        self.ocr_model = PaddleOCR(use_angle_cls=False,
                                   lang='en',
                                   det_model_dir="weights/det",
                                   rec_model_dir="weights/rec",
                                   cls_model_dir="weights/cls")
        # Mapping dictionaries for character conversion
        self.dict_char_to_int = {'O': '0',
                                 'I': '1',
                                 'J': '3',
                                 'A': '4',
                                 'G': '6',
                                 'S': '5'}

        self.dict_int_to_char = {'0': 'O',
                                 '1': 'I',
                                 '3': 'J',
                                 '4': 'A',
                                 '6': 'G',
                                 '5': 'S'}

    def license_complies_format(self, text):
        if len(text) != 7:
            return False

        if (text[0] in string.ascii_uppercase or text[0] in self.dict_int_to_char.keys()) and \
                (text[1] in string.ascii_uppercase or text[1] in self.dict_int_to_char.keys()) and \
                (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[
                    2] in self.dict_char_to_int.keys()) and \
                (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[
                    3] in self.dict_char_to_int.keys()) and \
                (text[4] in string.ascii_uppercase or text[4] in self.dict_int_to_char.keys()) and \
                (text[5] in string.ascii_uppercase or text[5] in self.dict_int_to_char.keys()) and \
                (text[6] in string.ascii_uppercase or text[6] in self.dict_int_to_char.keys()):
            return True
        else:
            return False

    def format_license(self, text):
        license_plate_ = ''
        mapping = {0: self.dict_int_to_char, 1: self.dict_int_to_char, 4: self.dict_int_to_char,
                   5: self.dict_int_to_char,
                   6: self.dict_int_to_char,
                   2: self.dict_char_to_int, 3: self.dict_char_to_int}
        for j in [0, 1, 2, 3, 4, 5, 6]:
            if text[j] in mapping[j].keys():
                license_plate_ += mapping[j][text[j]]
            else:
                license_plate_ += text[j]

        final_license_plate = license_plate_[:4] + " " + license_plate_[4:]
        return final_license_plate

    def read_plate(self, image):
        result = self.ocr_model.ocr(image)[0]
        try:
            line = result[0]
            p1, p2, p3, p4 = line[0]
            text, conf = line[1]
            if self.license_complies_format(text):
                return self.format_license(text)
            else:
                return -1
        except:
            return -1