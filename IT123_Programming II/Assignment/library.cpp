#include <iostream>
#include <string>

using namespace std;

class Book{
    private:
        string bookTitle, authorName, bookID; 
        int numCopies; //number of copies in the Library
    public:
        // inputBook() --> Prompts the user to enter all book details
        void inputBook() {
            cout << "\n  Enter Book Title         : ";
            getline(cin, bookTitle);

            cout << "  Enter Author Name        : ";
            getline(cin, authorName);

            cout << "  Enter Book ID            : ";
            getline(cin, bookID);

            cout << "  Enter Number of Copies   : ";
            cin  >> numCopies;
            cin.ignore(); // Clear the newline from input buffer
        }

        // displayBook() --> Prints all stored book details to the console
        void displayBook() const {
            cout << "\n  ----------------------------------------";
            cout << "\n  Book Title       : " << bookTitle;
            cout << "\n  Author Name      : " << authorName;
            cout << "\n  Book ID          : " << bookID;
            cout << "\n  Number of Copies : " << numCopies;
            cout << "\n  ----------------------------------------\n";
        }

        // getNumCopies() --> Returns the number of copies — used for total calculation
        int getNumCopies() const {
            return numCopies;
        }
};

int main(){
    int numberOfBooks; // User will enter this at runtime

    cout << "====================================================";
    cout << "\n  LIBRARY BOOK MANAGEMENT SYSTEM";
    cout << "\n  Student Number: 127-813";
    cout << "\n====================================================\n";

    cout << "\n  How many books do you want to enter? : ";
    cin  >> numberOfBooks;
    cin.ignore(); // Clear newline

    // Validation: the user must enter at least 1 book
    if (numberOfBooks <= 0) {
        cout << "\n  Error: Number of books must be greater than 0.\n";
        return 1;
    }

    Book* books = new Book[numberOfBooks]; // Dynamic allocation of an array of Book objects

    //Input: Collect details of each book
    for (int i = 0; i < numberOfBooks; i++) {
        cout << "\n>> Enter details for Book " << (i + 1) << ":";
        books[i].inputBook();
    }

    //Display: show all book records
    cout << "\n====================================================";
    cout << "\n  DISPLAYING ALL BOOK RECORDS";
    cout << "\n====================================================";

    int totalCopies = 0; // Accumulator for total copies

    for (int i = 0; i < numberOfBooks; i++) {
        cout << "\n  [Book Record " << (i + 1) << "]";
        books[i].displayBook();

        totalCopies += books[i].getNumCopies(); // Adds each book's copies to the running total
    }

    // Display total copies across all books
    cout << "\n====================================================";
    cout << "\n  TOTAL COPIES (all books combined): " << totalCopies;
    cout << "\n====================================================\n";

    // Free dynamically allocated memory
    delete[] books;

    cout << "\n  Program ended successfully.\n";

    return 0;
}