from utils import load_input


def is_valid(password: int) -> bool:
    """
    Validate the password based on the following criteria:
    - Must have two adjacent repeating digits
    - Successive digits can never decrease
    - The two adjacent repeating digits should not be part of a larger group.
    """
    password = str(password)

    for digit in range(1, 6):
        # Check if the password has descending digits
        if password[digit] < password[digit-1]:
            return False

        # Check if we've got double adjacent repeating digits
        elif password[digit] == password[digit-1]:

            # Look behind it. If there are three in a row, it doesn't count.
            if digit > 1 and password[digit] == password[digit-2]:
                pass

            # Look ahead of it. If we've got three in a row, it doesn't count.
            elif digit < 5 and password[digit] == password[digit+1]:
                pass

            # Otherwise, we got an isolated double.
            else:
                return True

    return False


# Calculate total number of valid passwords in the range
lower, upper = load_input(raw=True).split("-")
lower = int(lower)
upper = int(upper)
valid_passwords = 0

for password in range(lower, upper):
    valid_passwords += is_valid(password)

print(valid_passwords)


