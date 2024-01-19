def to_data_line(key, value):
    data_line = f"[DATA] Key:{key}, Value:{value}"
    return data_line


def append_data_to_file(data: dict):
    file_object = open("./data/ip_query.txt", "a")

    for element in data:
        file_object.writelines(to_data_line(element, data[element]))

    file_object.close()
