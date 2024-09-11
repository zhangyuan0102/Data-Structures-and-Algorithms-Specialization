def change(money):
    # write your code here

    return (money // 10) +((money % 10)//5) + ((money % 10)%5)


if __name__ == '__main__':
    m = int(input())
    print(change(m))
