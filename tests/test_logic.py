import pytest

# ФИКСТУРА: Она "готовит" игру к тесту
@pytest.fixture
def player_with_sword():
    # Представь, что это команда серверу: "Дай игроку меч прямо сейчас"
    inventory = ["Iron Sword"]
    return inventory

def test_sell_sword(player_with_sword):
    """Тест продажи: Нам не важно, как меч появился, мы просто его продаем"""
    inventory = player_with_sword
    item_to_sell = "Iron Sword"
    
    inventory.remove(item_to_sell)
    
    assert item_to_sell not in inventory, "Меч должен был исчезнуть после продажи"
