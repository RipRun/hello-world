def main():
    print("Hello world")
    name = input("What is your name? ")
    print("Hello {}!".format(name))
    x = 10
    print(x)
    number = int(input("Give me a number: "))
    if number > 10:
        print("{} is greater than 10".format(str(number)))
    elif number < 10:
        print("{} is less than 10".format(str(number)))
    else:
        print("{} is equal to 10".format(str(number)))
    my_list = [1, 2, 3, 4, 5]
    for e in my_list:
        print(e)
    import random
    lister = []
    for i in range(10):
        lister.append(random.randint(1, 100))
    num = int(input("Enter a number: "))
    count = 0
    for e in lister:
        if e < num:
            count += 1
    print(str(count))

    def take_average():
        print("average")
    take_average()
    z = "stop"
    if z == "stop":
        print("ok")


if __name__ == "__main__":
    main()
