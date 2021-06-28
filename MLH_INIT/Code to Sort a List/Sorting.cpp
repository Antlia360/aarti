
#include <iostream>
#include <list>
using namespace std;

int main()
{

    list<int> mylist{10, 24, 57, 10, 8, 0}; // list declaration of integer type

    mylist.sort(); // sort function

    for (auto it = mylist.begin(); it != mylist.end(); ++it) // printing the list after sort
        cout << ' ' << *it;
    return 0;
}