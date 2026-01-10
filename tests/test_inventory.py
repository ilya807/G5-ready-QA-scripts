def test_check_magic_crystal_inventory():
    """Тест проверяет наличие и количество Магических Кристаллов в инвентаре"""
    
    # Имитация данных от сервера (API response)
    inventory_items = [
        {"name": "Health Potion", "count": 5},
        {"name": "Magic Crystal", "count": 12},
        {"name": "Gold Coin", "count": 100}
    ]
    
    crystal_found = False
    
    for item in inventory_items:
        if item["name"] == "Magic Crystal":
            crystal_found = True
            # Проверяем, что кристаллов не меньше 10
            assert item["count"] >= 10, f"Ошибка: Кристаллов всего {item['count']}, а нужно минимум 10!"
    
    # Проверяем, что предмет вообще был найден в списке
    assert crystal_found == True, "Ошибка: Magic Crystal не найден в инвентаре"

if __name__ == "__main__":
    test_check_magic_crystal_inventory()
    print("Тест инвентаря пройден успешно!")
