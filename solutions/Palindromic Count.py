def is_palindrome(string):
    temp = ""
    for s in string:
        if s != " ":
            temp = s + temp
    if temp == string:
        return True
    else:
        return False


def sub_string(string, length):
    result = []
    st, ls = 0, length
    while ls <= N:
        now = string[st:ls]
        if is_palindrome(now):
            result.append(now)
        st += 1
        ls += 1
    return result


def palindromic_count():
    sub_string_list = [sub_string(String, length) for length in Length]
    res_count_list = [len(sub_strings) for sub_strings in sub_string_list]
    return sum(res_count_list)


N = int(input())
if N > 10 ** 4:
    exit()
String = input()

if len(String) != N:
    exit()
M = int(input())

if M > 10 ** 4:
    exit()
length_str = input()
Length = [int(val) for val in length_str.split(" ")]

if M != len(Length):
    exit()

count_result = palindromic_count()
print(count_result)
