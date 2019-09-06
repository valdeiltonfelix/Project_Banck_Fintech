import ast
import os
import sys
class Serializada:
    
    def rum(self,rum):
        """
        Methodo que inicia o laço do programa!!
        """
        return rum;
    
    def insertTxt(self,dadosIsert,nomeArquivo,option):
        """
        Methodo que insere os dados no arquivo txt
        """

        if option==1:
            try:
                with open(nomeArquivo, 'a') as f:
                     let=open(nomeArquivo,"r");

                     if sum(1 for linha in let)==0:
                         f.write(dadosIsert);
                         f.close;
                     else:
                         f.write("\n"+dadosIsert);
                         f.close;

                   
            except IOError:
                print (u'ERRO: Arquivo não encontrado!')

        return dadosIsert;

    def updateTxt(self,dadosUpdate):
        """
        Methodo que atualiza o arquivo txt
        """
        return dadosUpdate;

    def deleteTxt(self,nomeArquivo,dadosDelet,where):
        """
        Methodo que deleta o registro no arquivo txt
        """
        print(nomeArquivo);
        
        try:
            result=""
            d=list()
            with open(nomeArquivo, 'r') as f:
                bandas = f.readlines()
                cont=0;
                for linhas in bandas:
                    striparse=linhas.replace('\n',"")
                    dadoscovert=ast.literal_eval(striparse);          
                    if dadoscovert[where]!=dadosDelet:
                        d.append(dadoscovert)
                    else:
                        cont+=1

            with open(nomeArquivo,"w") as arq:
                     arq.write(self.convertList(d).replace("},","}\n"))

        except IOError:
            print("Não foi possivel excuta operação sobre o arquivo")
            
            
    def selectTxt(self,nomeArquivo,optinon,values="",where=""):
        result="";
        """Methodo que faz o select no arquivo txt e retorna os dados
        """
        try:
            with open(nomeArquivo, 'r') as f:
                 if where=="":
                     result=f.readlines();

                 if where !="" and values !="":

                    re=f.readlines();
                    for i in re:
                        valor=ast.literal_eval(i)
                        if valor[where]==values:
                             result={"id":int(str(valor["id"])),"senha":valor["senha"],"login":valor["login"]}
                             break;                
                
                 else:
                     print("Termos de busca não preenchido para essa função")
                 
        except IOError:
                print (u'ERRO: Arquivo não encontrado!')
                        
        return result;

    def convertList(self,lista):
        """
          Metodo para converte uma lista em string
        """
        s = [str(i) for i in lista] 
        res = ",".join(s);
        return res;
        
    def sequence(self,nomeArquivo):
        
         try:
                with open(nomeArquivo, 'r') as f:
                    result = f.readlines().__len__();
                    print(result)
         except IOError:
                print (u'ERRO: Arquivo não encontrado!')

         return result+1;