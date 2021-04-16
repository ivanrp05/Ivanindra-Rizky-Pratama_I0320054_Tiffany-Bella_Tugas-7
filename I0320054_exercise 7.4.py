print("Praktikum Programa Komputer ")
print("Exercise 7.4")
print("")
print("===========================")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
print("")
def panggil(func):
    return func


def helloworld():
    return 'HELLO WORLD'


def main():
    s = panggil(helloworld())
    print(s)
    if __name__ == '__main__':
        main()