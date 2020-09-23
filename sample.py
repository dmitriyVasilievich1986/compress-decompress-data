from compress_decompress import get_compressed_file, get_decompressed_data
from pathlib import Path

# init constants
BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = BASE_DIR / "Pipfile"

# get compressed and decompressed data
compressed_data = get_compressed_file(FILE_NAME)
decompressed_data = get_decompressed_data(compressed_data)

# print result
print(f"\nCompressed data:\n{compressed_data}")
print(f"\nDecompressed data:\n{decompressed_data}")
