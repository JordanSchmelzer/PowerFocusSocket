"""
object holding messaging definitions for Server and Client
Standard In: string
Standard Out: dictionary
"""
# import json
import logging
from utils import leftpad


class AppMessageCodex:
    # decoded_packet = json.decoder()

    encoded_message = ""
    decoded_message = {}

    # Integrator: communication start
    def MID1():
        return "00200001003         " + chr(0)

    # Server:
    def MID2():
        pass

    # Integrator: communication stop
    def MID3():
        return "00200003            " + chr(0)

    # Server: Command Error
    def MID4(response):
        logging.info(f"[SERVER]:[" + response + "]: Command error")
        print(
            "[ERROR]: Something went wrong! Controller had an error processing request"
        )
        pass

    # Server: Command accepted
    def MID5(response):
        logging.info(f"[SERVER]:[" + response + "]: Command accepted")

    # Integrator: get pset
    def MID12(pset: int):
        return "00230012            " + leftpad(str(pset), 3, "0") + chr(0)

    # Server: pset request response
    # TODO: json schema should auto genearate dict struct by MID
    def MID13(message):
        decoded_message = {}

        logging.info("[SERVER]:[" + message + "]: Parameter set data upload reply")

        # HEADER
        decoded_message["length"] = message[:4]
        decoded_message["mid"] = message[4:8]
        decoded_message["revision"] = message[8:11]
        decoded_message["ack_flag"] = message[12]
        decoded_message["station_id"] = message[12:14]
        decoded_message["spindle_id"] = message[14:16]
        decoded_message["spare"] = message[16:20]

        if len(message) <= 20:
            return decoded_message

        # DATA
        decoded_message["pset_id"] = message[22:25]  # rng 000-999
        decoded_message["pset_name"] = message[27:52]  # 25 chr, right pad " "
        decoded_message["rotation_dir"] = message[55]  # 1=CW, 2=CCW
        decoded_message["batch_size"] = message[57:59]  # rng 00-99
        decoded_message["torque_min"] = message[61:67]  # multiplied by 100
        decoded_message["torque_max"] = message[69:75]  # multiplied by 100
        decoded_message["torque_target"] = message[77:83]  # multiplied by 100
        decoded_message["angle_min"] = message[85:90]  #
        decoded_message["angle_max"] = message[92:97]  #
        decoded_message["angle_target"] = message[99:104]  #

        return decoded_message
