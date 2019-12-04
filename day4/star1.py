from utils import load_input


def is_valid(password: int) -> bool:
    """
    Validate the password based on the following criteria:
    - Must have two adjacent repeating digits
    - Successive digits can never decrease
    """
    password = str(password)
    has_adjacent = False
    for digit in range(1, 6):

        if password[digit] < password[digit-1]:
            return False

        elif password[digit] == password[digit-1]:
            has_adjacent = True

    return has_adjacent


# Calculate total number of valid passwords in the range
lower, upper = load_input(raw=True).split("-")
lower = int(lower)
upper = int(upper)
valid_passwords = 0

for password in range(lower, upper):
    valid_passwords += is_valid(password)

print(valid_passwords)


