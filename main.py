from compress_decompress import get_compressed_file, get_decompressed_data

from argparse import ArgumentParser, Namespace
from os import path


def get_parsed_arguments() -> Namespace:
    """Create parser through inputed arguments.

    Returns:
        Namespace: Namespace class instance, contain inputed arguments.
    """

    # create parser
    parser: ArgumentParser = ArgumentParser(
        description="Simple module to compress and decompress data."
    )

    # parse arguments
    parser.add_argument(
        "method",
        help="Takes method: compress or decompress.",
        type=str,
        choices=["compress", "decompress"],
    )
    parser.add_argument("--read", help="Takes name of file to read.", required=True)
    parser.add_argument("--write", help="Takes name of file to write.", required=True)

    # return parsed data
    return parser.parse_args()


def start_compress_method() -> None:
    """Read file, compress data,
    write compressed data to file.
    """

    with open(namespace.write, "w") as write_file:
        write_file.write(get_compressed_file(namespace.read))


def start_decompress_method() -> None:
    """Read file, decompress data,
    write decompressed data to file.
    """

    # read file
    with open(namespace.read, "r") as read_file:
        compressed_data: str = read_file.read()

    # write decompressed data
    with open(namespace.write, "w") as write_file:
        write_file.write(get_decompressed_data(compressed_data))


if __name__ == "__main__":
    # parse through inputed arguments
    namespace: Namespace = get_parsed_arguments()

    # check if file exists
    if not path.exists(namespace.read):
        print(f"File {namespace.read} dosen`t exist.")
    elif namespace.method == "compress":
        start_compress_method()
    else:
        start_decompress_method()
