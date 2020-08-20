import pyttsx3
import PyPDF2

book = open('Ethical.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)

speaker = pyttsx3.init()
page = pdfReader.getPage(16)

while page<=426:
    text = page.extractText()
    speaker.save_to_file(text ,'AudioBook.mp3')
    page = page+1

# speaker.say(text)
speaker.runAndWait()

