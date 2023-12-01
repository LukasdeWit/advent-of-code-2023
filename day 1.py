
def one():
	data = [f.strip() for f in open("day 1 data.txt")]
	ans = 0
	for line in data:
		num = ""
		for char in line:
			if char not in "abcdefghijklmnopqrstuvwxyz":
				num += char
		ans += int(num[0] + num[-1])
	return ans


num_map = {
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9"
}


def replace_nums(line):
	new_line = ""
	for i in range(len(line)):
		for key in num_map:
			if line[i:].startswith(key):
				new_line += num_map[key]
			elif line[i] in "0123456789":
				new_line += line[i]
	return new_line


def two():
	data = [f.strip() for f in open("day 1 data.txt")]
	ans = 0
	for line in data:
		num = ""
		line = replace_nums(line)
		for char in line:
			if char not in "abcdefghijklmnopqrstuvwxyz":
				num += char
		ans += int(num[0] + num[-1])
	return ans
	

print(one())
print(two())
