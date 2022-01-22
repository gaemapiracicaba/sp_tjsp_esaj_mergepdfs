#!/usr/bin/env python
# coding: utf-8

import os.path
import webbrowser
from tkinter import *
from tkinter import filedialog, messagebox
from size_monitor import *
from run import *


def select_zip_file():
    """
    Function for opening the file explorer window
    """
    zipfile_file = filedialog.askopenfilename(
        initialdir=os.path.join(os.getcwd(), '..'),
        title='Selecionar arquivo zipado (.zip)',
        filetypes=(('Zip files', '*.zip'), ('All files', '*.*'))
    )
    # Configura o Entry
    ety_zip.delete(0, END)
    ety_zip.insert(0, '{}'.format(zipfile_file))

    # Processing
    txt_process.delete(1.0, END)
    txt_process.see('end')
    print('Arquivo Selecionado: {}\n'.format(ety_zip.get()))


def merge_file():
    # Variables
    main(ety_zip.get())

    # Message Box
    yes_no = messagebox.askyesno(
        title='Convertido!',
        message="""Processamento concluído com sucesso!.\n\nSeu arquivo está na mesma pasta do arquivo .zip.\n\nDeseja Fechar? """
    )
    if yes_no:
        root.destroy()
        root.quit()


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
        font=('Helvetica', 14, 'bold'),
        foreground='#fff',
        background='#333',
        height=2,
    )
    lbl_1.grid(row=0, padx=(10, 10), pady=(10, 10), sticky=NSEW)
    lbl_1.grid_rowconfigure(0, weight=1)

    lbl_2 = Label(
        about_frame,
        text='Para mais informações consultar o repositório abaixo',
        font=('Helvetica', 10),
        foreground='#fff',
        background='#333',
        cursor='hand2'
    )
    lbl_2.grid(row=1, padx=(10, 10), pady=(10, 10), sticky=NSEW)
    lbl_2.grid_rowconfigure(0, weight=1)

    lbl_3 = Label(
        about_frame,
        text='https://github.com/gaemapiracicaba/sp_tjsp_esaj',
        font=('Helvetica', 12),
        foreground='blue',
        background='#333',
        cursor='hand2'
    )
    lbl_3.grid(row=2, padx=(10, 10), pady=(10, 10), sticky=NSEW)
    lbl_3.grid_rowconfigure(0, weight=1)
    lbl_3.bind('<Button-1>', call_back)


def open_app_frame():
    global ety_zip
    global txt_process
    hide_all_frames()

    # Create Frames
    app_frame.config(background='#333')
    app_frame.grid(row=0, column=0, sticky=NSEW)
    app_frame.columnconfigure(0, weight=1)

    # Button/Label: File Explorer
    lbl_zip_title = Label(
        app_frame,
        text='Selecionar arquivo .zip',
        font=('Helvetica', 14, 'bold'),
        background='#333',
        foreground='white',
        height=2,
    )
    lbl_zip_title.grid(row=0, padx=(5, 5), pady=(5, 2), sticky=W)
    lbl_zip_title.grid_rowconfigure(0, weight=1)

    # Button Select File
    btn_file = Button(
        app_frame,
        text='{:^10}'.format('Browser'),
        font=('Helvetica', 10),
        command=select_zip_file
    )
    btn_file.grid(row=1, padx=(5, 5), sticky=W)
    btn_file.grid_rowconfigure(0, weight=1)

    # Entry File Selected
    ety_zip = Entry(
        app_frame,
        font=('Helvetica', 10),
        background='white',
        foreground='black',
    )
    ety_zip.grid(row=2, padx=(5, 5), sticky=EW)
    ety_zip.grid_rowconfigure(0, weight=1)

    # Title Convert
    lbl_convert_title = Label(
        app_frame,
        text='Converter .zip obtido no e-SAJ em .pdf',
        font=('Helvetica', 14, 'bold'),
        background='#333',
        foreground='white',
        height=2,
    )
    lbl_convert_title.grid(row=3, padx=(5, 5), pady=(35, 2), sticky=W)
    lbl_convert_title.grid_rowconfigure(0, weight=1)

    # Button to Convert
    btn_final = Button(
        app_frame,
        text='{:^10}'.format('Converter'),
        font=('Helvetica', 10),
        command=merge_file
    )
    btn_final.grid(row=4, padx=(5, 5), sticky=W)
    btn_final.grid_rowconfigure(0, weight=1)

    # Processing
    txt_process = Text(
        app_frame,
        font=('Helvetica', 10),
        background='white',
        foreground='black',
        height=9,
        wrap='word'
    )
    txt_process.grid(row=7, padx=(5, 5), sticky=EW)
    txt_process.grid_rowconfigure(0, weight=1)
    txt_process.tag_configure('stderr', foreground='#b22222')

    sys.stdout = RedirectText(txt_process, 'stdout')
    sys.stderr = RedirectText(txt_process, 'stderr')


def call_back(event):
    """
    Function to tKinter open links
    """
    webbrowser.open_new(event.widget.cget('text'))


class RedirectText(object):
    def __init__(self, widget, tag='stdout'):
        """Constructor"""
        self.widget = widget
        self.tag = tag

    def write(self, string):
        """Add text to the end and scroll to the end"""
        self.widget.insert('end', string, (self.tag))
        self.widget.see('end')
        self.widget.update_idletasks()


# Main
root = Tk()
root.title('Gerar Processo com Bookmarks (TJSP | e-SAJ)')
# photo = PhotoImage(file=os.path.join('..', 'imgs', 'icon.png'))
# root.iconphoto(False, photo)
root_width = 600
root_height = 370

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

# Inicial App
open_app_frame()
root.mainloop()
