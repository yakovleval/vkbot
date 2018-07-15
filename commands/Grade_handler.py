import command_system

list_with_double_classes = ['11г', '11к', '11л', '10в', '10к']


#users = {}

def klass_change(user_id, user_message):
    '''
    s = body[0] + body[1] + body[-1].lower()
    users[user_id] = s
    message = 'класс, для которого отсылается расписание, изменён на ' + '"' + s + '"'
    return message
    '''
    str_user_id = str(user_id)
    file = open('users.txt')
    lines = file.readlines()
    file.close()
    if str_user_id + '\n' in lines:
        f = open('users.txt')
        a = f.readlines()

        f.close()
        index = a.index(str_user_id + '\n') + 1
        a[index] = user_message + '\n'

        f = open('users.txt', 'w')
        for line in a:
            f.write(line)
        f.close()





    else:
        f = open('users.txt', 'a')
        f.write(str_user_id + '\n')
        f.write(user_message + '\n')
        f.close()
    s = user_message[0] + user_message[1] + user_message[-1].lower()
    message = 'класс, для которого отсылается расписание, изменён на ' + '"' + s + '"'
    return message

def klass_of_user(user_id):
    file = open('users.txt')
    lines = file.readlines()
    file.close()
    if str(user_id) + '\n' not in lines:
        return ''
    else:
        return lines[lines.index(str(user_id)+'\n') + 1][0] + lines[lines.index(str(user_id)+'\n') + 1][1] + lines[lines.index(str(user_id)+'\n') + 1][2]






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

