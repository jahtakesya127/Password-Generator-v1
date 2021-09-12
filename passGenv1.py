import random, string, argparse
from sys import argv
import xerox

def mixer():
	temp = random.sample(lst, length)
	global password
	password = "".join(temp)
	print(password)
	clip()

def clip():
	xerox.copy(password)

if len(argv) == 1:
	length = 8
	lst = string.ascii_lowercase
	print('[*] Default: 8 characters')
	mixer()
else:
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', type=int, help='password length')
	args = parser.parse_args()
	length = args.c
	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	num = string.digits
	symbols = string.punctuation
	lst = lower + upper + num + symbols
	mixer()
