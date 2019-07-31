class Nodo:
    def __init__(self, Nombre = None, Carne = None, siguiente=None):
        self.Nombre = Nombre
        self.Carne = Carne
        self.siguiente = siguiente
    
    def getElemento(self):
        return "%s %s" %(self.Nombre, self.Carne)

class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def getVacio(self):
        if self.cabeza == None:
            return True

    def setNodoAlInicio(self,elemento):
        if self.getVacio() == True:
            self.cabeza = self.cola = elemento
        else:
            elemento.siguiente = self.cabeza
            self.cabeza = elemento
    
    def setNodoAlFinal(self,elemento):
        if self.getVacio()==True:
            self.cabeza = self.cola = elemento
        else:
            self.cabeza.siguiente = elemento
            self.cola = elemento

    def eliminarPrimero(self):
        if self.getVacio() == True:
            print("Las Lista esta Vacia\n")
        elif self.cabeza == self.cola:
            self.cabeza = None
            self.ultimo = None
            print("Elemento Eliminado\n")
        else:
            temp = self.cabeza
            self.cabeza = self.cabeza.siguiente
            temp = None
            print("Elemento Eliminado\n")

    def eliminarUltimo(self):
        if self.getVacio() == True:
            print("Las Lista esta Vacia\n")
        elif self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
            print("Elemento Eliminado\n")
        else:
            validar = True
            temp = self.cabeza
            while(validar):
                if temp.siguiente == self.cola:
                    temp2 = self.cola
                    self.cola = temp
                    temp2 = None
                    validar = False
                    print("Elemento Eliminado\n")
                else:
                    temp = temp.siguiente

    def getNodoPrimero(self):
        if self.getVacio == True:
            return ("Lista Vacia\n")
        else:
            return self.cabeza
    
    def getNodoUltimo(self):
        if self.getVacio == True:
            return ("Lista Vacia\n")
        else:
            return self.cola

    def PrintLista(self):
        if self.getVacio() == True:
            print("Lista Vacia\n")
        else:
            validar = True
            temp = self.cabeza
            while(validar):
                print(temp.getElemento())
                if temp == self.cola:
                    validar=False
                else:
                    temp = temp.siguiente

    def modificar(self, cerne,elemento):
        if int(self.cabeza.Carne) == int(carne):
            elemento.siguiente = self.cabeza.siguiente
            self.cabeza = elemento
            return True
        else:
            aux = self.cabeza
            anterior = aux
            while aux != None
                if int(aux.Carne) == int(carne):
                    elemento.siguiente = aux.siguiente
                    anterior.siguiente = elemento
                    return True
                    aux = aux.siguiente
        return False
                    

if __name__ == "__main__":
    ls = ListaSimple()

    while(True):
        print("-----Menu----\n"+
                "1. Agregar\n"+
                "2. Eliminar\n"+
                "3. Listar\n"+
                "4. Modificar"
                 )
        num = input("Ingresar la opcion: ")
        if num == "1":
            nombre = input("Ingrese el Nombre: ")
            carne = input("Ingrese el Carné: ")
            nodo = Nodo(nombre,carne)
            ls.setNodoAlInicio(nodo)
        elif num == "2":
            ls.eliminarUltimo()
        elif num == "3":
            ls.PrintLista()
        elif num == "4":
            carnemodificar = input("Ingrese el carne: ")
            nombre = input("Ingrese el Nombre: ")
            carne = input("Ingrese el Carné: ")
            nodo = Nodo(nombre,carne)
            ls.modificar(carnemodificar,nodo)
            
