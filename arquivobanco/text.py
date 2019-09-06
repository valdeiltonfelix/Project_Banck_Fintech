"""
with open("arquivobanco/conta.txt") as f:
     line=f.readlines();
     for li in line:
         palavra=li.split(" ")
         print(palavra)
         for pal in palavra:
             if pal=="login:":
                 li="";
                 break;
"""

with open("arquivobanco/conta.txt") as f:
     newText=f.read().replace("'indigina'", "Orange")
     print(newText);
