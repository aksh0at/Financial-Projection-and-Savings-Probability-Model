import numpy as np
import matplotlib.pyplot as plt

# Constants
monthly_income = 50000  # Monthly income in ₹
annual_income = monthly_income * 12  # Annual income
healthcare_percentage = 0.1  # Assume 10% of income goes to healthcare
monthly_healthcare = monthly_income * healthcare_percentage

# Input monthly spending for one year
spending_per_month = []
for month in range(1, 13):
    spending = float(input(f"Enter spending amount for month {month} in ₹: "))
    spending_per_month.append(spending)

# Average spending and inflation/investment rates
average_monthly_spending = np.mean(spending_per_month)
years = 5  # Duration in years for projections
inflation_rate = 0.05  # Annual inflation rate
investment_growth_rate = 0.08  # Expected annual return on investments

# Normal Calculation for Savings and Investment Growth Over 5 Years
normal_savings = []
normal_investment_values = []
total_savings = 0

for year in range(1, years + 1):
    # Adjust spending and healthcare with inflation
    adjusted_spending = average_monthly_spending * (1 + inflation_rate) ** year
    adjusted_healthcare = monthly_healthcare * (1 + inflation_rate) ** year
    annual_savings = (monthly_income * 12) - (adjusted_spending * 12) - adjusted_healthcare
    total_savings += annual_savings
    investment_value = total_savings * (1 + investment_growth_rate) ** year

    normal_savings.append(total_savings)
    normal_investment_values.append(investment_value)

# Probabilistic Simulation (Monte Carlo) for Savings and Investment Growth
simulations = 1000  # Number of simulations
probabilistic_savings = []

for simulation in range(simulations):
    total_savings_sim = 0
    for year in range(1, years + 1):
        # Randomized annual spending, inflation, and investment growth
        rand_spending = average_monthly_spending * (1 + np.random.normal(inflation_rate, 0.02)) ** year
        rand_healthcare = monthly_healthcare * (1 + np.random.normal(inflation_rate, 0.02)) ** year
        rand_growth_rate = np.random.normal(investment_growth_rate, 0.02)
        
        # Calculate savings and investment for the simulated path
        annual_savings_sim = (monthly_income * 12) - (rand_spending * 12) - rand_healthcare
        total_savings_sim += annual_savings_sim
        investment_value_sim = total_savings_sim * (1 + rand_growth_rate) ** year
        
    probabilistic_savings.append(investment_value_sim)

# Get average probabilistic savings for each year
average_prob_savings = np.mean(probabilistic_savings)

# Print normal calculation results
print("\nNormal Savings and Investment Growth Over 5 Years")
for year, (savings, investment) in enumerate(zip(normal_savings, normal_investment_values), start=1):
    print(f"Year {year}: Total Savings: ₹{savings:.2f}, Investment Value: ₹{investment:.2f}")

# Print probabilistic average results
print("\nAverage Investment Value Over 5 Years (Probabilistic Model)")
print(f"Average Investment Value after 5 years: ₹{average_prob_savings:.2f}")

# Suggestions based on total investment value after 5 years (normal calculation)
total_investment_value_5_years = normal_investment_values[-1]  # Final investment value after 5 years
suggestions = {
    "car": 600000,         # Example cost of a mid-range car
    "bike": 100000,        # Example cost of a motorbike
    "vacation": 200000,    # Example cost of a vacation
    "home_downpayment": 1000000  # Example cost of a down payment for a home
}

print("\nAfter 5 years, the person could consider buying:")
for item, cost in suggestions.items():
    if total_investment_value_5_years >= cost:
        print(f"- {item.capitalize()} (Cost: ₹{cost})")

# Healthcare emergency fund recommendation
healthcare_emergency_fund = total_investment_value_5_years * 0.2
print(f"\nRecommended Healthcare Emergency Fund: ₹{healthcare_emergency_fund:.2f}")

# Plotting
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Normal Savings Plot
axs[0].bar(range(1, years + 1), normal_investment_values, color='blue', alpha=0.7)
axs[0].set_title("Normal Savings & Investment Growth Over 5 Years")
axs[0].set_xlabel("Year")
axs[0].set_ylabel("Investment Value in ₹")
axs[0].set_xticks(range(1, years + 1))
axs[0].grid(axis="y", linestyle="--", alpha=0.6)

# Probabilistic Savings Plot
axs[1].bar(range(1, years + 1), [average_prob_savings] * years, color='green', alpha=0.7)
axs[1].set_title("Probabilistic Savings & Investment Growth Over 5 Years")
axs[1].set_xlabel("Year")
axs[1].set_ylabel("Average Investment Value in ₹")
axs[1].set_xticks(range(1, years + 1))
axs[1].grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()
