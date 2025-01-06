import socket

def make_move(board, space, player):
    board[space] = player
    return board

def check_win(board):
    equiv = lambda x, y, z: x == y == z

    for i in range(3):
        if equiv(*board[3*i:3*(i+1)]) or equiv(board[0+i], board[3+i], board[6+i]):
            return True

    if equiv(board[0], board[4], board[8]) or equiv(board[2], board[4], board[6]):
        return True

    return False

def print_board(board):
    for i in range(3):
        print(" {0} | {1} | {2} ".format(*board[3*i: 3*(i+1)]))
        if i != 2:
            print("---|---|---")

    return

def valid_move(board, move):
    # given
    spaces = set(range(9))
    if move not in set(map(str, spaces)):
        # if its not a number 0-8
        return False

    space = int(move)
    if space not in spaces:
        # invalid chosen space because number out of range
        return False

    if board[space] not in spaces:
        # invalid choice because player already used this space
        return False

    return True

# -------------------------------------- #
# --------- MODIFY BELOW HERE ---------- #
# Aditya Jain
# aj727
# 31585944


import socket

def main():
    print("Welcome to tic tac toe game")
    action = input("Would you like to host or join a session? (host/join): ").strip().lower()
    player_name = input("Please provide your name: ").strip()
    
    if action == "host":
        host_port = int(input("Specify the port number to host the session: "))
        game_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        game_socket.bind(('', host_port))
        game_socket.listen(1)
        print(f"Awaiting connection from another player on port {host_port}...")
        connection, address = game_socket.accept()
        print(f"Player connected from {address}")
        connection.sendall(player_name.encode())
        rival_name = connection.recv(1024).decode()
        print(f"Connected with: {rival_name}")
        player_role = 1
    elif action == "join":
        host_ip = input("Provide the IP address to connect: ").strip()
        host_port = int(input("Provide the port number to connect: "))
        client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_connection.connect((host_ip, host_port))
        except ConnectionRefusedError:
            print("Unable to connect to the host. Exiting.")
            return
        client_connection.sendall(player_name.encode())
        rival_name = client_connection.recv(1024).decode()
        print(f"Connected to the host: {rival_name}")
        connection = client_connection
        player_role = 2
    else:
        print("Invalid option. Exiting.")
        return

    avatars = [None, None]
    try:
        if player_role == 1:
            avatars[0] = input("Choose your character (Player 1): ")[0]
            connection.sendall(avatars[0].encode())
            avatars[1] = connection.recv(1024).decode()
        else:
            avatars[0] = connection.recv(1024).decode()
            avatars[1] = input("Choose your character (Player 2): ")[0]
            connection.sendall(avatars[1].encode())

        print(f"Your character: {avatars[player_role - 1]}, {rival_name}\'s character: {avatars[(player_role % 2)]}")
        
        board_state = list(range(9))
        current_turn = 0

        while True:
            print_board(board_state)
            if current_turn % 2 == player_role - 1:
                move = input(f"Your move, {player_name}: Select a position (0-8): ")
                while not valid_move(board_state, move):
                    move = input("Invalid choice. Please try again (0-8): ")
                connection.sendall(move.encode())
                board_state = make_move(board_state, int(move), avatars[player_role - 1])
            else:
                print(f"Waiting for {rival_name}'s move...")
                try:
                    move = connection.recv(1024).decode()
                    if not move:  
                        print(f"{rival_name} has left the game. Exiting...")
                        break
                    if not valid_move(board_state, move):
                        print(f"Rival attempted an invalid move: {move}")
                        continue
                    board_state = make_move(board_state, int(move), avatars[(player_role % 2)])  
                except ConnectionResetError:
                    print(f"Connection lost. {rival_name} has exited the game.")
                    break

            if check_win(board_state):
                print_board(board_state)
                if current_turn % 2 == player_role - 1:
                    print("Congratulations, you win!")
                else:
                    print("Game over, you lose!")
                connection.sendall("GG".encode())
                print(connection.recv(1024).decode())
                break
            elif all(isinstance(x, str) for x in board_state):
                print_board(board_state)
                print("The game ends in a draw!")
                connection.sendall("GG".encode())
                print(connection.recv(1024).decode())
                break

            current_turn += 1

    except (ConnectionResetError, BrokenPipeError):
        print(f"{rival_name} has disconnected. Exiting the game.")
    finally:
        connection.close()

if __name__ == "__main__":
    main()


