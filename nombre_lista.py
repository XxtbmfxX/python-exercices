import unittest

def namelist(lista):
    print(type(lista))
    a = "".join(lista)
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace("{" , "")
    a = a.replace("}" , "")
    a = dict(a)
    
    print(a)
    # for nombre in lista:
    #     print(nombre)
    return(lista)
    
    

def test_name_list(self):
    resultado = namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])
    self.assertEqual(resultado, 'Bart, Lisa, Maggie, Homer & Marge')


if __name__ == "__main__":
    namelist(input("nombres por favor "))
    unittest.main()


    # dict in list nidos y viseversa