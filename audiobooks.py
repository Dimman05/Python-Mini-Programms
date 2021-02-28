import pyttsx3
import PyPDF2

file = input('Enter the path of the book: ')
book = open(file, "rb")

speaker = pyttsx3.init()

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

start = int(input("Enter a page"))

for num in range(start, pages):
    page = pdfReader.getPage(start)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()