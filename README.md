# Telegram Group Automation Manager

A professional, modular Python script to automate the creation and management of Telegram groups. Features include bulk creation, user/bot invitations, muting, archiving, and sending welcome messages, all with "human-like" safety delays to prevent account bans.

---

## 🚀 Features

- **Multi-Account Support:** Easily switch between different Telegram accounts (profiles) at runtime.
- **Bulk Creation:** Create sequences of groups (e.g., 100-110).
- **Smart Safety Delays:** Randomized sleep timers (10-20s) to mimic human behavior and avoid Flood Waits.
- **Rich Terminal UI:** Beautiful, color-coded output for real-time status tracking.
- **Modular Design:** Clean code structure split into config, core logic, and utilities.

---

## 🛠 Prerequisites

- **Python 3.8+**
- **Telegram API Credentials:** You need an `API_ID` and `API_HASH` for each account you want to use.
- Get them here: [my.telegram.org](https://my.telegram.org)

---

## 📦 Installation

1. **Clone the repository** (or download the files):

```bash
git clone https://github.com/yourusername/telegram-manager.git
cd telegram-manager

```

2. **Install dependencies:**

```bash
pip install -r requirements.txt

```

_(Note: If you don't have a `requirements.txt` yet, install manually: `pip install telethon python-dotenv rich`)_

---

## ⚙️ Configuration

This script uses a `.env` file to store your sensitive credentials securely.

1. Create a file named `.env` in the project root.
2. Add your account details using **Prefixes**.

### Understanding Profile Prefixes (The "User Account Name")

The script asks for a "Profile Name" when it starts. This name corresponds to the **prefix** you use in the `.env` file.

- If you type `ALI`, the script looks for `ALI_API_ID`.
- If you type `WORK`, the script looks for `WORK_API_ID`.

**Example `.env` File:**

```ini
# --- Profile 1: Personal (Prefix: ALI) ---
ALI_API_ID=123756758
ALI_API_HASH=a1b2c994e5f6g7h8i9j0
ALI_PHONE=+201234567890

# --- Profile 2: Work (Prefix: OMAR) ---
OMAR_API_ID=87658821
OMAR_API_HASH=0j9i8h7g6f588d3c2b1a
OMAR_PHONE=+19876543210

# --- General Settings ---
DEFAULT_BOT_USERNAME=x6AzkarBOT

```

---

## 🏃‍♂️ How to Run

1. Start the script:

```bash
python main.py

```

2. **Enter Profile Name:**

- The script will ask: `👤 Enter Profile Name`.
- Type the prefix from your `.env` file (e.g., `ALI` or `OMAR`).
- _Hint: This allows you to manage multiple Telegram accounts from one script without changing code._

3. **Follow the Prompts:**

- Enter Start/End range for group names (e.g., `100` to `105`).
- Choose your options (Mute, Archive, Add Users, etc.).

4. **Login:**

- If it's your first time running a profile, Telegram will ask for your phone number and the login code sent to your app.

---

## ⚠️ Safety Warnings

- **Avoid "Flood Wait":** Do not create too many groups too quickly. The script has built-in delays, but Telegram's limits are strict.
- _Recommendation:_ Run batches of 10-20 groups, then take a break.

- **New Accounts:** Newly created Telegram accounts have very low limits. Use an aged account for best results.
- **Privacy:** Never share your `.env` or `*.session` files. These contain access to your Telegram account.

---

## 📂 Project Structure

- `main.py`: The entry point. Run this file.
- `config.py`: Handles loading credentials from `.env`.
- `core.py`: Contains the logic for processing a single group.
- `utils.py`: Helper functions for inputs and formatting.
- `.env`: **(Hidden)** Stores your API keys. **DO NOT UPLOAD TO GITHUB.**
