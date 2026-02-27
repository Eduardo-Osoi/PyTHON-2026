class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        # Línea de título con nombre centrado entre asteriscos
        title = self.name.center(30, "*") + "\n"
        
        # Lista de transacciones
        items = ""
        for item in self.ledger:
            # Descripción: hasta 23 caracteres
            description = item["description"][:23]
            
            # Cantidad: formateada con 2 decimales, máximo 7 caracteres
            amount = f"{item['amount']:.2f}"
            
            # Espaciado entre descripción y cantidad
            items += f"{description:<23}{amount:>7}\n"
        
        # Línea total
        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total


def create_spend_chart(categories):
    # Título del gráfico
    result = "Percentage spent by category\n"
    
    # Calcular retiros totales por categoría
    withdrawals = []
    category_names = []
    total_withdrawals = 0
    
    for category in categories:
        category_names.append(category.name)
        category_withdrawals = 0
        for item in category.ledger:
            if item["amount"] < 0:  # Solo retiros (números negativos)
                category_withdrawals += abs(item["amount"])
        withdrawals.append(category_withdrawals)
        total_withdrawals += category_withdrawals
    
    # Calcular porcentajes (redondeados hacia abajo al 10 más cercano)
    percentages = []
    if total_withdrawals > 0:
        for w in withdrawals:
            percentage = int((w / total_withdrawals) * 100)
            # Redondear hacia abajo al 10 más cercano
            percentage = (percentage // 10) * 10
            percentages.append(percentage)
    else:
        percentages = [0] * len(categories)
    
    # Construir el gráfico de barras (de 100 a 0)
    for i in range(100, -1, -10):
        line = f"{i:3}| "
        for percentage in percentages:
            if percentage >= i:
                line += "o  "
            else:
                line += "   "
        result += line + "\n"
    
    # Línea horizontal - con el espaciado correcto
    result += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Nombres de categorías verticalmente
    # Encontrar la longitud máxima del nombre
    max_name_length = max(len(name) for name in category_names)
    
    # Escribir cada letra verticalmente
    for i in range(max_name_length):
        line = "     "
        for name in category_names:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        # Eliminar espacios extras al final pero mantener la longitud consistente
        result += line + "\n"
    
    # Eliminar el último carácter de nueva línea
    return result.rstrip("\n")