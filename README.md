# app0

Small command-line utility built with **Python**, **Poetry**, and **Typer**.

> Minimal scaffold ready for building CLI tools and helpers.

---

## ✨ Features

- Modern CLI built with **Typer**
- Managed with **Poetry**
- Type-safe arguments and automatic `--help`
- Cross-platform (Windows / macOS / Linux)

---

## 📦 Requirements

- Python **3.11+**
- Poetry **1.6+**

---

## 🧰 Install Poetry

If Poetry is not installed yet, install it using the official installer.

### macOS / Linux / WSL
```bash
$ curl -sSL https://install.python-poetry.org | python3 -
```

### windows:powershell
```bash
$ (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### create virtualenv inside project --optional --recommended
```bash
$ poetry config virtualenvs.in-project true
```

## run command --demo
```bash
$ poetry run app0 demo
```
