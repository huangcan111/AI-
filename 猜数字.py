import random
lower_bound = 1  #最小数
upper_bound = 2 #最大数
secret_number = random.randint(lower_bound, upper_bound) #生成随机数
scores = {}  #记录成绩
max_attempts = 10 #最多尝试次数

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("请输入一个有效的整数。")

def play_game():
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    guess = None

    while attempts < max_attempts and guess != secret_number:
        guess = get_int_input(f"猜一个{lower_bound}到{upper_bound}之间的数字（剩余尝试次数{max_attempts - attempts}）: ")
        attempts += 1
        if guess < secret_number:
            print("太小了！")
        elif guess > secret_number:
            print("太大了！")
        else:
            print("恭喜你，猜对了！")
            break

    if attempts == max_attempts and guess != secret_number:
        print(f"很遗憾，你没有猜中。正确答案是{secret_number}。")
    return attempts
#成绩看板
def show_leaderboard():
    print("\n排行榜：")
    for player, score in sorted(scores.items(), key=lambda item: item[1]):
        print(f"{player}: {score}次尝试")

def update_scores(player_name, attempts):
    scores[player_name] = attempts
    print(f"{player_name}的最好成绩是{attempts}次尝试。")

def main():
    player_name = input("请输入你的名字: ")
    attempts = play_game()
    update_scores(player_name, attempts)
    show_leaderboard()

if __name__ == "__main__":
    main()