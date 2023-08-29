"""
Summary
"""

import sys

from esaj_functions import *


def main(zipfile_file):
    """
    _summary_

    :param zipfile_file: _description_
    :type zipfile_file: _type_
    """
    # Set Directories
    input_path, output_path, output_apartados_path = set_directories(zipfile_file)

    # Unzip
    unzip_zipfile(zipfile_file, output_apartados_path)

    # Renomeia os arquivos
    rename_files(output_apartados_path)

    # Sort Files
    list_files = sort_files_as_list(output_apartados_path)

    # Output Filename
    output_filename = create_output_filename(zipfile_file)

    # Merge Files
    merge_files(output_apartados_path, input_path, output_filename)

    # Clean Directories
    shutil.rmtree(output_path, ignore_errors=True)

    print('> Fim.')


if __name__ == '__main__':
    print('Módulo Run')

    # Function
    try:
        zipfile_file2 = os.path.join('..', 'data', '1010642-60.2020.8.26.0019 pequeno.zip')
        main(zipfile_file2)
    except Exception as e:
        print('Rodar por aqui não')
        print(e)

    try:
        main(sys.argv[1])
    except Exception as e:
        print('Rodar por "argv" não deu')
        print(e)
