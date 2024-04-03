"""
Module for text detection.

This module provides functionality to detect text
and extract relevant information from the detected text.
"""


import uuid
import datetime


class Detection:
    """
    Class for text detection and extraction.
    """

    def __init__(self, data=''):
        """
        Initialize the Detection object.

        Args:
            data (str): The input text data to be processed.
        """
        self.data = data

    def detect_text(self):
        """
        Perform text detection and extraction.

        This method processes the input text data
        to detect relevant information.
        It filters the detected text to extract product
        information such as name, price, and category.

        Returns:
            list: A list of dictionaries containing the
            extracted product information.
        """
        def filter_text(info) -> list:
            """
            Filter the detected text to extract product information.

            Args:
                info (list): The detected text information.

            Returns:
                list: A list of dictionaries containing the extracted product information.
            """
            result = []
            index = 2
            current_date = datetime.datetime.now()
            day = current_date.day
            month = current_date.month
            year = current_date.year
            date = f'{day}/{month}/{year}'
            while index < len(info):
                keywords = ["Հատ", "Յ1ատ", "Յատ", "Վատ", 'Գատ', "գի", "կգ", "գր"]
                if any(keyword in info[index] for keyword in keywords):
                    product = {
                        'id': str(uuid.uuid4()),
                        'name': self.find_name(info[index]),
                        'price': (
                            info[index + 1].split(" ")[-1]
                            if info[index + 1].replace('.', '')
                            else 0
                        ),
                        'category': '',
                        'date': date
                    }
                    result.append(product)
                index += 1
            return result

        def process_text(info):
            """
            Process the detected text and extract product information.

            Args:
                info (str): The detected text data.

            Returns:
                list: A list of dictionaries containing the extracted product information.
            """
            text_lines = info.split("\n")
            filtered_text = [line for line in text_lines if line]
            return filter_text(filtered_text)

        return process_text(self.data)

    @staticmethod
    def find_name(name):
        """
        Extract the product name from the detected text.

        Args:
            name (str): The detected text containing the product name.

        Returns:
            str: The extracted product name.
        """
        output_name = ''
        for char in name:
            if char.isdigit() or char in '()<>':
                break
            output_name += char
        output_name = output_name.replace('կգ', '')
        return output_name
