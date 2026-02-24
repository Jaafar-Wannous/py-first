# Python Environment Setup with UV

This project demonstrates how to:

- Create a Python virtual environment using UV
- Manage dependencies professionally with `uv add`
- Structure a minimal Python project
- Track changes using Git

---

## Requirements

- Python 3.13+
- UV package manager

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Jaafar-Wannous/py-first.git
cd py-first
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Activate environment

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Run the project

```bash
python main.py
```