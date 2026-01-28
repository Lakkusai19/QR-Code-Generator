from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

# Ensure the folder for the QR image exists
QR_FOLDER = os.path.join('static', 'qr_codes')
if not os.path.exists(QR_FOLDER):
    os.makedirs(QR_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_filename = None
    if request.method == 'POST':
        link = request.form.get('url')
        if link:
            # Generate the QR Code
            img = qrcode.make(link)
            qr_filename = "last_generated.png"
            img.save(os.path.join(QR_FOLDER, qr_filename))
            
    return render_template('index.html', qr_image=qr_filename)

if __name__ == '__main__':
    app.run(debug=True)