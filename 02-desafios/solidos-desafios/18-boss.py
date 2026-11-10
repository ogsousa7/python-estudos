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

                update_option = int(input("Choose an option: "))

                if update_option == 1:
                    new_name = input("New name: ").strip().capitalize()
                    customer['name'] = new_name

                elif update_option == 2:
                    new_age = int(input("New age: "))
                    customer['age'] = new_age

                elif update_option == 3:
                    customer['active'] = not customer['active']

                else:
                    print("Invalid option.")

                break

        if not customer_found:
            print("Customer not found.")            

while True:
    print("=== CUSTUMER MANAGEMENT ===\n")
    print("1 - List customers")
    print("2 - Register customer")
    print("3 - Update customer")
    print("4 - Generate report")
    print("5 - Exit\n")

    option = int(input("Choose an option: "))

    if option == 1:

        list_customers()

    elif option == 2:

        name = input("Name: ")
        age = int(input("Age: "))

        register_customer(name, age)

    elif option == 3:

        customer_id = int(input("Customer ID: "))

        update_customer(customer_id)

    elif option == 4:

        pass

    elif option == 5:

        print("Exiting...")
        break