import random
words = 'wordlist.txt'

def group_words():
	word_dict = {}
	with open(words,'r') as read_obj:
		for line in read_obj:
			word_dict[line[:-1].lower()] = len(line)
	group = []
	for x in range(11):
		y = []
		group.append(y)
	for x in word_dict.keys():
		if len(x)==1:
			group[0].append(x)
		elif len(x)==2:
			group[1].append(x)
		elif len(x)==3:
			group[2].append(x)
		elif len(x)==4:
			group[3].append(x)
		elif len(x)==5:
			group[4].append(x)
		elif len(x)==6:
			group[5].append(x)
		elif len(x)==7:
			group[6].append(x)
		elif len(x)==8:
			group[7].append(x)
		elif len(x)==9:
			group[8].append(x)
		elif len(x)==10:
			group[9].append(x)
		elif len(x)==11:
			group[10].append(x)
		else:
			pass
	return group

def grab_word(n,wordlist):
	if n<12 and n>0:
		word = random.choice(wordlist[n-1])
		return word
	else:
		print("Invalid length Selection..")

def verify_letter(word,c):
	if c in word:
		print(f"{c} is in the word..")
		return True
	else:
		print(f"{c} is not in the word")
		return False

def print_word(k,word,guess):
	global pr
	sp = word
	for x in guess:
		for y in range(0,len(word)):
			if x==sp[y]:
				pr[y]=x
	expected = ''.join(pr)
	print(expected+'\n')
	if word == expected:
		print("You have won the game..")
		print(f"The word is {word}")
		return True
	else:
		return False

while True:
	print("Starting the Hangman Game...")
	while True:
		try:
			n = int(input('What is the minimum length of the word (4-11)?: '))
		except:
			print("Invalid Input.. Please Try Again..")
		else:
			if n<12 and n>3:
				break
			else:
				print("Invalid Input.. Please Try Again..")

	k = random.randint(n,11)
	inc = k+4
	lst = group_words()
	word = grab_word(k,lst)
	print("Selecting a word..\n")
	print(f"The word has {k} letters in it.")
	pr = []
	for x in range(0,k):
		pr.append('$')
	b=0
	guess = []
	print(k*'$')
	while b<inc:
		print(f"Attempts Remaining {inc-b}")
		if b!=0:
			print(f"Previous Guesses: {guess} ")
		else:
			pass
		choose = input("Choose the Next Letter: ")
		guess.append(choose)
		verify_letter(word,choose)
		if print_word(k,word,guess):
			b += inc
		b+=1

	if (inc-b)==0:
		print("You Lost the Game...")
		print(f"The word is {word}")

	print("Do you want to play again?")
	while True:
		try:
			i = input('Enter y or n : ').lower()
		except:
			pass
		else:
			if i=='y' or i=='n':
				break
			else:
				continue
	if i=='n':
		break