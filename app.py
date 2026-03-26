from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    shop_info = {
        "name": "HAMER SHOP",
        "city": "Апостолове",
        "tg": "@hamer_manager"
    }
    
    products = [
        {"id": 1, "name": "Nike Air Monarch", "price": 2990, "old": 3500, "desc": "Біла класика", "img": "p1.webp", "hot": True},
        {"name": "Nike Shox TL", "price": 3390, "old": 4200, "desc": "Агресивний дизайн", "img": "p2.webp", "hot": True},
        {"name": "Mizuno Wave Rider", "price": 3629, "old": 4100, "desc": "Японська якість", "img": "p3.webp", "hot": False},
        {"name": "Hamer Exclusive", "price": 4500, "old": 5500, "desc": "Тільки в Апостолове", "img": "banner.jpg", "hot": False}
    ]
    
    return render_template('index.html', info=shop_info, products=products)

if __name__ == '__main__':
    app.run(debug=True)
