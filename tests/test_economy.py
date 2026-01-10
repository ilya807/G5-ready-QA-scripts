# Наша бизнес-логика (обычно лежит в приложении, но для практики пишем здесь)
def check_transaction(balance, price):
    """Возвращает новый баланс после покупки или None, если денег мало"""
    if balance >= price:
        return balance - price
    return None

# ТЕСТЫ (Pytest найдет их по префиксу test_)
def test_successful_purchase():
    # Проверка: если баланс 1000, а цена 200, остаток должен быть 800
    new_balance = check_transaction(1000, 200)
    assert new_balance == 800, f"Ожидалось 800, но получили {new_balance}"

def test_insufficient_funds():
    # Проверка: если денег меньше цены, транзакция не должна пройти
    result = check_transaction(50, 100)
    assert result is None, "Транзакция должна вернуть None при нехватке средств"

def test_exact_balance_purchase():
    # Граничное значение: покупка на все деньги
    result = check_transaction(100, 100)
    assert result == 0, "При покупке на всю сумму остаток должен быть 0"
