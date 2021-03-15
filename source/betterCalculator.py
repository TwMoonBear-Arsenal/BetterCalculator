import argparse  # from std


class BetterCalculator:

    @staticmethod
    def Conj(x, y):
        return  x+y# 宇森

    @staticmethod
    def Pow(x, y):
        for i in range(y-1):
            x = x * x
        return x  # 庭維

    @staticmethod
    def Gcd(x, y):
            x, y = y % x, x
        return y  # 咚咚組  # 咚咚組

    @staticmethod
    def Mod(x, y):
        t=int(x/y)
        x=x-(y*t)
        return x # 學姊組


def main():

    # 準備參數解析
    example_text = "example usage: py.exe .\BetterCalculator.py 5 c 3"
    parser = argparse.ArgumentParser(
        description="簡單數學運算功能", epilog=example_text)
    parser.add_argument("x", help="第1個數字",
                        type=int)
    parser.add_argument("operator", help="運算符號:連接(c),次方(p),公約數(g),餘數(m)}",
                        type=str)
    parser.add_argument("y", help="第2個數字",
                        type=int)
    args = parser.parse_args()

    if(args.operator == "c"):
        ans = Calculator.Conj(args.x, args.y)
    elif(args.operator == "p"):
        ans = Calculator.Pow(args.x, args.y)
    elif(args.operator == "g"):
        ans = Calculator.Gcd(args.x, args.y)
    elif(args.operator == "m"):
        ans = Calculator.Mod(args.x, args.y)
    else:
        ans = "輸入錯誤"

    # end
    if(ans == "輸入錯誤"):
        print(ans)
    else:
        print("結果:", args.x, "", args.operator, "", args.y, "=", ans)
        print()


if __name__ == "__main__":
    main()
