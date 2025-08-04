import string

def give_tips(password):
    tips = []
    if len(password) < 12:
        tips.append("Use at least 12 characters.")
    if password.islower() or password.isupper():
        tips.append("Mix uppercase and lowercase letters.")
    if password.isalnum():
        tips.append("Include symbols to increase complexity.")
    if any(p in password.lower() for p in ["123", "admin", "password"]):
        tips.append("Avoid common words like '123', 'admin', or 'password'.")
    
    if not tips:
        tips.append("Great! Your password is strong.")
    
    return tips

# ✅ ADD THIS FUNCTION BELOW
def analyze_complexity(password):
    return {
        "Length": len(password),
        "Has Uppercase": any(c.isupper() for c in password),
        "Has Lowercase": any(c.islower() for c in password),
        "Has Numbers": any(c.isdigit() for c in password),
        "Has Symbols": any(c in string.punctuation for c in password)
    }
