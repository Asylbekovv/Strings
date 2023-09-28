# Reversed strings with used input
user_input = str(input('Enter number for reverse: '))
reversed_str = ''.join(reversed(user_input))
print(reversed_str)

# Str count
count_str = 'System out Linux and Windows'
w = count_str.count(str(count_str))
print(w)

def contain(my_str, sub_string):
    if my_str.find(sub_string) != -1:
        return True
    else:
        return False

my_str = input("Enter main strings: ")
sub_string = input("Enter substring: ")
if contain(my_str, sub_string):
    print("Substring find in main string")
else:
    print('Substring not find main string')







