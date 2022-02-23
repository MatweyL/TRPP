from random import randint


def main():
    for i in range(randint(1, 10)):
        print((i + randint(11, 21)) * randint(2, 10))
        
if __name__ == "__main__":
    main()
