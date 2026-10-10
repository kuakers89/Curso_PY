v_nombre = "Mi variable es"
v_bool = False
v_int_to_str =5

print(v_nombre,": ",v_bool) #Concatenacion de variables
print(type(print(str(v_int_to_str),"soy un numero"))) # Tipo NoneType
print("mi tamaño es:",len(v_nombre)) #el codigo len me permite ver tamaño

#variable de una sola linea
name, surname, alias, age ="Eddy", "Sanchez","kuakers",37.0
print("Me llamo:",name, "mi edad es:",age)

#Inputs
""""
name= input("Cual es tu nombre?")
age = input("how old are you?")

print(name,"Tiene",age,"años")
"""

#cambiamos ell tipo
name= 35        
age = "Eddy"
print(name)
print(age)

address: str="Mi direccion es: Calle 123"
address= 123+1

print (type(address)   )