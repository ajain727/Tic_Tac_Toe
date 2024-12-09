# Projects
Multiplayer Tic-Tac-Toe Game

This project implements a multiplayer Tic-Tac-Toe game where two players can connect and play using a TCP socket connection. The game allows users to host or join sessions and provides a fun and interactive way to play this classic game.

Features
Multiplayer Functionality

Players can host or join a game session over a network using TCP sockets.
Interactive Gameplay

Players choose their unique characters to represent their moves on the board.
Turns alternate between players until a winner is determined or the game ends in a draw.
Dynamic Game Board

The game board updates after every move and is displayed for both players.
Win Detection and Game End

The game automatically detects win conditions or a draw.
A "GG" message is exchanged at the end of the game.
Error Handling

Invalid moves are handled gracefully and communicated to both players.
How to Use
Host a Game

Run the script and choose the "host" option.
Provide a port number for hosting the game.
Share the IP and port number with another player who will join.
Join a Game

Run the script and choose the "join" option.
Provide the host's IP address and port number.
Gameplay

Players take turns selecting a position (0-8) on the board to place their character.
The game continues until a player wins or the board is full (draw).
Prerequisites
Python 3.x
Basic knowledge of TCP sockets and networking
Installation
Clone the repository:
bash
Copy code
git clone <repository_url>  
Navigate to the project directory:
bash
Copy code
cd <project_directory>  
Run the script:
bash
Copy code
python3 <script_name>.py  
Technologies
Python: Programming language used to build the project
Socket Library: For TCP communication between players
Customization
Feel free to modify the code to:

Change the game board design.
Add new features or enhance the user interface.
Author
Aditya Jain
