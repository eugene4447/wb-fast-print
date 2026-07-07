import json
import random
from datetime import datetime

def generate_order():
    # Гарантируем наличие всех полей, чтобы не было 'undefined'
    return {
        "id": random.randint(1000000, 9999999),
        "sku": f"WB-{random.randint(1000000000, 9999999999)}",
        "article": random.choice(["Футболка Oversize", "Худи", "Джоггеры", "Кепка Logo"]),
        "buyer": random.choice(["Иван И.", "Анна С.", "Петр В."]),
        "price": f"{random.randint(500, 5000)} ₽",
        "status": "Новый",
        "date": datetime.now().strftime("%d.%m %H:%M")
    }

# Читаем или создаем список
orders = [generate_order() for _ in range(3)] # Генерируем 3 новых заказа

# Сохраняем в файл
with open('orders.json', 'w', encoding='utf-8') as f:
    json.dump(orders, f, ensure_ascii=False, indent=4)
