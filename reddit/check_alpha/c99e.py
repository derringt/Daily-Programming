

words = open('enable1.txt').readlines()
count = 0

for word in words:
	word = word.replace('\n', '').replace('\r','')
	if list(word) == sorted(word): count+=1

print count
