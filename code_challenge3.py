# Global Freight Calculator

sender_name = input("Sender Name: ")
item_type = input("Type of Item: ")
is_fragile = input("Is Fragile? (True/False): ") == "True"
weight = float(input("Weight (kg): "))
distance = float(input("Distance (km): "))
is_express = input("Express? (True/False): ") == "True"
is_international = input("International? (True/False): ") == "True"

# Step 1: Calculate Base Cost
base_cost = (weight * 2.50) + (distance * 0.15)

# Step 2: Evaluate Pricing Tiers
if weight <= 2.0 and distance <= 100:
    total_cost = 0

elif is_international and is_express:
    total_cost = (base_cost * 1.40) + 50

elif (is_express or is_international) and weight > 20:
    total_cost = (base_cost * 1.20) + 25

elif distance > 1000 or weight > 30:
    total_cost = base_cost + 30

else:
    total_cost = base_cost


print("\n--- Freight Summary ---")
print("Sender:", sender_name)
print("Item:", item_type)
print("Fragile:", is_fragile)
print("Weight:", weight, "kg")
print("Distance:", distance, "km")
print("Express:", is_express)
print("International:", is_international)
print(f"Total Shipping Cost: $", total_cost)
