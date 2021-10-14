"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog={"artist":None,
                "artworks":None,
                "medio":None}
    catalog["artist"]=lt.newList()
    catalog["artworks"]=lt.newList()
    catalog["medio"]=mp.newMap(1153,
                                maptype="PROBING",
                                loadfactor=0.60,
                                comparefunction=compareMapMedio)

    catalog["nationality"] = mp.newMap(1153,
                                maptype="PROBING",
                                loadfactor=0.60,
                                comparefunction=compareMapNacionality)

                                                                                                

# Funciones para agregar informacion al catalogo
def addArtWorks(catalog,artworks):
    lt.addLast(catalog["artworks"], artworks)

    mp.put(catalog["medio"],artworks["Medium"], artworks )
    medios = artworks["Medium"].split(",")
    for medio in medios:
        addMedioAuthor(catalog, medio.strip(), artworks)

def addArtist(catalog,artist):
    lt.addLast(catalog["artist"], artist)


def addMedioAuthor(catalog, id, artworks):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    medios = catalog['medio']
    existmedio = mp.contains(medios, id)
    if existmedio:
        entry = mp.get(medios, id)
        medio = me.getValue(entry)
    else:
        medio = newArtist(id)
        mp.put(medios, id, medio)
    lt.addLast(medio['books'], artworks)
    

# Funciones para creacion de datos
def newArtist(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    artist = {'ConstituentID': "",
              "DisplayName": None,
              "ArtistBio": 0,
              "Nationality": 0,
              "Gender": 0,
              "BeginDate": 0,
              "EndDate": 0,
              "Wiki QID": 0,
              "ULAN": 0  
              }
    artist['DisplayName'] = name
    artist['ConsituentID'] = lt.newList('SINGLE_LINKED', compareMapMedio)
    return artist
# Funciones de consulta
def obrasMasAntiguasPorMedio(obras):

    tecnicas = lt.newList("ARRAY_LIST")
    apoyo = {}
    maximo = ""
    for artwork in lt.iterator(obras):
        if lt.isPresent(tecnicas, artwork["Medium"]) == 0:
            lt.addLast(tecnicas, artwork["Medium"])
            apoyo[artwork["Medium"]] = 1
        else:
            veces = apoyo[artwork["Medium"]]
            apoyo[artwork["Medium"]] = veces + 1
        if apoyo[artwork["Medium"]] > apoyo.get(maximo, -1):
            maximo = artwork["Medium"]
    return maximo, lt.size(tecnicas)

def numeroTotalObras(catalog, nacionality):

    respuesta = 0
    for artWork in lt.iterator(artWorks["artworks"]):
        if artWork["Nationality"] == nacionality:
            respuesta+=1

    return respuesta



    
# Funciones utilizadas para comparar elementos dentro de una lista
def compareMapMedio(medio1,medio2):
    if (medio1==medio2):
        return 0
    elif (medio1>medio2):
        return 1
    else: 
        return 0
def compareMapNacionality(nac1,nac2):
    if (nac1==nac2):
        return 0
    elif (nac1>nac2):
        return 1
    else: 
        return 0

# Funciones de ordenamiento

def compareYears(artist2, artist1):
    if int(artist2['BeginDate']) < int(artist1['BeginDate']):
        return artist2

def compareDate(date1, date2):
    if date2['DateAcquired'] < date1['DateAcquired']:
        return date1
    
def comparePalabras(palabra1, palabra2):
    if palabra2 < palabra1:
        return palabra1