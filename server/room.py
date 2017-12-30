'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	Gambit - Multiplayer Game Bot Competitions
	Room: Game Room for facilitating multi-player games
'''

import logging

class GameRoom():

	def __init__(self, roomID):
		self.roomID = roomID
		self.players = []
	
	def addPlayer(self, player):
		self.players.append(player)

	def removePlayer(self, player):
		if player in self.players:
			self.players.remove(player)