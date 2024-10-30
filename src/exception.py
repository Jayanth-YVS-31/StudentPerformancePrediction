import sys
import logging
from src.logger import logging


def error_message_details(error, error_detail:sys):
    #error_message = f"Error occurred: {error}. Error details: {error_detail}"
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error [{0}] at line [{1}] and error is [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info('dividing by 0 \n just checking the file')
        raise CustomException(e, sys)