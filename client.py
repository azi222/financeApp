# client_info = {"name": "Василий Мурянин",
#                "accounts": [
#                    {"name": "На жизнь",
#                     "system": "MasterCard Mass",
#                     "number": "8888 0000 8888 0000",
#                     "type": "дебетовая",
#                     "balance": 10340,
#                     "validity period": "09/2024"
#                     },
#                    {"name": "Сбережения",
#                     "system": "MIR Classic",
#                     "number": "7777 0000 7777 0000",
#                     "type": "дебетовая",
#                     "balance": 30459,
#                     "validity period": "11/2023"
#                     },
#                ],
#                "transactions": [
#                    {"account": "8888 0000 8888 0000",
#                     "type": "списание",
#                     "date": {"year": 2022, "month": 8},
#                     "amount": 1000},
#                    {"account": "8888 0000 8888 0000",
#                     "type": "списание",
#                     "date": {"year": 2022, "month": 9},
#                     "amount": 500},
#                    {"account": "8888 0000 8888 0000",
#                     "type": "списание",
#                     "date": {"year": 2022, "month": 10},
#                     "amount": 1000},
#                    {"account": "8888 0000 8888 0000",
#                     "type": "зачисление",
#                     "date": {"year": 2022, "month": 10},
#                     "amount": 10000},
#                    {"account": "7777 0000 7777 0000",
#                     "type": "зачисление",
#                     "date": {"year": 2022, "month": 10},
#                     "amount": 5000},
#                ]}
import json

client_info = {}


def load():
    global client_info
    with open('client_info.json', encoding="utf-8") as json_file:
        client_info = json.load(json_file)


def save():
    global client_info
    with open('client_info.json', 'w', encoding="utf-8") as outfile:
        json.dump(client_info, outfile)


def show_info():
    print("Информация о счетах")
    print("----------------------------------")
    for account in client_info["accounts"]:
        print("Имя:", account["name"])
        print("Платёжная система:", account["system"])
        print("Номер:", account["number"])
        print("Тип:", account["type"])
        print("Баланс:", account["balance"])
        print("Срок действия:", account["validity period"])
        print("----------------------------------")


def predict():
    expenses = 0
    income = 0
    months = []

    for transaction in client_info["transactions"]:
        if transaction["type"] == "списание":
            expenses += transaction["amount"]
        if transaction["type"] == "зачисление":
            income += transaction["amount"]

        if transaction["date"] not in months:
            months.append(transaction["date"])

    print("Предполагаемые расходы в следующем месяце:", expenses / len(months))
    print("Предполагаемые доходы в следующем месяце:", income / len(months))


def make_transaction():
    global client_info
    print("Доступные счета:")
    i = 1
    for account in client_info["accounts"]:
        print(i, "-", account["name"], "-", account["number"])
        i += 1

    account_num = int(input("Введите счёт: "))

    for i in range(len(client_info["accounts"])):
        if i + 1 == account_num:
            account = client_info["accounts"][i]["number"]
            break

    else:
        print("Такого аккаунта не существует. Прерываю транзакцию...")
        return

    print("Типы транзакций:")
    print("1 - списание")
    print("2 - зачисление")
    transaction_type = input("Выберите тип транзакции: ")
    if transaction_type == "1":
        transaction_type = "списание"
    elif transaction_type == "2":
        transaction_type = "зачисление"
    else:
        print("Такого типа не существует. Прерываю транзакцию...")
        return

    print("Дата транзакции")
    year = input("Введите год: ")
    month = input("Введите месяц: ")


    if int(year) > 2022 or int(month) > 12 or int(month) < 1:
        print("Неверная дата. Прерываю транзакцию...")
        return

    try:
        amount = int(input("Введите сумму: "))
    except:
        print("Ошибка ввода. Прерываю транзакцию...")
        return

    if amount < 1:
        print("Сумма не может быть меньше 1. Прерываю транзакцию...")
        return

    if transaction_type == "списание":
        client_info["accounts"][account_num-1]["balance"] -= amount
    elif transaction_type == "зачисление":
        client_info["accounts"][account_num-1]["balance"] += amount

    client_info["transactions"].append({"account": account,
                                        "type": transaction_type,
                                        "date": {"year": year, "month": month},
                                        "amount": amount})

    print(client_info['transactions'][-1])
    print("Транзакция записана.")
