

while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n 3. Quit\nPlease enter an option: 1")
    imp = int(input("Please enter your password to encode:"))
    print("Your password has been encoded and stored!")

    def encode(imp):
            temp = []
            for i in range len(imp):
                if imp[i] == 7:
                    imp[i] = 0

                elif imp[i] == 8:
                    imp[i] = 1

                elif imp[i] == 9:
                    imp[i] = 2
                else:
                    imp[i] = imp[i+3]

def __init__== __main__
##