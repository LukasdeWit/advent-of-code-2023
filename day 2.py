
def check_game(game, maxes):
	for subgame in game.split(";"):
		for balls in subgame.split(","):
			amount, color = balls.strip().split(" ")
			if maxes[color] < int(amount):
				return False
	return True
			

def one():
	data = [f.strip() for f in open("day 2 data.txt")]
	max_ball_colors = {
		"red": 12,
		"green": 13,
		"blue": 14
	}
	ans = 0
	for line in data:
		no, game = line.split(":")
		num = int(no[5:])
		if check_game(game, max_ball_colors):
			ans += num
	return ans


def count_mins(game):
	minima = {
		"red": 0,
		"green": 0,
		"blue": 0
	}
	for subgame in game.split(";"):
		for balls in subgame.split(","):
			amount, color = balls.strip().split(" ")
			minima[color] = max(minima[color], int(amount))
	return minima["red"] * minima["green"] * minima["blue"]


def two():
	data = [f.strip() for f in open("day 2 data.txt")]
	ans = 0
	for line in data:
		game = line.split(":")[1]
		ans += count_mins(game)
	return ans


print(one())
print(two())
