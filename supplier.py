

class Supplier:
    def __init__(self, supplier_id, supplier_name, supplier_email):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.supplier_email = supplier_email

    def display_information(self):
        print(f"Supplier ID: {self.supplier_id}")
        print(f"Supplier Name: {self.supplier_name}")
        print(f"Supplier Email: {self.supplier_email}")