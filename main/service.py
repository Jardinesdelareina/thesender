from django.core.files import File
import datetime

def record_data(user_email):
    f = open(f'./emails.txt', 'a')
    email_list = File(f)
    email_list.write(str(datetime.datetime.now()) + ' ' + user_email + '\n')
    email_list.close()
    f.close()
