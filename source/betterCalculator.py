import argparse  # from std

#我好帥
#我超帥
# 我好帥


class BetterCalculator:

    @staticmethod
    def Conj(x, y):
        return str(x)+str(y)  # 宇森

    @staticmethod
    def Pow(x, y):
        a = 1
        for i in range(y):
            a = a * x
        return a  # 庭維上傳囉~~~衝翁出衝衝衝

    @staticmethod
    def Mod(x, y):
        t = int(x/y)
        x = x-(y*t)
        return x  # 學姊組

    @staticmethod
    def Add(x, y):
        return x+y

    @staticmethod
    def Minus(x, y):
        return x-y

    @staticmethod
    def Multiple(x, y):
        return x*y
    
    @staticmethod
    def Divide(x, y):
        return x/y

def main():

    # 準備參數解析
    example_text = "example usage: py.exe .\BetterCalculator.py 5 c 3"
    parser = argparse.ArgumentParser(
        description="好一點數學運算功能", epilog=example_text)
    parser.add_argument("x", help="第1個數字",
                        type=int)
    parser.add_argument("operator", help="運算符號:加法(+), 減法(+), 乘法(+), 除法(+), 連接(c),次方(p), 餘數(m)}",
                        type=str)
    parser.add_argument("y", help="第2個數字",
                        type=int)
    args = parser.parse_args()

    if(args.operator == "+"):
        ans = BetterCalculator.Add(args.x, args.y)
    elif(args.operator == "*"):
        ans = BetterCalculator.Multiple(args.x, args.y)
    elif(args.operator == "-"):
        ans = BetterCalculator.Minus(args.x, args.y)
    elif(args.operator == "/"):
        ans = BetterCalculator.Divide(args.x, args.y)
    elif(args.operator == "c"):
        ans = BetterCalculator.Conj(args.x, args.y)
    elif(args.operator == "p"):
        ans = BetterCalculator.Pow(args.x, args.y)
    elif(args.operator == "m"):
        ans = BetterCalculator.Mod(args.x, args.y)
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
