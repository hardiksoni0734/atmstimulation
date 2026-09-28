# 🏧 Smart Secure ATM

A Python-based **ATM Management System** that simulates real-world ATM operations with basic security and transaction management.

## ✨ Features

* 🔐 PIN-based authentication
* 🚨 Account lock after 3 incorrect PIN attempts
* 💰 Balance inquiry
* 💵 Cash withdrawal
* 💳 Cash deposit
* 🔑 PIN change
* 📄 Mini statement
* 🔎 Last transaction
* 🛡️ Security status
* 🧾 Transaction receipt generation
* 🔒 OTP verification for withdrawals of ₹5,000 or more

## 💵 Transaction Rules

| Rule                    |   Limit |
| ----------------------- | ------: |
| Starting Balance        | ₹25,000 |
| Daily Withdrawal Limit  | ₹20,000 |
| Single Withdrawal Limit | ₹10,000 |
| Minimum Balance         |  ₹1,000 |
| Maximum PIN Attempts    |       3 |
| OTP Required            | ₹5,000+ |

## 🔄 Withdrawal Process

```text
Enter Amount
     ↓
Validate Amount
     ↓
Check Daily Limit
     ↓
Check Balance
     ↓
Maintain Minimum Balance
     ↓
OTP Verification
     ↓
Update Balance
     ↓
Generate Receipt
```

## 🧩 Main Functions

* `verify()` – PIN verification and account locking
* `cbalance()` – Check balance
* `withdraww()` – Withdraw cash
* `deposit()` – Deposit cash
* `pinchange()` – Change PIN
* `ministate()` – View transaction history
* `lasttrans()` – View last transaction
* `sec_stat()` – View security status
* `receiptgenarate()` – Generate receipt
* `atm_menu()` – Main ATM menu

## 🛠️ Technologies

* **Python 3**
* Functions
* Loops & Conditions
* Lists
* Input Validation
* Basic Security Logic

## 🚀 How to Run

```bash
python atm.py
```

### 🔑 Default Credentials

```text
PIN: 1234
OTP: 5678
```

## 📂 Project Structure

```text
Smart-Secure-ATM/
├── atm.py
└── README.md
```

## ⚠️ Disclaimer

This is an **educational ATM simulation** and does not connect to any real banking system or process real transactions.

## 👨‍💻 Author

**Hardik Soni**
