import string

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_character, index):
        self._illegal_character = illegal_character
        self._index = index

    def __str__(self):
        return f"The username contains an illegal character '{self._illegal_character}' at index {self._index}"

class UsernameTooShort(Exception):
    def __str__(self):
        return "Username is too short"

class UsernameTooLong(Exception):
    def __str__(self):
        return "Username is too long"

class PasswordMissingCharacter(Exception):
    def __str__(self):
        return f"Password is missing a required character"

class PasswordTooShort(Exception):
    def __str__(self):
        return "Password is too short"

class PasswordTooLong(Exception):
    def __str__(self):
        return "Password is too long"
    
class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"

def check_input(username, password):
    illegal_chars = [char for char in username if not (char.isalnum() or char == "_")]
    if len(illegal_chars) > 0:
        raise UsernameContainsIllegalCharacter(illegal_chars[0], username.index(illegal_chars[0]))
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()
    
    if not any(char in string.ascii_uppercase for char in password):
        raise PasswordMissingUppercase()
    elif not any(char in string.ascii_lowercase for char in password):
        raise PasswordMissingLowercase()
    elif not any(char in string.digits for char in password):
        raise PasswordMissingDigit()
    elif not any(char in string.punctuation for char in password):
        raise PasswordMissingSpecial()
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()

try:
    check_input("A_a1.", "4BCD3F6.1jk1mn0p")
    print("OK")
except Exception as e:
    print(e)
