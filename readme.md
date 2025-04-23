# Django CAPTCHA

Beautiful and easy-to-integrate CAPTCHA module for Django projects. Protect your forms from spam and bots by generating an image-based code and verifying user input.

---

## 🔹 Features

- Random code generation (letters and digits)
- Background noise lines to thwart OCR
- Simple integration into any Django project
- Session-based code storage
- Easy customization of code length, font, and style

---

## 🚀 Requirements

- Python 3.8+
- Django 3.2+
- Pillow

> Install Pillow with:
> ```bash
> pip install pillow
> ```

---

## 🛠 Installation & Setup

1. **Clone the repository** or copy the files into your project:
   ```bash
   git clone https://github.com/yourusername/django-captcha.git
   cd django-captcha
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🔍 Usage

1. Navigate to the home page (`/`) to view the CAPTCHA form.
2. Enter the code displayed in the image and click **Verify Now**.
3. On successful verification, you’ll be redirected to `/index/` (or your configured next URL).

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request and describe your changes.

---

## 📂 Links

- [Project Repository](https://github.com/yourusername/django-captcha)
- [Website Developer](https://ananas1k.vercel.app)
- [MIT License](LICENSE)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

