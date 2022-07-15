input_sequence = input().split()
palindrome = input()
palindrome_list = []
for el in input_sequence:
    if el == el[::-1]:
        palindrome_list.append(el)
print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(palindrome)} times')