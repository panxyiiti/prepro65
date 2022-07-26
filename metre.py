"""metre"""

def main():
    howlong = float(input())
    if howlong == 0:
        print("No Tape Measure")
    total = 0
    num = input()
    if num != "No more!":
        while True float(num) <= howlong:
            if num != 0:
                total = total+float(num)
            elif num == "No more!":
                break            
main()
