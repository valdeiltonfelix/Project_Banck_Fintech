from classe import Serializada
if __name__=="__main__":
    print("dentro do main")
    
    serial=Serializada.Serializada();
    initProgram=serial.rum(True)
    while initProgram :
         interupt=input("Digite 1 para interromper o programa");
         if interupt=="1":
             initProgram=serial.rum(False);

