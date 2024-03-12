from preprocessing.preprocessing import Preprocessing
from preprocessing.post_processing import Post_Processing
from detection.detection import Detection


def receipt_recognition(image_path):
    preprocess = Preprocessing(image_path)
    post = Post_Processing(preprocess.process_image())
    data = Detection(post.post_process())
    return data.detection()