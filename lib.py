def txtToArray(txt):
    if isinstance(txt, str):
        return txtToArray(txt.split("\n"))
    if isinstance(txt, list):
        if len(txt) > 1:
            return [list(map(int, txt[0].split(" ")))] + txtToArray(txt[1:])
        else:
            return [list(map(int, txt[0].split(" ")))]

def imprimirCaracol(matriz, x, y):
    if x==0 and y<(len(matriz[x])-1):
        return str(matriz[x][y]) + "," + imprimirCaracol(matriz, x, y + 1)
    print(len(matriz)-1)
    if y==(len(matriz[x])-1) and x<(len(matriz)-1):
        return str(matriz[x][y]) + "," + imprimirCaracol(matriz, x + 1, y)
    return "."
