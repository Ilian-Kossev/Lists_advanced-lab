notes = 10 * [0]
command = input()
while not command == 'End':
    importance, text = command.split('-')
    current_index = int(importance) - 1
    notes[current_index] = text
print([el for el in notes if not el == 0])
