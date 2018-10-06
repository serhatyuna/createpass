import random

def create_random_passwords(chars='abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ1234567890_-.', len=8, repeat=1):
	passwords = []
	for i in range(repeat):
		password = ''
		for j in range(len):
			password += random.choice(chars)
		passwords.append(password)
	return passwords