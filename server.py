# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:11:41 2020
@author: Daniel Felipe Gomez Martinez, Cesar Andres Garcia Posada
"""

# Import libraries for networking communication
import _thread
import socket
import constants
import os
import sys
import shutil
import time

# import thread module
import threading

print_lock = threading.Lock()
bucket_route = ""

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def threaded(client_connection, client_address, route):
    while True:
        data_received = client_connection.recv(constants.RECV_BUFFER_SIZE)
        remote_string = str(data_received.decode(constants.ENCODING_FORMAT))
        remote_command = remote_string.split()
        command = remote_command[0]
        print(f'Data received from: {client_address[0]}:{client_address[1]}')
        print(command)
        if (command == constants.QUIT):
            response = '200 BYE\n'
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
            print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected.')
            break
        elif (command == constants.HELP):
            response = constants.HELP_ARRAY
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
            response = constants.HELP_ARRAY2
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        elif (command == constants.CREATE_B):
            try:
                name = remote_command[1]
                name = "\\" + name
                os.mkdir(route + name)
                response = '300 BCS\n'
            except:
                print("Fatal error bucket doesnt have name")
                response = '301 BCF\n'
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        elif (command == constants.LIST_B):
            lista = os.listdir(route)
            lista.append("400 LS")
            response = str(lista)
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        elif (command == constants.DELETE_B):
            try:
                name = remote_command[1]
                name = "\\" + name
                shutil.rmtree(route + name)
                response = '600 DBS\n'
                client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
            except:
                print("Fatal error delete a bucket")
                response = '601 DBF\n'
                client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        elif (command == constants.UPLOAD):
            destination = remote_command[1]
            destination = "\\" + destination
            name = remote_command[2]
            size = remote_command[3]
            try:
                file = open(route + destination + '\\' + name, 'wb')
                if size != "0":
                    line = client_connection.recv(1024)
                    total_recv = len(line)
                    while (len(line) > 0):
                        file.write(line)
                        if (str(total_recv) != size):
                            line = client_connection.recv(1024)
                            total_recv = total_recv + len(line)
                        else:
                            break
                file.close()
                print("File received successfully.")
                response = '700 FUBS\n'
                client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
            except BaseException as e:
                print("ERROR: " + str(e))
                response = '701 FUBF\n'
                client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        elif (command == constants.LIST_F):
            dic = {}
            for dirName, subdirList, fileList in os.walk(route):
                array = []
                for fname in fileList:
                    array.append(fname)
                dic[dirName] = array
            dic['response'] = '800 LFS\n'
            response = str(dic)
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        elif (command == constants.DOWNLOAD):
            origin_bucket = remote_command[1]
            name = remote_command[2]
            origin_file_path = route + '\\' + origin_bucket + '\\' + name
            origin_file_path = origin_file_path.replace("\\", '/')
            try:
                size = str(os.path.getsize(origin_file_path))
                client_connection.send(bytes(size, constants.ENCODING_FORMAT))
                time.sleep(1)
                file = open(origin_file_path, 'rb')
                line = file.read(constants.RECV_BUFFER_SIZE)
                while (line):
                    client_connection.send(line)
                    line = file.read(constants.RECV_BUFFER_SIZE)
                file.close()
                response = '900 FDBS\n'
            except BaseException as e:
                print("ERROR: " + str(e))
                response = '901 FDBF\n'
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        elif (command == constants.DELETE_F):
            try:
                bucket = remote_command[1]
                file_name = remote_command[2]
                name = "\\" + bucket + "\\" + file_name
                os.remove(route + name)
                response = '1000 DFS\n'
                client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
            except:
                print("Fatal error delete a file")
                response = '1001 DFF\n'
                client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        else:
            response = '401 BCMD\n\rCommand-Description: Bad command\n\r'
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
    try:
        print_lock.release()
    except BaseException:
        pass
    client_connection.close()


# Main function
def main():
    try:
        bucket_route = sys.argv[1]
    except:
        print("Invalid route")
        sys.exit(1)
    print('*' * 50)
    print('Server is running...')
    print('IP addr: ', constants.SERVER_ADDRESS)
    print('Port: ', constants.PORT)
    tuple_connection = (constants.SERVER_ADDRESS, constants.PORT)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(tuple_connection)
    server_socket.listen(constants.BACKLOG)
    print('Socket is listening...', server_socket.getsockname())

    # Loop for waiting new conection
    while True:
        client_connection, client_address = server_socket.accept()

        print(f'New incoming connection is accepted. Remote IP address: {client_address[0]}')
        # Start a new thread and return its identifier
        _thread.start_new_thread(threaded, (client_connection, client_address, bucket_route))
    server_socket.close()


if __name__ == '__main__':
    main()
