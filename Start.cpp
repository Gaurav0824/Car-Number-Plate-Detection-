#include<iostream>
#include<regex>

using namespace std;

int main()
{
    const char *first = "abc";
    regex rx("a(b)c");
    
    bool found = regex_match(first,rx);
    if (found)
        wcout << L"Regex found in abc" << endl;
}