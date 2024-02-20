from main import *

if __name__ == "__main__":
    # Add some medicines
    add_medicine("Aspirin", "Painkiller", 50, date(2024, 6, 1))
    add_medicine("Ibuprofen", "Painkiller", 30, date(2023, 12, 1))
    add_medicine("Amoxicillin", "Antibiotic", 20, date(2024, 3, 1))

    # Add a user
    add_user("user1")

    # Search for medicines
    print("Search results for 'Aspirin':", search_medicines("Aspirin"))

    # Mark a medicine as unavailable
    mark_medicine_unavailable(2)

    # Remove expired medicines
    remove_expired_medicines()

    # Display remaining medicines
    print("Remaining medicines:")
    session = Session()
    for med in session.query(Medicine).all():
        print(med)
    session.close()
