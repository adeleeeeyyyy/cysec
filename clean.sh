#!/bin/bash

# Konfigurasi
NUM_LEVELS=5
CTF_DIR="/home/ctf_levels"
VERBOSE=true # Mode verbose

# Fungsi untuk menampilkan pesan saat mode verbose aktif
log() {
    if [ "$VERBOSE" = true ]; then
        echo -e "[INFO] $1"
    fi
}

# Mulai eksekusi script
log "🧹 Memulai proses penghapusan CTF..."

# Hapus user dari level 1 sampai 5
for i in $(seq 1 $NUM_LEVELS); do
    if id "level$i" &>/dev/null; then
        log "👤 Menghapus user level$i..."
        userdel -r "level$i"
    else
        log "⚠️ User level$i tidak ditemukan, melewati..."
    fi
done

# Hapus direktori utama CTF
if [ -d "$CTF_DIR" ]; then
    log "🗑️ Menghapus direktori CTF: $CTF_DIR"
    rm -rf "$CTF_DIR"
else
    log "⚠️ Direktori CTF tidak ditemukan, melewati..."
fi

# Hapus entri di SSH config
log "🛡️ Menghapus konfigurasi SSH terkait CTF..."
sed -i '/AllowUsers level1 level2 level3 level4 level5/d' /etc/ssh/sshd_config
systemctl restart sshd
log "✅ SSH telah dikonfigurasi ulang"

log "🎉 Cleanup selesai! Semua jejak CTF telah dihapus."
