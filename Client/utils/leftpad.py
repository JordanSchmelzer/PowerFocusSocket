import logging


def leftpad(str: str, final_size: int, fill_char: str):
    if str.__len__ > final_size:
        logging.fatal(
            f"[FATAL] input {str} length is larger than final size {final_size}"
        )
        return

    padded_string = fill_char * (final_size - str.__len__) + str
    return padded_string
