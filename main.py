import pyttsx3
# friend = pyttsx3.init()
# friend.say("I will speak this text")
# friend.say("Mon boshe na porar table e")
# friend.runAndWait()

import bangla
bangla_date = bangla.get_date()
print(bangla_date)


# pdf file read
import PyPDF2
book = open('python.pdf', 'rb')
#book = open('HTML5.pdf', encoding='the-encoding').readlines()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
# print(pages)
friendRead = pyttsx3.init()
# single page read
# page = pdfReader.getPage(43)
# textRead = page.extractText()
# friendRead.say(textRead)
# friendRead.runAndWait()

# Total read book
for num in range(65, pages):
    page = pdfReader.getPage(num)
    textRead = page.extractText()
    friendRead.say(textRead)
    friendRead.runAndWait()