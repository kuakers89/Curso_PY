#Strings
my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string)) #len me permite ver el tamaño de la cadena
print(len(my_other_string)) 
print(my_string + " " + my_other_string) #Concatenacion de cadenas

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_line_string = "\tEste es un String con tabulación"
print(my_tab_line_string)

my_scape_line_string = "\\tEste es un String \n escapado"
print(my_scape_line_string)

name, surname,age="Eddy", "Sanchez",37
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age)) #Concatenacion de cadenas con format
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age)) #Concatenacion de cadenas con %s
print(F"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetados de caracteres
Lenguaje="python"
a,b,c,d,e,f=Lenguaje
print(a)
print(b)

#División
language_slice=Lenguaje[1:3] #El primer numero es el inicio y el segundo es el final
print(language_slice)
language_slice=Lenguaje[1:2:4] #El primer numero es el inicio y el segundo es el final
print(language_slice)

language_slice=Lenguaje[1:] #El primer numero es el inicio y el segundo es el final
print(language_slice)
language_slice=Lenguaje[:-1] #El primer numero es el inicio y el segundo es el final
print(language_slice)

#rEVERSE
reverse_lenguage=Lenguaje[::-1] #El primer numero es el inicio y el segundo es el final
print(reverse_lenguage)

#Funciones
print(Lenguaje.capitalize()) #Primera letra en mayuscula
print(Lenguaje.upper()) #Todas las letras en mayuscula
print(Lenguaje.lower()) #Todas las letras en minuscula
print(Lenguaje.isnumeric()) #Verifica si es un numero
print(Lenguaje.isalpha()) #Verifica si es una letra
print(Lenguaje.startswith("p")) #Verifica si comienza con un caracter específico
print(Lenguaje.endswith("n")) #Verifica si termina con un caracter específico
