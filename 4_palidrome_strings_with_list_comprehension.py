input_sequence = input().split()
palindrome = input()
palindrome_list = [el for el in input_sequence if el == el[::-1]]
print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(palindrome)} times')