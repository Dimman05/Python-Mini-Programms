from functions import *

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()


    while True:

        query = listen().lower()
        try:
            if 'open youtube' in query:
                open_youtube()
            elif 'open google' in query:
                open_google()
            elif 'open stackoverflow' in query:
                open_stackoverflow()
            elif 'the time' in query:
                current_time()
            elif 'exit' in query:
                close()
            elif 'joke' in query:
                joke()
            elif 'lock window' in query:
                lock()
            elif 'shutdown system' in query:
                shutdown()
            elif 'empty recycle bin' in query:
                empty_bin()
            elif "don't listen" in query or "stop listening" in query:
                speak("for how much time you want to stop jarvis from listening commands")
                a = int(listen())
                time.sleep(a)
                print(a)
            elif "restart" in query:
                restart()
            elif "hibernate" in query or "sleep" in query:
                hibernate()
            elif "log off" in query or "sign out" in query:
                log_out()
            elif "write a note" in query:
                make_note()
            elif "show note" in query:
                show_notes()
            elif "wikipedia" in query:
                open_wikipedia()
            elif 'air console' in query:
                open_airconsole()
            elif 'show' and 'calendar' in query:
                show_calendar()
            elif 'random' and 'information' in query:
                random_wiki()
            elif 'show' and 'ip' in query:
                my_ip()
            elif 'OneNote' in query:
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
        except Exception as e:
           pass
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
