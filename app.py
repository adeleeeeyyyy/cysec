import string
import math
from flask import Flask, request, render_template, send_file

app = Flask(__name__)

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    char_set = 0
    if has_upper:
        char_set += 26
    if has_lower:
        char_set += 26
    if has_digit:
        char_set += 10
    if has_special:
        char_set += len(string.punctuation)
    
    combinations = char_set ** length
    hash_per_second = 1e9
    
    seconds_to_crack = combinations / hash_per_second
    time_to_crack = convert_time(seconds_to_crack)
    
    strength = "Weak"
    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif length >= 6 and (has_upper or has_lower) and has_digit:
        strength = "Moderate"
    
    return strength, time_to_crack

def convert_time(seconds):
    periods = [
        ('year', 60 * 60 * 24 * 365),
        ('month', 60 * 60 * 24 * 30),
        ('day', 60 * 60 * 24),
        ('hour', 60 * 60),
        ('minute', 60),
        ('second', 1)
    ]
    
    time_str = ""
    
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            time_str += f"{int(period_value)} {period_name}{'s' if period_value > 1 else ''} "
    
    return time_str.strip()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert():
    password = request.form['passwordinput']
    strength, time_to_crack = check_password_strength(password)
    return render_template('index.html', password=password, strength=strength, time_to_crack=time_to_crack)

if __name__ == '__main__':
    app.run(debug=True)

# Contoh penggunaan
#password = input("Enter a password to check: ")
#strength, time_to_crack = check_password_strength(password)
#print(f"Password Strength: {strength}")
#print(f"Estimated Time to Crack: {time_to_crack}")
