#include <iostream>
#include <string> //to enable the use of the string data type

using namespace std;

class Student{ 
    private:
        string studentName, studyProgram, studentNumber;
        int studyYear;
    public:
        // inputStudent() method --> Prompts the user to enter all student details
        void inputStudent(){
            cout << "\n  Enter Student Name     : ";
            getline(cin, studentName);

            cout << "  Enter Student Number     : ";
            getline(cin, studentNumber);

            cout << "  Enter Programme of Study : ";
            getline(cin, studyProgram);

            cout << "  Enter Year of Study      : ";
            cin  >> studyYear;
            cin.ignore(); // Clear the newline left in the buffer
        }
        // displayStudent() method --> Prints all stored student details to the console
        void displayStudent() const {
        cout << "\n  ----------------------------------------";
        cout << "\n  Student Name       : " << studentName;
        cout << "\n  Student Number     : " << studentNumber;
        cout << "\n  Programme of Study : " << studyProgram;
        cout << "\n  Year of Study      : " << studyYear;
        cout << "\n  ----------------------------------------\n";
        }
};

int main(){
    // My Student Number: 127-813, Last digit = 3  →  Number of students = 2
    const int numberOfStudents = 2;

    Student students[numberOfStudents]; //an array of Student objects

    cout << "====================================================";
    cout << "\n  STUDENT INFORMATION SYSTEM";
    cout << "\n  Student Number: 127-813 | Last Digit: 3";
    cout << "\n  Number of Students to enter: " << numberOfStudents;
    cout << "\n====================================================\n";

    // --- Input: collect details for each student ---
    for (int i = 0; i < numberOfStudents; i++) {
        cout << "\n>> Enter details for Student " << (i + 1) << ":";
        students[i].inputStudent();
    }

    // --- Display: show all students ---
    cout << "\n====================================================";
    cout << "\n  DISPLAYING ALL STUDENT RECORDS";
    cout << "\n====================================================";

    for (int i = 0; i < numberOfStudents; i++) {
        cout << "\n  [Student Record " << (i + 1) << "]";
        students[i].displayStudent();
    }

    cout << "\n  Program ended successfully.\n";

    return 0;
}