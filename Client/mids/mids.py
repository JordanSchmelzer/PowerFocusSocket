# import json
from utils import leftpad


class AppMessageCodex:
    # decoded_packet = json.decoder()

    encoded_message = ""
    decoded_message = {}

    # communication start
    def MID1():
        return "00200001003         " + chr(0)

    # communication stop
    def MID3():
        return "00200003            " + chr(0)

    # get pset
    def MID12(pset: int):
        return "00230012            " + leftpad(str(pset), 3, "0") + chr(0)

    # pset request response
    def MID0013(message):
        decoded_packet = {}
        decoded_packet = message[:4]
