import random

class PersonalFinanceAgent:
    def __init__(self, monthly_income, savings_goal, current_savings):
        self.monthly_income = monthly_income
        self.savings_goal = savings_goal
        self.current_savings = current_savings
        self.expenses = []

    def track_expenses(self):
        # Clear previous expenses and simulate between 5 to 15 expense transactions.
        self.expenses = []
        categories = ["Food", "Transport", "Entertainment", "Utilities", "Others"]
        for _ in range(random.randint(5, 15)):
            category = random.choice(categories)
            amount = round(random.uniform(10, 100), 2)
            self.expenses.append((category, amount))
            
    def summarize_expenses(self):
        return sum(amount for _, amount in self.expenses)
    
    def provide_budgeting_suggestions(self):
        total_expenses = self.summarize_expenses()
        disposable_income = self.monthly_income - total_expenses
        if disposable_income < 0:
            suggestion = "Your expenses exceed your income. Consider cutting down non-essential spending."
        elif disposable_income < 0.1 * self.monthly_income:
            suggestion = "Your disposable income is low. Try reducing expenses to free up more savings."
        else:
            suggestion = "Your budget looks good. Keep tracking your expenses and maintain your spending habits."
        return suggestion, disposable_income
    
    def recommend_savings(self):
        total_expenses = self.summarize_expenses()
        disposable_income = self.monthly_income - total_expenses
        if self.current_savings < self.savings_goal:
            recommended_saving = 0.2 * self.monthly_income
            if recommended_saving > disposable_income:
                recommended_saving = disposable_income * 0.8
            suggestion = f"Consider saving at least ${recommended_saving:.2f} this month."
        else:
            suggestion = "You are on track with your savings goal!"
        return suggestion

    def run(self):
        self.track_expenses()
        print("Expense Report:")
        for category, amount in self.expenses:
            print(f"  {category}: ${amount:.2f}")
        total_expenses = self.summarize_expenses()
        print(f"Total Expenses: ${total_expenses:.2f}")
        suggestion, disposable_income = self.provide_budgeting_suggestions()
        print(suggestion)
        print(f"Disposable Income: ${disposable_income:.2f}")
        savings_suggestion = self.recommend_savings()
        print(savings_suggestion)
        print("===")

# Run the agent 5 times, simulating different financial conditions
for i in range(5):
    print(f"--- Run {i+1} ---")
    # Randomize current savings for each run (within a reasonable range)
    current_savings = random.randint(200, 1200)
    agent = PersonalFinanceAgent(monthly_income=3000, savings_goal=1000, current_savings=current_savings)
    agent.run()
