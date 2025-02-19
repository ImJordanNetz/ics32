import socket

def start_server(host_address, host_port):
    with socket.socket() as srv:
        srv.bind((host_address, host_port))
        srv.listen()

        print("ICS32 simple server listening on port", host_port)
        connection, address = srv.accept()

        with connection:
            print("client connected")

            while True:
                rec_msg = connection.recv(4096)

                print("echo", rec_msg)

                if not rec_msg:
                    break
                connection.sendall(rec_msg)

            print("client disconnected")

if __name__ == "__main__":
    start_server("localhost", 8000)