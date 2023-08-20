# a = int(input('enter your age '))
# print('Your age is ', a)

a = 'bobby'
b = 'do you like carrots'
x = ''

def dialog_moment(interlocutor, piece):
    return input(f'{interlocutor}: {piece} ')
     

x = dialog_moment(a,b)
print(f'you answered {x}')