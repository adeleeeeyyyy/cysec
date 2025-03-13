#!/bin/bash

# === Konfigurasi Telegram ===
BOT_TOKEN="YOUR_BOT_TOKEN"
CHAT_ID="YOUR_CHAT_ID"
API_URL="https://api.telegram.org/bot$BOT_TOKEN/sendMessage"

# Ambil informasi login
USER=$(whoami)
IP=$(echo $SSH_CONNECTION | awk '{print $1}')
TIME=$(date "+%Y-%m-%d %H:%M:%S")

# Kirim pesan ke Telegram
MESSAGE="🚨 *CTF LOGIN ALERT* 🚨
👤 User: $USER
📍 IP: $IP
⏰ Waktu: $TIME"

# Kirim ke Telegram
curl -s -X POST "$API_URL" -d "chat_id=$CHAT_ID&text=$MESSAGE&parse_mode=Markdown"
