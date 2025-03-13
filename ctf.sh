#!/bin/bash

# === Konfigurasi ===
NUM_LEVELS=5
BASE_PASSWORD="ctf3344"
CTF_DIR="/home/ctf_levels"

# Konfigurasi Telegram
BOT_TOKEN="YOUR_BOT_TOKEN"
CHAT_ID="YOUR_CHAT_ID"
API_URL="https://api.telegram.org/bot$BOT_TOKEN/sendMessage"

# Fungsi untuk log proses
log() {
    echo -e "[INFO] $1"
}

# Buat direktori CTF
log "📁 Membuat direktori CTF..."
mkdir -p "$CTF_DIR"
chmod 755 "$CTF_DIR"

# Fungsi untuk membuat user level
create_user() {
    local LEVEL=$1
    local PASSWORD=$2
    local HOME_DIR="$CTF_DIR/level$LEVEL"

    log "👤 Membuat user: level$LEVEL"
    
    # Pastikan user belum ada sebelum dibuat
    if id "level$LEVEL" &>/dev/null; then
        log "⚠️ User level$LEVEL sudah ada, melewati..."
    else
        useradd -m -d "$HOME_DIR" -s /bin/bash "level$LEVEL"
        echo "level$LEVEL:$PASSWORD" | chpasswd
    fi

    # Batasi akses direktori
    chmod 550 "$HOME_DIR"
    chown root:"level$LEVEL" "$HOME_DIR"

    # Tambahkan script log Telegram ke .bashrc
    log "📡 Menambahkan logging Telegram untuk level$LEVEL"
    echo 'bash /home/ctf_levels/log_telegram.sh' >> "$HOME_DIR/.bashrc"

    # Batasi perintah yang bisa digunakan (whitelist)
    echo "PATH=/usr/bin:/bin" >> "$HOME_DIR/.bashrc"
}

# Buat user level pertama
create_user 1 "$BASE_PASSWORD"

# Loop untuk membuat level 2 - 5
PREV_PASSWORD="$BASE_PASSWORD"
for i in $(seq 2 $NUM_LEVELS); do
    NEXT_PASSWORD=$(openssl rand -base64 12)
    HOME_DIR="$CTF_DIR/level$((i-1))"

    # Simpan flag ke level sebelumnya
    echo "$NEXT_PASSWORD" > "$HOME_DIR/flag.txt"
    chmod 444 "$HOME_DIR/flag.txt"
    chown root:level$((i-1)) "$HOME_DIR/flag.txt"

    create_user $i "$NEXT_PASSWORD"
    PREV_PASSWORD="$NEXT_PASSWORD"
done

# === Hardening SSH ===
log "🛡️ Mengamankan SSH..."
echo "PermitRootLogin no" >> /etc/ssh/sshd_config
echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
echo "AllowUsers level1 level2 level3 level4 level5" >> /etc/ssh/sshd_config
systemctl restart sshd
log "✅ SSH dikonfigurasi ulang"

log "🎉 CTF Setup Selesai!"
log "🔑 Login dengan user level1 dan password: $BASE_PASSWORD"
