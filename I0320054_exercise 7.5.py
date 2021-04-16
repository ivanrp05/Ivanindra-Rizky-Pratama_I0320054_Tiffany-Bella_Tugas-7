print("Praktikum Programa Komputer ")
print("Exercise 7.5")
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
    daftarnama = ['Adi', 'Cahyo', 'budi', 'Dedi']
    print('keadaan awal')
    print(daftarnama)

    print('\nmenggunakan sorted():')
    print(sorted(daftarnama))

    daftarnama.sort(key=lambda n: n.lower())

    print('\nkeadaan akhir')
    print(daftarnama)
if __name__ == '__main__':
    main()
