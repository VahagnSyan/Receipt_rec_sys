"""
Module for Receipt Recognition.

This module provides functionality to recognize text from receipt images.
It includes preprocessing the image, extracting text, and detecting relevant information.

Dependencies:
    - preprocessing.Preprocessing
    - preprocessing.PostProcessing
    - detection.Detection
"""


from preprocessing.preprocessing import Preprocessing
from postprocessing.post_processing import PostProcessing
from extraction.extraction import Extraction


def receipt_recognition(image_path):
    """
    Perform receipt recognition.

    This function preprocesses the input image, post-processes
    the extracted text, and detects relevant information from the text.

    Args:
        image_path (str): The path to the input image.

    Returns:
        list: A list containing the detected text information.
    """
    preprocess = Preprocessing(image_path)
    post = PostProcessing(preprocess.process_image())
    data = Extraction(post.post_process())
    return data.detect_text()
