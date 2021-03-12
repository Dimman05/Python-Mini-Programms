import pyshorteners

url = input('Enter a url: ')
s = pyshorteners.Shortener()
print(s.tinyurl.short(url))
