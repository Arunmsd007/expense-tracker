import datetime

class Expense:
    def __init__(self, amount, category, note=""):
        self.amount = amount
        self.category = category
        self.note = note
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return f"{self.date} | ₹{self.amount} | {self.category} | {self.note}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, note=""):
        expense = Expense(amount, category, note)
        self.expenses.append(expense)
        print("✅ Expense added!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses yet.")
            return
        print("\n📋 All Expenses:")
        for exp in self.expenses:
            print(exp)

    def total_expense(self):
        total = sum(exp.amount for exp in self.expenses)
        print(f"\n💰 Total Spent: ₹{total}")

    def filter_by_category(self, category):
        filtered = [exp for exp in self.expenses if exp.category.lower() == category.lower()]
        if not filtered:
            print("No expenses found in this category.")
            return
        print(f"\n📂 Expenses in '{category}':")
        for exp in filtered:
            print(exp)


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expense")
        print("4. Filter by Category")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category (e.g., Food, Travel): ")
                note = input("Enter note (optional): ")
                tracker.add_expense(amount, category, note)
            except ValueError:
                print("❌ Please enter a valid number!")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.total_expense()
        elif choice == "4":
            category = input("Enter category to filter: ")
            tracker.filter_by_category(category)
        elif choice == "5":
            print("👋 Exiting. Thank you for using Expense Tracker!")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()







