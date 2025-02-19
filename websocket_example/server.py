import socket
import sys
import si32p
from si32p import SI32PConnection, SI32PProtocolError

def check_hello(si32p_conn: SI32PConnection, cmd: bytes) -> bool:
    '''
    Check if the client was polite enough to say at least a hello
    '''
    if cmd[:len(si32p.SI32P_CLI_HELLO)] == si32p.SI32P_CLI_HELLO:
        return True
    else:
        return False

def is_command_recognized(msg: bytes) -> bool:
    '''
    A server doesn't need to implement all commands of a protocol, only
    the required ones at least. (in the simple si32p case we have full support)
    '''
    res = False
    # All the commands from the SI32P protocol supported by this server
    all_cmd = [si32p.SI32P_CLI_HELLO, si32p.SI32P_CLI_INVERT,
               si32p.SI32P_CLI_BYE, si32p. SI32P_CLI_LOWERCASE]
    # Checks if the received command is one of the supported commands
    for rec_cmd in all_cmd:
        if rec_cmd == msg[:len(rec_cmd)]:
            res = True
    return res

def process_command(msg: bytes, cmd: bytes) -> bytes:
    '''
    Process commands and retrieves data payloads
    '''
    print(msg[:len(cmd)])
    if msg[:len(cmd)] == cmd:
        # Received command matches expected command, so get data
        # if there is any data arriving with the command
        msg_data = msg[len(cmd)+1:]
        print(msg_data)
        if len(cmd) != len(msg):
            try:
                # Our SI32P implementation does not support spaces
                if b' ' not in msg_data:
                    return msg_data
                else:
                    raise SI32PProtocolError
            except Exception:
                raise SI32PProtocolError
        else:
            # If the message and command have the same size return the message
            return msg


def message_exchange(si32p_conn: SI32PConnection) -> None:
    while True:
        rec_msg = si32p.listen(si32p_conn)
        print("message: ", rec_msg)
        try:
            if is_command_recognized(rec_msg):
                # If command is INVERT
                if rec_msg.startswith(si32p.SI32P_CLI_INVERT):
                    msg_data = process_command(rec_msg, si32p.SI32P_CLI_INVERT)
                    print (msg_data)
                    if msg_data:
                        si32p.send(si32p_conn, msg_data[::-1])
                        si32p.complete(si32p_conn)
                    else:
                        si32p.send(si32p_conn, b"error")
                        si32p.complete(si32p_conn)

                # If command is LOWERCASE
                elif rec_msg.startswith(si32p.SI32P_CLI_LOWERCASE):
                    msg_data = process_command(rec_msg, si32p.SI32P_CLI_LOWERCASE)
                    if msg_data:
                        si32p.send(si32p_conn, msg_data.lower())
                        si32p.complete(si32p_conn)
                    else:
                        si32p.send(si32p_conn, b"error")
                        si32p.complete(si32p_conn)

                # If command is BYE
                elif rec_msg.startswith(si32p.SI32P_CLI_BYE):
                    si32p.send(si32p_conn, si32p.SI32P_SRV_BYE)
                    si32p.disconnect(si32p_conn)
                    break
             
            else:
                # If command was not recognized
                si32p.send(si32p_conn, si32p.SI32P_UNREC)
        except SI32PProtocolError:
            print("Error: Client sent payload out of SI32P specification.")
            si32p.disconnect(si32p_conn)
            break
        except Exception as e:
            print(e)
            break

def start_server(host_address: str, host_port: int) -> None:
    '''
    Creates a simple socket server that understands the SI32P protocol
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.bind((host_address, host_port))
        srv.listen()

        print("ICS32 Simple Invert ICS32 Protocol Server " +
              f"listening on IP: {host_address} and port {host_port}")

        while True:
            try:
                connection, address = srv.accept()
                with connection:
                    print(f"client connected from {address[0]}")
                    si32p_conn = si32p.init(connection)

                    # First message should be a HELLO
                    rec_msg = si32p.listen(si32p_conn)
                    if check_hello(si32p_conn, rec_msg):
                        print(f"The client from {address[0]} seems " +
                              "to be polite. Allowing connection.")

                        # If client was polite, server sends back to the client
                        # a standard server hello command
                        si32p.send(si32p_conn, si32p.SI32P_SRV_HELLO)

                        # And now we can continue to other possible message
                        # exchanges with the client
                        message_exchange(si32p_conn)
                    else:
                        # If client was impolite, refuse connection.
                        print("Impolite client. Refusing connection.")
                        si32p.disconnect(si32p_conn)

                    print(f"client from {address[0]} disconnected")
            except KeyboardInterrupt:
                print("Stopping server\n")
                break

if __name__ == "__main__":
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    start_server(IPAddr, int(sys.argv[1]))