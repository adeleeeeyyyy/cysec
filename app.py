import string
import math
from flask import Flask, request, render_template, send_file
import random


app = Flask(__name__)


def generate_password(length=12):
    # Membuat kumpulan karakter yang bisa digunakan dalam password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Mengacak karakter-karakter tersebut
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password



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

@app.route('/generate', methods=['POST'])
def generate():
    generated_password = generate_password(16)
    return render_template('index.html', generated_password=generated_password)



if __name__ == '__main__':
    app.run(port=5678)

# Contoh penggunaan
#password = input("Enter a password to check: ")
#strength, time_to_crack = check_password_strength(password)
#print(f"Password Strength: {strength}")
#print(f"Estimated Time to Crack: {time_to_crack}")
