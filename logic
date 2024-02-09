# Default values
default_visits_per_page = 500
default_conversion_rate = 0.02
default_order_value = 25
default_investment = 7650  # Lower end of the investment scale

# Function to calculate ROI
def calculate_roi(visits_per_page=default_visits_per_page, conversion_rate=default_conversion_rate,
                  order_value=default_order_value, total_investment=default_investment):
    total_visits = visits_per_page * 10  # Assuming 10 pages
    total_conversions = total_visits * conversion_rate
    total_revenue = total_conversions * order_value
    months_to_break_even = total_investment / total_revenue
    roi_multiplier = total_revenue / total_investment
    return roi_multiplier, months_to_break_even

# User inputs (can use input() function for interactivity in a notebook environment)
# Example:
# visits_per_page = int(input("Enter average monthly visits per page (default 500): ") or default_visits_per_page)

# Calculate and display ROI
roi_multiplier, months_to_break_even = calculate_roi()
print(f"ROI Multiplier: {roi_multiplier:.2f}")
print(f"Time to Break Even: {months_to_break_even:.2f} months")
