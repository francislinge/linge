# range(101)：可以用来产生到范围的整数，需要注意的是取不到。0100101
# range(1, 101)：可以用来产生到范围的整数，相当于是左闭右开的设定，即。1100[1, 101)
# range(1, 101, 2)：可以用来产生到的奇数，其中是步长（跨度），即每次递增的值，取不到。11002101
# range(100, 0, -2)：可以用来产生到的偶数，其中是步长（跨度），即每次递减的值，取不到。1001-20
# answer = random.randrange(1, 101)  一个 1 到 100 之间的随机数

# CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，
# 玩家通过摇两粒骰子获得点数进行游戏。简化后的规则是：
# 玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，
# 庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。
# 为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，每局游戏开始之前，
# 玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，玩家就会输掉自己下注的金额。
# 游戏结束的条件是玩家破产（输光所有的赌注）。

import random


def roll_dice():
    """模拟摇两粒骰子并返回总点数"""
    return random.randint(1, 6) + random.randint(1, 6)


def get_valid_bet(current_funds):
    """获取玩家的有效下注金额"""
    while True:
        try:
            bet = int(input(f"你目前有 {current_funds} 元，请输入你的下注金额: "))
            if 0 < bet <= current_funds:
                return bet
            else:
                print("下注金额无效，请确保金额大于0且不超过你的现有资金！")
        except ValueError:
            print("请输入一个有效的整数！")


def play_craps():
    """主游戏逻辑"""
    funds = 1000  # 初始资金
    print("欢迎来到CRAPS游戏！你目前有 1000 元。")

    while funds > 0:
        print("\n新的一局开始！")

        # 玩家下注
        bet = get_valid_bet(funds)
        print(f"你下注了 {bet} 元。")

        # 第一次摇骰子
        first_roll = roll_dice()
        print(f"第一次摇骰子的结果是: {first_roll}")

        if first_roll in (7, 11):  # 玩家胜
            print("恭喜你，你赢了这一局！")
            funds += bet
        elif first_roll in (2, 3, 12):  # 庄家胜
            print("很遗憾，庄家赢了这一局！")
            funds -= bet
        else:  # 游戏继续
            print(f"游戏继续，你的目标点数是 {first_roll}。")
            while True:
                next_roll = roll_dice()
                print(f"再次摇骰子的结果是: {next_roll}")
                if next_roll == first_roll:  # 玩家胜
                    print("恭喜你，你赢了这一局！")
                    funds += bet
                    break
                elif next_roll == 7:  # 庄家胜
                    print("很遗憾，庄家赢了这一局！")
                    funds -= bet
                    break

        print(f"你现在有 {funds} 元。")

    print("游戏结束，你已经破产了！")


if __name__ == "__main__":
    play_craps()
