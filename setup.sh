#!/bin/bash

# Cập nhật và nâng cấp gói
apt update -y
apt upgrade -y

# Chạy termux-change-repo và chọn mặc định (nhấn Enter 2 lần)
termux-change-repo

# Cài đặt Python
apt install python -y

# Cập nhật lại hệ thống
apt update -y
apt upgrade -y

# Tải script Main.py từ GitHub
curl -L -o ~/Main.py https://raw.githubusercontent.com/ndamod/GolikeToolThread/main/Main.py

# Cấu hình Termux tự động chạy Python script khi mở Termux
echo 'python ~/Main.py' >> ~/.bashrc
