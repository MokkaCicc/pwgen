from argparse import ArgumentParser, ArgumentTypeError, Namespace
from string import ascii_lowercase, ascii_uppercase
from random import choice


NAME = "pwgen"
VERSION = "1.0.0"

LOWER_ALPHA = ascii_lowercase
UPPER_ALPHA = ascii_uppercase
NUMBERS = "0123456789"
SPECIALS = "!@#$%^&*"


def init_parser() -> ArgumentParser:
	parser = ArgumentParser(
		prog=NAME,
		description="Password generator"
	)
	parser.add_argument(
		"-v", "--version", action='version',
		version=f"{NAME} v{VERSION}"
	)
	parser.add_argument(
		"length", action='store',
		metavar="length", type=strictly_positive_int,
		help="The length of the password"
	)
	parser.add_argument(
		"-a", "--all", action='store_true',
		dest="has_all",
		help="Add uppercase letters, numbers and special characters in the password"
	)
	parser.add_argument(
		"-u", "--uppercase", action='store_true',
		dest="has_uppercase",
		help="Add uppercase letters in the password"
	)
	parser.add_argument(
		"-n", "--number", action='store_true',
		dest="has_number",
		help="Add numbers in the password"
	)
	parser.add_argument(
		"-s", "--special", action='store_true',
		dest="has_special",
		help="Add special characters in the password"
	)
	return parser

def strictly_positive_int(value: str) -> int:
	ivalue = int(value)
	if ivalue <= 0:
		raise ArgumentTypeError(f"invalid strictly_positive_int value: {value}")
	return ivalue

# 2 time more letters than number or special (2 time the alphabet)
def construct_letters_set(args: Namespace) -> str:
	letters_set = LOWER_ALPHA
	if args.has_uppercase or args.has_all:
		letters_set += UPPER_ALPHA
	if args.has_number or args.has_all:
		letters_set += NUMBERS
	if args.has_special or args.has_all:
		letters_set += SPECIALS
	return letters_set

# add minimum one of each letters type (upper, lower, number and special)
def generate_password(length: int, letters_set: str) -> str:
	password = ""
	for i in range(length):
		password += choice(letters_set)
	return password


def main() -> None:
	parser = init_parser()
	args = parser.parse_args()
	letters_set = construct_letters_set(args)
	password = generate_password(args.length, letters_set)
	print(password)

if __name__ == "__main__":
	main()