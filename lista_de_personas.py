class Persona:
    def __init__(self,nombre,apellido,edad,entretenimiento):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.entretenimiento=entretenimiento
    def __str__(self):
        return f"{self.nombre }  {self.apellido }  ,Edad:{self.edad}  ,Entretenimientro:   {self.entretenimiento }"
def ingresar_persoas():
    personas=[]
    while True:
        print("\nIngrese los datos de la persona:")    
        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        edad=int(input("Edad: "))
        entretenimiento=input("Entretenimiento: ")


        persona=Persona(nombre,apellido,edad,entretenimiento)
        personas.append(persona)

        continuar=input("Desea ingresar otra persona ? (s/n): ").lower()
        if continuar !='s':
            break
    return personas

def mostrar_personas(personas):
    print("\nLista de personas: ")
    for persona in personas:
        print(persona)

def ordenar_personas(personas):
    print("\nOpciones de Ordenamiento: ")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Edad")

    opcion=input("Elija una opcion (1-3): ") 
    if opcion=='1':
        personas.sort(key=lambda p: p.nombre.lower())
    elif opcion=='2':
        personas.sort(key=lambda p: p.apellido.lower())
    elif opcion=='3':
        personas.sort(key=lambda p: p.edad)
    else:
        print("opcion invalida :( ")

# se devuelve 
personas=ingresar_persoas()
ordenar_personas(personas)
mostrar_personas(personas)
