#!/usr/bin/env python
# coding: utf-8

import os
import sys

# Functions
sys.path.append(os.getcwd())
from src.fix_filenames import *

# Major Path
data_path = os.path.join('data')
output_path, output_apartados_path = set_directories(data_path)

# Unzip
zipfile_file = os.path.join('data', 'input', '1010642-60.2020.8.26.0019 pequeno.zip')
unzip_zipfile(zipfile_file, output_apartados_path)

# Renomeia os arquivos
rename_files(output_apartados_path)

# Sort Files
list_files = sort_files_as_list(output_apartados_path)

# Output Filename
output_filename = create_output_filename(zipfile_file)

# Merge Files
merge_files(output_apartados_path, output_path, output_filename)

# Clean Directories
shutil.rmtree(output_apartados_path, ignore_errors=True)

print("{:<100}".format('> Fim.'))
