#!/usr/bin/env python
# coding: utf-8

import os
import re
import shutil
from zipfile import ZipFile
from PyPDF2 import PdfFileMerger, PdfFileReader


def set_directories(zipfile_file):
    # Paths
    input_path = os.path.dirname(os.path.abspath(zipfile_file))

    while not zipfile_file.lower().endswith(('.zip', '.ZIP')):
        return 'Selecionar um arquivo .zip'

    #
    temp = os.path.basename(zipfile_file).replace('.zip', '')
    output_path = os.path.join(input_path, temp)
    output_apartados_path = os.path.join(input_path, temp, 'apartados')

    # Clean Directories
    shutil.rmtree(output_path, ignore_errors=True)

    # Make Directories
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(output_apartados_path, exist_ok=True)
    return input_path, output_path, output_apartados_path


def unzip_zipfile(zipfile_file, output_path):
    """
    Para descompactar apenas um arquivo .zip específico
    """
    print('> Etapa 1: Descompacta arquivo')
    if not os.path.isfile(zipfile_file):
        msg = 'É necessário selecionar um arquivo .zip'
        print(msg)

    if not os.path.isdir(output_path):
        msg = 'É necessário selecionar uma pasta'
        print(msg)

    try:
        with ZipFile(zipfile_file, 'r') as zipObj:
            # Extract all the contents of zip file in different directory
            zipObj.extractall(output_path)
        msg = '{:<100}'.format('> Etapa 1: Concluída.')
    except Exception as e:
        msg = '{:<100}'.format('Erro: ' + e)
    print(msg, end='\r')
    return msg


def extract_text(filename):
    """
    Função que pega o nome do arquivo e cria o nome nome, utilizando
    a primeira página dos documentos extraidos dos documentos do e-SAJ
    imediatamente após o "(pag "...
    """
    # Prefixo e Sufixo da busca, para ser deletado
    start = 'pag '
    end = '.pdf'
    
    # Deleta
    text = re.search('(?<={}).*?(?={})'.format(start, end), filename)
    text = text.group()
    text = text.replace(')', '')
    page_1st = text.split(' - ')[0]
    page_1st = int(page_1st)
    return '{} - {}'.format(page_1st, filename)


def get_n_files(input_path):
    n_files = 0
    for path, dirs, files in os.walk(input_path):
        n_files += len(files)
    return n_files


def rename_files(input_files_path):
    print('> Etapa 2: Renomear Arquivos')
    
    # Parameters
    n_file = 0
    n_files = get_n_files(input_files_path)
    
    # Loop
    for path, dirs, files in os.walk(input_files_path):
        for file in files:
            n_file+=1
            input_file = os.path.join(path, file)
            output_filename = extract_text(file)
            output_file = os.path.join(input_files_path, output_filename)
            print('Arquivo {} de {} renomeado - {}% concluído. Aguarde.'.format(n_file, n_files, int(n_file/n_files*100)), end='\r')
            os.rename(input_file, output_file)
    
    # 
    print("{:<100}".format('> Etapa 2: Concluída.'), end='\r')


def adjust_bookmark(filename):
    """
    Cria um nome para o bookmark a partir do nome do arquivo.
    """
    bookmark = filename.split(' - ', maxsplit=1)[-1]
    bookmark = bookmark.replace('.pdf', '')
    return bookmark


def get_int(name):
    """
    Custom Function to sort list of files, based in their names.
    """
    num = name.split(' - ')[0]
    return int(num)


def sort_files_as_list(path):
    """
    Sort list os files in directort
    """
    # List Files
    list_files = os.listdir(path)

    # Sort
    list_files.sort(key=get_int)
    return list_files


def merge_files(input_files_path, output_file_path, filename):
    # Append PDF files sorted
    print('> Etapa 3: Unifica Arquivos')

    # List Files
    list_files = sort_files_as_list(input_files_path)

    # Parameters
    n_file = 0
    n_files = get_n_files(input_files_path)

    # Call the PdfFileMerger
    merged_object = PdfFileMerger()
    
    # Loop
    for file in list_files:
        n_file+=1
        bookmark = adjust_bookmark(file)
        merged_object.append(
            PdfFileReader(os.path.join(input_files_path, file), 'rb'),
            bookmark,
        )
        print('Arquivo {} de {} juntado - {}% concluído. Aguarde.'.format(n_file, n_files, int(n_file/n_files*100)), end = '\r')

    # Write all the files into a file which is named as shown below
    merged_object.write(os.path.join(output_file_path, filename))
    
    # Fim
    print("{:<100}".format('> Etapa 3: Concluída.'), end='\r')
    return 0


def create_output_filename(zipfile_file):
    output_filename = os.path.basename(zipfile_file)
    output_filename = output_filename.replace('.zip', '.pdf').replace('.ZIP', '.pdf')
    return output_filename




