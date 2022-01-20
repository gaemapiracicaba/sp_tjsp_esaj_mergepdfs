#!/usr/bin/env python
# coding: utf-8

import os
import sys

# Functions
sys.path.append(os.getcwd())
from src.merge_process_esaj import *

# Check Directory
print(os.getcwd())

# Variables
data_path = os.path.join('..', 'data')
zipfile_file = os.path.join('..', 'data', 'input', '1010642-60.2020.8.26.0019 pequeno.zip')

# Set Directories
output_path, output_apartados_path = set_directories(data_path)

# Unzip
unzip_zipfile(zipfile_file, output_apartados_path)

# Renomeia os arquivos
rename_files(output_apartados_path)

# Sort Files
list_files = sort_files_as_list(output_apartados_path)

# Output Filename
output_filename = create_output_filename(zipfile_file)

# Merge Files
merge_files(output_apartados_path, os.path.dirname(zipfile_file), output_filename)

# Clean Directories
shutil.rmtree(output_path, ignore_errors=True)

print("{:<100}".format('> Fim.'))

if __name__ == '__main__':
    print('Módulo Run')
