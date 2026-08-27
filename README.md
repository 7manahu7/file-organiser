# 📁 Organise Files

A simple and lightweight CLI tool written in Python that automatically organises files into folders based on their file extensions.

No more digging through a messy `Downloads` directory. Just run the command and let it do the sorting.

## ✨ Features

- 📂 Automatically categorises files
- 🖼️ Sorts images
- 📜 Sorts text and document files
- 💻 Sorts scripts
- 📦 Sorts archives
- ⚡ Simple one-command operation
- 📊 Displays a progress bar while organising
- 📋 Shows a summary of affected files
- 🐍 Written entirely in Python

## 📸 Example

### Before

```text
Downloads/
├── image.png
├── photo.jpg
├── script.py
├── hello.go
├── notes.txt
└── archive.zip
```

### Run

```bash
organise-files
```

### After

```text
Downloads/
├── Images/
│   ├── image.png
│   └── photo.jpg
├── Scripts/
│   ├── script.py
│   └── hello.go
├── Text/
│   └── notes.txt
└── Zips/
    └── archive.zip
```

## 🖥️ Output

The program provides feedback while it works:

```text
-------------------------------------------
moved image.png to the 'Images' directory.
-------------------------------------------

-------------------------------------------
moved script.py to the 'Scripts' directory.
-------------------------------------------

men in work... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ files that were affected                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│                                          │
│ Images                                   │
│                                          │
│ Scripts                                  │
│                                          │
│ Text                                     │
│                                          │
│ image.png                                │
│                                          │
│ script.py                                │
└──────────────────────────────────────────┘
```

## 🛠️ Requirements

- Python 3
- Rich

## 🚀 Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd organise-files
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Make the CLI executable:

```bash
chmod +x organise-files
```

Move it somewhere in your `$PATH`:

```bash
mv organise-files ~/.local/bin/
```

Make sure `~/.local/bin` is included in your `$PATH`.

## ▶️ Usage

Simply run:

```bash
organise-files
```

The program scans your `Downloads` directory and organises files into their corresponding folders.

## 📁 Categories

| Category | File Types |
|----------|------------|
| 🖼️ Images | `.png`, `.jpg`, `.jpeg` |
| 💻 Scripts | `.py`, `.go`, `.sh` |
| 📜 Text | `.txt`, `.md` |
| 📦 Zips | `.zip` |

## 🧠 How It Works

1. Scans the `Downloads` directory.
2. Identifies files based on their extensions.
3. Determines the appropriate category.
4. Creates the required directory if it doesn't exist.
5. Moves the file.
6. Displays information about the operation.
7. Shows a progress bar.
8. Displays a summary of affected files.

## 🔧 Customisation

File extensions and their destination directories can be modified in the source code.

You can easily add new categories or file extensions according to your needs.

Example:

```python
categories = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Scripts": [".py", ".go", ".sh"],
    "Text": [".txt", ".md"],
    "Zips": [".zip", ".tar", ".gz"],
}
```

## 📌 Planned Improvements

- [ ] Command-line arguments for selecting the directory
- [ ] Custom category configuration
- [ ] Better handling of unknown file types
- [ ] Dry-run mode
- [ ] Undo functionality
- [ ] Configuration file
- [ ] Logging
- [ ] More file categories

## 🤝 Contributing

Feel free to open an issue or submit a pull request if you have suggestions, improvements, or bug fixes.

## 📄 License

This project is licensed under the MIT License.
