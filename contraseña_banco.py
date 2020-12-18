#colocar como '#' todos los caracteres 
# de un string excepto los últimos 4
def maskfit(texto):
    texto = texto.replace(' ', '')
    print(texto, texto[0], len(texto) - 4)
    print(texto[-4::])
    

    for i in range(len(texto) - 4):
        # reemplazo la letra por "#" y 
        # como hay caracteres que se repiten pongo 1 de que se reemplaze una vez
        texto = texto.replace(texto[i], "#", 1)
        
        print(texto)
                        
if __name__ == "__main__":
    maskfit(input("coloque un texto su contraseña por favor "))

#otras formas
#  def maskify(cc):
  
#   word = list(cc)
#   #loop through the list except the last 4 index's this will also prevent
#   #the loop from running for anything less than 5 index's long
#   for i in range(len(word) - 4):
#     word[i] = '#'
#   # join and return the list
#   return ''.join(word)
#   pass


#--------------
# def maskify(cc):
#     l = len(cc)
#     if l <= 4: return cc
#     return (l - 4) * '#' + cc[-4:]