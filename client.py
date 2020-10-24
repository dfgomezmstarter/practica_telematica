# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:05:32 2020

@author: Daniel Felipe Gómez Martinez, Cesar Andres Garcia Posada
"""

import socket
import constants
import ast
import json 
import os
import sys
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bucket_route = ""

def download(command_and_data_to_send, destination, file_name):
    new_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_client_socket.connect(("127.0.0.1", constants.PORT))
    new_client_socket.send(bytes(command_and_data_to_send, constants.ENCODING_FORMAT))
    data_received = new_client_socket.recv(constants.RECV_BUFFER_SIZE)
    file_size = data_received.decode(constants.ENCODING_FORMAT)

    try:
        f = open(destination+'\\'+file_name,'wb')
        if file_size is not "0":
            print("Receiving file...")
            l = new_client_socket.recv(1024)
            total = len(l)
            while(len(l)>0):
                f.write(l)
                if (str(total) != file_size):
                    l = new_client_socket.recv(1024)
                    total = total + len(l)
                else:
                    break
        f.close()
    except BaseException as e:
        print("ERROR: " + str(e))
    print("File received")
    data_received = new_client_socket.recv(constants.RECV_BUFFER_SIZE)
    print(data_received.decode(constants.ENCODING_FORMAT))
    new_client_socket.close()
    sys.exit()

def main():
    print("*************************************")
    print("Client is running...")
    client_socket.connect(("127.0.0.1", constants.PORT))
    local_tuple = client_socket.getsockname()
    print("Connected to the server from:", local_tuple)
    print('Enter \"quit\" to exit')
    print('Input commands: ')
    command_to_send = input()

    while  command_to_send != constants.QUIT:
        if command_to_send == '':
            print("Please input a valid command...")
            command_to_send = input()
        elif (command_to_send == constants.HELP):
            command_and_data_to_send = command_to_send
            client_socket.send(bytes(command_and_data_to_send, constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            print(data_received.decode(constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            print(data_received.decode(constants.ENCODING_FORMAT))
            command_to_send = input()
        elif(command_to_send== constants.CREATE_B):
            data_to_send = input("name of the bucket: ")
            command_and_data_to_send = command_to_send + ' ' + data_to_send 
            client_socket.send(bytes(command_and_data_to_send, constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            print(data_received.decode(constants.ENCODING_FORMAT))
            command_to_send = input()
        elif(command_to_send== constants.LIST_B):
            command_and_data_to_send = command_to_send
            client_socket.send(bytes(command_and_data_to_send, constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            lista = ast.literal_eval(data_received.decode(constants.ENCODING_FORMAT))
            print(lista[:-1])
            print(lista[-1])
            command_to_send = input()
        elif(command_to_send== constants.DELETE_B):
            data_to_send = input("name of the bucket that you would like to delete: ")
            command_and_data_to_send = command_to_send + ' ' + data_to_send 
            client_socket.send(bytes(command_and_data_to_send, constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            print(data_received.decode(constants.ENCODING_FORMAT))
            command_to_send = input()
        elif(command_to_send==constants.UPLOAD):
            try:
                origin_directory = input("Path of the directory of the file: ")
                bucket = input("Name of the destination bucket: ")
                name = input("File name (with extension): ")
                size = str(os.path.getsize(origin_directory))
                command_and_data_to_send = command_to_send + ' ' + bucket + ' ' + name + ' ' + size
                client_socket.send(bytes(command_and_data_to_send, constants.ENCODING_FORMAT))
                origin_directory = origin_directory.replace("\\", '/')
                file = open(origin_directory, 'rb')
                line = file.read(constants.RECV_BUFFER_SIZE)
                while (line):
                    client_socket.send(line)
                    line = file.read(constants.RECV_BUFFER_SIZE)
                file.close()
                data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
                print(data_received.decode(constants.ENCODING_FORMAT))
                command_to_send = input()
            except BaseException as e:
                print("ERROR: " + str(e))
                command_to_send = input()
        elif(command_to_send==constants.LIST_F):
            command_and_data_to_send = command_to_send
            client_socket.send(bytes(command_and_data_to_send, constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            data_received = str(data_received.decode(constants.ENCODING_FORMAT)).replace("'", '"').replace("\\\\", '/')
            lista = json.loads(str(data_received))
            for key in lista:
                if (key != "response"):
                    print(key)
                    print("----> "+str(lista[key]))
            print(lista["response"])
            command_to_send = input()
        elif (command_to_send == constants.DOWNLOAD):
            origin_bucket = input("Name of the origin bucket: ")
            name = input("Name of the file: ")
            destination = input("Path of the destination: ")
            command_and_data_to_send = command_to_send + ' ' + origin_bucket + ' ' + name
            client_socket.send(bytes(command_and_data_to_send, constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            size = data_received.decode(constants.ENCODING_FORMAT)

            try:
                file = open(destination + '\\' + name, 'wb')
                if size is not "0":
                    line = client_socket.recv(constants.RECV_BUFFER_SIZE)
                    total_recv = len(line)
                    while (len(line) > 0):
                        file.write(line)
                        if (str(total_recv) != size):
                            line = client_socket.recv(constants.RECV_BUFFER_SIZE)
                            total_recv = total_recv + len(line)
                        else:
                            break
                file.close()
            except BaseException as e:
                print("ERROR: " + str(e))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            print(data_received.decode(constants.ENCODING_FORMAT))
            command_to_send = input()
        elif (command_to_send == constants.DELETE_F):
            bucket = input("name of the bucket where you would like to delete a file: ")
            file_name = input("name of the file: ")
            command_and_data_to_send = command_to_send + ' ' + bucket + ' ' + file_name
            client_socket.send(bytes(command_and_data_to_send, constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            print(data_received.decode(constants.ENCODING_FORMAT))
            command_to_send = input()
        else:
            client_socket.send(bytes(command_to_send, constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            print(data_received.decode(constants.ENCODING_FORMAT))
            command_to_send = input()
    
    client_socket.send(bytes(command_to_send, constants.ENCODING_FORMAT))
    data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
    print(data_received.decode(constants.ENCODING_FORMAT))
    client_socket.close()

if __name__ == '__main__':
    main()