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
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate spending amounts and total
    spent_amounts = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_amounts.append(spent)
    total_spent = sum(spent_amounts)

    # Calculate percentages rounded down to nearest 10
    percentages = [(int((amount / total_spent) * 10) * 10) for amount in spent_amounts]

    # Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    # Add the horizontal line
    chart += "    -" + "---" * len(categories) + "\n"

    # Find the longest category name
    max_len = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_len) for category in categories]

    # Build the vertical category name lines
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += f"{name[i]}  "
        chart += "\n"

    return chart.rstrip("\n")  # Remove trailing newline
