def test_shop_prices():
    # Словарь: Название товара и его цена
    shop_items = {
        "Small Health Pack": 100,
        "Mega Sword": 5000,
        "Free Gift": 0,
        "Premium Skin": -10 # ОШИБКА: Цена не может быть отрицательной
    }

    for item, price in shop_items.items():
        # Проверяем, что цена каждого товара 0 или больше
        assert price >= 0, f"Ошибка в товаре '{item}': цена {price} ниже нуля!"
