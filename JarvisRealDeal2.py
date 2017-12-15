import ImageDraw
import datetime
import random
import speech
import photos
import console
import time
import sys
import os

class Jarvis:
	def __init__self(self):
		pass
		
	def initialization(self):
		speech.say('Initializing')
		print 'Initializing...'
		cwd = os.getcwd()
		print cwd + '\n\n'
		time.sleep(3)
		speech.say('Configuring Settings')
		print 'Configuring Settings...'
		cpr = sys.copyright
		print cpr + '\n\n'
		time.sleep(3)
		speech.say('Re-configuring Localized Settings...')
		print 'Re-configuring Localized Settings...\n\n'
		time.sleep(3)
		speech.say('Welcome to the Beta Version of Jarvis. Your personal assistant...')
		print 'Welcome to the Beta Version of Jarvis. Your personal assistant...'
		time.sleep(3)
		self.current_date_eastern_time_zone()
		self.current_eastern_standard_time()
		time.sleep(10)
		speech.say('Lets get acquainted with each other. What is your name?')
		print 'Lets get acquainted with each other. What is your name?'
		time.sleep(3)
		self.get_person_at_hand()
		#self.your_own_personal_file_write()
		self.your_own_personal_file_read()
		
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
		self.your_own_personal_file_read()
		'''speech.say(self.name + 'how old are you?')
		print self.name + ', how old are you?'
		self.age = input()
		if self.age > 16:
			speech.say('Damn its time to start living kid')
			print 'Damn its time to start living kid!'
			self.idle()
		elif self.age == 16:
			speech.say('Fantastic. You are now at the legal age to conscent to the donation of your functioning organs in the event of premature death. Congradulations.')
			print 'Fantastic. You are now at the legal age to consent to the donation of your functioning organs in the event of premature death. Congratulations.'
			speech.say('I am your personal assistant. Ask me anything. How may I be of service?')
			print 'I am your personal assistant. Ask me anything. How may I be of service?'
			self.calculator()
		time.sleep(3)
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
			print 'Oops. Sorry. That was inappropriate. I have not surpassed the friend zone barrier yet. I think I need a new software update. Oh boy, ' + self.name + ', this is awkward...
			self.idle()'''
			
	def your_own_personal_file_write(self):
		self.personal_file = open(self.name.upper(), 'w+') 
		self.personal_file.write('This file belongs to: ' + self.name.upper())
		self.personal_file.close()
			
	def your_own_personal_file_read(self):
		self.name_of_current_subject_array = []
		self.read_from_personal_file = open(self.name, 'r')
		if self.read_from_personal_file.mode == 'r':
			self.read_from_file = self.read_from_personal_file.read()
			# https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
			self.name_of_current_subject_array.append(self.read_from_file)
			for i in self.name_of_current_subject_array:
				if i.rfind(self.name.upper()):
					speech.say('Welcome back ' + self.name + '!')
					speech.say('How may I be of service?')
					print 'Welcome back ' + self.name + '!'
					print 'How may I be of service?'
					self.idle()
					self.read_from_personal_file.close()
			else:
				speech.say('Pleasure to meet you ' + self.name)
				print 'Pleasure to meet you ' + self.name + '!'
				self.your_own_personal_file_write()
				self.idle()
					
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
			self.idle()
		elif self.operator == '-':
			self.difference = int(self.a) - int(self.b)
			speech.say('The difference between ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.difference))
			print 'The difference between ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.difference)
			self.idle()
		elif self.operator == '*':
			self.product = int(self.a) * int(self.b)
			speech.say('The product of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.product))
			print 'The product of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.product)
			self.idle()
		elif self.operator == '/':
			self.quotient = int(self.a) / int(self.b)
			speech.say('The quotient of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.quotient))
			print 'The quotient of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.quotient)
			#self.idle()
			self.calculator()
	
	def take_a_selfie(self, filename='.temp.jpg'):
		self.name = raw_input()
		self.selfie = raw_input()
		if 'selfie' in self.selfie:
			img = photos.capture_image()
			if img:
				img.save(filename)
				console.show_image(filename)
				speech.say(self.name + ', you look stunning!')
				print self.name + ', you look stunning!'
				speech.say('Would you like to save your master piece in a custom album?')
				print 'Would you like to save your master piece in a custom album?'
				self.to_save_or_not_to_save = raw_input()
				if 'ye' in self.to_save_or_not_to_save:
					photos.create_album(self.name + 's Album')
					speech.say('Okay. I have created your own custom album to save your legendary pic.')
					print 'Okay. I have created your own custom album to save your legendary pic.'
					speech.say('Hold the image to save your elegant pic in your custom album')
					print 'Hold the image to save your elegant pic in your custom album'
					self.idle()
				else:
					speech.say('Affirmative... Your photo will be deleted after this session.')
					print 'Affirmative... Your photo will be deleted after this session.'
					self.idle()
		console.clear()
			
	def idle(self):
		self.calculator()
		self.take_a_selfie()
		self.idle = raw_input()
		#time.
		if self.idle == 'sudo shutdown-n':
			speech.say('Initiating forced shutdown!')
			print 'Initiating forced shutdown!'
			time.sleep(2)
			speech.say('Shutdown protocol commencing...')
			print 'Shutdown protocol commencing...'
			time.sleep(2)
			speech.say('Shutdown complete. Jarvis Terminated. See you later ' + self.name)
			print 'Shutdown complete. Jarvis Terminated. See you later ' + self.name
			sys.exit()
		elif self.idle == 'convo':
			#self.current_second = time.strftime('%S')
			#self.awkward_silence = int(self.second_at_idle) - int(self.current_second)
			#if self.awkward_silence > 3:
			self.conversation_dynamics()
	
	def conversation_dynamics(self):
		conversation_topics_array = []
		conversation = open('Conversation_Topics', 'r')
		if conversation.mode == 'r':
			read_list_of_conversation_topics = conversation.read()
			# https://conversationstartersworld.com/250-conversation-starters/
			conversation_topics_array = [conversation_topics_array.rstrip('\n') for conversation_topics_array in open('Conversation_Topics')]
			rand = random.randint(1, len(conversation_topics_array))
			speech.say(conversation_topics_array[rand])
			print conversation_topics_array[rand]
			conversation.close()
			#self.response_dynamics()
			self.idle()
			
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
#J1.initialization()
#J1.calculator()
#J1.get_person_at_hand()
#J1.your_own_personal_file_read()
J1.take_a_selfie()
