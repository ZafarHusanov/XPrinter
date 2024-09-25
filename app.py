from flask import Flask, request
from win32printing import Printer
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/xprinter', methods=['POST'])
def printer():
    data = request.get_json()
    fontTitle = {
        "height": 10,
    }
    font = {
        "height": 8,
    }
    with Printer(linegap=1) as printer:
        print(data)
        printer.text(text=f"*** {data['company']['name']} ***                          MCHJ", font_config=fontTitle)
        printer.text(text=f"Manzil: {data['company']['address']}", font_config=font)
        printer.text(text=f"STIR: {data['receipt']['stir']}", font_config=font)
        created_at_dt = datetime.strptime(data['receipt']['create_at'], '%Y-%m-%dT%H:%M:%S.%f')
        printer.text(text=f"Sana: {created_at_dt.strftime('%Y-%m-%d %H:%M:%S')}", font_config=font)
        printer.text(text="--------------------------------------------------------", font_config=font)
        count = 1
        for product in data['products']:
            printer.text(
                text=f"{count}. {product['name']}. Narxi: {product['price']}*{product['count']}={product['price'] * product['count']} so'm",
                font_config=font)
            count += 1
        printer.text(text="--------------------------------------------------------", font_config=font)
        printer.text(text=f"Naqd: {data['receipt']['cash_pay']} so'm", font_config=font)
        printer.text(text=f"Karta: {data['receipt']['card_pay']} so'm", font_config=font)
        printer.text(text=f"Jami: {data['receipt']['total']} so'm", font_config=font)
        printer.text(text=f"Qaytim: {data['receipt']['change']} so'm", font_config=font)
        # printer.text("title6", font_config=font)
    return 'Success'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)