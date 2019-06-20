## Project 2: Connect Four - Network version ##
## fely magaoay 27278238 & andrel11 16436720 ##

import project2
import connectfour
import socket
from collections import namedtuple 

ConnectfourConnection = namedtuple(
    'ConnectfourConnection',
    ['socket', 'input', 'output'])

class ConnectionError(Exception):
    pass

def main():
    '''Runs server-mode of connect four game'''
    host1 = read_host()
    port1 = read_port()
    connection = connect(host1, port1)
    username = ' ' + _username(connection) 
    hello(connection, username)
    AI_GAME(connection)
    new_game = connectfour.new_game()
    while True:
        project2.print_board(new_game)
        new_game = askinput_server(new_game, connection)

        x = connectfour.winner(new_game)
        if x == connectfour.RED:
            print("The Winner Is RED.")
            break
        elif x == connectfour.YELLOW:
            print("The Winner Is YELLOW.")
            break        
    project2.game_ends(new_game)
    close(connection)
    
#program starts/specify host & port
def connect(host: str, port: int) -> ConnectfourConnection:

    connectfour_socket = socket.socket()
    connectfour_socket.connect((host, port))

    connectfour_input = connectfour_socket.makefile('r')
    connectfour_output = connectfour_socket.makefile('w')

    return ConnectfourConnection(
        socket = connectfour_socket,
        input = connectfour_input,
        output = connectfour_output)

def askinput_server(game_state: connectfour.GameState, connection: ConnectfourConnection):
    while True:
        if game_state.turn == connectfour.RED:
            move = input("Red player DROP or POP: ")
            player = int(input("Red player column 1-7: "))

            player_move = move + ' ' + str(player)
            _write_line(connection, player_move.upper())
                    
            if move == 'DROP':
                return connectfour.drop(game_state, player-1)

            else:
                return connectfour.pop(game_state, player-1)
        else:
            if _read_line(connection) == 'OKAY':
                server_move = _read_line(connection)
                togetridoftheline = _read_line(connection)
                
                move = server_move.split()[0]
                player = int(server_move.split()[1])                       
                if move == 'DROP':
                    return connectfour.drop(game_state, player-1)
                    
                else:
                    return connectfour.pop(game_state, player-1)

            else:
                _expect_line(connection, 'READY')
                return game_state





def _expect_line(connection: ConnectfourConnection, expected: str) -> None:

    line = _read_line(connection)

    if line != expected:
        raise ConnectionError()


#def moves(connection: ConnectfourConnection, player_move: str):
#
#    _write_line(connection, player_move.upper())
#    print(_read_line(connection))

def read_host() -> str:
    '''User is asked to specify host'''
    while True:
        host = input('Host: ').strip()

        if len(host) == 0:
            print('Please specify a host (either a name or an IP address)')
        else:
            return host


def read_port() -> int:
    '''User is asked to specify port number'''
    while True:
        try:
            port = int(input('Port: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port

        except ValueError:
            print('Ports must be an integer between 0 and 65535')

def _username(connection: ConnectfourConnection)-> str:
    '''User is asked to specify a username'''
    username = input('Create an Username: ')
    return username

def hello(connection: ConnectfourConnection, username1: str) -> str:
    '''Client sends the characters I32CFSP_HELLO, a space, and a username'''
    _write_line(connection, 'I32CFSP_HELLO' + username1)
    print(_read_line(connection))

def AI_GAME(connection: ConnectfourConnection)-> str:
    _write_line(connection, 'AI_GAME')
    print(_read_line(connection))
    
def _write_line(connection: ConnectfourConnection, line: str) -> None:
    connection.output.write(line + '\r\n')
    connection.output.flush()

def _read_line(connection: ConnectfourConnection) -> str:
    return connection.input.readline()[:-1]

def close(connection: ConnectfourConnection) -> None:
    'Closes the connection to the server'
    connection.input.close()
    connection.output.close()
    connection.socket.close()


if __name__ == '__main__':
    main()
