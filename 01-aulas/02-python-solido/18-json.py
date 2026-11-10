import json
from pathlib import Path

current_folder = Path(__file__).resolve().parent # pasta atual
file_path = current_folder / "18-customers.json" # caminho do arquivo

new_customer = {
    "name": "Carlos",
    "age": 22,
    "active": True
}

with open(file_path, "r", encoding="utf-8") as file:
    customers = json.load(file)

customers.append(new_customer)


with open(file_path, "w", encoding="utf-8") as file:
    json.dump(customers, file, indent=4, ensure_ascii=False)

print("Custumer registred successfully!")