str1 = input("Enter a string: ")

for ch in str1:
    if ch not in str1[:str1.index(ch)]:
        print(ch, ":", str1.count(ch))