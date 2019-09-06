from classe import Serializada
import os

if __name__=="__main__":
    print("dentro do main")

    serial=Serializada.Serializada();
    initProgram=serial.rum(True)

    while initProgram :
          nomeArquivo="arquivobanco/conta.txt"
          interupt=input("Digite 1 para interromper o programa");

         # dados=[{"id":serial.sequence(nomeArquivo),"senha":"@cabral","login":'indigina'}];
          
          if interupt=="1":
                #serial.insertTxt(serial.convertList(dados),nomeArquivo,1)
                print("procura ",serial.selectTxt(nomeArquivo,1,"indigina","login"));
                for wr in serial.selectTxt(nomeArquivo,1,"indigina","login"):
                    print("result",wr)
                serial.deleteTxt(nomeArquivo,"indigina","login")
                initProgram=serial.rum(False);
                #{'id': 1, 'senha': '@cabral', 'login': 'indigina'}
