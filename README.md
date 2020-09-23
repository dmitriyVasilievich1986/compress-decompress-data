module "compress_decompress" contain 3 functions:
  get_compressed_string, get_compressed_file, get_decompressed_data

function "get_compressed_string" takes string and returns compressed string.
example: take:"aasssde" out:"a2s3d1e1"

function "get_compressed_file" takes name of file as an argument and returns compressed string.

function "get_decompressed_data" takes string, which was properly compress by functions above, as an argument and return decompressed string.

*** Entry Point ***
script "main.py" is a etry point.

"main.py" takes 3 arguments:
  "method": comrpess or decompress.
  "--read file_name": File name, which need to read.
  "--write file_name": File name, which need to write.
  
  example: "python main.py compress --read Pipfile --write compressed_data.txt"
  
*** Example script ***
script "sample.py" contain some simple example usage of module "compress_decompress".
It takes no arguments.
