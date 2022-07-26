"""ngoung"""
def main():
    """ngoung"""
    word = input()
    atoz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    revatoz = atoz[::-1]
    for i in word:
        if i.isupper() == True:
            finalword = atoz.lower().index(i)
            print(revatoz.lower()[finalword], end="")
        elif i.islower() == True:
            finalword = atoz.index(i)
            print(revatoz[finalword], end="")
        else:
            print(i, end="")
main()
