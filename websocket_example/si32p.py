import socket
from collections import namedtuple

# Specify variables holding protocol commands following
# SI32P specifications
SI32P_CLI_HELLO = b"HELLO_FROM_CLIENT"
SI32P_CLI_INVERT = b"INVERT"
SI32P_CLI_BYE = b"BYE"
SI32P_CLI_LOWERCASE = b"LOWERCASE"
SI32P_SRV_HELLO = b"HELLO_FROM_SERVER"
SI32P_SRV_COMPLETE = b"COMPLETE"
SI32P_SRV_BYE = b"BYE"
SI32P_UNREC = b"UNRECOGNIZED"

class SI32PProtocolError(Exception):
    '''
    An exception to be used when received commands do not follow
    protocol specifications
    '''
    pass

"""
A namedtuple conveniently encapsulates the objects we need to use to
communicate over a socket connection in many of the functions in this
module. Rather than pass multiple objects, it is cleaner to wrap them
in a single namedtuple.
"""
SI32PConnection = namedtuple('SI32PConnection', ['socket', 'send', 'recv'])

def init(sock: socket) -> SI32PConnection:
    '''
    The init method should be called for every program that uses the
    SI32P Protocol. The calling program should establish a connection
    with a socket object, then pass that open socket to init.
    init will then create file objects to handle input and output and
    return in a SI32PConnection namedtuple.
    '''
    try:
        f_send = sock.makefile('wb')
        f_recv = sock.makefile('rb')
    except Exception:
        raise SI32PProtocolError("Invalid socket connection")
    return SI32PConnection(
            socket=sock,
            send=f_send,
            recv=f_recv
            )

def disconnect(si32p_conn: SI32PConnection) -> None:
    '''
    provide a way to close read and write file objects
    '''
    si32p_conn.send.close()
    si32p_conn.recv.close()

def listen(si32p_conn: SI32PConnection) -> bytes:
    '''
    listen will block until a new message has been received
    '''
    return _read_command(si32p_conn)

def send(si32p_conn: SI32PConnection, cmd: bytes) -> None:
    '''
    send a command via a connection. A wrapper for _write_command()
    '''
    _write_command(si32p_conn, cmd)

def complete(si32p_conn: SI32PConnection) -> None:
    '''
    A wrapper for a completion message to be sent via the connection.
    '''
    _write_command(si32p_conn, SI32P_SRV_COMPLETE)

def _write_command(si32p_conn: SI32PConnection, cmd: bytes) -> None:
    '''
    performs the required steps to send a message,
    including appending a newline sequence and flushing the socket to ensure
    the message is sent immediately.
    '''
    try:
        si32p_conn.send.write(cmd + b'\r\n')
        si32p_conn.send.flush()
    except Exception:
        raise SI32ProtocolError

def _read_command(si32p_conn: SI32PConnection) -> bytes:
    '''
    performs the required steps to receive a message. Trims the
    newline sequence before returning
    '''
    cmd = si32p_conn.recv.readline()[:-2]
    return cmd