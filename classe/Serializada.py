import ast
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

    def deleteTxt(self,dadosDelet):
        """
        Methodo que deleta o registro no arquivo txt
        """
        return dadosDelet;
    
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
                             result={"id":str(valor["id"]),"senha":valor["senha"],"login":valor["login"]}
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