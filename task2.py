words = input("Введите слова через пробел: ")
 
words = words.split()
 
words.sort(key=len)
 
words = " ".join(words)
 
print(words)