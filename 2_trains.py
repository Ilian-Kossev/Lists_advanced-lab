number = int(input())
train = number * [0]
command = input().split()
while not command == ['End']:   # or the condition can be - while not command[0] == 'End'
    if command[0] == 'add':
        train[- 1] += int(command[1])
    elif command[0] == 'insert':
        train[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        train[int(command[1])] -= int(command[2])
    command = input().split()
print(train)