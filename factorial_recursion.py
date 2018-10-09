def recur_fac(i):
    if i < 1: # Corner case
        return 1
    else:
        return i * recur_fac(i-1) #recursively calling the same function


def main():
    num = input("Enter number: ")
    print(recur_fac(int(num)))

if __name__ == "__main__":
    main()