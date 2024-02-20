from models import Session, Medicine, User

# Function to add a new medicine
def add_medicine(name, category, quantity, expiry_date):
    session = Session()
    medicine = Medicine(name=name, category=category, quantity=quantity, expiry_date=expiry_date, available=True)
    session.add(medicine)
    session.commit()
    session.close()

# Function to update an existing medicine
def update_medicine(medicine_id, **kwargs):
    session = Session()
    medicine = session.query(Medicine).get(medicine_id)
    if medicine:
        for key, value in kwargs.items():
            setattr(medicine, key, value)
        session.commit()
    session.close()

# Function to remove a medicine
def remove_medicine(medicine_id):
    session = Session()
    medicine = session.query(Medicine).get(medicine_id)
    if medicine:
        session.delete(medicine)
        session.commit()
    session.close()

# Function to add a new user
def add_user(username):
    session = Session()
    user = User(username=username)
    session.add(user)
    session.commit()
    session.close()

# Function to remove a user
def remove_user(user_id):
    session = Session()
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
    session.close()

# Function to search medicines by name or category
def search_medicines(search_term):
    session = Session()
    medicines = session.query(Medicine).filter(Medicine.name.ilike(f'%{search_term}%') | Medicine.category.ilike(f'%{search_term}%')).all()
    session.close()
    return medicines

# Function to mark medicine as available
def mark_medicine_available(medicine_id):
    update_medicine(medicine_id, available=True)

# Function to mark medicine as unavailable
def mark_medicine_unavailable(medicine_id):
    update_medicine(medicine_id, available=False)

# Function to remove expired medicines
def remove_expired_medicines():
    session = Session()
    expired_medicines = session.query(Medicine).filter(Medicine.expiry_date < date.today()).all()
    for medicine in expired_medicines:
        remove_medicine(medicine.id)
    session.close()

# Example usage
if __name__ == "__main__":
    add_medicine("Paracetamol", "Painkiller", 100, date(2024, 6, 1))
    add_medicine("Amoxicillin", "Antibiotic", 50, date(2023, 12, 1))
    print(search_medicines("Paracetamol"))
    remove_medicine(2)
