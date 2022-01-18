# TJSP e-SAJ

<br>

O Sistema e-SAJ do TJSP permite o acesso do processo judicial para as partes interessadas. A navegação nos documentos é feita clicando sobre os títulos, por meio de um índice (***bookmarks***) e é necessário aguardar o tempo de carregamento do arquivo.

![](https://i.imgur.com/FMBKHLg.png)

<br>

O Sistema possibilita ainda a exportar o processo de duas formas:
![](https://i.imgur.com/dboJbpC.png)

<br>

Quando exportamos por ***arquivo único***, perde-se a navegação pelos *bookmarks* (índice/sumário) que é possível quando se navega pelo processo usando o sistema do e-SAJ, inviabilizando a leitura dos extensos processos judiciais.

Para contornar esse problema, foi escrito esse *script* para juntar os documentos apartados --- obtidos por meio da exportação de  ***um arquivo para cada documento*** --- gerando um arquivo único, com um painel para os *bookmarks*, facilitando a leitura do processo, conforme abaixo demonstrado:

![](https://i.imgur.com/9Yz6jdO.png)

<br>

-----

### Como Usar?

*Modo 1:*

Para usuários não-programadores, basta instalar o arquivo *processo_esaj_tjsp.exe*.

Assumo que você é um usuário de sistema Windows.

*Modo 2:*

Clone o repositório e seja feliz.

Customize, ao seu modo, os *bookmarks*.

<br>

-----

### *TODO*

1. Inserir função para passar como *input* a pasta zipada.
2. Empacotar https://pyinstaller.readthedocs.io/en/stable/operating-mode.html. https://www.youtube.com/watch?v=I8fGmQh6Ui0
