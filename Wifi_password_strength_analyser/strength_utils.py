# strength_utils.py
import string
import math

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)
    
    if charset == 0:
        return 0
    
    return round(len(password) * math.log2(charset), 2)

def classify_strength(entropy):
    if entropy < 30:
        return "Weak"
    elif entropy < 50:
        return "Moderate"
    else:
        return "Strong"
def estimate_crack_time(entropy):
    guesses = 2 ** entropy
    guesses_per_second = 1e9  # Assume a fast attacker (1 billion guesses/sec)
    seconds = guesses / guesses_per_second

    if seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds // 60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds // 86400)} days"
    else:
        return f"{int(seconds // 31536000)} years"
def is_common_password(password):
    with open("common_passwords.txt") as file:
        common = file.read().splitlines()
    return password.lower() in common
