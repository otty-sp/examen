
#Examen, de llamadas
class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)

class LlamadasRealizadas:
    def init (self,fecha,hora,numTel,duracion,valor):
        self.Fecha = fecha
        self.Hora = hora
        self.NumTelf = noTelf
        self.Duracion = duracion
        self.Valor = valor

    def getFecha (self):
        return self.Fecha
    def getHora (self):
        return self.Hora
    def getNumeroTelf (self):
        return self.NumTelf
    def getDuracion (self):
        return self.Duracion
    def getValor (self):
        return self.Valor

class Llamadasfacturadas:
    def init (Tel1,Total1,Total2):
        self.TelenoDestino = Tel1
        self.TotalFacturado = Total1
        self.TotalDeLlamadas = Total2

    def getTelefono (self):
        return self.Tel1
    def getFacturado (self):
        return self.Total1
    def getTotalLlamadas (self):
        return self.Total2

class FacturaLlamadasPorFec:
    def init (self):
        self.pila = Stack()

    def buscar (self,fecha):
        contador = 0
        temp = self.pila
        while not temp.isEmpty:
            LlamadasRealizadas = temp.pop()
            print LlamadasRealizadas.getFecha()
            if LlamadasRealizadas.getFecha()== fecha:
                contador = contador + 1
        return contador

    def buscar (self,DestinoTel):
        contador = 0
        temp = self.pila
        while not temp.isEmpty:
            Llamadasfacturadas = temp.pop()
            print Llamadasfacturadas.getTelefono()
            if Llamadasfacturadas.getTelefono()== DestinoTel:
                contador = contador + 1
        return contador
