import toss, time

def main():
    name = input("입금자명: ")
    amount = input("입금액: ")

    ok = input("입금 완료 후 아무키나 눌러요")
    time.sleep(2)

    res = toss.check(name.strip(), int(amount))
    print(res)

if __name__ == "__main__":
    main()