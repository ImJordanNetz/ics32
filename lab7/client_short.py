# echo_client.py
#
# ICS 32 
# Lab 7 Code 
import socket

def read_host() -> str:
    '''
    Asks user for the host name or IP address until a valid one is provided
    Returns the valid host name/IP address 
    '''

    while True:
        IP = socket.gethostbyname(input("Valid Host: "))

        try:
            socket.inet_aton(IP)
            return IP
        except socket.error:
            print("Invalid IP")
            

def read_port() -> int:
    '''
    Asks user for the port number until a valid one is provided
    Returns the valid port number between 1 and 65535
    '''
    
    while True:
        port_num = int(input("Valid Port Num [1, 65535]: "))
        if 1 <= port_num <= 65535:
            return port_num
        print("Invalid Port Num [1, 65535]")

def read_message() -> str:
    '''
    Asks user for a message to send
    returns message
    '''
    return input("Message to send: ")

def print_response(response: str) -> None:
    '''
    Prints reponse
    '''
    print("Response: " + response)

def connect(host: str, port: int) -> 'connection':
    '''
    Create a socket 
    Connect to the host and port provided
    Create input and output streams for this socket
    return a connection consisting of the following:
    1) the socket, 2) the input stream, and 3) the output stream
    '''
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))

        send = client.makefile("w")
        recv = client.makefile("r")

        return client, recv, send


def close(connection: 'connection') -> None:
    '''
    Given a connection, consisting of 
    1) the socket, 2) the input stream, and 3) the output stream
    close all 3 components of the connection
    '''
    sock, recv, send = connection
    recv.close()
    send.close()


def send_message(connection: 'connection', message: str) -> None:
    '''
    Given a connection and a message,
    send message to the output stream of the socket connection
    '''
    sock, recv, send = connection
    send.write(message + "\r\n")
    send.flush()


def receive_response(connection: 'connection') -> str:
    '''
    Receive message from socket input stream
    Return string
    '''
    sock, recv, send = connection
    srv_msg = recv.readline().strip()
    return srv_msg



def run() -> None:
    host = read_host()
    port = read_port()

    print(f'Connecting to {host} (port {port}) ...')
    connection = connect(host, port)
    print('Connected!')

    while True:
        message = read_message()

        if message == '':
            break
        else:
            send_message(connection, message)
            response = receive_response(connection)
            print_response(response)

    print('Closing connection...')
    close(connection)
    print('Closed!')


if __name__ == '__main__':
    run()