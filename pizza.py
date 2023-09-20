class Pizza:
    def __init__(self, testo, nachinka, souse, cost):
        self.testo = testo
        self.nachinka = nachinka
        self.souse = souse
        self.cost = cost

    def prepare(self):
        print("Приготовить пиццу...")

    def bake(self):
        print("Испечь пиццу...")

    def cut(self):
        print("Нарезать пиццу...")

    def pack(self):
        print("Упаковать пиццу...")

Pepperoni = Pizza("Обычное", "Пепперони", "Томатный", int("50000"))
Barbeku = Pizza("Тонкое тесто", "Курица", "Барбекю", int("70000"))
Sea = Pizza("Обычное", "Креветки", "Сыр", int("100000"))

class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total_cost(self):
        total_cost = 0
        for pizza in self.pizzas:
            total_cost += pizza.cost
        return total_cost

class Terminal:
    def __init__(self):
        self.order = Order()

    def display_menu(self):
        print("Добро пожаловать!")
        print("1. Пицца пепперони")
        print("2. Пицца барбекю")
        print("3. Пицца с морепродуктами")

    def take_order(self):
        while True:
            choice = input("Выберите пиццу: (1, 2, 3, нет)")
            if choice == "1":
                pizza = Pepperoni
                self.order.add_pizza(pizza)
                print("Пепперони пицца добавлена к заказу.")

            elif choice == "2":
                pizza = Barbeku
                self.order.add_pizza(pizza)
                print("Барбекю пицца добавлена к заказу.")

            elif choice == "3":
                pizza = Sea
                self.order.add_pizza(pizza)
                print("Пицца с морепродуктами добавлена к заказу")
            elif choice == "нет":
                print("Заказ собран")
                break
            else:
                print("Ошибка.")

    def confirm_order(self):
        print("Ваш заказ:")
        for index, pizza in enumerate(self.order.pizzas, start=1):
            print(f"{index}. {pizza.testo}, {pizza.souse}, {pizza.nachinka}")
        total_cost = self.order.calculate_total_cost()
        print(f"Общая стоимость: {total_cost} сум")


    def process_payment(self):
        payment_method = input("Выберите способ оплаты: (наличные/карта) ")
        if payment_method.lower() == "наличные":
            print(f"Оплата наличными ")
        elif payment_method.lower() == "карта":
            print(f"Оплата картой")
        else:
            print("Ошибка.")

    def zakaz(self):
        self.display_menu()
        self.take_order()
        self.confirm_order()
        self.process_payment()

a = Terminal()
a.zakaz()

