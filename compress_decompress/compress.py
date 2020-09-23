from os import path


def get_compressed_string(full_sized_data: str) -> str:
    """Function returns compressed version of inputed data.
    Takes repeated character and chande it to "#character" + "#count".

    Args:
        full_sized_data (str): Inputes text.

    Returns:
        str: Decompressed version of inputed text.
    """

    # check if inputed text is string and not empty.
    if not isinstance(full_sized_data, str) or full_sized_data == "":
        return ""

    # init variables
    repeatable_char: str = full_sized_data[0]
    compressed_data: str = ""
    count: int = 1
    cycle: int = 1

    # cycle through inputed text
    for next_char in full_sized_data[1:]:
        if next_char == repeatable_char:
            count += 1
        else:
            compressed_data += f"{repeatable_char}{count}"
            repeatable_char = next_char
            count = 1
    compressed_data += f"{repeatable_char}{count}"

    # return compressed data
    return compressed_data


def get_compressed_file(file_name: str) -> str:
    """Function get file name, read its content and
    returns compressed data.

    Args:
        file_name (str): File name.

    Returns:
        str: Compressed data in 1 string.
    """

    # init variables
    compressed_file: str = ""

    # check if file exists
    if not path.exists(file_name):
        return compressed_file

    # read file and compress data
    with open(file_name, "r") as file_read:
        for line in file_read.readlines():
            compressed_file += get_compressed_string(line)

    # return compressed data
    return compressed_file
