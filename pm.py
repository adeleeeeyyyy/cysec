def generate_password(length=12):
    # Membuat kumpulan karakter yang bisa digunakan dalam password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Mengacak karakter-karakter tersebut
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Menjalankan fungsi dan mencetak hasilnya
password = generate_password(16)
print("Generated Password:", password)
