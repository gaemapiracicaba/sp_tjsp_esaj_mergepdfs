#!/usr/bin/env python
# coding: utf-8

import os.path
import webbrowser
from tkinter import *
from tkinter import filedialog, messagebox
from merge_process_esaj import *
from size_monitor import *


def callback(event):
    webbrowser.open_new(event.widget.cget('text'))


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
    lbl_zip.configure(text='{:<80}'.format(os.path.basename(zipfile_file)))
    # text='{}'.format(os.path.basename(zipfile_file)))

    # Results
    print('Input "zipfile": {}'.format(zipfile_file))


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
    app_frame.config(background='#333')
    app_frame.grid(row=0, column=0, sticky=NSEW)
    # app_frame.rowconfigure(0, weight=1)
    app_frame.columnconfigure(0, weight=1)

    # Button/Label: File Explorer
    lbl_zip_title = Label(
        app_frame,
        text='Selecionar Arquivo .zip',
        font=('Medium 500', 14, 'bold'),
        background='#333',
        foreground='white',
        height=2,
    )
    lbl_zip_title.grid(
        row=0,
        columnspan=2,
        padx=(5, 5),
        pady=(5, 2),
        sticky=W,
    )
    lbl_zip_title.grid_rowconfigure(0, weight=1)

    btn_file = Button(
        app_frame,
        text='{:^10}'.format('Browser'),
        font=('Light 300', 10),
        command=select_zip_file
    )
    btn_file.grid(
        row=1,
        column=0,
        padx=(5, 5),
        sticky=EW,
    )
    btn_file.grid_rowconfigure(0, weight=1)

    lbl_zip = Label(
        app_frame,
        text='{:<80}'.format('Arquivo Selecionado...'),
        font=('Light 300', 10),
        background='white',
        foreground='black',
        height=2
    )
    lbl_zip.grid(
        row=1,
        column=1,
        padx=(5, 5),
        sticky=E,
    )
    lbl_zip.grid_rowconfigure(0, weight=1)

    lbl_convert_title = Label(
        app_frame,
        text='Converter .zip com pdfs individualizados em PDF único',
        font=('Medium 500', 14, 'bold'),
        background='#333',
        foreground='white',
        height=2,
    )
    lbl_convert_title.grid(
        row=5,
        columnspan=2,
        padx=(5, 5),
        pady=(35, 2),
        sticky=W,
    )
    lbl_convert_title.grid_rowconfigure(0, weight=1)

    btn_final = Button(
        app_frame,
        text='{:^10}'.format('Converter'),
        font=('Light 300', 10),
        command=merge_file
    )
    btn_final.grid(
        row=6,
        column=0,
        padx=(5, 5),
        sticky='nwe',
    )
    btn_final.grid_rowconfigure(0, weight=1)
    lbl_process = Label(
        app_frame,
        text='{:<80}'.format('Processamento...'),
        font=('Light 300', 10),
        height=8,
        background='white',
        foreground='black'
    )
    lbl_process.grid(
        row=6,
        column=1,
        padx=(5, 5),
        sticky=W,
    )
    lbl_process.grid_rowconfigure(0, weight=1)


def open_about_frame():
    # Frame
    hide_all_frames()
    about_frame.config(background='#333')
    about_frame.grid(row=0, column=0, sticky=NSEW)
    # about_frame.rowconfigure(0, weight=1)
    about_frame.columnconfigure(0, weight=1)

    # Add Label
    texto = """
    Programa escrito por Michel Metran,
    Biólogo, Assessor do MPSP.
    """
    lbl_1 = Label(
        about_frame,
        text=texto,
        font=('Medium 500', 14, 'bold'),
        foreground='#fff',
        background='#333',
        height=2,
    )
    lbl_1.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky=NSEW)
    lbl_1.grid_rowconfigure(0, weight=1)

    lbl_2 = Label(
        about_frame,
        text='Para mais informações consultar o repositório abaixo',
        font=('Light 300', 10),
        foreground='#fff',
        background='#333',
        cursor='hand2'
    )
    lbl_2.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky=NSEW)
    lbl_2.grid_rowconfigure(0, weight=1)

    lbl_3 = Label(
        about_frame,
        text='https://github.com/gaemapiracicaba/sp_tjsp_esaj',
        font=('Light 300', 10),
        foreground='blue',
        background='#333',
        cursor='hand2'
    )
    lbl_3.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky=NSEW)
    lbl_3.grid_rowconfigure(0, weight=1)
    lbl_3.bind('<Button-1>', callback)


def merge_file():
    # Set Directories
    input_path, output_path, output_apartados_path = set_directories(zipfile_file)

    # Unzip
    unzip_zipfile(zipfile_file, output_apartados_path)

    # Renomeia os arquivos
    rename_files(output_apartados_path)

    # Sort Files
    # list_files = sort_files_as_list(output_apartados_path)

    # Output Filename
    output_filename = create_output_filename(zipfile_file)

    # Merge Files
    merge_files(output_apartados_path, input_path, output_filename)

    # Clean Directories
    shutil.rmtree(output_path, ignore_errors=True)

    print("{:<100}".format('> Fim.'))

    yes_no = messagebox.askyesno(
        title='Convertido!',
        message="""Processamento concluído com sucesso!.\n\nSeu arquivo está na mesma pasta do arquivo .zip.\n\nDeseja Fechar? """
    )
    if yes_no:
        root.destroy()
        root.quit()


# Main
root = Tk()
root.title('Gerar Processo com Bookmarks (TJSP | e-SAJ)')
root_width = 700
root_height = 350

# Screen
screen_height, screen_width = get_size_primary_monitor()
x = int((screen_width / 2) - (root_width / 2))
y = int((screen_height / 2) - (root_height / 2))
root.geometry(f'{root_width}x{root_height}+{x}+{y}')

# Frames
app_frame = Frame(root, width=root_width, height=root_height)
about_frame = Frame(root, width=root_width, height=root_height)

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)
my_menu.add_command(label='Aplicação', command=open_app_frame)
my_menu.add_command(label='Sobre', command=open_about_frame)

# Grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Loop
open_app_frame()
root.mainloop()

if __name__ == '__main__':
    print('Módulo tkinter Fechado')
