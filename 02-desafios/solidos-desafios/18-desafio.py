import json
from pathlib import Path

current_folder = Path(__file__).resolve().parent
file_path = current_folder / "18-customers.json"

with open(file_path, "r", encoding="utf-8") as file:

    try:
        customers = json.load(file)

        if not customers:
            print("No customers registered.")

        else:
            active_count = 0
            inactive_count = 0
            total_age = 0
            oldest_customer = None

            print("=== CUSTOMER REPORT ===")

            for customer in customers:

                status = "Active" if customer["active"] else "Inactive"

                print(
                    f"ID: {customer['id']} | "
                    f"Name: {customer['name']} | "
                    f"Age: {customer['age']} | "
                    f"Status: {status}"
                )

                if customer["active"]:
                    active_count += 1
                else:
                    inactive_count += 1

                if oldest_customer is None or customer["age"] > oldest_customer["age"]:
                    oldest_customer = customer

                total_age += customer["age"]

            average_age = total_age / len(customers)

            print(f"\nActive customers: {active_count}")
            print(f"Inactive customers: {inactive_count}")
            print(f"Average age: {average_age}")
            print(
                f"Oldest customer: {oldest_customer['name']} "
                f"({oldest_customer['age']} years)"
            )

    except json.JSONDecodeError:
        print("Error: invalid or empty JSON file.")