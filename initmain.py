from classe import Serializada
import os

if __name__=="__main__":
    print("dentro do main")

    serial=Serializada.Serializada();
    initProgram=serial.rum(True)

    while initProgram :
          nomeArquivo="arquivobanco/conta.txt"
          interupt=input("Digite 1 para interromper o programa");

          dados=[{"id":serial.sequence(nomeArquivo),"senha":"@cabral","login":'indigina'}];
          
          if interupt=="1":
                serial.insertTxt(serial.convertList(dados),nomeArquivo,1)
                print(serial.selectTxt(nomeArquivo,1,"@90BOBSENHA","senha"));
                for wr in serial.selectTxt(nomeArquivo,1,"122","senha"):
                   # print("result",wr)
                initProgram=serial.rum(False);

