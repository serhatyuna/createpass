import createpass as p

chars = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ1234567890_-.'
chars_options = {
	"az": False,
	"AZ": False,
	"nu": False,
	"sy": False
}

print('-' * 8, 'RANDOM PASSWORD CREATOR', '-' * 8)
print("(Default options: [a-zA-Z0-9_-.])")
change_options = input('Do you want to change options? (y/n): ')

if change_options.upper() == 'Y':
	chars_options["az"] = True if input('\t-> [a-z] ? (y/n): ').upper() == 'Y' else False
	chars_options["AZ"] = True if input('\t-> [A-Z] ? (y/n): ').upper() == 'Y' else False
	chars_options["nu"] = True if input('\t-> [0-9] ? (y/n): ').upper() == 'Y' else False
	chars_options["sy"] = True if input('\t-> [.-_] ? (y/n): ').upper() == 'Y' else False

	while True:
		try:
			repeat_time = int(input("Number of passwords: "))
			if repeat_time > 0:
				break
			else:
				print("Please enter a number greater than 0")
		except:
			print("Please enter a number")

	while True:
		try:
			length = int(input("Length: "))
			if length > 0:
				break
			else:
				print("Please enter a number greater than 0")
		except:
			print("Please enter a number")

	updated_chars = ''
	if any(option == True for option in chars_options.values()):
		if chars_options["az"] == True:
			updated_chars += 'abcdefghijklmnoprstuvwxyz'
		if chars_options["AZ"] == True:
			updated_chars += 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
		if chars_options["nu"] == True:
			updated_chars += '1234567890'
		if chars_options["sy"] == True:
			updated_chars += '_-.'

		created_passwords = p.create_random_passwords(updated_chars, length, repeat_time)
		for ps in created_passwords:
			print(ps)
	else:
		for ps in p.create_random_passwords(chars, length, repeat_time):
			print(ps)
else:
	while True:
		try:
			repeat_time = int(input("Number of passwords: "))
			if repeat_time > 0:
				break
			else:
				print("Please enter a number greater than 0")
		except:
			print("Please enter a number")
	while True:
		try:
			length = int(input("Length: "))
			if length > 0:
				break
			else:
				print("Please enter a number greater than 0")
		except:
			print("Please enter a number")

	for ps in p.create_random_passwords(chars, length, repeat_time):
		print(ps)