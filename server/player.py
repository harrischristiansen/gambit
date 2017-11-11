'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	Gambit - Multiplayer Game Bot Competitions
	Player: Connected Player Client
'''

import logging

class Player():

	def __init__(self, client, addr):
		self.client = client
		self.addr = addr
		self.player_key = ""

	######################### Message Handing #########################

	def startReceivingMessages(self):
		while True:
			try:
				msg = p.recv(1024)
				if not msg: # Client Closed Connection
					p.close()
					return

				self.player_key = msg.strip("\r\n ")
			except: # Timed Out
				p.close()
				return
