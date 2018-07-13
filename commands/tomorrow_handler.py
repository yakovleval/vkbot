import xlrd
import datetime
import commands.Grade_handler as klass
import command_system as command_system
from commands.Grade_handler import list_with_double_classes as list







rb = xlrd.open_workbook('r.xlsx')




now_date = datetime.date.today()
num_week = now_date.isoweekday()
weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

def name_of_klass(body, user_id):
    global sheet
    if klass.users[user_id][0] + klass.users[user_id][1] == '11':
        sheet = rb.sheet_by_index(1)
    else:
        sheet = rb.sheet_by_index(0)
    i = 2
    while str((sheet.row_values(0)[i])).lower() != body:
        i += 1
    return i





def day_of_week(user_id, body):
    if klass.request_for_commands(user_id) == '':
        return 'Тебе необходимо отправить свой класс, чтобы получать расписание'

    x = klass.request_for_commands(user_id)
    klassnumber = name_of_klass(x, user_id)
    daynumber = 2
    subj_number = 1
    message = ''
    if weekdays[num_week] == 'воскресенье':
        return 'Завтра выходной;)'
    while sheet.row_values(daynumber)[0].lower() != weekdays[num_week]:
        daynumber += 1
    for i in range(daynumber, daynumber + 7):
        message += str(subj_number) + '.' + str((sheet.row_values(i)[klassnumber])).lower() + '\n'
        subj_number += 1

    return message, now_date



tomorrow_command = command_system.Command()

tomorrow_command.keys = ['завтра']
tomorrow_command.process = day_of_week