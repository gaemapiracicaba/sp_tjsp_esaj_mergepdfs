# TJSP e-SAJ

<br>

O Sistema [e-SAJ](https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090) do TJSP permite o acesso do processo judicial para as partes interessadas. A navegação nos documentos é feita clicando sobre os títulos, por meio de um índice (**_bookmarks_**) e é necessário aguardar o tempo de carregamento do arquivo.

<center><img src="https://i.imgur.com/FMBKHLg.png"></center>

<br>

O Sistema possibilita ainda a exportar o processo de duas formas:

<center><img src="https://i.imgur.com/dboJbpC.png"></center>

<br>

Quando exportamos por **_arquivo único_**, perde-se a navegação pelos **_bookmarks_** (índice/sumário/marcadores) que é possível quando se navega pelo processo usando o sistema do e-SAJ, inviabilizando a leitura dos extensos processos judiciais.

Para contornar esse problema, foi escrito esse _script_ para juntar os documentos apartados --- obtidos por meio da exportação de **_um arquivo para cada documento_** --- gerando um arquivo único, com um painel para os _bookmarks_, facilitando a leitura do processo, conforme abaixo demonstrado:

<center><img src="https://i.imgur.com/9Yz6jdO.png"></center>

<br>

---

### Como Usar?

**Modo 1: usuário padrão**

Para usuários não-programadores, basta usar o arquivo **_esaj_app.exe_** (um executável _portable_), disponível para sistema operacional Windows.
<br>Basta fazer o [**_download_ aqui**](https://github.com/gaemapiracicaba/sp_tjsp_esaj/releases/download/app/esaj_app.exe).

<br>

**Modo 2: usuário avançado**

Clone o repositório! Proponha ajustes com _pull requests_.
<br>Customize, ao seu modo, os **_bookmarks_**, as funções.
<br>O uso padrão é:

```bash
python run.py {caminho para o arquivo .zip obtido no e-SAJ}
python run.py "..\data\1010642-60.2020.8.26.0019.zip"
```

<br>

---

### Como compilar o .exe?

Com auxílio do módulo **_pyinstaller_** foi possível compilar o código em um arquivo executável, livre de dependências.

```bash
conda activate pablocarreira-py38

pyinstaller src/app.py --nowindowed --noconsole --onefile --name=esaj_merge_docs
pyinstaller src/esaj_tkinter.py --nowindowed --noconsole --onefile --name=esaj_app
pyinstaller src/esaj_tkinter.py --onefile --name=esaj_app
```

<br>

---

### _TODO_

1. ~~Empacotar~~

<br>

---

### Referências

- [StackOverflow | Using tkinter filedialog.askdirectory to choose paths and preform a script using those paths](https://stackoverflow.com/questions/62593336/using-tkinter-filedialog-askdirectory-to-choose-paths-and-preform-a-script-using)
- [StackOverflow | How to redirect print statements to Tkinter text widget](https://stackoverflow.com/questions/12351786/how-to-redirect-print-statements-to-tkinter-text-widget)
