# QR-Code-Generator
A sleek full-stack app using Python (Flask) &amp; Bootstrap 5. Converts URLs to QR codes via the qrcode library. Features a colorful Glassmorphism UI with animated CSS gradients.

✨ Features
Real-time Generation: Instant QR code creation using the qrcode library.

Animated UI: Smooth CSS3 background gradients and "pop-in" effects.

Glassmorphism: Frosted glass interface built with Bootstrap 5 and custom CSS.

Fully Responsive: Works perfectly on mobile, tablet, and desktop.

🛠️ Tech Stack
Backend: Python 3.x, Flask

Frontend: HTML5, CSS3, Bootstrap 5

Libraries: qrcode, Pillow (for image processing)

🚀 Quick Start
1. Clone the repository
Bash
git clone https://github.com/YOUR_USERNAME/neon-qr-generator.git
cd neon-qr-generator
2. Install dependencies
Bash
pip install flask qrcode pillow
3. Run the application
Bash
python app.py
4. View in Browser
Open your browser and navigate to: http://127.0.0.1:5000

📂 Project Structure
Plaintext
├── app.py              # Flask Backend Logic
├── static/
│   ├── style.css       # Custom Neon/Glass Styles
│   └── qr_codes/       # Generated QR images
└── templates/
    └── index.html      # Bootstrap Frontend
