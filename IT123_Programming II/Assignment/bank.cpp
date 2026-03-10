#include <iostream>
#include <string>
#include <iomanip>   // For setprecision and fixed formatting
using namespace std;

// -------------------------------------------------------
// Class Definition: BankAccount
// -------------------------------------------------------
class BankAccount {
private:
    // Private data members — hidden from outside the class
    string accountHolderName; // Name of the account owner
    string accountNumber;     // Unique account number
    double accountBalance;    // Current account balance (ZMW ..Zambian Kwacha)

public:
    // -------------------------------------------------------
    // createAccount()
    // Initialises account with name, number and opening balance
    // -------------------------------------------------------
    void createAccount() {
        cout << "\n  === CREATE NEW ACCOUNT ===\n";
        cout << "  Enter Account Holder Name : ";
        getline(cin, accountHolderName);

        cout << "  Enter Account Number      : ";
        getline(cin, accountNumber);

        cout << "  Enter Opening Balance (ZMW): ";
        cin  >> accountBalance;
        cin.ignore(); // Clear newline from buffer

        // Prevent negative opening balance
        if (accountBalance < 0) {
            cout << "  Warning: Opening balance cannot be negative. Set to 0.\n";
            accountBalance = 0.0;
        }

        cout << "\n  Account created successfully!\n";
    }

    // -------------------------------------------------------
    // deposit()
    // Adds a valid amount to the account balance
    // -------------------------------------------------------
    void deposit() {
        double amount;
        cout << "\n  === DEPOSIT ===\n";
        cout << "  Enter amount to deposit (ZMW): ";
        cin  >> amount;
        cin.ignore();

        // Validate: deposit must be a positive amount
        if (amount <= 0) {
            cout << "  Error: Deposit amount must be greater than zero.\n";
            return;
        }

        // Add to balance
        accountBalance += amount;
        cout << fixed << setprecision(2);
        cout << "  Deposit successful! New balance: ZMW " << accountBalance << "\n";
    }

    // -------------------------------------------------------
    // withdraw()
    // Deducts amount from balance if funds are sufficient
    // -------------------------------------------------------
    void withdraw() {
        double amount;
        cout << "\n  === WITHDRAWAL ===\n";
        cout << "  Enter amount to withdraw (ZMW): ";
        cin  >> amount;
        cin.ignore();

        // Validate: withdrawal must be a positive amount
        if (amount <= 0) {
            cout << "  Error: Withdrawal amount must be greater than zero.\n";
            return;
        }

        // Check if balance is sufficient before allowing withdrawal
        if (amount > accountBalance) {
            cout << "\n  Withdrawal denied: Insufficient balance.\n";
            cout << fixed << setprecision(2);
            cout << "  Current balance: ZMW " << accountBalance << "\n";
        } else {
            // Deduct amount from balance
            accountBalance -= amount;
            cout << fixed << setprecision(2);
            cout << "  Withdrawal successful! New balance: ZMW " << accountBalance << "\n";
        }
    }

    // -------------------------------------------------------
    // displayAccount()
    // Prints all account details to the console
    // -------------------------------------------------------
    void displayAccount() const {
        cout << fixed << setprecision(2);
        cout << "\n  ----------------------------------------";
        cout << "\n  ACCOUNT DETAILS";
        cout << "\n  ----------------------------------------";
        cout << "\n  Account Holder  : " << accountHolderName;
        cout << "\n  Account Number  : " << accountNumber;
        cout << "\n  Account Balance : ZMW " << accountBalance;
        cout << "\n  ----------------------------------------\n";
    }
};

// -------------------------------------------------------
// printMenu()
// Displays the main menu options to the user
// -------------------------------------------------------
void printMenu() {
    cout << "\n====================================================";
    cout << "\n  BANK ACCOUNT SYSTEM — MAIN MENU";
    cout << "\n====================================================";
    cout << "\n  1. Display Account Details";
    cout << "\n  2. Deposit Money";
    cout << "\n  3. Withdraw Money";
    cout << "\n  4. Exit Program";
    cout << "\n----------------------------------------------------";
    cout << "\n  Enter your choice (1-4): ";
}

// -------------------------------------------------------
// main()
// -------------------------------------------------------
int main() {
    BankAccount account; // Create a single BankAccount object
    int choice;          // Stores the user's menu selection

    cout << "====================================================";
    cout << "\n  SIMPLE BANK ACCOUNT PROGRAM";
    cout << "\n  IT123 Programming II  |  Student: 127-813";
    cout << "\n====================================================\n";

    // Step 1: Set up the account before showing the menu
    account.createAccount();

    // Step 2: Menu-driven loop — runs until user selects Exit
    do {
        printMenu();
        cin >> choice;
        cin.ignore(); // Clear the newline from buffer

        // Process the user's menu choice
        switch (choice) {
            case 1:
                // Option 1: Display account info
                account.displayAccount();
                break;

            case 2:
                // Option 2: Deposit money into account
                account.deposit();
                break;

            case 3:
                // Option 3: Withdraw money from account
                // (insufficient balance is handled inside withdraw())
                account.withdraw();
                break;

            case 4:
                // Option 4: Exit the program
                cout << "\n  Thank you for using the Bank Account System.\n";
                cout << "  Goodbye!\n\n";
                break;

            default:
                // Handle any invalid menu input
                cout << "\n  Invalid choice. Please enter a number between 1 and 4.\n";
                break;
        }

    } while (choice != 4); // Keep looping until user chooses to exit

    return 0;
}