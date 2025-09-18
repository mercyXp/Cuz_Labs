# AIRTEL USSD SIMULATION (Function-based with balances and eligibility check)

# -------------------------
# INITIAL BALANCES
# -------------------------
user_balances = {
    "main_account": 50,   # K50
    "airtel_money": 100   # K100
}

# -------------------------
# HELPER FUNCTIONS
# -------------------------
def check_balance():
    print("\n--- Account Balances ---")
    print(f"Main Account: K{user_balances['main_account']}")
    print(f"Airtel Money: K{user_balances['airtel_money']}\n")

def deduct_balance(payment_choice, cost):
    """Deducts balance if funds are sufficient"""
    if payment_choice == "1":  # Main Account
        if user_balances["main_account"] >= cost:
            user_balances["main_account"] -= cost
            print(f"Payment of K{cost} successful from Main Account.")
            return True
        else:
            print("Insufficient funds in Main Account.")
            return False
    elif payment_choice == "2":  # Airtel Money
        if user_balances["airtel_money"] >= cost:
            pin = input("Enter your Airtel Money PIN: ")
            print(f"PIN {pin} accepted.")
            user_balances["airtel_money"] -= cost
            print(f"Payment of K{cost} successful via Airtel Money.")
            return True
        else:
            print("Insufficient funds in Airtel Money.")
            return False
    else:
        print("Invalid payment option.")
        return False

def payment_menu(cost=5):
    """Handles payment with default cost=5 for demo"""
    print("1. Main Account\n2. Airtel Money")
    payment_choice = input("Choose payment method: ")
    deduct_balance(payment_choice, cost)
    check_balance()

# ------------------- Menus -------------------

def ikali_menu():
    print(
        "Select:\n"
        "1. K2 = 9 All Networks Min, 24Hrs\n"
        "2. K5 = 22 All Networks Min, 7 DAYS\n"
        "3. K10 = 42 Mins, Allnet, 7 Days\n"
        "4. K6 = 450MB, 7 Days\n"
        "5. K10 = 1.1GB, 30Days\n"
        "6. K60 = 5.5GB, 7 Days\n"
        "7. K120 = 9GB, 30 Days\n"
    )
    sub_choice = input("Enter Option: ")
    if sub_choice in ["1","2","3","4","5","6","7"]:
        payment_menu()
    elif sub_choice == "0":
        print("Returning to Main Menu...")

def soche_pack_menu():
    print(
        "1. For 24 hours Daily Pack\n"
        "2. For Weekly Pack\n"
        "3. For Monthly Pack\n"
        "4. Buy for Other\n"
        "5. Cancel Auto Renewal\n"
        "0. Return to Main Menu"
    )
    sub_choice = input("Enter Option: ")
    if sub_choice == "1":
        daily_pack()
    elif sub_choice == "2":
        weekly_pack()
    elif sub_choice == "3":
        monthly_pack()
    elif sub_choice == "4":
        print("Enter the subscribers number you wish to purchase a So Che Pack for (097X XXXXXX/077X XXXXXX)")
    elif sub_choice == "5":
        print("Dear Customer, you currently do not have any auto-renewal")
    else:
        print("Returning to the main menu...")

def daily_pack():
    print(
        "Press:\n"
        "1.K2=7Min+100SMS\n"
        "2.K5=27Mins+20MB+250SMS\n"
        "3.K10=62Mins+50mb+500SMS\n"
        "4.Upgrade to Weekly\n"
        "0 Return to main menu\n"
    )
    bundle = input("Choose bundle: ")
    if bundle in ["1","2","3"]:
        payment_menu()
    elif bundle == "4":
        print("Upgrading to the Weekly Pack...")
    else:
        print("Returning to Main Menu")

def weekly_pack():
    print(
        "Press:\n"
        "1.K5=15Min+100SMS\n"
        "2.K10=42Mins+75MB+200SMS\n"
        "3.K20=125Mins+100mb+500SMS\n"
        "4.Upgrade to Monthly\n"
        "0 Return to main menu\n"
    )
    bundle = input("Choose bundle: ")
    if bundle in ["1","2","3"]:
        payment_menu()
    elif bundle == "4":
        print("Upgrading to the Monthly Pack...")
    else:
        print("Returning to Main Menu")

def monthly_pack():
    print(
        "Press:\n"
        "1.K50=200Mins+500MB+500SMS\n"
        "2.K100=540Mins+1GB+1000SMS\n"
        "3.K200=1350Mins+3GB+2000SMS\n"
        "0 Return to main menu\n"
    )
    bundle = input("Choose bundle: ")
    if bundle in ["1","2","3"]:
        payment_menu()
    else:
        print("Returning to Main Menu")

def siliza_menu():
    print("\n--- Siliza (Airtime Loan) ---")
    print("1. Request Siliza Airtime\n2. Check Eligibility\n3. Payment\n4. Help\n5. Balance Check")
    choice = input("Enter option: ")

    if choice == "1":
        print("Request unsuccessful. You are not eligible for Siliza.")
    elif choice == "2":
        print("Not eligible. Please top up more to qualify.")
    elif choice == "3":
        print("No loan balance to pay back.")
    elif choice == "4":
        print("Help: You must be a frequent user with good repayment history to qualify.")
    elif choice == "5":
        print("Balance check is being processed...")
    else:
        print("Invalid option.")

def intl_menu():
    print(
        "9.INTL calling & roaming\n"
        "0.Return to main menu\n"
    )
    sub_choice = input("Enter Option: ")

    if sub_choice == "9":
        print(
            "Welcome to Airtel International Services\n"
            "1.One Airtel Roaming\n"
            "2.Global Roaming\n"
            "3.International Voice Calling\n"
            "4.Balance Check\n"
            "5.Zambia Tourist Pack\n"
        )
        sub_sub_choice = input("Enter Option: ")

        if sub_sub_choice == "1":                
            print(
                "1.distination coutries\n"
                "2.buy bundles\n"
                "3.buy for other\n"
                "4.00 Back\n"
            )
        elif sub_sub_choice == "2": 
            print(
                "1.distination coutries\n"
                "2.buy bundles\n"
                "3.buy for other\n"
                "4.00 Back\n"
            )
        elif sub_sub_choice == "3": 
            print(
                "1.buy bundles\n"
                "2.buy for other\n"
                "3.00 Back\n"
            )
        elif sub_sub_choice == "4":
            print(
                "Please Select:\n"
                "1.One Airtel Roaming\n"
                "2.Global Roaming\n"
                "3.International Voice Calling\n"
                "00 Back\n"
            )
        elif sub_sub_choice == "5":
            print(
                "Welcome to Zambia! Get 250 local mins, 250SMS,10GB,K100 for international calls @ K350 valid 14days.\n"
                "1.Subscribe\n"
                "2.Check Balance\n"
                "00 Back\n"
            )
    elif sub_choice == "0":
        print("Returning to the main menu")
    else:
        print("Invalid Option")

# ------------------- Main Flow -------------------

def main():
    print("Welcome to Airtel Services\nDial *117# to get started")
    ussd_code = input("Enter: ")

    if ussd_code == "*117#":
        print(
            "1. Ikali - Data and Voice\n"
            "2. Airtel SoChe Pack\n"
            "3. All networks SoChe\n"
            "4. Data Packs\n"
            "5. Buy for Other\n"
            "6. Balance Check\n"
            "7. Siliza - Airtime Loan\n"
            "8. Get Airtel App (100MB Free)\n"
            "n  Next\n"
        )
        choice = input("Enter Option: ")

        if choice == "1":
            ikali_menu()
        elif choice == "2":
            soche_pack_menu()
        elif choice == "6":
            check_balance()
        elif choice == "7":
            siliza_menu()
        elif choice == "8":
            print("You will receive an SMS with a download link for the Airtel App.")
        elif choice.lower() == "n":
            intl_menu()
        else:
            print("Feature not implemented in this demo.")
    else:
        print("Please enter the correct USSD code!")

# program starts running from here
if __name__ == "__main__":
    main()
