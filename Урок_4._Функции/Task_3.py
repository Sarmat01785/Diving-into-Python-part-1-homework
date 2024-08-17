'''
Задача 3

 Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
 Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

def apply_wealth_tax(balance):
    tax_deducted = 0
    if balance > 5000000:
        tax_deducted = balance * 0.1
        balance -= tax_deducted
        print(f"Налог на богатство 10% составил: {tax_deducted:.2f} условных единиц")
    return balance, tax_deducted


def perform_transaction(action, balance, transaction_count, operations):
    try:
        amount = int(input("Введите сумму кратную 50: "))

        if amount % 50 != 0:
            print("Сумма должна быть кратна 50.")
            return balance, transaction_count, operations
        if amount <= 0:
            print("Сумма должна быть положительной.")
            return balance, transaction_count, operations

        if action == "пополнить":
            balance += amount
            transaction_count += 1
            operations.append(f"Пополнение: {amount}")
            print(f"Сумма {amount} успешно пополнена.")

        elif action == "снять":
            commission = max(30, min(600, amount * 0.015))
            if amount + commission <= balance:
                balance -= amount + commission
                transaction_count += 1
                operations.append(f"Снятие: {amount}, комиссия: {commission:.2f}")
                print(f"Сумма {amount} успешно снята. Комиссия: {commission:.2f} условных единиц.")
            else:
                print("Недостаточно средств на счету.")
                return balance, transaction_count, operations

        if transaction_count % 3 == 0:
            interest = balance * 0.03
            balance += interest
            operations.append(f"Начисление процентов: {interest:.2f}")
            print(f"Начислены проценты в размере 3%: {interest:.2f} условных единиц")

    except ValueError:
        print("Пожалуйста, введите целое число.")

    return balance, transaction_count, operations


def main():
    balance = 0
    transaction_count = 0
    operations = []

    while True:
        balance, tax_deducted = apply_wealth_tax(balance)
        if tax_deducted > 0:
            operations.append(f"Налог на богатство: {tax_deducted:.2f}")

        print(f"Текущая сумма на счету: {balance:.2f} условных единиц")

        actions = {"1": "пополнить", "2": "снять", "3": "выйти"}
        action = actions.get(input("Выберите действие (1 - пополнить, 2 - снять, 3 - выйти): "), "3")

        if action in ["пополнить", "снять"]:
            balance, transaction_count, operations = perform_transaction(action, balance, transaction_count, operations)
        elif action == "выйти":
            print(f"Операция завершена. Конечная сумма: {balance:.2f} условных единиц")
            print("Список операций:")
            for operation in operations:
                print(operation)
            break
        else:
            print("Неверная команда. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()