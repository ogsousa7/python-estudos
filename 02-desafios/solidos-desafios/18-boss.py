import json
from pathlib import Path

current_folder = Path(__file__).resolve().parent
file_path = current_folder / "18-customers.json"

def list_customers():
    with open(file_path, "r", encoding="utf-8") as file:
        customers = json.load(file)

        for customer in customers:
            print(f"ID: {customer['id']} | Name: {customer['name']} | age: {customer['age']} | status: {'Active' if customer['active'] else 'Inactive'}")


def register_customer(name, age):
    with open(file_path, "r", encoding="utf-8") as file:
        customers = json.load(file)

        new_id = max(customer["id"] for customer in customers) + 1 if customers else 1 # caso não tenha nenhum cadastrado 

        new_dict = {
            "id": new_id,
            "name": name,
            "age": age,
            "active": True
        }

        customers.append(new_dict)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(customers, file, indent=4, ensure_ascii=False)

    print(f"Customer {name} registred succesfully!")


def update_customer(customer_id):
    with open(file_path, "r", encoding="utf-8") as file:
        customers = json.load(file)
        customer_found = False

        for customer in customers:
            if customer["id"] == customer_id:
                customer_found = True
                print("Customer found!\n")

                print(f"ID: {customer['id']}\n Name: {customer['name']}\n Age: {customer['age']}\n Status: {customer['active']}\n")

                print("What do you want to update?")
                print("1 - Name")
                print("2 - Age")
                print("3 - Status")

                try:
                    update_option = int(input("Choose an option: "))
                except ValueError:
                    print("Invalid option!")
                    return

                if update_option == 1:
                    new_name = input("New name: ").strip().capitalize()

                    if not new_name:
                        print("New name is empty.")
                        return

                    customer['name'] = new_name

                elif update_option == 2:

                    try:
                        new_age = int(input("New age: "))
                    except ValueError:
                        print("Invalid age.")
                        return

                    if new_age <= 0:
                        print("Age must be greater than zero.")
                        return

                    customer['age'] = new_age

                elif update_option == 3:
                    customer['active'] = not customer['active']

                else:
                    print("Invalid option.")
                    return

                break

        if not customer_found:
            print("Customer not found.") 
            return    

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(customers, file, indent=4, ensure_ascii=False)  

    print("Customer updated succesfully!")


def generate_report():
    with open(file_path, "r", encoding="utf-8") as file:
        customers = json.load(file)

    if not customers:
        print("No customers registered.")
        return

    total_customers = len(customers)
    active = 0
    inactive = 0
    total_age = 0
    oldest_customer = None

    for customer in customers:

        if customer['active']:
            active += 1
        else:
            inactive += 1

        if oldest_customer is None or customer['age'] > oldest_customer['age']:
            oldest_customer = customer

        total_age += customer['age']

    average_age = total_age / total_customers

    print(f"\nTotal customers: {total_customers} \nActive customers: {active} \nInactive customers: {inactive} \nAverage age: {average_age:.2f} \nOldest customer: {oldest_customer['name']} {oldest_customer['age']} years\n")

while True:
    print("=== CUSTUMER MANAGEMENT ===\n")
    print("1 - List customers")
    print("2 - Register customer")
    print("3 - Update customer")
    print("4 - Generate report")
    print("5 - Exit\n")

    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if option < 1 or option > 5:
        print("Invalid option. Choose between 1 and 5.")
        continue

    if option == 1:

        list_customers()

    elif option == 2:

        name = input("Name: ").strip()

        if not name:
            print("Plase enter a name.")
            continue

        try:
            age = int(input("Age: "))
        except ValueError:
            print("Invalid age.")
            continue

        if age <= 0:
            print("Age is not greater than zero.")
            continue

        register_customer(name, age)

    elif option == 3:

        try:
            customer_id = int(input("Customer ID: "))
        except ValueError:
            print("ID invalid.")
            continue

        update_customer(customer_id)

    elif option == 4:

        generate_report()

    elif option == 5:

        print("Exiting...")
        break