#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>

// #include<iostream>
// #include<regex>
// #include<dirent.h>
// #include<dir.h>
// #include<direct.h>
// #include<process.h>
// #include<dos.h>

// #include <iostream>
// #include <fstream>
// #include <cstring>
// #include <string.h>
// #include <iomanip>
// #include <cstdio>
// #include <conio.h>
// #include <ctime>
// #include <stdlib.h>
// #include <bits/stdc++.h>

// #include<windows.h>

using namespace std;

int main()
{
    //directory();
    char line[50]; 
    char cmd[70];
    // system("cd > cwd.txt");
    system("DIR *.jpg /B > jpgfiles.txt");
    fstream file;
    file.open("jpgfiles.txt",ios::in|ios::out);
    while(file)
    {   
        strcpy(cmd," python test_image.py ");
        file>>line;
        //cout<<line<<endl;
        strcat(cmd,line);
        cout<<cmd<<endl;
        system(cmd);
    }
    file.close();

}

