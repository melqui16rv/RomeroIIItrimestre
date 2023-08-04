class pais:
    def __init__(self,pais,edadMe,pobla,altura,):
        self.__pais=pais
        self.__pobla=pobla
        self.__altura=altura
        self.__edadMe=edadMe
        
    def info(self):
        return f"{self.__pais} {self.__edadMe} {self.__pobla} {self.__altura}"
    
    def getpais(self):
        return self.__pais
    
    
    def getpobla(self):
        return self.__pobla

    def getaltura(self):
        return self.__altura
    
    def getedadMe(self):
        return self.__edadMe