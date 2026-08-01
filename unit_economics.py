import math

import matplotlib.pyplot as plt


def unit_economics(
    price,
    variable_cost=40,
    fixed_cost=3000,
    trolleys=25
):
    contribution_per_trolley = price - variable_cost

    monthly_profit = (
        trolleys * contribution_per_trolley
    ) - fixed_cost

    break_even_exact = fixed_cost / contribution_per_trolley
    break_even_trolley = math.ceil(break_even_exact)

    return {
        "price": price,
        "contribution": contribution_per_trolley,
        "profit": round(monthly_profit, 2),
        "break_even": round(break_even_trolley, 1)
    }


# £200, £250 and £300 are the required price tiers.
# £150 is included as a comparison floor.
prices = [150, 200, 250, 300]

results = []

print("SMART TROLLEY UNIT ECONOMICS")
print("-" * 72)

print(
    f"{'Price':<12}"
    f"{'Contribution':<18}"
    f"{'Profit':<16}"
    f"{'Break-even':<15}"
)

print("-" * 72)

for price in prices:
    result = unit_economics(price)
    results.append(result)

    print(
        f"£{result['price']:<11}"
        f"£{result['contribution']:<17}"
        f"£{result['profit']:<15,.2f}"
        f"{result['break_even']:<15}"
    )


# Prepare data for the graph
chart_prices = [
    result["price"]
    for result in results
]

chart_profits = [
    result["profit"]
    for result in results
]


# Create the profit-versus-price graph
plt.figure(figsize=(8, 5))

plt.plot(
    chart_prices,
    chart_profits,
    marker="o"
)

# Show the break-even profit line
plt.axhline(
    y=0,
    linestyle="--",
    label="Break-even profit"
)

plt.title(
    "Smart Trolley Pilot: Monthly Profit vs Price"
)

plt.xlabel(
    "Price per trolley per month (£)"
)

plt.ylabel(
    "Monthly profit for 25 trolleys (£)"
)

plt.xticks(chart_prices)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the chart in the project folder
plt.savefig(
    "profit_vs_price.png",
    dpi=300
)

# Display the chart
plt.show()