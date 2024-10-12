import random
import time

# Function to generate a 6-digit OTP for secure missile checkout
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to verify an OTP
def verify_otp(otp, entered_otp):
    return otp == entered_otp

# Function to check missile availability in the inventory
def check_missile_availability(inventory, missile_name):
    if missile_name in inventory:
        return inventory[missile_name]
    return None

# Function to get the original location of the missile
def get_original_location(missile_name):
    locations = {
        "BrahMos": "INS Vikramaditya, Mumbai",
        "Astra": "AFS Jodhpur",
        "MICA": "AFS Ambala",
        "Python": "AFS Gorakhpur",
        "Harpoon": "INS Chennai"
    }
    return locations.get(missile_name, "Unknown Location")

# Function to checkout a missile from the inventory
def checkout_missile(inventory, missile_name):
    if missile_name in inventory and inventory[missile_name] > 0:
        otp = generate_otp()
        print(f"OTP displayed on deck monitor: {otp}")

        entered_otp = input("Enter the OTP: ")
        
        if verify_otp(otp, entered_otp):
            coordinates = input("Enter the launch coordinates (latitude and longitude): ")
            reason = input("Enter the reason to launch (Enemy Attack, Trial, Self Defense): ")
            inventory[missile_name] -= 1
            print(f"Launching {missile_name} at coordinates: {coordinates}")
            print(f"Original Location of {missile_name}: {get_original_location(missile_name)}")
            print(f"{missile_name} checked out successfully. Remaining stock: {inventory[missile_name]}")
            print(f"Launch Reason: {reason}")
            print(f"Checkout Time: {time.strftime('%H:%M:%S')}")
        else:
            print("Incorrect OTP! Missile checkout failed.")
    else:
        print(f"{missile_name} is out of stock or not found in the inventory!")

# Function to return a missile to the inventory
def return_missile(inventory, missile_name):
    if missile_name in inventory:
        inventory[missile_name] += 1
        print(f"{missile_name} returned successfully. Updated stock: {inventory[missile_name]}")
    else:
        print("Missile not found in the inventory!")

def main():
    missile_inventory = {
        "BrahMos": 10,
        "Astra": 5,
        "MICA": 15,
        "Python": 8,
        "Harpoon": 3
    }

    print("Welcome to the Indian Air Force Missile Management System.")
    captain_password = "captain123"  # Password for captain access

    while True:
        print("\n1. Check Missile Availability")
        print("2. Checkout Missile")
        print("3. Return Missile")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            missile_name = input("Enter the name of the missile to check availability: ")
            availability = check_missile_availability(missile_inventory, missile_name)
            if availability is not None:
                print(f"{missile_name} is available. Stock: {availability}")
                print(f"Original Location of {missile_name}: {get_original_location(missile_name)}")
            else:
                print("Missile not found in the inventory!")

        elif choice == 2:
            entered_password = input("Enter Captain's Password: ")
            if entered_password == captain_password:
                missile_name = input("Enter the name of the missile to checkout: ")
                checkout_missile(missile_inventory, missile_name)
            else:
                print("Invalid password! Access denied.")

        elif choice == 3:
            missile_name = input("Enter the name of the missile to return: ")
            return_missile(missile_inventory, missile_name)

        elif choice == 4:
            print("Exiting the system. Have a good day!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
