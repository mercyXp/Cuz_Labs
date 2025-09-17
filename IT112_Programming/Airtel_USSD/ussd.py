class USSDApp:
    def __init__(self):
        self.running = True

    # ------------------- START -------------------
    def start(self):
        print("Welcome to Airtel Services\nDial *117# to get started")
        ussd = input("Enter: ")
        if ussd == "*117#":
            self.main_menu()
        else:
            print("Invalid USSD code. Try again.")

    # ------------------- MAIN MENU -------------------
    def main_menu(self):
        while self.running:
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
            if choice == "1": self.ikali_menu()
            elif choice == "2": self.soche_menu()
            elif choice == "3": self.allnet_soche_menu()
            elif choice == "4": self.data_packs_menu()
            elif choice == "5": self.buy_for_other()
            elif choice == "6": self.balance_check()
            elif choice == "7": self.siliza_menu()
            elif choice == "8": print("You will receive a confirmation SMS with a download link.")
            elif choice == "n": self.next_menu()
            elif choice == "0":
                print("Thank you for using Airtel USSD. Goodbye!")
                self.running = False
            else: print("Invalid Option")

    # ------------------- IKALI -------------------
    def ikali_menu(self):
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
        if sub_choice in [str(i) for i in range(1, 8)]:
            self.payment_menu()
        elif sub_choice == "0":
            return
        else: print("Invalid Option")

    # ------------------- SOCHE -------------------
    def soche_menu(self):
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
        if sub_choice == "1": self.soche_daily()
        elif sub_choice == "2": self.soche_weekly()
        elif sub_choice == "3": self.soche_monthly()
        elif sub_choice == "4": self.buy_for_other()
        elif sub_choice == "5": print("Auto Renewal Cancelled")
        elif sub_choice == "0": return
        else: print("Invalid Option")

    def soche_daily(self):
        print("\nDaily SoChe:\n1. K2=7Min+100SMS\n2. K5=27Mins+20MB+250SMS\n3. K10=62Mins+50MB+500SMS\n0. Back")
        bundle = input("Choose: ")
        if bundle in ["1", "2", "3"]:
            self.payment_menu()
        elif bundle == "0": return
        else: print("Invalid")

    def soche_weekly(self):
        print("\nWeekly SoChe:\n1. K20=200Mins+200MB\n2. K50=600Mins+1.5GB\n0. Back")
        bundle = input("Choose: ")
        if bundle in ["1", "2"]: self.payment_menu()
        elif bundle == "0": return
        else: print("Invalid")

    def soche_monthly(self):
        print("\nMonthly SoChe:\n1. K100=1200Mins+3GB\n2. K200=Unlimited Calls+10GB\n0. Back")
        bundle = input("Choose: ")
        if bundle in ["1", "2"]: self.payment_menu()
        elif bundle == "0": return
        else: print("Invalid")

    # ------------------- ALLNET SOCHE -------------------
    def allnet_soche_menu(self):
        print("\nAll Networks SoChe:\n1. K10=50Min\n2. K20=120Min\n0. Back")
        sub_choice = input("Enter Option: ")
        if sub_choice in ["1","2"]: self.payment_menu()
        elif sub_choice == "0": return
        else: print("Invalid")

    # ------------------- DATA PACKS -------------------
    def data_packs_menu(self):
        print("\nData Packs:\n1. Daily\n2. Weekly\n3. Monthly\n4. Long Validity\n0. Back")
        sub_choice = input("Enter: ")
        if sub_choice == "1": self.data_daily()
        elif sub_choice == "2": self.data_weekly()
        elif sub_choice == "3": self.data_monthly()
        elif sub_choice == "4": self.data_long_validity()
        elif sub_choice == "0": return
        else: print("Invalid")

    def data_daily(self):
        print("\nDaily Bundles:\n1. K5=100MB\n2. K10=300MB\n0. Back")
        ch = input("Enter: ")
        if ch in ["1","2"]: self.payment_menu()
        elif ch == "0": return
        else: print("Invalid")

    def data_weekly(self):
        print("\nWeekly Bundles:\n1. K20=1GB\n2. K50=3GB\n0. Back")
        ch = input("Enter: ")
        if ch in ["1","2"]: self.payment_menu()
        elif ch == "0": return
        else: print("Invalid")

    def data_monthly(self):
        print("\nMonthly Bundles:\n1. K100=5GB\n2. K200=15GB\n0. Back")
        ch = input("Enter: ")
        if ch in ["1","2"]: self.payment_menu()
        elif ch == "0": return
        else: print("Invalid")

    def data_long_validity(self):
        print("\nLong Validity Bundles:\n1. K500=50GB/90days\n2. K1000=120GB/180days\n0. Back")
        ch = input("Enter: ")
        if ch in ["1","2"]: self.payment_menu()
        elif ch == "0": return
        else: print("Invalid")

    # ------------------- BUY FOR OTHER -------------------
    def buy_for_other(self):
        number = input("Enter subscriber number (097/077/057): ")
        if len(number) == 10 and number.startswith(("097", "077", "057")):
            print(f"Buying bundle for {number}")
            self.data_packs_menu()
        else:
            print("Invalid Airtel number")

    # ------------------- BALANCE -------------------
    def balance_check(self):
        print("Dear Customer, your balance request is being processed...")

    # ------------------- SILIZA -------------------
    def siliza_menu(self):
        print("\nSiliza:\n1. Loan\n2. Eligibility\n3. Payment\n4. Help\n5. Balance Check\n0. Back")
        sub = input("Enter: ")
        if sub == "1": print("Not eligible. Top up more.")
        elif sub == "2": print("Eligibility check failed.")
        elif sub == "3": print("Please recharge K0.00 to repay loan.")
        elif sub == "4": print("Help: 1. Qualification 2. Repayment")
        elif sub == "5": self.balance_check()
        elif sub == "0": return
        else: print("Invalid")

    # ------------------- NEXT MENU -------------------
    def next_menu(self):
        print("\nNext Menu:\n9. INTL calling & roaming\n0. Back")
        sub_choice = input("Enter Option: ")
        if sub_choice == "9": self.intl_menu()
        elif sub_choice == "0": return
        else: print("Invalid Option")

    def intl_menu(self):
        print("\nInternational Services:\n1. One Airtel Roaming\n2. Global Roaming\n3. International Voice Calling\n4. Balance Check\n0. Back")
        sub_choice = input("Enter Option: ")
        if sub_choice in ["1","2","3"]: print("Service being processed...")
        elif sub_choice == "4": self.balance_check()
        elif sub_choice == "0": return
        else: print("Invalid")

    # ------------------- PAYMENT -------------------
    def payment_menu(self):
        print("1. Main Account\n2. Airtel Money")
        choice = input("Choose payment method: ")
        if choice == "1":
            print("Transaction processing from Main Account...")
        elif choice == "2":
            pin = input("Enter Airtel Money PIN: ")
            print(f"PIN {pin} accepted. Transaction processing...")
        else:
            print("Invalid payment option.")


# ------------------- RUN APP -------------------
app = USSDApp()
app.start()
