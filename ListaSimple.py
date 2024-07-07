from Nodo import Nodo

class Lista:
    def __init__(self):
        self.L = None
        self.n = 0

    def add(self, data, peso):  
        Ant = None  
        p = self.L  

        while p is not None and data >= p.get_data():   
            Ant = p
            p = p.get_link()  

        if Ant is None:  
            nuevo = Nodo(data, peso)
            nuevo.set_link(self.L)
            self.L = nuevo
            self.n += 1
        elif Ant.get_data() != data: 
            nuevo = Nodo(data, peso)
            Ant.set_link(nuevo)
            nuevo.set_link(p)
            self.n += 1

    def del_data(self, data):  
        Ant = None
        p = self.L

        while p is not None and data > p.get_data():
            Ant = p
            p = p.get_link()

        if p is not None and p.get_data() == data:  
            if Ant is None:
                self.L = self.L.get_link()  
            else:
                Ant.set_link(p.get_link())

            p.set_link(None)
            self.n -= 1

    def existe(self, data):  
        return self.exist(data) is not None

    def get(self, k):  
        p = self.L
        i = 0
        while p is not None:
            if i == k:
                return p.get_data()

            p = p.get_link()
            i += 1

        print("Lista.get: Fuera de rango")
        return -1

    def get_peso(self, data):  
        p = self.exist(data)
        if p is not None:
            return p.get_peso()

        return 0

    def length(self):
        return self.n

    def str(self):
        S = "["
        coma = ""

        p = self.L
        while p is not None:
            S += f"{coma}{p.get_data()}/{self.double_to_str(p.get_peso())}"
            coma = ", "
            p = p.get_link()

        return S + "]"

    def double_to_str(self, d):  
        s = str(d)
        pos_punto = s.find('.')
        for i in range(pos_punto + 1, len(s)): 
            if s[i] != '0':
                return s

        return s[:pos_punto]

    def exist(self, data): 
        p = self.L

        while p is not None and data > p.get_data():
            p = p.get_link()

        if p is not None and p.get_data() == data:
            return p

        return None  