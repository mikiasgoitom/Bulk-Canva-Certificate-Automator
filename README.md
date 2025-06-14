# 🎓 Canva Certificate Automator

A Python-based automation tool to personalize and email certificates in bulk. Designed for organizers of bootcamps, workshops, and study sessions.

---

## ✨ Features

- 🖨️ Bulk generates personalized certificates from a Canva-designed template
- 📧 Emails each certificate to the appropriate participant
- 🔒 Secure `.env`-based credential storage (no hardcoded secrets)
- 💬 Customizable email message via plain text template
- 📁 Takes in a `.csv` list of recipients with names and emails

---

## 📂 Project Structure

├── fonts/ # Font files used in the certificate  
├── output/ # Generated certificates  
├── certificate_bot/ # Virtual environment (excluded by .gitignore)  
├── cert_template.png # Blank certificate template (exported from Canva)  
├── students.csv # CSV with recipient name and email  
├── email_template.txt # Email body (with {name} placeholder)  
├── generate_certificates.py # Main Python script  
├── .env # Stores email credentials  
├── requirements.txt # Python dependencies  
└── README.md # Documentation (you are here)

---

## 🏁 Getting Started

### 🧩 Step 1: Design Your Certificate in Canva

1. Go to [Canva](https://www.canva.com) and create your certificate design.
2. Use a placeholder like **"Participant Name"** for the name area.
3. Choose a font that’s available on your system or download the font file.
4. Download your certificate as a **PNG file**:
   - Make sure the certificate has a **blank name field** (leave it empty).
   - Export as `cert_template.png`.

### 🧑‍💻 Step 2: Prepare Your Recipient List

Create a `.csv` file named `students.csv` with the following headers:

```csv
name,email
Kenenisa Bekele,kenenisa@example.com
John Doe,john.doe@gmail.com
```

**Note**: You can first write it in Microsoft Excel or Google Spreadsheet then export it as a csv file

## 📨 Step 3: Write Your Email Template

Create a file named `email_template.txt` and write the body of your email. Use `{name}` as a placeholder to personalize each email:

Dear {name},

Congratulations on completing the GDG AASTU 2024–2025 Beginners Track!

Your certificate is attached. Share your success using #GDGAASTU.

Best,  
Mikias Goitom  
GDG AASTU Technical Lead

---

## 🔐 Step 4: Create a `.env` File

In the root directory of your project, create a file named `.env` and add the following:

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password

> 🛡️ **Note**: If you have 2FA enabled on your Gmail, generate an [App Password](https://support.google.com/accounts/answer/185833) to use here.

---

## 🔧 Installation

### ⏬ 1. Clone the Repo

```bash
git clone https://github.com/your-username/canva-cert-automator.git
cd canva-cert-automator
```

### 🐍 2. Create a Virtual Environment

```
python -m venv env
```

#### Activate the environment:

- On Windows:

```
env\Scripts\activate
```

- On macOS/Linux:

```
source env/bin/activate
```

### 📦 3. Install Dependencies

```
pip install -r requirements.txt
```

### 🚀 4. Run the Script

```
python generate_certificates.py
```

## 🖼️ Font + Text Customization

You can adjust the following parameters in generate_certificates.py:

```
font_path = "./fonts/Matangi/static/Matangi-Regular.ttf"
font_size = 75
x, y = 147, 355
draw.text((x, y), name.upper(), fill="#40ad5d", font=font)
```

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests with improvements.

## 💡 Project Motivation

This script was developed for GDG AASTU to automate certificate distribution during the 2024–2025 GDG study session.
It reduced what used to be hours of manual certificate generation and email sending into just a few minutes of automated execution.

## 🔗 Acknowledgements

- Google Developer Groups (GDG)
- Pillow
- Yagmail
