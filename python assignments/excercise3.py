#Write a Python program that accepts a sequence of lines (blank line to terminate) 
#as input and prints the lines as output (all characters in lower case).
word = []
while True:
    w = input()
    if w:
        word.append(w.upper())
    else:
        break
for w in word:
    print(w)