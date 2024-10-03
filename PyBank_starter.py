# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
#file_to_output = os.path.join("Resources", "budget_analysis.txt")  # Output file path

# Initialize variables
changes = []
previous_value = None
total_months = 0
total_net = 0
Avg_change = 0
max_increase = float('-inf')  # Start with the smallest possible value
max_decrease = float('inf')    # Start with the largest possible value
max_increase_month = ""
max_decrease_month = ""

# Function to print appended values
def print_appended_values(values):
    print("Changes in Profits/Losses:")
    for value in values:
        print(value)

# Open and read the CSV
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")
    
    # Skip the header row
    header = next(reader)
    print(f"header: {header}")
    # Process each row of data
    for row in reader:
        total_months += 1
        total_net += float(row[1])

        current_value = float(row[1])

        if previous_value is not None:
            change = current_value - previous_value
            changes.append(change)

            # Check for max increase and decrease
            if change > max_increase:
                max_increase = change
                max_increase_month = row[0]  # Assuming the first column is the month

            if change < max_decrease:
                max_decrease = change
                max_decrease_month = row[0]  # Assuming the first column is the month

        previous_value = current_value  # Update the previous value

# Calculate the average change
if changes:
    Avg_change = sum(changes) / len(changes)

# Print the appended values
#print_appended_values(changes)

# Track the total
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months = {total_months}")
print("-----------------------------")
print(f"Total: {total_net}")
print(f"Average Change = {Avg_change:.2f}")
print("-----------------------------")
print(f"Greatest Increase in Profits: {max_increase} in {max_increase_month}")
print(f"Greatest Decrease in Profits: {max_decrease} in {max_decrease_month}")

# Prepare output text
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"----------------------------\n"
    f"Total: {total_net}\n"
    f"Average Change: {Avg_change:.2f}\n"
    f"----------------------------\n"
    f"Greatest Increase in Profits: {max_increase} in {max_increase_month}\n"
    f"Greatest Decrease in Profits: {max_decrease} in {max_decrease_month}\n"
)

# Write output to a text file
with open(file_to_output, 'w') as txt_file:
    txt_file.write(output)

#print("Financial analysis written to text file.")
print("Values updated to budget_analysis file, Thank you !!")
