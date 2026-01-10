import pytest

def test_add_item_to_inventory():
    """Тест: Проверка добавления предмета в инвентарь"""
    inventory = ["Healing Potion", "Mana Potion"]
    new_item = "Iron Sword"
    
    inventory.append(new_item)
    
    # Проверяем, что предмет появился в списке
    assert new_item in inventory, f"Предмет {new_item} не добавился в инвентарь"
    # Проверяем общее количество
    assert len(inventory) == 3

def test_inventory_limit():
    """Тест: Проверка, что инвентарь не резиновый (макс. 5 слотов)"""
    inventory = ["Item1", "Item2", "Item3", "Item4", "Item5"]
    max_slots = 5
    extra_item = "Forbidden Scroll"
    
    # Логика: если в инвентаре уже 5 предметов, новый не должен добавиться
    if len(inventory) < max_slots:
        inventory.append(extra_item)
    
    # Проверяем, что размер остался прежним (5), а не стал 6
    assert len(inventory) == max_slots, "Ошибка: Превышен лимит инвентаря!"
    assert extra_item not in inventory, "Ошибка: Лишний предмет попал в полный инвентарь"

