[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Recommender Systems - Practical Activities

Repo-ul oficial pentru laboratoarele/lucrările practice de **Sisteme de Recomandare**.

## 📚 Structura Laboratoarelor / Labs Index

| Laborator | Tematică / Topic | Ghid (RO) | Guide (EN) |
| :--- | :--- | :---: | :---: |
| **Lab 01** | Colectarea datelor implicite (HTTP & context) | [🇷🇴 Read](lab01/ro/) | 🇬🇧 TBA |
| **Lab 02** | Sistem de recomandare cu Recombee - înregistrare proprietăți | [🇷🇴 Read](lab02/ro/) | 🇬🇧 TBA |
| **Lab 03** | Sistem de recomandare cu Recombee - trimitere items | [🇷🇴 Read](lab03/ro/) | 🇬🇧 TBA |

## 🛠️ Instalare rapidă
```bash
git clone https://github.com/GG-Academy/Recommender-Systems.git
cd Recommender-Systems
```

## ⚙️ Pregătirea mediului de lucru (Recomandat)

Pentru a evita conflictele de dependențe, este recomandat să creați un mediu virtual Python înainte de a instala pachetele.

### 1. Crearea mediului virtual
Deschideți terminalul în directorul proiectului și rulați:

* **Windows:**
```cmd
python -m venv .venv
```

* **macOS / Linux:**
```bash
python3 -m venv .venv
```

### 2. Activarea mediului virtual

* **Windows (Command Prompt):**
```cmd
.venv\Scripts\activate
```

* **Windows (Power Shell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

* **macOS / Linux:**
```bash
source .venv/bin/activate
```

### 3. Instalarea dependențelor

Cu mediul virtual activat, instalați bibliotecile necesare:

```bash
pip install -r requirements.txt
```
