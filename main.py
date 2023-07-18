# Matthew Juranek
def menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")


def encode(original_password):
    encoded_password = ""
    for digit in original_password:
        new_digit = int(digit) + 3
        new_digit = str(new_digit)
        if len(new_digit) > 1:
            new_digit = new_digit[1]
        encoded_password += str(new_digit)
    return encoded_password

def decode(encoded_password):
    decoded_password = ''
      for digit in encoded_password:
        if int(digit) < 3:
          if digit == '2':
            decoded_password += '9'
          if digit == '1':
            decoded_password += '8'
          if digit == '0'
            decoded_password += '7'
        else:
          digit = int(digit) - 3
          decoded_password += str(digit)
  return decoded_password

def main():
    while True:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            original_password = str(input("Please enter your password to encode: "))
            encoded_password = encode(original_password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print('The encoded password is', encoded_password, 'and the original password is', decode(encoded_password) + '.')
            pass
        elif option == 3:
            break


if __name__ == "__main__":
    main()

