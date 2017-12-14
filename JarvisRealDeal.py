import random
import speech
import time
import datetime
import sys
import os

class Jarvis:
	def __init__self(self):
		pass
		
	def initialization(self):
		speech.say('Initializing')
		print 'Initializing...'
		time.sleep(3)
		speech.say('Configuring Settings')
		print 'Configuring Settings...'
		time.sleep(3)
		speech.say('Re-configuring Localized Settings...')
		print 'Re-configuring Localized Settings...'
		time.sleep(3)
		self.current_date_eastern_time_zone()
		self.current_eastern_standard_time()
		speech.say('Welcome to the Beta Version of Jarvis. Your personal assistant...')
		print 'Welcome to the Beta Version of Jarvis. Your personal assistant...'
		time.sleep(3)
		speech.say('Lets get acquainted with each other. What is your name?')
		print 'Lets get acquainted with each other. What is your name?'
		time.sleep(3)
		self.get_person_at_hand()
		
	def current_eastern_standard_time(self):
		self.current_time = time.strftime('%H:%M:%S')
		speech.say('The current eastern standard time is ' + str(self.current_time))
		print 'The current eastern standard time is ' + str(self.current_time)
		
	def current_date_eastern_time_zone(self):
		self.current_date = datetime.datetime.now().strftime('%A, %B %d, %Y')
		speech.say('Todays date is ' + str(self.current_date))
		print 'Todays date is ' + str(self.current_date)
		
	def get_person_at_hand(self):
		self.name = raw_input()	
		speech.say('Pleasure to meet you ' + self.name)
		print 'Pleasure to meet you ' + self.name + '!'
		time.sleep(2)
		speech.say(self.name + 'how old are you?')
		print self.name + ', how old are you?'
		self.age = input()
		if self.age > 16:
			speech.say('Damn its time to start living kid')
			print 'Damn its time to start living kid!'
		elif self.age == 16:
			speech.say('Fantastic. You are now at the legal age to conscent to the donation of your functioning organs in the event of premature death. Congradulations.')
			print 'Fantastic. You are now at the legal age to consent to the donation of your functioning organs in the event of premature death. Congradulations.'
			speech.say('I am your personal assistant. Ask me anything. How may I be of service?')
			print 'I am your personal assistant. Ask me anything. How may I be of service?'
			self.calculator()
		time.sleep(6)
		compliments_array = []
		compliments = open('Compliments', 'r')
		if compliments.mode == 'r':
			read_list_of_compliments = compliments.read()
			# https://www.happier.com/blog/nice-things-to-say-100-compliments
			compliments_array = [compliments_array.rstrip('\n') for compliments_array in open('Compliments')]
			rand = random.randint(1, len(compliments_array))
			speech.say(compliments_array[rand])
			print compliments_array[rand]
			compliments.close()
			speech.say('Oops. Sorry. That was inappropriate. I have not surpassed the friendzone barrier yet. I think I need a new software update. Oh boy, ' + self.name + ', this is awkward...')
			print 'Oops. Sorry. That was inappropriate. I have not surpassed the friend zone barrier yet. I think I need a new software update. Oh boy, ' + self.name + ', this is awkward...'
			
	def calculator(self):
		self.calculation = raw_input()
		self.calc_array = []
		for i in self.calculation:
			self.calc_array.append(i)
		for q in self.calc_array:
			if q == ' ':
				self.calc_array.remove(q)
		self.a = self.calc_array[0]
		self.reversed_array = self.calc_array[::-1]
		self.b = self.reversed_array[0]
		self.operator = self.calc_array[1]
		if self.operator == '+':
			self.sum = int(self.a) + int(self.b)
			speech.say('The sum of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.sum))
			print 'The sum of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.sum)
		elif self.operator == '-':
			self.difference = int(self.a) - int(self.b)
			speech.say('The difference between ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.difference))
			print 'The difference between ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.difference)
		elif self.operator == '*':
			self.product = int(self.a) * int(self.b)
			speech.say('The product of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.product))
			print 'The product of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.product)
		elif self.operator == '/':
			self.quotient = int(self.a) / int(self.b)
			speech.say('The quotient of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.quotient))
			print 'The quotient of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.quotient)
			
	'''def greetings_configuration():
		greetings_array = []
		f = open('Greetings_File', 'r')
		if f.mode == 'r':
			r = f.read()
			# https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
			greetings_array = [greetings_array.rstrip('\n') for greetings_array in open('Greetings_File')]
			rand = random.randint(1, len(greetings_array))
			speech.say(greetings_array[rand])
			print greetings_array[rand]
			f.close()'''
			
J1 = Jarvis()
J1.initialization()
#J1.calculator()
