def palindrom(data_string):
    reverse_str = list(reversed(data_string))
    print(''.join(reverse_str))
    if data_string == ''.join(reverse_str):
        print("Palindrome")
    else:
        print("Not really")


# palindrom('121')
a = '12121'
print(bool(a.find(a[::-1])+1))
