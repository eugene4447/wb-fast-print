import json
import random
from datetime import datetime

# Наборы данных для реалистичности
articles = ["Футболка Oversize", "Худи с принтом", "Джоггеры", "Кепка Logo", "Носки набор", "Платье летнее"]
names = ["Александр П.", "Мария С.", "Дмитрий К.", "Елена В.", "Игорь М."]

def generate_orders():
    # Генерируем от 1 до 3 новых заказов
    new_orders = []
    for _ in range(random.randint(1, 3)):
        order = {
            "id": random.randint(1000000, 9999999),
            "sku": f"WB-{random.randint(1000000000, 9999999999)}",
            "article": random.choice(articles),
            "buyer": random.choice(names),
            "price": f"{random.randint(500, 5000)} ₽",
            "status": "Новый",
            "date": datetime.now().strftime("%d.%m %H:%M")
        }
        new_orders.append(order)
    return new_orders

# Читаем существующие заказы
try:
    with open('orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

# Добавляем новые
data.extend(generate_orders())

# Сохраняем (оставляем последние 20 заказов, чтобы список не бесконечный)
with open('orders.json', 'w', encoding='utf-8') as f:
    json.dump(data[-20:], f, ensure_ascii=False, indent=4)
