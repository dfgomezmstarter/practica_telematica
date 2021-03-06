# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:05:32 2020

@author: Daniel Felipe Gomez Martinez, Cesar Andres Garcia Posada
"""

SERVER_ADDRESS = "127.0.0.1"
PORT = 1234
BACKLOG = 5
RECV_BUFFER_SIZE = 1024
ENCODING_FORMAT = "utf-8"
QUIT = "QUIT"
DELETE_B ="DELETE_B"
CREATE_B ="CREATE_B"
LIST_B = "LIST_B"
UPLOAD = "UPLOAD"
DELETE_F ="DELETE_F"
LIST_F = "LIST_F"
DOWNLOAD = "DOWNLOAD"
HELP = "HELP"
HELP_ARRAY = (
 "------------------------\n"
 "COMANDOS VALIDOS\n"
 "HELP: nos proporciona una lista de ayuda\n"
 "QUIT: Se cierra la conexion entre el cliente y el servidor\n"
 "CREATE_B: Crear un bucket\n"
 "---> Sintaxis: CREATE_B <nombre del bucket>\n"
 "LIST_B: Listado de los bukets\n"
 "DELETE_B: Eliminar un bucket\n"
 "---> Sintaxis: DELETE_B <nombre del bucket>\n"
 "UPLOAD: Carga de un archivo a un bucket en especifico\n"
 "---> Sintaxis: \n"
 "---> UPLOAD\n"
 "---> <Ruta del archivo a cargar>\n"
 "---> <Nombre del bucket donde se desea cargar el archivo>\n"
 "---> <Nuevo nombre del archivo>\n"
 "LIST_F: Listado de los archivos de todos los buckets\n"
 "DOWNLOAD: Descarga de un archivo desde el servidor a una ruta que ingresa el cliete\n"
 "---> Sintaxis: \n"
 "---> DOWNLOAD\n"
 "---> <Nombre del bucket origen>\n"
 "---> <Nombre del archivo a descargar>\n"
 "---> <Ruta de destino>\n"
 "DELETE_F: Eliminar un archivo de un bucket\n"
 "---> Sintaxis: \n"
 "---> DELETE_F\n"
 "---> <Nombre del bucket origen>\n"
 "---> <Nombre del archivo a eliminar>\n"
 "------------------------\n")
HELP_ARRAY2 = ("RESPUESTAS\n"
 "Para el comando CREATE_B\n"
 "---> 300 BCS: creación del bucket exitosa\n"
 "---> 301 BCF: creación del bucket fallo en algun momento\n"
 "Para el comando LIST_B\n"
 "---> 400 LS: lista de los buckets se ha generado exitosamente\n"
 "Para el comando DELETE_B\n"
 "---> 600 DBS: eliminación del bucket exitosa\n"
 "---> 601 DBF: eliminación del bucket fallo en algún momento\n"
 "Para el comando UPLOAD\n"
 "---> 700 FUBS: carga de un archivo en un bucket se genero de forma exitosa\n"
 "---> 701 FUBF: carga de un archivo en un bucket fallo en algún momento\n"
 "Para el comando LIST_F\n"
 "---> 800 LFS: lista de los archivos de cada bucket se generó de manera exitosa\n"
 "Para el comando DOWNLOAD\n"
 "---> 900 FDBS: descarga de un archivo desde el servidor hasta una ruta exitosa\n"
 "---> 901 FDBF: descarga de un archivo desde el servidor hasta una ruta tuvo un fallo \n"
 "Para el comando DELETE_F\n"
 "---> 1000 DFS: eliminación de un archivo exitosa\n"
 "---> 1001 DFF: eliminación de un archivo tuvo problemas \n"
 "Error de comando\n"
 "---> 401 BCMD: Comando no identidicado\n")
