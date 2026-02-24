# 🔎 Python TCP Port Scanner

A simple educational TCP port scanner written in Python.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Educational-orange)

---

⚠️ IMPORTANT
This project is for educational purposes only.
Only scan systems you own or have explicit permission to test.

---

## 📌 Overview

This project implements a TCP Connect Port Scanner using Python’s built-in `socket` library.

### ✨ Features

- 🔌 TCP connect scanning
- 📡 Custom port range scanning
- ⏱ Configurable timeout
- ⚡ Multi-threaded scanning
- 🗂 Clean Git project structure
- 📘 Fully documented

---

## 🏗 Project Structure

py-port-scanner/
│
├── scanner.py      # Core scanning logic
├── main.py         # CLI interface
├── .gitignore      # Ignored files
├── README.md       # Documentation
└── .venv/          # Virtual environment (ignored by Git)

---

## ⚙️ How It Works

This scanner performs a TCP Connect Scan:

1️⃣ Creates a TCP socket
2️⃣ Attempts to connect to a target host and port
3️⃣ If the connection succeeds → Port is OPEN
4️⃣ If it fails → Port is CLOSED or FILTERED

💡 This method is simple and detectable (not stealthy).

---

## 🧠 Technologies Used

- 🐍 Python 3
- 🔗 socket (standard library)
- 🧭 argparse (CLI argument parsing)
- ⚡ concurrent.futures (ThreadPoolExecutor)
- 🗃 Git (version control)

No external libraries required.

---

## 🖥 Requirements

- Python 3.10+
- Git installed
- Basic command-line knowledge

---

## 🚀 Setup Instructions

### 1️⃣ Clone or Create the Project

If cloning:

git clone `<your-repo-url>`
cd py-port-scanner

Or manually:

mkdir py-port-scanner
cd py-port-scanner
git init

---

### 2️⃣ Create a Virtual Environment

Windows (PowerShell):

python -m venv .venv
.venv\Scripts\Activate.ps1

macOS/Linux:

python -m venv .venv
source .venv/bin/activate

---

## ▶️ Usage

🔎 Default Scan (Ports 1–1024):

python main.py 127.0.0.1

🎯 Custom Range:

python main.py 127.0.0.1 --ports 1-200

⏱ Custom Timeout:

python main.py 127.0.0.1 --ports 1-200 --timeout 1.0

⚡ Control Thread Workers:

python main.py 127.0.0.1 --ports 1-1024 --workers 100

---

## ⚡ Performance & Threading

Uses ThreadPoolExecutor to:

- 🚀 Scan ports concurrently
- 🛡 Prevent unlimited thread creation
- ⚖ Balance speed and stability

Default workers: 100

⚠ Increasing workers too much can:

- Spike CPU usage
- Trigger firewall limits
- Reduce performance

---

## 🔒 Legal & Ethical Notice

- ❌ Do NOT scan random public IP addresses
- ❌ Do NOT scan networks without authorization
- ⚖ Unauthorized scanning may violate laws and policies
- 🧑‍💻 Always test responsibly in labs or authorized environments

You are responsible for how you use this tool.

---

## 📚 Learning Objectives

This project helps you understand:

- How TCP connections work
- What an “open port” actually means
- How timeouts affect network scanning
- How threading improves performance
- How to structure a Python project properly
- How to use Git professionally

---

## 🚀 Future Improvements

You can extend this project by adding:

- 📊 JSON or CSV export
- 🔍 Service detection (e.g., port 80 → HTTP)
- 🧾 Banner grabbing (advanced)
- 🧪 Unit tests with pytest
- 🌐 IPv6 support
- 🖥 GUI version
- 🔄 GitHub Actions CI

---

## 📜 MIT License

MIT License

Copyright (c) 2026 Mazuba Malambo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


<p align="center">
Built out of curiosity by Mazuba Malambo
</p>


---
