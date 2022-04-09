class Ncomplejo:
    #atributos
    preal = 0
    pima = 0

    def __init__(self,real,imaginario):

        self.preal = real
        self.pima = imaginario

    #para imprimir def es para funciones en este caso para metodos
    def imprimir(self):
        if self.pima < 0: #si imaginario es menor a 0
            print(self.preal, self.pima, "i")

        else:
            print(self.preal, "+", self.pima, "i")
    #setter reales
    def cambio_real(self, real):

        self.preal = real
    #getter reales
    def regresareal(self):

        return self.preal


    #un setter para los imaginarios
    def cambio_imaginarios(self, imaginarios: object) -> object:

        self.pima=imaginarios


    #getter para los imaginarios
    def regresa_imaginarios(self):

        return self.pima

    def operaciones(self):
        suma=self.pima + self.preal
        print("esta es una suma: ",suma)
        resta=self.pima - self.preal
        print("esta es una resta", resta)
        multiplicacion=self.pima*self.preal
        print("esta es una multiplicacion",multiplicacion)
        divicion = self.pima / self.preal
        print("esta es una divicion", divicion)


numero=Ncomplejo(5,2)
numero.imprimir()
numero.operaciones()

numero=Ncomplejo(7,3)
numero.imprimir()
numero.operaciones()

