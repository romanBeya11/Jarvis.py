import linguistictagger as lt
import reminders
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
		time.sleep(3)
		console.hud_alert('Initializing...', '3')
		speech.say('Initializing', 'en-EN', 0.5)
		print 'Initializing...'
		cwd = os.getcwd()
		print cwd + '\n\n'
		time.sleep(3)
		console.hud_alert('Configuring Settings', '3')
		speech.say('Configuring Settings', 'en-EN', 0.5)
		print 'Configuring Settings...'
		cpr = sys.copyright
		print cpr + '\n\n'
		time.sleep(3)
		console.hud_alert('Re-configuring Localized Settings...', '3')
		speech.say('Re-configuring Localized Settings...', 'en-EN', 0.5)
		print 'Re-configuring Localized Settings...\n\n'
		time.sleep(3)
		console.hud_alert('Welcome to Jarvis', '5')
		speech.say('Welcome to the Beta Version of Jarvis. Your personal assistant...', 'en-EN', 0.5)
		print 'Welcome to the Beta Version of Jarvis. Your personal assistant...'
		time.sleep(3)
		self.login_protocol()
		self.current_date_eastern_time_zone()
		self.current_eastern_standard_time()
		time.sleep(10)
		self.conversation_dynamics()
		self.take_a_selfie()
		self.calculator()
		
	def current_eastern_standard_time(self):
		#self.name = raw_input()
		self.current_time = time.strftime('%H:%M:%S')
		if time.strftime('%H') > 12:
			speech.say('Good Morning' + self.name, 'en-EN', 0.5)
			console.hud_alert('Good Morning ' + self.name.capitalize(), '3')
			speech.say('The current eastern standard time is ' + str(time.strftime('%H:%M:%S')), 'en-EN', 0.5)
			print 'The current eastern standard time is ' + str(time.strftime('%H:%M:%S'))
		#speech.say('The current eastern standard time is ' + str(self.current_time), 'en-EN', 0.5)
		#print 'The current eastern standard time is ' + str(self.current_time)
		
	def current_date_eastern_time_zone(self):
		self.current_date = datetime.datetime.now().strftime('%A, %B %d, %Y')
		speech.say('Todays date is ' + str(self.current_date), 'en-EN', 0.5)
		print 'Todays date is ' + str(self.current_date)
	
	def login_protocol(self):
		speech.say('Please log into your Jarvis Account to utilize my services', 'en-EN', 0.5)
		self.login_personel = console.login_alert('Please log into your Jarvis Account to utilize services')
		self.login_personel_array = []
		for i in self.login_personel:
			self.login_personel_array.append(i)
		self.name_of_current_subject_array = []
		self.name = self.login_personel_array[0]
		try:
			self.read_from_personal_file = open(self.name.upper(), 'r')
			if self.read_from_personal_file.mode == 'r':
				self.read_from_file = self.read_from_personal_file.read()
				# https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
				self.name_of_current_subject_array.append(self.read_from_file)
				for i in self.name_of_current_subject_array:
					if i.rfind(self.name.upper()):
						speech.say('Welcome back ' + self.name + '!', 'en-EN', 0.5)
						speech.say('How may I be of service?', 'en-EN', 0.5)
						print 'Welcome back ' + self.name + '!'
						print 'How may I be of service?'
						self.idle()
						self.read_from_personal_file.close()
					else:
						speech.say('Pleasure to meet you ' + self.name, 'en-EN', 0.5)
						print 'Pleasure to meet you ' + self.name + '!'
						self.your_own_personal_file_write()
		except:
			speech.say('Pleasure to meet you ' + self.name, 'en-EN', 0.5)
			print 'Pleasure to meet you ' + self.name + '!'
			self.your_own_personal_file_write()
			self.getting_to_know_you()
	
	def data_mining(self):
		self.file_of_subject = open(self.name.upper(), 'r')
		self.file_of_subject_array = []
		if self.file_of_subject.mode == 'r':
			self.file_of_subject_array = [self.file_of_subject_array.rstrip('\n') for self.file_of_subject_array in open(self.name.upper())]
			for i in self.file_of_subject_array:
				if '\n' + self.name + ' is ' + str(self.age) + ' years young!' in i:
					pass
				else:
					self.file_of_current_subject = open(self.name.upper(), 'a+')
					self.file_of_current_subject.write('\n' + self.name + ' is ' + str(self.age) + ' years young!')
					self.file_of_current_subject.close()
		
	def getting_to_know_you(self):
		speech.say('Lets get acquainted with each other.', 'en-EN', 0.5)
		print 'Lets get acquainted with each other.'
		self.name = raw_input()
		speech.say(self.name + ', how old are you?', 'en-EN', 0.5)
		print self.name + ', how old are you?'
		self.age = input()
		if self.age >= 16:
			self.data_mining()
			time.sleep(2)
			speech.say('Lets have a conversation. Here are a few issues that have come to mind', 'en-EN', 0.5)
			print 'Lets have a conversation. Here are a few issues that have come to mind.'
			time.sleep(3)
			self.conversation_dynamics()
		'''elif self.age == 16:
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
					
	def calculator(self):
		try:
			self.calculation = raw_input()
			self.original_array = []
			self.first_segment_of_digits = []
			self.second_segment_of_digits = []
			self.concate_first_segment_of_digits = ''
			self.concate_second_segment_of_digits = ''
			for i in self.calculation:
				self.original_array.append(i)
			for i in self.original_array:
				if ' ' in i:
					index = self.original_array.index(i)
					for x in range(index):
						self.first_segment_of_digits.append(self.original_array[x])
					self.original_array.remove(i)
					break
			for i in self.original_array:
				if ' ' in i:
					self.reverse_of_original_array = self.original_array[::-1]
					index = self.reverse_of_original_array.index(i)
					for x in range(index):
						self.second_segment_of_digits.append(self.reverse_of_original_array[x])
						self.reverse_of_second_array = self.second_segment_of_digits[::-1]
			for i in self.first_segment_of_digits:
				self.concate_first_segment_of_digits += i
			for i in self.reverse_of_second_array:
				self.concate_second_segment_of_digits += i
			self.a = self.concate_first_segment_of_digits
			self.b = self.concate_second_segment_of_digits
			for i in self.original_array:
				if '+' in i:
					self.sum = int(self.a) + int(self.b)
					speech.say('The sum of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.sum), 'en-EN', 0.5)
					print 'The sum of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.sum)
					self.calculator()
					#self.force_shutdown_now()
				elif '-' in i:
					self.difference = int(self.a) - int(self.b)
					speech.say('The difference between ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.difference), 'en-EN', 0.5)
					print 'The difference between ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.difference)
					self.calculator()
				elif '*' in i:
					self.product = int(self.a) * int(self.b)
					speech.say('The product of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.product), 'en-EN', 0.5)
					print 'The product of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.product)
					self.calculator()
				elif '/' in i:
					self.quotient = int(self.a) / int(self.b)
					speech.say('The quotient of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.quotient), 'en-EN', 0.5)
					print 'The quotient of ' + str(self.a) + ' and ' + str(self.b) + ' is ' + str(self.quotient)
					self.calculator()
				'''else:
					speech.say('Sorry. My software does not recognize that command.')
					print 'Sorry. My software does not recognize that command.'
					self.calculator()'''
		except:
			speech.say('Sorry. My software does not recognize that command.', 'en-EN', 0.5)
			print 'Sorry. My software does not recognize that command.'
			self.calculator()
		#self.calculator()
	
	def take_a_selfie(self, filename='.temp.jpg'):
		self.name = raw_input()
		self.pic = raw_input()
		if 'pic' in self.pic or 'selfie' in self.pic:
			img = photos.capture_image()
			if img:
				img.save(filename)
				console.show_image(filename)
				speech.say(self.name + ', you look stunning!', 'en-EN', 0.5)
				print self.name + ', you look stunning!'
				speech.say('Would you like to save your master piece in a custom album?', 'en-EN', 0.5)
				print 'Would you like to save your master piece in a custom album?'
				self.to_save_or_not_to_save = raw_input()
				if 'ye' in self.to_save_or_not_to_save or 'sure' in self.to_save_or_not_to_save or 'ok' in self.to_save_or_not_to_save:
					photos.create_album(self.name + 's Album')
					speech.say('Okay. I have created your own custom album.', 'en-EN', 0.5)
					print 'Okay. I have created your own custom album'
					speech.say('Hold the image to save your elegant picture', 'en-EN', 0.5)
					print 'Hold the image to save your elegant picture.'
					self.take_a_selfie()
				else:
					speech.say('Affirmative... Your photo will be deleted after this session.', 'en-EN', 0.5)
					print 'Affirmative... Your photo will be deleted after this session.'
					self.take_a_selfie()
		console.clear()
		self.take_a_selfie()
	
	def reminders(self):
		self.set_a_reminder = raw_input() 	
		for i in self.set_a_reminder:
			if 'remind' in i:
				reminders.Reminder.title = 'Reminder1'
				speech.say('Okay. I am setting a new reminder for ' + self.reason_for_reminder + ', on ' + self.time_of_reminder, 'en-EN', 0.5)
				print 'Okay. I am setting a new reminder for ' + self.reason_for_reminder + ', on ' + self.time_of_reminder
				
	def idle(self):
		self.calculator()
		self.take_a_selfie()
		self.idle = raw_input()
		#time.
		if self.idle == 'sudo shutdown-n':
			speech.say('Initiating forced shutdown!', 'en-EN', 0.5)
			print 'Initiating forced shutdown!'
			time.sleep(2)
			speech.say('Shutdown protocol commencing...', 'en-EN', 0.5)
			print 'Shutdown protocol commencing...'
			time.sleep(2)
			speech.say('Shutdown complete. Jarvis Terminated. See you later ' + self.name, 'en-EN', 0.5)
			print 'Shutdown complete. Jarvis Terminated. See you later ' + self.name
			sys.exit()
		elif self.idle == 'convo':
			#self.current_second = time.strftime('%S')
			#self.awkward_silence = int(self.second_at_idle) - int(self.current_second)
			#if self.awkward_silence > 3:
			self.conversation_dynamics()
		else:
			self.responce_dynamics()
	
	def conversation_dynamics(self):
		self.conversation_topics_array = []
		self.conversation = open('Conversation_Topics', 'r')
		if self.conversation.mode == 'r':
			self.read_list_of_conversation_topics = self.conversation.read()
			# https://conversationstartersworld.com/250-conversation-starters/
			self.conversation_topics_array = [self.conversation_topics_array.rstrip('\n') for self.conversation_topics_array in open('Conversation_Topics')]
			self.rand = random.randint(1, len(self.conversation_topics_array))
			speech.say(self.conversation_topics_array[self.rand], 'en-EN', 0.5)
			print self.conversation_topics_array[self.rand]
			self.conversation.close()
			self.response_dynamics()
			#self.idle()
			
	def force_shutdown_now(self):
		#self.name = raw_input()
		self.shutdown = raw_input()
		if 'sudo shutdown-n' in self.shutdown:
			console.hud_alert('Initiating forced shutdown!', '5')
			speech.say('Initiating forced shutdown!', 'en-EN', 0.5)
			console.set_color(1, 0, 0)
			print 'Initiating forced shutdown!'
			print os.getcwd() * 25
			time.sleep(2)
			console.hud_alert('Shutdown protocol commencing...', '5')
			speech.say('Shutdown protocol commencing...', 'en-EN', 0.5)
			console.set_color(1, 0, 0)
			print 'Shutdown protocol commencing...'
			print sys.copyright * 25
			time.sleep(2)
			console.hud_alert('Jarvis Terminated', '3')
			speech.say('Shutdown complete. Jarvis Terminated. See you later ' + self.name, 'en-EN', 0.5)
			console.set_color(1, 0, 0)
			print 'Shutdown complete. Jarvis Terminated. See you later ' + self.name
			sys.exit()
			
	#def response_dynamics(self):
		
	
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
#J1.getting_to_know_you()
#J1.take_a_selfie()
#J1.conversation_dynamics()
#J1.idle()
#J1.force_shutdown_now()
#J1.login_protocol()
J1.current_eastern_standard_time()
