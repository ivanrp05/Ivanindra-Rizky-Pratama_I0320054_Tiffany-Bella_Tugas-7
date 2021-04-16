print("Praktikum Programa Komputer ")
print("Exercise 7.3")
print("")
print("===========================")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
print("")
import time


def hitungmundur(n):
    li = (n)
    def next():
        r = li(0)
        li[0] -= 1
        return r
    return next


def main():
    next = hitungmundur(3)
    while True :
        val = next()
        if val == 0:
            print('Go!')
            break
        print(val, end='')
        time.sleep(1)
        main()