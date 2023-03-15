#import os
import telebot
import pdf2docx
#from io import BytesIO
import requests
#from docx2pdf import convert
#import arabic_reshaper


bot = telebot.TeleBot("5895784304:AAFUM1dABr_HC713sgdc-52L-uU3HuQBQmQ")

@bot.message_handler(content_types=['document'])
def handle_pdf_files(message):
    if message.document.mime_type == 'application/pdf':
        bot.reply_to(message,"Don't send anythings!, please wait :)")
        file_id = message.document.file_id
        file_info = bot.get_file(file_id)
        filePath=file_info.file_path
        userID=message.from_user.id
        Oname=message.document.file_name
        url='https://api.telegram.org/file/bot5895784304:AAFUM1dABr_HC713sgdc-52L-uU3HuQBQmQ/'+filePath
        file = requests.get(url)
        with open(Oname, "wb") as f:
              f.write(file.content)
        pdf='/home/NodeUser2/'+Oname
        new_filename = Oname[:-4] + ".docx"
        word='/home/NodeUser2/'+ new_filename
        pdf2docx.parse(pdf,word)
        with open(word, 'rb') as f:
             bot.send_document(chat_id=userID, document=f)
    #--------------docx ----> pdf----------
    elif message.document.file_name.endswith('.docx') :
        bot.reply_to(message,"Don't send anythings!, please wait :)")
        file_id2 = message.document.file_id
        file_info2 = bot.get_file(file_id2)
        filePath2=file_info2.file_path
        userID2=message.from_user.id
        Oname2=message.document.file_name
        url2='https://api.telegram.org/file/bot6133293710:AAH7tok-0EvE2uR85_VGC3mJJwOlYsQDvfA/'+filePath2
        file2 = requests.get(url2)
        with open(Oname2, "wb") as f2:
              f2.write(file2.content)
        Doc_path='/home/NodeUser2/'+Oname2
        PDF_f= Oname2[:-5] + ".pdf"
        doc = aw.Document(Doc_path)
        doc.save(PDF_f)
        with open(PDF_f, 'rb') as f3:
             bot.send_document(chat_id=userID2, document=f3)
    else:
       bot.reply_to(message, "Sorry, I can only process PDF files.")

@bot.message_handler(content_types=['text'])
def hi_handler(message):
    bot.reply_to(message, "Hello! How can I help you today?")
bot.polling()

"""elif message.document.mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        # Save the file with the original name and .docx extension
        file_name = message.document.file_name
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
        # Convert the file to pdf
        pdf_file = file_name[:-5] + '.pdf'
        convert(file_name, pdf_file)
        # Send the pdf file to the user
        with open(pdf_file, 'rb') as f:
            bot.send_document(message.chat.id, f)"""



