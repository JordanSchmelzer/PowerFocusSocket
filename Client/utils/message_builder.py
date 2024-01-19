from utils import leftpad


def integrator_msg(mid, rev, data=""):
    mid_str = leftpad(mid, 4, "0")
    rev_str = leftpad(rev, 3, "0")
    ackflag_str = " "
    stationId_str = " " * 2
    spindleId_str = " " * 2
    spare_bytes = " " * 4
    header = (
        mid_str + rev_str + ackflag_str + stationId_str + spindleId_str + spare_bytes
    )

    if not data:
        return "0020" + header + chr(0)

    # TODO: build something for handling data and total str length
    return header + leftpad(data, 3, 0) + chr(0)
