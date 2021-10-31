from io import BytesIO
import numpy as np
import cv2
class ImageConverter:
    @staticmethod
    def read_image(file):
        image_stream = BytesIO(file)
        image = cv2.imdecode(np.fromstring(image_stream.read(), np.uint8), 1)
        return image
