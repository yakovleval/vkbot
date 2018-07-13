import command_system

list_with_double_classes = ['11г', '11к', '11л', '10в', '10к']


users = {}

def klass_change(user_id, body):
    s = body[0] + body[1] + body[-1].lower()
    users[user_id] = s
    message = 'класс, для которого отсылается расписание, изменён на ' + '"' + s + '"'
    return message

def request_for_commands(user_id):
    if user_id not in users:
        return ''
    else:
        return users[user_id]






grade = command_system.Command()
grade.keys = ['10 а', '10-а','10а','10-б', '10 б','10б',
                            '10 в', '10-в', '10в', '10-г', '10 г', '10г',
                            '10 и', '10-и', '10и', '10-к', '10 к', '10к',
                            '10 м', '10-м', '10м', '10-с', '10 с', '10с',
                            '11 а', '11-а', '11а', '11-б', '11 б', '11б',
                            '11 в', '11-в', '11в', '11-г', '11 г', '11г',
                            '11 и', '11-и', '11и', '11-к', '11 к', '11к',
                            '11 м', '11-м', '11м', '11-с', '11 с', '11с', '11л', '11 л', '11-л']
grade.process = klass_change

