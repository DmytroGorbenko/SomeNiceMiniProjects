import qr


print("Welcome to QRcode encoder and decoder!\n")
while True:
    print("1 - Encode.\n2 - Decode.\n3 - Exit.")
    choice = input("Your choice: ")

    if choice == '1':
        qr.encoder()
    elif choice == '2':
        qr.decoder()
    elif choice == '3':
        print("Thanks! Bye!")
        exit(0)
    else:
        print("Invalid input! Sorry!\n")
