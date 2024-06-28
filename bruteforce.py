import itertools
import string

def brute_force_attack(password):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for length in range(1, 6):  # Adjust length as needed
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return attempts, guess

password = "abc123"
attempts, guess = brute_force_attack(password)
print(f"Password found: {guess} in {attempts} attempts")
