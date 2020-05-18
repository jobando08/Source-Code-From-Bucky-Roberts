#!/usr/bin/python
# coding: utf-8
print("main actions that you can do with a list")

l = [23, 15, 12, 56, 78];
k = [89, 65, 77];


#1 insert an element at the end of the list

l.append(99);

#2 contar las veces que aparece uu elemento en la lista

print("This method counts the times that twelve appears in the list");
print(l.count(12));

# agregar un objeto iterable al final de una lista

print("se agrego la lista k a la l");
l.extend(k);
print(l);

# insertar un elemento en el indice dado

print("se inserto hola a la lista l en la posicion 2");
l.insert(2, "hola");
print(l);

# eliminar elemento en el indice indicado

print("se elimino la posicion 2 de la lista l");
l.pop(2);
print(l);

# ordenar una lista

print("se ondeno la lista l");
l.sort();
print(l);


# ordenarla de forma inversa
print("se ordeno la lista de forma descendente");
l.reverse();
print(l);


raw_input()
