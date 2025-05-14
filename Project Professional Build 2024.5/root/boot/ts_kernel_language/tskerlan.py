from ts_kernel_language.grammer.print.print import printtext


def tskerlan():
    print("TS-KERNEL-LANGUAGE COPYRIGHT (C) 2025 TADEO A GONZALEZ") 
    print("           TYPE 'help' FOR COMMANDS                   ")
    print("               TSKERLAN 1.0.0                         ")

    while True:
        user_input = input(">>")

        if user_input == "print":
            printtext()

        elif user_input == "help":
            print("print")
            print(" help")