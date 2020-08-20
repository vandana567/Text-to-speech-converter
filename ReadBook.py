import pyttsx3
import PyPDF2

book = open('Ethical.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
page = pdfReader.getPage(16)

# sound = speaker.getProperty('voices')
# speaker.setProperty('voice',sound[1].id)

text = page.extractText()

speaker.say(text)
speaker.runAndWait()
