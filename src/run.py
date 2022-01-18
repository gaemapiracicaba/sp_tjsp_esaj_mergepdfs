#!/usr/bin/env python
# coding: utf-8

import os
import sys

# Functions
sys.path.append(os.getcwd())
from src.fix_filenames import *

# Paths
#data_path = os.path.join('..', 'data')
data_path = os.path.join('data')
input_path = os.path.join(data_path, 'input')
output_path = os.path.join(data_path, 'output')
output_apartados_path = os.path.join(output_path, 'apartados')
output_final_path = os.path.join(output_path, 'final')

# Make Directories
os.makedirs(input_path, exist_ok=True)
os.makedirs(output_path, exist_ok=True)
os.makedirs(output_apartados_path, exist_ok=True)
os.makedirs(output_final_path, exist_ok=True)

# Renomeia (copia!) os arquivos
rename_files(input_path, output_apartados_path)

# Sort Files
list_files = sort_files_as_list(output_apartados_path)

# Merge Files
merge_files(output_apartados_path, output_final_path, filename='processo.pdf')
