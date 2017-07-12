#Primer Examen padron


class Consultar:

  def _init_(self,fecha, municipio, lugares, tip):
    self.Fecha = fecha
    self.Municipio = municipio
    self.Lugares = lugares
    self.tip=1

  def getFecha(self):
      return self.Fecha
  def getMunicipio(self):
      return self.Municipio
  def getLugares(self):
      return self.Lugares
  def getTipo(self):
      return self.tip

class padron:

    def _init_(self):
        self.pila= Stack()
        self.Ine=Ine
        self.NombreAp=NombreAp
        self.Codigo=Codigo
        self.Estado=Estado
        self.Municip=Municip
        self.Calle=Calle

    def getIne(self):
         return self.Ine
    def getNombreAp(self):
         return self.NombreAp
    def getCodigo(self):
         return self.Codigo
    def getEstado(self):
         return self.Estado
    def getMuncip(self):
         return self.Municip
    def getCalle(self):
         return self.Calle

    def buscar(self,votante):
            contador=0
            temp=self.pila
            while not temp.isEmpty():
                Consultar= temp.pop()
                print Consultar.getIne()
                if Consul.getIne()== votante:
                    contador = contador +  1
            return contador

    def mostrar(self):
        temp= self.pila
        while not temp.isEmpty():
            Consul= temp.pop()
            print Consul.getIne()
            print Consu.getNombreAp()
            print Consul.getCodigo()

    def buscar(self,numMun):
            contador=0
            temp=self.pila
            while not temp.isEmpty():
                Consultar= temp.pop()
                print Consultar.getIne()
                if Consul.getIne()== numMun:
                    contador = contador +  1
            return contador

    def mostrar(self):
        temp= self.pila
        while not temp.isEmpty():
            Consul= temp.pop()
            print Consul.getIne()
            print Consu.getNombreAp()
            print Consul.getCodigo()

    class Provincia:
    
        def _init_(self):
            self.pila= Stack()

        def buscar(self,provincia):
                contador=0
                temp=self.pila
                while not temp.isEmpty():
                    Consultar= temp.pop()
                    print Consultar.getIne()
                    if Consul.getIne()== provincia:
                        contador = contador +  1
                return contador

        def mostrar(self):
            temp= self.pila
            while not temp.isEmpty():
                Consul= temp.pop()
                print Consul.getEstado()
                print Consul.getMuncip()
                print Consul.getCalle()

    class LugarVota:
        def _init_(self):
            self.pila= Stack()
            self.Codig=Codig
            self.Local=Local

        def getCodig(self):
          return self.Codig
        def getDirec(self):
          return self.Direc
        def getLocal(self):
          return self.Local

        def buscar(self,lugarVota):
                contador=0
                temp=self.pila
                while not temp.isEmpty():
                    Consultar= temp.pop()
                    print Consultar.getIne()
                    if Consul.getIne()== lugarVota:
                        contador = contador +  1
                return contador

        def mostrar(self):
            temp= self.pila
            while not temp.isEmpty():
                Consul= temp.pop()
                print Consul.getCodig()
                print Consul.getDirec()
                print Consul.getLocal()

