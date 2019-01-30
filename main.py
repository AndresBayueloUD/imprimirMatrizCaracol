import lib as lb

def main():
    m = lb.txtToArray(open("matriz.txt").read())
    print(lb.imprimirCaracol(m,0,0))

if __name__ == "__main__":
    main()