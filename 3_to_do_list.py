command = input()
to_do_list = 10*[0]
while not command == 'End':
    notes = command.split('-')
    index = int(notes[0]) - 1
    to_do_list.pop(index)
    action = ''.join(notes[1])
    to_do_list.insert(index, action)
    command = input()
print([el for el in to_do_list if not el == 0])
#while 0 in to_do_list:
#    to_do_list.remove(0)

#print(to_do_list)