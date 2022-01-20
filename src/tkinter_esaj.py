#!/usr/bin/env python
# coding: utf-8

import os
import sys
from tkinter import *
from tkinter import filedialog

# Functions
sys.path.append(os.getcwd())
from src.merge_process_esaj import *


def select_zip_file():
    """
    Function for opening the file explorer window
    """
    global zipfile_file
    zipfile_file = filedialog.askopenfilename(
        initialdir=os.path.join(os.getcwd(), '..'),
        title='Selecionar arquivo zipado (.zip)',
        filetypes=(('Zip files', '*.zip'), ('All files', '*.*'))
    )
    # Configura o Label
    lbl_zip.configure(text='Arquivo Selecionado: {}'.format(zipfile_file))

    # Results
    print('Input "zipfile": {}'.format(zipfile_file))


def select_temp_path():
    """
    Function for opening the file explorer window
    """
    global temp_path
    temp_path = filedialog.askdirectory(
        initialdir=os.path.join(os.getcwd(), '..'),
        title='Selecionar Diretório',
        mustexist=True,
    )
    # Configura o Label
    lbl_temp.configure(text='Arquivo Selecionado: {}'.format(temp_path))

    # Results
    print('Input "temp path": {}'.format(temp_path))


def hide_all_frames():
    """
    Function for opening the file explorer window
    """
    app_frame.grid_forget()
    about_frame.grid_forget()

    app_frame.pack_forget()
    about_frame.pack_forget()

    for widget in about_frame.winfo_children():
        widget.destroy()
    for widget in app_frame.winfo_children():
        widget.destroy()


def open_app_frame():
    global lbl_temp
    global lbl_zip
    hide_all_frames()

    # Create Frames
    app_frame.config(background='blue')
    app_frame.pack(side=TOP, fill='both', expand=True)
    # app_frame.grid(row=0, column=0, sticky='nesw')
    app_frame.columnconfigure(0, weight=1, minsize=200)

    # Button/Label: File Explorer
    btn_file = Button(app_frame, text='Selecionar .zip', height=2, command=select_zip_file)
    btn_file.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    # btn_file.pack()

    lbl_zip = Label(app_frame, text='Arquivo Selecionado: None')
    lbl_zip.config(background='green', foreground='blue')
    lbl_zip.config(height=2)
    lbl_zip.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    # lbl_zip.pack(side=LEFT)

    # Button/Label: Select Path
    btn_temp = Button(app_frame, text='Selecionar Pasta', height=2, command=select_temp_path)
    btn_temp.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    # btn_temp.pack()

    lbl_temp = Label(app_frame, text='Pasta Selecionada: None')
    lbl_temp.config(background='white', foreground='black')
    lbl_temp.config(height=2)
    lbl_temp.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    # lbl_temp.pack(side=LEFT)

    # Button
    btn_final = Button(app_frame, text='Converter .zip com pdfs individualizados ', height=2, command=merge_file)
    btn_final.grid(row=2, columnspan=2, padx=10, pady=10, sticky='s')
    # btn_final.pack(side=BOTTOM)


def open_about_frame():
    hide_all_frames()

    # Frame
    about_frame.pack(fill='both', expand=1)
    about_frame.config(background='red')

    # Add Label
    texto = """
    Programa escrito por Michel Metran,
    Biólogo, Assessor do MPSP.        
    """
    lbl_1 = Label(about_frame, text=texto)
    lbl_1.config(background='blue', foreground='black')
    lbl_1.pack()


def merge_file():
    # Variables
    print(os.path.isfile(zipfile_file))
    print(os.path.isdir(temp_path))

    # Set Directories
    output_path, output_apartados_path = set_directories(temp_path)

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


# Main
root = Tk()
root.title('TJSP: Juntar Documentos e-SAJ')
width = 500
height = 300
root.geometry('{}x{}'.format(width, height))

try:
    root.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
    root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
except:
    print(11111)

# Frames
app_frame = Frame(root, width=width, height=height)
about_frame = Frame(root, width=width, height=height)

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)
my_menu.add_command(label='Aplicação', command=open_app_frame)
my_menu.add_command(label='Sobre', command=open_about_frame)

# Grid
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)

# Loop
open_app_frame()
root.mainloop()

if __name__ == '__main__':
    print('Módulo Tkinter')
