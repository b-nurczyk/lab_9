def encode(pas):
    new = []
    for char in pas:
        current_char = int(char) + 3
        if current_char >= 10:
            new.append(str(current_char % 10))
        else:
            new.append(str(current_char))
    return ''.join(new)
def main():
    print("Welcome to the (De/En)coder!")
    print("----------------------------")
    while True:
        choice = input("1. Encode a password\n"
                       "2. Decode a password\n"
                       "What would you like to do? \n")

        if choice == "1":
            pas = input("Enter the password to be encoded: ")
            print(encode(pas))
        elif choice == "2":
            pas = input("Enter the password to be decoded: ")
            print(decode(pas))
        else:
            print("Invalid input!\n")

if __name__ == '__main__':
    main()

