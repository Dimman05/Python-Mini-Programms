# This is a prototype of Jarvis assistant
from functions import *

greeting()

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	clear()

	while True:
		query = listen().lower()
		print(query)

		if 'open' and 'youtube' in query:
			open_youtube()
		elif 'open' and 'google' in query:
			open_google()
		elif 'stack overflow' in query:
			open_stackoverflow()
		elif 'time' in query:
			current_time()
		elif 'exit' or 'close' in query:
			close()
		elif 'joke' in query:
			joke()
		elif 'lock window' or 'lock computer' in query:
			lock()
		elif 'shutdown' in query:
			shutdown()
		elif 'empty recycle bin' in query:
			empty_bin()
		elif "restart" in query:
			restart()
		elif "hibernate" in query or "sleep" in query:
			hibernate()
		elif "log off" in query or "sign out" in query:
			log_out()
		elif "write a note" or 'make a note' in query:
			make_note()
		elif "show" and 'notes' or 'note' in query:
			show_notes()
		elif "wikipedia" in query:
			open_wikipedia()
		elif 'show' and 'calendar' in query:
			show_calendar()
		elif 'random' and 'information' in query:
			random_wiki()
		elif 'show' and 'ip' in query:
			my_ip()
		elif 'one note' in query:
			open_oneNote()
		elif 'open' and 'youtube music' in query:
			open_youtubeMusic()
		elif 'github' in query:
			open_github()
		elif 'dego' in query:
			open_degoo()
		elif 'google drive' in query:
			open_googleDrive()
		elif 'spotify' in query:
			open_spotify()
		elif 'calculator' in query:
			open_calc()
		elif 'notepad' in query:
			open_notepad()
		elif 'wordpad' in query:
			open_wordpad()
























