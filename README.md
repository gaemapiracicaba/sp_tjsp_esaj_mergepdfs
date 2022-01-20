# TJSP e-SAJ

<br>

O Sistema [e-SAJ](https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090) do TJSP permite o acesso do processo judicial para as partes interessadas. A navegação nos documentos é feita clicando sobre os títulos, por meio de um índice (***bookmarks***) e é necessário aguardar o tempo de carregamento do arquivo.

![](https://i.imgur.com/FMBKHLg.png)

<br>

O Sistema possibilita ainda a exportar o processo de duas formas:
![](https://i.imgur.com/dboJbpC.png)

<br>

Quando exportamos por ***arquivo único***, perde-se a navegação pelos ***bookmarks*** (índice/sumário/marcadores) que é possível quando se navega pelo processo usando o sistema do e-SAJ, inviabilizando a leitura dos extensos processos judiciais.

Para contornar esse problema, foi escrito esse *script* para juntar os documentos apartados --- obtidos por meio da exportação de  ***um arquivo para cada documento*** --- gerando um arquivo único, com um painel para os *bookmarks*, facilitando a leitura do processo, conforme abaixo demonstrado:

![](https://i.imgur.com/9Yz6jdO.png)

<br>

-----

### Como Usar?

**Modo 1:**

Para usuários não-programadores, basta instalar o arquivo ***processo_esaj_tjsp.exe***.
<br>Disponível para sistema operacional Windows.

<br>

**Modo 2:**

Clone o repositório e seja feliz!
<br>Customize, ao seu modo, os ***bookmarks***.

<br>

-----

### Como compilar o .exe?



```bash
pyinstaller src/app.py --nowindowed --noconsole --onefile --name=esaj_merge_docs
pyinstaller src/tkinter_esaj.py --nowindowed --noconsole --onefile --name=esaj_merge_docs
```

<br>

-----

### *TODO*

1. Empacotar!
