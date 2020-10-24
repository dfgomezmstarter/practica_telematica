# Sockets

 ## Descripción

 Este proyecto se desarrolló por medio de la Librería Sockets de Python con el fin de crear una comunicación cliente servidor.
 Tomando en cuenta que la API de sockets nos permite enviar mensajes a través de una red lógica definida por las direcciones IP tanto del
 cliente como del servidor (entiéndase mensajes como archivos de texto, archivos ejecutables, etc).
 En el momento de crear el socket, se define que el socket va a trabajar con un -socket.SOCK_STREAM- lo que significa que el socket será de tipo TCP

## Vocabulario de Mensajes
 **help:** Nos proporciona información con relación a los diferentes comandos que podemos ingresar y las posibles repuestas que nos retorna el servidor
 Sintaxis:
 ```HELP```
 
**quit:** Se cierra la conexión cliente - servidor que se ha establecido
 Sintaxis:
 ```QUIT```
 
**CREATE_B:** Nos permite crear un bucket con un nombre en específico, esto en la ruta en la que el servidor es ejecutado
 Sintaxis:
 ```CREATE_B <nombre del bucket>```
 
**LIST_B:** Nos permite ver la lista de los buckets que hay creados, esto en la ruta en la que el servidor es ejecutado
 Sintaxis:
 ```LIST_B```
 
**DELETE_B:** Nos permite eliminar un bucket con un nombre en específico, esto en la ruta en la que el servidor es ejecutado
 Sintaxis:
 ```DELETE_B <nombre del bucket>```

**UPLOAD:** Nos permite cargar un archivo a un bucket.
 Proceso - Sintaxis:
 - ```UPLOAD```
 - ```<Ruta del fichero a cargar en el bucket>``` (Esta ruta contiene el nombre del archivo a cargar)
 - ```<nombre del bucket>``` Bucket donde se desea cargar el archivo
 - ```<nombre del fichero>``` Nuevo nombre del archivo

**LIST_F:** Nos permite ver los diferentes archivos que hay en cada uno de los buckets que hay creados en la ruta donde se corre el servidor
 Sintaxis:
 ```LIST_F```

**DOWNLOAD:** Nos permite descargar un archivo desde el cliente hasta el servidor, es decir, desde uno de los buckets hasta una ruta que ingresa el cliente
 Proceso - Sintaxis:
 *```DOWNLOAD```
 *```<nombre del bucket>``` Bucket donde se desea cargar el archivo
 *```<nombre del fichero>``` Nuevo nombre del archivo
 *```<Ruta del fichero donde se va a descargar>```
 
**DELETE_F:** Nos permite borrar un archivo desde uno de los buckets del servidor
 Proceso - Sintaxis:
 ```DELETE_F```
 ```<nombre del bucket origen>``` Nombre del bucket donde se encuentra almacenado el archivo
 ```<nombre del archivo>``` Nombre del archivo que se desea eliminar del bucket ingresado anteriormente

## Regla de Procedimientos

 **Para el comando CREATE_B**
 **300 BCS:** significa que la creación del bucket fue exitosa
 **301 BCF:** significa que la creación del bucket falló en algún momento

 **Para el comando LIST_B**
 **400 LS:** significa que la lista de los buckets se ha generado exitosamente
 
 **Para el comando DELETE_B**
 **600 DBS:** significa que la eliminación del bucket fue exitosa
 **601 DBF:** significa que la eliminación del bucket falló en algún momento

 **Para el comando UPLOAD**
 **700 FUBS:** significa que la carga de un archivo a un determinado bucket se generó de forma exitosa
 **701 FUBF:** significa que la carga de un archivo a un determinado bucket falló en algún momento

 **Para el comando LIST_F**
 **800 LFS:** significa que la lista de los archivos de cada uno de los buckets se generó de manera exitosa

 **Para el comando DOWNLOAD**
 **900 FDBS:** significa que la descarga de un archivo desde el servidor hasta una ruta ingresada por el cliente ocurrió de forma exitosa
 **901 FDBS:** significa que la descarga de un archivo desde el servidor hasta una ruta ingresada por el cliente tuvo un falló en algún momento

 **Para el comando DELETE_F**
 **1000 DFS:** significa que la eliminación de un archivo en un bucket determinado ocurrió de forma exitosa
 **1001 DFF:** significa que la eliminación de un archivo en un bucket determinado tuvo problemas al realizar la petición
