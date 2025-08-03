# 🗨️ TCP Chat Application

A simple multi-client chat system built with Python using **TCP socket programming** and **multi-threading**.

This project demonstrates core networking concepts, such as TCP/IP communication, port binding, and concurrent client handling — ideal for learning systems fundamentals or distributed communication.

---

## 🚀 Features

- ✅ Real-time message broadcasting to all connected clients
- ✅ Supports multiple clients simultaneously using threads
- ✅ Nickname registration on join
- ✅ Run locally or across devices on the same network (LAN)

---

## 🛠 How to Run

### 1. Clone the Repository


git clone https://github.com/yourusername/tcp-chat-app.git
cd tcp-chat-app

### 2. Run the Server

```bash
python server.py

### 3. Run One or More Clients (each in a separate terminal)

```bash
python client.py

You'll be prompted to enter a nickname for each client.

---

## 🌐 Run Across Devices (LAN)

To test on multiple devices:

1. On the server machine, run `ipconfig` (Windows) or `ifconfig` (Mac/Linux) to get your local IP.
2. Replace `HOST = '127.0.0.1'` with your local IP in both `server.py` and `client.py`.
3. Start the server.
4. Connect from other devices on the same Wi-Fi network.

---

## 📚 Tech Stack

- Python 3
- `socket` – for TCP communication
- `threading` – for handling multiple clients concurrently

---

## 📎 License

MIT – feel free to use and modify.
