# Создайте программу lab_02_05.py, которая выводит на экран все
# возможные уникальные строки, составленные из символов строки
# введенной с клавиатуры.

a = set()


def rec(s, res):
    global a
    a.add(res)
    if len(s) > 0:
        for i in range(len(s)):
            rec(s[:i] + s[i + 1:], res + s[i])


my_str = input()
rec(my_str, "")
a.remove("")
print(*a)