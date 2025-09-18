# AIRTEL USSD SIMULATION
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
        print( # Sub-menu for Ikali
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
                # Same payment menu for all bundles
            print("1. Main Account\n2. Airtel Money")
            payment_choice = input("Choose payment method: ")

            if payment_choice == "1":
                print("Your transaction is being processed from Main Account...")
            elif payment_choice == "2":
                pin = input("Enter your Airtel Money PIN: ")
                print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
            else:
                print("Invalid option.")

        elif sub_choice == "0":
            print("Returning to Main Menu...")

    elif choice == "2":
        print(# Sub-menu for Airtel SoChe Pack
            "1. For 24 hours Daily Pack\n"
            "2. For Weekly Pack\n"
            "3. For Monthly Pack\n"
            "4. Buy for Other\n"
            "5. Cancel Auto Renewal\n"
            "0. Return to Main Menu"
        )
        sub_choice = input("Enter Option: ")

        if sub_choice == "1":
            print( #Sub-menu for Daily Pack
                "Press:\n"
                "1.K2=7Min+100SMS\n"
                "2.K5=27Mins+20MB+250SMS\n"
                "3.K10=62Mins+50mb+500SMS\n"
                "4.Upgrade to Weekly\n"
                "0 Return to main menu\n"
            )
            bundle = input("Choose bundle: ")

            if bundle in ["1","2","3"]:
                print("1. Main Account\n2. Airtel Money")
                payment_choice = input("Choose payment method: ")

                if payment_choice == "1":
                    print("Your transaction is being processed from Main Account...")
                elif payment_choice == "2":
                    pin = input("Enter your Airtel Money PIN: ")
                    print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                else:
                    print("Invalid option.")
            elif bundle == "4":
                print("Upgrading to the Weekly Pack...")
            else:
                print("Returning to Main Menu")

        elif sub_choice == "2":
            print( #Sub-menu for Weekly Pack
                "Press:\n"
                "1.K5=15Min+100SMS\n"
                "2.K10=42Mins+75MB+200SMS\n"
                "3.K20=125Mins+100mb+500SMS\n"
                "4.Upgrade to Monthly\n"
                "0 Return to main menu\n"
            )
            bundle = input("Choose bundle: ")

            if bundle in ["1","2","3"]:
                print("1. Main Account\n2. Airtel Money")
                payment_choice = input("Choose payment method: ")

                if payment_choice == "1":
                    print("Your transaction is being processed from Main Account...")
                elif payment_choice == "2":
                    pin = input("Enter your Airtel Money PIN: ")
                    print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                else:
                    print("Invalid option.")
            elif bundle == "4":
                print("Upgrading to the Monthly Pack...")
            else:
                print("Returning to Main Menu")

        elif sub_choice == "3":
            print( #Sub-menu for Monthly Pack
                "Press:\n"
                "1.K50=200Mins+500MB+500SMS\n"
                "2.K100=540Mins+1GB+1000SMS\n"
                "3.K200=1350Mins+3GB+2000SMS\n"
                "0 Return to main menu\n"
            )
            bundle = input("Choose bundle: ")

            if bundle in ["1","2","3"]:
                print("1. Main Account\n2. Airtel Money")
                payment_choice = input("Choose payment method: ")

                if payment_choice == "1":
                    print("Your transaction is being processed from Main Account...")
                elif payment_choice == "2":
                    pin = input("Enter your Airtel Money PIN: ")
                    print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                else:
                    print("Invalid option.")
            else:
                print("Returning to Main Menu")   
        elif sub_choice == "4":
            print("Enter the subscribers number you wish to purchase a So Che Pack for (097X XXXXXX/077X XXXXXX)")
        elif sub_choice == "5":
            print("Dear Customer, you currently do not have any auto-renewal")
        else:
            print("Returning to the main menu...")
    elif choice == "3":
        print(# Sub-menu for All Networks SoChe Pack
            "1. For 24 hours Daily Pack\n"
            "2. For Weekly Pack\n"
            "3. For Monthly Pack\n"
            "4. Buy for Other\n"
            "0. Return to Main Menu\n"
        ) 
        sub_choice = input("Enter Option: ")

        if sub_choice == "1":
            print( #Sub-menu for Daily Pack
                "Press:\n"
                "1.K2=5Mins+100SMS\n"
                "2.K5=18Mins+20MB+250SMS\n"
                "3.K10=42Mins+50mb+500SMS\n"
                "4.Upgrade to Weekly\n"
                "0 Return to main menu\n"
            )
            bundle = input("Choose bundle: ")

            if bundle in ["1","2","3"]:
                print("1. Main Account\n2. Airtel Money")
                payment_choice = input("Choose payment method: ")

                if payment_choice == "1":
                    print("Your transaction is being processed from Main Account...")
                elif payment_choice == "2":
                    pin = input("Enter your Airtel Money PIN: ")
                    print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                else:
                    print("Invalid option.")
            elif bundle == "4":
                print("Upgrading to the Weekly Pack...")
            else:
                print("Returning to Main Menu")
        elif sub_choice == "2":
            print( #Sub-menu for Weekly Pack
                "Press:\n"
                "1.K5=10Mins+100SMS\n"
                "2.K10=30Mins+75MB+200SMS\n"
                "3.K20=80Mins+100mb+500SMS\n"
                "4.K50=225Mins+250SMS+500SMS\n"
                "5.Upgrade to Monthly\n"
                "0 Return to main menu\n"
            )
            bundle = input("Choose bundle: ")

            if bundle in ["1","2","3","4"]:
                print("1. Main Account\n2. Airtel Money")
                payment_choice = input("Choose payment method: ")

                if payment_choice == "1":
                    print("Your transaction is being processed from Main Account...")
                elif payment_choice == "2":
                    pin = input("Enter your Airtel Money PIN: ")
                    print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                else:
                    print("Invalid option.")
                    exit
            elif bundle == "4":
                print("Upgrading to the Monthly Pack...")
            else:
                print("Returning to Main Menu")
        elif sub_choice == "3":
            print( #Sub-menu for Monthly Pack
                "Press:\n"
                "1.K50=140Mins+500MB+500SMS\n"
                "2.K100=320Mins+1GB+1000SMS\n"
                "3.K200=900Mins+3GB+2000SMS\n"
                "0 Return to main menu\n"
            )
            bundle = input("Choose bundle: ")

            if bundle in ["1","2","3"]:
                print("1. Main Account\n2. Airtel Money")
                payment_choice = input("Choose payment method: ")

                if payment_choice == "1":
                    print("Your transaction is being processed from Main Account...")
                elif payment_choice == "2":
                    pin = input("Enter your Airtel Money PIN: ")
                    print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                else:
                    print("Invalid option.")
                    exit
            else:
                print("Returning to Main Menu")   
        elif sub_choice == "4":
            print("Enter the subscribers number you wish to purchase a So Che Pack for (097X XXXXXX/077X XXXXXX)")
        else:
            print("Returning to the main menu...")
    elif choice == "4":
        print( # sub-menu for Data Packs
            "1.Ikali - Data and Voice\n"
            "2.Tonse Internet Bundles\n"
            "3.Buy for other\n"
            "4.Check balance\n"
            "5.Night Data\n"
            "6.Cancel auto renewal\n"
        )
        sub_choice = input("Enter Option: ")

        if sub_choice == "1":
            print( # Sub-menu for Ikali
            "Select:\n"
            "1. K2 = 9 All Networks Min, 24Hrs\n"
            "2. K5 = 22 All Networks Min, 7 DAYS\n"
            "3. K10 = 42 Mins, Allnet, 7 Days\n"
            "4. K6 = 450MB, 7 Days\n"
            "5. K10 = 1.1GB, 30Days\n"
            "6. K60 = 5.5GB, 7 Days\n"
            "7. K120 = 9GB, 30 Days\n")

            sub_sub_choice = input("Enter Option: ")

            if sub_sub_choice in ["1","2","3","4","5","6","7"]: 
                # Same payment menu for all bundles
                print("1. Main Account\n2. Airtel Money")
                payment_choice = input("Choose payment method: ")

                if payment_choice == "1":
                    print("Your transaction is being processed from Main Account...")
                elif payment_choice == "2":
                    pin = input("Enter your Airtel Money PIN: ")
                    print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                else:
                    print("Invalid option.")
                    exit
            else:
                print("Invalid option.")
        elif sub_choice == "2":
            print(#sub-menu for Tonse Internet Bundles
                "1.Daily\n"
                "2.Weekly\n"
                "3.Monthly\n"
                "4.60 or 90 Days"
                "5.90 to 365 Days"
                "6.No expiry bundles"
            )
            sub_sub_choice = input("Enter Option: ")

            if sub_sub_choice == "1":
                print( #menu for Daily
                    "1.110MB 30Days - K3.0\n"
                    "2.300MB 30Days - K6.0\n"
                    "3.1GB 30Days - K10.0\n"
                    "4.Upgrade to Weekly\n"
                )
                sub_sub_sub_choice = input("Enter Option: ")

                if sub_sub_sub_choice in ["1","2","3"]: 
                        # Same payment menu for all bundles
                    print("1. Main Account\n2. Airtel Money")
                    payment_choice = input("Choose payment method: ")

                    if payment_choice == "1":
                        print("Your transaction is being processed from Main Account...")
                    elif payment_choice == "2":
                        pin = input("Enter your Airtel Money PIN: ")
                        print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                    else:
                        print("Invalid option.")
                        exit
                else:
                    print("Upgrading to Weekly pack...")
            elif sub_sub_choice == "2":
                print( #menu for Weekly
                    "1.3.7GB 30Days - K60.0\n"
                    "2.7.5GB 30Days - K100.0\n"
                    "3.22GB 30Days - K200.0\n"
                    "4.60GB 30Days - K400.0\n"
                )
                sub_sub_sub_choice = input("Enter Option: ")

                if sub_sub_sub_choice in ["1","2","3","4"]: 
                        # Same payment menu for all bundles
                    print("1. Main Account\n2. Airtel Money")
                    payment_choice = input("Choose payment method: ")

                    if payment_choice == "1":
                        print("Your transaction is being processed from Main Account...")
                    elif payment_choice == "2":
                        pin = input("Enter your Airtel Money PIN: ")
                        print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                    else:
                        print("Invalid option.")
                else:
                    print("Upgrading to Monthly pack...")
            elif sub_sub_choice == "4":
                print( # 60 or 90 days
                    "60 or 90 Days bundels. Please Select: \n"
                    "1.35GB 60Days - K700.0\n"
                    "2.50GB 90Days - K900.0\n"
                    "3.100GB 90Days - K1,500.0\n"
                )
                sub_sub_sub_choice = input("Enter Option: ")

                if sub_sub_sub_choice in ["1","2","3"]: 
                        # Same payment menu for all bundles
                    print("1. Main Account\n2. Airtel Money")
                    payment_choice = input("Choose payment method: ")

                    if payment_choice == "1":
                        print("Your transaction is being processed from Main Account...")
                    elif payment_choice == "2":
                        pin = input("Enter your Airtel Money PIN: ")
                        print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                    else:
                        print("Invalid option.")
                exit
            elif sub_sub_choice == "5":
                print(# 90 to 365 days bundles. Please Select:
                    "1.90 days bundles\n"
                    "2.180 days bundels\n"
                    "3.365 days bundles\n"
                )
                sub_sub_sub_choice = input("Enter Option: ")

                if sub_sub_sub_choice == "1":
                    print( #90 days bundles
                        "Please Selec: \n"
                        "1.1.5GB 90days -K100\n"
                        "2.5GB 90days -K200\n"
                        "3.12GB 90days -K350\n"
                        "4.25GB 90days -K700\n"
                        "5.35GB 90days - K850\n"
                    )
                    sub_sub_sub_sub_choice = input("Enter Option: ")

                    if sub_sub_sub_sub_choice in ["1","2","3","4","5"]: 
                        # Same payment menu for all bundles
                        print("1. Main Account\n2. Airtel Money")
                        payment_choice = input("Choose payment method: ")

                        if payment_choice == "1":
                            print("Your transaction is being processed from Main Account...")
                        elif payment_choice == "2":
                            pin = input("Enter your Airtel Money PIN: ")
                            print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                        else:
                            print("Invalid option.")
                    exit
                elif sub_sub_sub_choice == "2":
                    print( #180 days bundles
                        "Please Selec: \n"
                        "1.1.5GB 180days -K150\n"
                        "2.5GB 180days -K300\n"
                        "3.12GB 180days -K600\n"
                        "4.25GB 180days -K1,200\n"
                        "5.35GB 180days -K2100\n"
                        "6.50GB 180days -K2700\n"
                        "7.100GB 180days -K4,500\n"
                    )
                    sub_sub_sub_sub_choice = input("Enter Option: ")

                    if sub_sub_sub_sub_choice in ["1","2","3","4","5","6","7"]: 
                        # Same payment menu for all bundles
                        print("1. Main Account\n2. Airtel Money")
                        payment_choice = input("Choose payment method: ")

                        if payment_choice == "1":
                            print("Your transaction is being processed from Main Account...")
                        elif payment_choice == "2":
                            pin = input("Enter your Airtel Money PIN: ")
                            print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                        else:
                            print("Invalid option.")
                    exit
                elif sub_sub_sub_choice == "3":
                    print( #365 days bundles
                        "Please Select: \n"
                        "1.1.5GB 365days -K200\n"
                        "2.5GB 365days -K400\n"
                        "3.12GB 365days -K800\n"
                        "4.25GB 365days -K1,600\n"
                        "5.35GB 365days -K2,800\n"
                        "6.50GB 365days -K3,600\n"
                        
                    )
                    sub_sub_sub_sub_choice = input("Enter Option: ")

                    if sub_sub_sub_sub_choice in ["1","2","3","4","5","6"]: 
                        # Same payment menu for all bundles
                        print("1. Main Account\n2. Airtel Money")
                        payment_choice = input("Choose payment method: ")

                        if payment_choice == "1":
                            print("Your transaction is being processed from Main Account...")
                        elif payment_choice == "2":
                            pin = input("Enter your Airtel Money PIN: ")
                            print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                        else:
                            print("Invalid option.")
                    exit
                else:
                    print("Invalid Option")
                    exit
            elif sub_sub_choice == "6":
                print(# No expiry
                    "No expiry bundles. Please Select: \n"
                    "1.1GB -k90.0\n"
                    "2.2.5GB -K200.0\n"
                    "3.5.5GB - K400.0\n"
                )
                sub_sub_sub_choice = input("Enter Option: ")

                if sub_sub_sub_choice in ["1","2","3"]: 
                    # Same payment menu for all bundles
                    print("1. Main Account\n2. Airtel Money")
                    payment_choice = input("Choose payment method: ")

                    if payment_choice == "1":
                        print("Your transaction is being processed from Main Account...")
                    elif payment_choice == "2":
                        pin = input("Enter your Airtel Money PIN: ")
                        print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                    else:
                        print("Invalid option.")
                exit
            else:
                print("Invalid Option")
                exit
        elif sub_choice == "3":
            print( # Buy for other
                "Enter the subscribers number you wish to purchase a Data bundle for (097xxxxxxx/077xxxxxxx/057xxxxxxx"
            )
            
            number = input("Enter the number: ")

            # Validation
            if len(number) != 10 or not number.isdigit():
                print("Invalid number. Must be 10 digits.")
            elif not (number.startswith("097") or number.startswith("077") or number.startswith("057")):
                print("Dear Customer, the entered number {number}is not a valid Airtel number.")
            else:
                print("Please select a bundle:")
                print("1.Internet Bundles")
                
                choice = input("Enter option 1:")

                if choice == "1":
                    print(
                        "Please select a bundle: " #all options must take you to the options under Tonse Bundles
                        "1.Daily\n" 
                        "2.Weekly\n"
                        "3.Monthly\n"
                        "4.60 or 90 Days\n"
                        "5.90 to 365 Days\n"
                        "6.No expiry bundles\n"
                        "# Home\n"
                        "* Back\n"
                    )
                else:
                    exit
        elif sub_choice == "4":
            print( #Check Balance
                "Balance/Validity check. Please select: \n"
                "1.Internet Bundle\n" 
                "2.Ikali\n"
                "3.No expiry bundle\n"
                "4.Hybrid Bundle\n"
            )
            sub_sub_choice = input("Enter option: ")

            if sub_sub_choice in ["1","2","3","4"]:
                print("Dear Customer, your balance request is being processed. You will receive a confirmation essage shortly")
            else:
                print("Invalid Option")
            exit
        elif sub_choice == "5":
            print(# Night Data
                "Night Data Pack, 1.5GB at K5\n"
                "1. To buy"
            )
            sub_sub_choice = input("Enter option: ")

            if sub_sub_choice == "1":
                print("1. Main Account\n2. Airtel Money")
                payment_choice = input("Choose payment method: ")

                if payment_choice == "1":
                    print("Your transaction is being processed from Main Account...")
                elif payment_choice == "2":
                    pin = input("Enter your Airtel Money PIN: ")
                    print(f"PIN {pin} accepted.\nYour transaction is being processed via Airtel Money...")
                else:
                    print("Invalid option.")
            else:
                print("Invalid Option")
            exit
        elif sub_choice == "6":
            print(#Auto renewal
                "To cancel auto renewal. Please select: \n"
                "1.Internet bundle"   
            )
            sub_sub_choice = input("Enter option: ")

            if sub_sub_choice == "1":
                print("You do not currently have a Data Bundle on auto-renew.")
            else:
                print("Invalid Option")
            exit
        else:
            print("Invalid Option")
    elif choice == "5":
        print( # Buy for other
            "Enter the subscribers number you wish to purchase a Data bundle for (097xxxxxxx/077xxxxxxx/057xxxxxxx"
        )
            
        number = input("Enter the number: ")

        # Validation
        if len(number) != 10 or not number.isdigit():
            print("Invalid number. Must be 10 digits.")
        elif not (number.startswith("097") or number.startswith("077") or number.startswith("057")):
            print("Dear Customer, the entered number {number}is not a valid Airtel number.")
        else:
            print("Please select a bundle:")
            print("1.Internet Bundles")
                    
            sub_choice = input("Enter option 1:")

            if sub_choice == "1":
                print(
                    "Please select a bundle: " #all options must take you to the options under Tonse Bundles
                    "1.Daily\n" 
                    "2.Weekly\n"
                    "3.Monthly\n"
                    "4.60 or 90 Days\n"
                    "5.90 to 365 Days\n"
                    "6.No expiry bundles\n"
                    "# Home\n"
                    "* Back\n"
                    )
            else:
                exit
    elif choice == "6":
        print("Dear Customer, your balance request is being processed. You will receive a confirmation essage shortly")
    elif choice == "7":
        print( #Siliza Airtime
            "Reply with: \n"
            "1.for Siliza Airtime\n"
            "2.for Eligibility\n"
            "3.for Payment\n"
            "4.for Help\n"
            "5.for Balance Check\n"
        )
        sub_choice = input("Enter option: ")

        if sub_choice in ["1","2"]:
            print("Dear Customer, your request was unsucessful.Top up more to qualify for this service\n Top up more to qualify for this service." )
        elif sub_choice == "3":
            print("Please Recharge with K0.0000 to fully payback your loan")
        elif sub_choice =="4":
            print(
                "1 Qualification\n"
                "2 Repayment\n"
                "# Main Menu\n"
            )
        elif sub_choice =="5":
            print("Dear Customer, your balance request is being processed. You will receive a confirmation essage shortly")
        else:
            print("Invalid Option")
        exit
    elif choice == "8":
        print("Dear Customer, your request is being processed. You will receive a confirmation message with a link shorlty. Click on the link to download the App.")   
    elif choice == "n":
        print(
            "9.INTL calling & roaming\n"
            "0.Return to main menu\n"
        )    
        sub_choice = input("Enter Option: ")

        if sub_choice == "9":
            print(
                "Welcome to Airtel International Services"
                "1.One Airtel Roaming"
                "2.Global Roaming"
                "3.International Voice Calling"
                "4.Balance Check"
                "5.Zambia Tourist Pack"
            )
            sub_sub_choice = input("Enter Option: ")

            if sub_sub_choice == "1":                
                print(# One Airtel Roaming
                    "1.distination coutries\n"
                    "2.buy bundles\n"
                    "3.buy for other\n"
                    "4.00 Back\n"
                )
            if sub_sub_choice == "2": 
                print(# Global Roaming
                    "1.distination coutries\n"
                    "2.buy bundles\n"
                    "3.buy for other\n"
                    "4.00 Back\n"
                )
            if sub_sub_choice == "2": 
                print(
                    "1.buy bundles\n"
                    "2.buy for other\n"
                    "3.00 Back\n"
                )
        elif sub_choice == "0":
                print("Returning to the main menu")
        else:
            print("Invalid Option")
        exit
    else:
        print("Invalid option.")       
else:
    print("Please enter the correct USSD code!")