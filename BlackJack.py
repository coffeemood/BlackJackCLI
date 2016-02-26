# -*- coding: UTF-8 -*-
import random
import sys
import os

rank = {'A':1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':10,'Q':10,'K':10}
class Deck(object): 

	def __init__(self):
		self.suits = ['Spade','Club','Diamond','Heart']
		self.val = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
		self.deck = []
		for i in self.suits: 
			for x in self.val: 
				self.deck.append([x,i])
		random.shuffle(self.deck)

	def printDeck(self):
		return self.deck

	def __len__(self):
		return len(self.deck)

	def dealCard(self):
		i = self.deck.pop()
		return i 

	def shuffle(self):
		random.shuffle(self.deck)

class Hand(object): 
	global rank
	def __init__(self): 
		self.cards = []
		self.count = 0
		self.ace = False

	def grabCount(self):
		return self.count 

	def __str__(self): 
		sym = {'Spade':'♠', 'Diamond':'♦', 'Heart':'♥', 'Club':'♣'}
		hand = ""
		for i in self.cards:
			name,symbol = i 
			hand += " " + str(name) + sym[symbol]
		return hand

	def __len__(self): 
		return len(self.cards)


	def addCard(self,card):
		self.cards.append(card)
		card_rank = rank[card[0]]
		if card_rank == 1:
			self.ace = True
		self.count += card_rank
		if (self.ace == True and self.count > 21):
			self.count -= 10
			self.ace = False
		if (self.ace == True and self.count < 12):
			self.count += 10

	def BJ(self):
		if (self.count == 21) & (len(self.cards) == 2): 
			print 'Black Jack!'
			return 2
		elif (self.count == 21) & (len(self.cards) > 2):
			print '21!'
			return 0
		elif self.count > 21: 
			print 'Busted!'
			return 1
		elif (self.count < 21) & (len(self.cards) == 5): 
			print 'Five card charlie!'
			return 5

class Player(object):

	def __init__(self, name, money=0):
		self.name = name
		self.money = money

	def showBalance(self):
		return self.money

	def topup(self,money): 
		self.money += money


def NewGame(name): 

	def makePlayer(): 
		while True:
			stake = raw_input('Chips > ')
			try: 
				stakee = float(stake)
				
			except ValueError: 
				print 'Please enter a correct amount!'
			if stakee > 0: 
				return stakee
			else:
				print 'Please enter a positive amount'
				pass

	def staking(playuh):
		while True:
			bet = raw_input('Staking > ')
			try: 
				bett = float(bet)
			except ValueError: 
				print 'Please enter a correct amount!'
			if bett < 0 or bett > playuh.showBalance():
				print 'You can only stake what you have!'
			else:
				return bett
			

	def stay(dcards,pcards):
		print 'Dealer has: {a}'.format(a=str(dcards))
		exit1 = dcards.BJ()
		val1 = dcards.count
		val2 = pcards.count
		while val1 < 17: 
			print 'Dealer Hit...'
			dcards.addCard(d.dealCard())
			val1 = dcards.count
			val2 = pcards.count
			print 'Dealer has: {a}'.format(a=str(dcards))
			exit1 = dcards.BJ()
			if exit1 == 1 or exit1 == 5 or exit1 == 0: 
				break

		if exit1 == 1: 
			return 1
		elif (exit1 != 1) and (val1 > val2): 
			return 0 
		elif (exit1 != 1) and (val1 < val2): 
			return 1
		elif (exit1 != 1) and (val1 == val2):
			return 3

	def Hit(player,cards):
		if player != 'Dealer':
			print 'Hittin...'
		else: 
			print '\nDealer hit...'
		hitC = d.dealCard()
		cards.addCard(hitC)
		print str(cards)
		print '{a}\'s New score: {b}'.format(a=player,b=cards.count)
		exit = cards.BJ()
		return exit

	def PlayerPlays(dcards,player,cards,stake):
		dd = True
		while True: 
			choices = {1:'Hit',2:'Stay',3:'Double Down'}
			print
			for i in choices: print i,choices[i]
			choice = raw_input('Choice > ')
			try: 
				choicez = int(choice)
			except ValueError: 
				print 'Please select a correct choice!'
				pass
			if choicez == 1:
				dd = False
				exit = Hit(player,cards)
				if exit == 1: 
					print '\nYou lost!'
					p.topup(-stake)
					return 
				elif (exit == 0) or (exit == 5):
					print '\nYou won!'
					p.topup(stake)
					return
			elif choicez == 2:
				exit = stay(dcards,cards)
				if exit == 0: 
					print '\nYou lost!'
					p.topup(-stake)
					return
				elif exit == 1:
					print '\nYou won!'
					p.topup(stake)
					return
				elif exit == 3: 
					print '\nTie!'
					return
			elif choicez == 3: 
				if dd == True:
					stake *= 2
					if stake > p.showBalance():
						print 'You don\'t have enough money left!'
						stake = stake/2
						pass
					else:
						exit = Hit(player,cards)
						if exit == 1: 
							print '\nYou lost!'
							p.topup(-stake)
							return 
						elif (exit == 0) or (exit == 5):
							print '\nYou won!'
							p.topup(stake)
							return
						else:
							exit = stay(dcards,cards)
							if exit == 0: 
								print '\nYou lost!'
								p.topup(-stake)
								return
							elif exit == 1:
								print '\nYou won!'
								p.topup(stake)
								return
							elif exit == 3: 
								print '\nTie!'
								return
				elif dd == False: 
					print 'You cannot double down at this point.'
					pass
			else: 
				print 'Wrong choice!'

	def bet(d,p):
		os.system('clear')

		dhand = Hand()
		phand = Hand()

		dhand.addCard(d.dealCard())
		dhand.addCard(d.dealCard())
		phand.addCard(d.dealCard())
		phand.addCard(d.dealCard())

		print 'Dealer: ', str(dhand)[:5]
		print 'Player: ', str(phand), ' ', 'Score: {a}'.format(a=phand.count)

		exit = phand.BJ()
		if exit == 2: 
			p.topup((bett*1.5))
		else:
			PlayerPlays(dhand,p.name,phand,bett)
		print
		print p.showBalance()

	d = Deck()
	d.shuffle()
	stakez = makePlayer()
	p = Player(name,stakez)
	bett = staking(p)
	bet(d,p)
	
	while True:
		if len(d) < 7: 
			d = Deck()
		print 'What now?'
		choices = {1:'Again',2:'Quit'}
		print
		for i in choices: print i,choices[i]
		choice = raw_input('Choice > ')
		try: 
			choicez = int(choice)
		except ValueError: 
			print 'Please select a correct choice!'
			pass
		if choicez == 1: 
			os.system('clear')
			print 'Current Balance: {a}'.format(a=p.showBalance())
			bett = staking(p)
			bet(d,p)
		elif choicez == 2: 
			return
		else: 
			print 'Wrong choice!'

os.system('clear')
namez = raw_input('Name > ')
NewGame(namez)







