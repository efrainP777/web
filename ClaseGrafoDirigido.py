from ListaSimple import Lista
from collections import deque

class Grafo:
    MAXVERTEX = 100   
    def __init__(self):
        self.V = [Lista() for _ in range(self.MAXVERTEX + 1)]    
        self.num_vertices = -1
        self.marca = [False for _ in range(self.MAXVERTEX + 1)]    

    def add_vertice(self):
        if self.num_vertices == self.MAXVERTEX:
            print("Grafo.addVertice: Demasiados vértices (solo se permiten {})".format(self.MAXVERTEX + 1))
            return
        self.num_vertices += 1
        self.V[self.num_vertices] = Lista()

    def cant_vertices(self):
        return self.num_vertices + 1

    def is_vertice_valido(self, v, metodo=None):
        valido = 0 <= v <= self.num_vertices       
        if not valido and metodo is not None:
            print("Grafo.{}: {} no es un vértice del Grafo {}".format(metodo, v, self.get_indicacion()))
        return valido

    def tiene_conexiones_salientes(self, u):
        if not self.is_vertice_valido(u):
            return False
        return self.V[u].length() > 0
    
    def tiene_conexiones_entrantes(self, v):
        if not self.is_vertice_valido(v):
            return False
        for u in range(self.cant_vertices()):
            if self.costo(u, v) > 0:
                return True
        return False
    
    def add_arista(self, u, peso, v):  
        if peso <= 0:
            print("Grafo.addArista: El peso debe ser mayor que cero")
            return
        if not self.is_vertice_valido(u, "addArista") or not self.is_vertice_valido(v, "addArista"):
            return
        self.V[u].add(v, peso)     
    def del_arista(self, u, v):
        if not self.is_vertice_valido(u, "delArista") or not self.is_vertice_valido(v, "delArista"):
            return
        self.V[u].del_data(v)

    def costo(self, u, v):
        if not self.is_vertice_valido(u) or not self.is_vertice_valido(v):
            return 0
        return self.V[u].get_peso(v)

    def desmarcar_todos(self):
        for i in range(self.num_vertices + 1):
            self.marca[i] = False

    def marcar(self, u):
        if self.is_vertice_valido(u):
            self.marca[u] = True

    def desmarcar(self, u):
        if self.is_vertice_valido(u):
            self.marca[u] = False

    def is_marcado(self, u):
        return self.marca[u]

    def costo_peso_minimo(self, peso):    
        i = 0                                                 
        while self.is_marcado(i):
            i += 1
        menor = peso[i]
        posicion = i
        for j in range(i + 1, len(peso)):
            if not self.is_marcado(j) and peso[j] < menor:
                menor = peso[j]
                posicion = j
        return posicion

    def camino_mas_corto_completo(self, a, z):
        peso = [float('inf')] * (self.num_vertices + 1)
        anterior = [-1] * (self.num_vertices + 1)
        peso[a] = 0
        self.desmarcar_todos()

        while not self.is_marcado(z):
            u = self.costo_peso_minimo(peso)
            self.marcar(u)

            for i in range(self.V[u].length()):
                w = self.V[u].get(i)
                if not self.is_marcado(w):
                    s = peso[u] + self.costo(u, w)
                    if peso[w] > s:
                        peso[w] = s
                        anterior[w] = u

        camino = []
        u = z
        while u != -1:
            camino.append(u)
            u = anterior[u]
        camino.reverse()
        return camino
    
