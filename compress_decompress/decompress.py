def get_decompressed_data(compressed_data: str) -> str:
    """Function get compressed data in 1 string and
    returns decompressed data.

    Args:
        compressed_data (str): Compressed data.

    Returns:
        str: Decompressed data.
    """

    # check if inputed string is empty
    if not isinstance(compressed_data, str) or compressed_data == "":
        return ""

    # decompress data and check if inpited data properly compressed.
    decompressed_data_list: list = [
        compressed_data[x] * int(compressed_data[x + 1])
        for x in range(0, len(compressed_data), 2)
        if isinstance(compressed_data[x], str) and compressed_data[x + 1].isdigit()
    ]

    # return decompressed data
    return "".join(decompressed_data_list)
