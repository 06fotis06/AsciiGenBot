import os
import shutil
token= input("введи токен телеграм бота: ")






os.system("pip install -r requirements.txt")

my_file = open('.env', 'w')
 
text_for_file = f"TOKEN = '{token}'"
my_file.write(text_for_file)
 
my_file.close()


my_file = open('settings.py', 'w')
 
text_for_file = "from dotenv import load_dotenv \nload_dotenv()"
my_file.write(text_for_file)
 
my_file.close()


