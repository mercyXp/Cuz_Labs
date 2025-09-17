# ------------------- Airtel USSD SIMULATION -------------------

def start():
    print("Welcome to Airtel Services\nDial *117# to get started")
    ussd = input("Enter: ")
    if ussd == "*117#":
        main_menu()
    else:
        print("Invalid USSD code. Try again.")


# ------------------- MENUS -------------------

def main_menu():
    print(
        "\n--- Airtel Main Menu ---\n"
        "1. Ikali - Data and Voice\n"
        "2. Airtel SoChe Pack\n"
        "3. All networks SoChe\n"
        "4. Data Packs\n"
        "5. Buy for Other\n"
        "6. Balance Check\n"
        "7. Siliza - Airtime Loan\n"
        "8. Get Airtel App (100MB Free)\n"
        "n. Next\n"
        "0. Exit"
    )
    choice = input("Enter Option: ")
    if choice == "1": ikali_menu()
    elif choice == "2": soche_menu()
    elif choice == "3": allnet_soche_menu()
    elif choice == "4": data_packs_menu()
    elif choice == "5": buy_for_other()
    elif choice == "6": balance_check()
    elif choice == "7": siliza_menu()
    elif choice == "8": print("You will receive a confirmation SMS with a download link."); main_menu()
    elif choice == "n": next_menu()
    elif choice == "0": print("Thank you for using Airtel USSD. Goodbye!")
    else: print("Invalid Option"); main_menu()


# ------------------- IKALI -------------------

def ikali_menu():
    print(
        "\nIkali Bundles:\n"
        "1. K2 = 9 All Networks Min, 24Hrs\n"
        "2. K5 = 22 All Networks Min, 7 DAYS\n"
        "3. K10 = 42 Mins, Allnet, 7 Days\n"
        "4. K6 = 450MB, 7 Days\n"
        "5. K10 = 1.1GB, 30Days\n"
        "6. K60 = 5.5GB, 7 Days\n"
        "7. K120 = 9GB, 30 Days\n"
        "0. Back"
    )
    sub_choice = input("Enter Option: ")
    if sub_choice in [str(i) for i in range(1, 8)]: payment_menu(); main_menu()
    elif sub_choice == "0": main_menu()
    else: print("Invalid Option"); ikali_menu()


# ------------------- SOCHE -------------------

def soche_menu():
    print(
        "\nAirtel SoChe Pack:\n"
        "1. Daily Pack\n"
        "2. Weekly Pack\n"
        "3. Monthly Pack\n"
        "4. Buy for Other\n"
        "5. Cancel Auto Renewal\n"
        "0. Back"
    )
    sub_choice = input("Enter Option: ")
    if sub_choice == "1": soche_daily()
    elif sub_choice == "2": soche_weekly()
    elif sub_choice == "3": soche_monthly()
    elif sub_choice == "4": buy_for_other()
    elif sub_choice == "5": print("Auto Renewal Cancelled"); main_menu()
    elif sub_choice == "0": main_menu()
    else: print("Invalid Option"); soche_menu()


def soche_daily():
    print("\nDaily SoChe:\n1. K2 = 7Min+100SMS\n2. K5 = 27Min+20MB+250SMS\n3. K10 = 62Min+50MB+500SMS\n0. Back")
    bundle = input("Choose: ")
    if bundle in ["1", "2", "3"]: payment_menu(); main_menu()
    elif bundle == "0": soche_menu()
    else: print("Invalid"); soche_daily()


def soche_weekly():
    print("\nWeekly SoChe:\n1. K20=200Mins+200MB\n2. K50=600Mins+1.5GB\n0. Back")
    bundle = input("Choose: ")
    if bundle in ["1", "2"]: payment_menu(); main_menu()
    elif bundle == "0": soche_menu()
    else: print("Invalid"); soche_weekly()


def soche_monthly():
    print("\nMonthly SoChe:\n1. K100=1200Mins+3GB\n2. K200=Unlimited Calls+10GB\n0. Back")
    bundle = input("Choose: ")
    if bundle in ["1", "2"]: payment_menu(); main_menu()
    elif bundle == "0": soche_menu()
    else: print("Invalid"); soche_monthly()


# ------------------- ALLNET SOCHE -------------------

def allnet_soche_menu():
    print("\nAll Networks SoChe:\n1. K10=50Min\n2. K20=120Min\n0. Back")
    sub_choice = input("Enter Option: ")
    if sub_choice in ["1","2"]: payment_menu(); main_menu()
    elif sub_choice == "0": main_menu()
    else: print("Invalid"); allnet_soche_menu()


# ------------------- DATA PACKS -------------------

def data_packs_menu():
    print("\nData Packs:\n1. Daily\n2. Weekly\n3. Monthly\n4. Long Validity\n0. Back")
    sub_choice = input("Enter: ")
    if sub_choice == "1": data_daily()
    elif sub_choice == "2": data_weekly()
    elif sub_choice == "3": data_monthly()
    elif sub_choice == "4": data_long_validity()
    elif sub_choice == "0": main_menu()
    else: print("Invalid"); data_packs_menu()


def data_daily():
    print("\nDaily Bundles:\n1. K5=100MB\n2. K10=300MB\n0. Back")
    ch = input("Enter: ")
    if ch in ["1","2"]: payment_menu(); main_menu()
    elif ch == "0": data_packs_menu()
    else: print("Invalid"); data_daily()


def data_weekly():
    print("\nWeekly Bundles:\n1. K20=1GB\n2. K50=3GB\n0. Back")
    ch = input("Enter: ")
    if ch in ["1","2"]: payment_menu(); main_menu()
    elif ch == "0": data_packs_menu()
    else: print("Invalid"); data_weekly()


def data_monthly():
    print("\nMonthly Bundles:\n1. K100=5GB\n2. K200=15GB\n0. Back")
    ch = input("Enter: ")
    if ch in ["1","2"]: payment_menu(); main_menu()
    elif ch == "0": data_packs_menu()
    else: print("Invalid"); data_monthly()


def data_long_validity():
    print("\nLong Validity Bundles:\n1. K500=50GB/90days\n2. K1000=120GB/180days\n0. Back")
    ch = input("Enter: ")
    if ch in ["1","2"]: payment_menu(); main_menu()
    elif ch == "0": data_packs_menu()
    else: print("Invalid"); data_long_validity()


# ------------------- BUY FOR OTHER -------------------

def buy_for_other():
    number = input("Enter subscriber number (097/077/057): ")
    if len(number) == 10 and number.startswith(("097", "077", "057")):
        print(f"Buying bundle for {number}")
        data_packs_menu()
    else:
        print("Invalid Airtel number"); main_menu()


# ------------------- BALANCE -------------------

def balance_check():
    print("Dear Customer, your balance request is being processed...")
    main_menu()


# ------------------- SILIZA -------------------

def siliza_menu():
    print("\nSiliza:\n1. Loan\n2. Eligibility\n3. Payment\n4. Help\n5. Balance Check\n0. Back")
    sub = input("Enter: ")
    if sub == "1": print("Not eligible. Top up more."); main_menu()
    elif sub == "2": print("Eligibility check failed."); main_menu()
    elif sub == "3": print("Please recharge K0.00 to repay loan."); main_menu()
    elif sub == "4": print("Help: 1. Qualification 2. Repayment"); siliza_menu()
    elif sub == "5": balance_check()
    elif sub == "0": main_menu()
    else: print("Invalid"); siliza_menu()


# ------------------- NEXT MENU -------------------

def next_menu():
    print("\nNext Menu:\n9. INTL calling & roaming\n0. Back")
    sub_choice = input("Enter Option: ")
    if sub_choice == "9": intl_menu()
    elif sub_choice == "0": main_menu()
    else: print("Invalid Option"); next_menu()


def intl_menu():
    print("\nInternational Services:\n1. One Airtel Roaming\n2. Global Roaming\n3. International Voice Calling\n4. Balance Check\n0. Back")
    sub_choice = input("Enter Option: ")
    if sub_choice in ["1","2","3"]: print("Service being processed..."); main_menu()
    elif sub_choice == "4": balance_check()
    elif sub_choice == "0": next_menu()
    else: print("Invalid"); intl_menu()


# ------------------- PAYMENT -------------------

def payment_menu():
    print("1. Main Account\n2. Airtel Money")
    choice = input("Choose payment method: ")
    if choice == "1":
        print("Transaction processing from Main Account...")
    elif choice == "2":
        pin = input("Enter Airtel Money PIN: ")
        print(f"PIN {pin} accepted. Transaction processing...")
    else:
        print("Invalid payment option.")
        payment_menu()


# ------------------- RUN PROGRAM -------------------
start()
