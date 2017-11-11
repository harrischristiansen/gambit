'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	Gambit - Multiplayer Game Bot Competitions
	Server: Primary Game Server
'''

import logging
import socket

from player import Player

PORT_GAME_SERVER = 23345

# Show all logging
logging.basicConfig(level=logging.DEBUG)

class GameServer():

	def __init__(self):
		self._players = []
		self._rooms = []

		self.startServer()

	######################### Setup #########################

	def startServer(self):
		logging.debug("Starting game server on port: %d" % (PORT_GAME_SERVER))
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind(('', PORT_GAME_SERVER))
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Make Address Reusable - No Lockout
		self.s.listen(20)

	######################### Player Connections #########################

	def acceptPlayers(self):
		while True:
			player = self.s.accept()
			threading.Thread(target=addPlayer, args=(player)).start()

	def addPlayer(self, player):
		(client, addr) = player
		logging.debug("Client Connected: %s:%s" % (addr[0], addr[1]))
		player = Player(client, addr)
		self._players.append(player)

		player.startReceivingMessages()

######################### Main #########################

# Start Server
if __name__ == '__main__':
	server = GameServer()
	server.acceptPlayers()
