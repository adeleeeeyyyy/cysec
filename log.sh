#!/bin/bash

# Configure your telegram here
BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID="YOUR_CHAT_ID"

# path to log file (can be any log file)
LOG_FILE="/var/log/auth.log"

# log keyword 
KEYWORDS=("Failed password" "Invalid user" "root login")

# push notification to telegram
send_telegram() {
    local message="$1"
    curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
        -d "chat_id=$CHAT_ID&text=$message"
}

# Monitoring latest log
tail -Fn0 "$LOG_FILE" | while read line; do
    for keyword in "${KEYWORDS[@]}"; do
        if [[ "$line" == *"$keyword"* ]]; then
            echo "[!] Alert: $line" | tee -a /var/log/security_alerts.log
            send_telegram "🚨 Security Alert: $line"
        fi
    done
done
