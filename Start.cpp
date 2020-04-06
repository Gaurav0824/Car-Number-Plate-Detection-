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

int i=0;

// char files[50][30];
// void directory();
// void directory()
// { 
//     // const char str[10]=".";
//     // DIR *dir;
//     // struct dirent *ent;

//     // if ((dir = opendir (str)) != NULL)
//     // {
//     //     // print all the files and directories within directory
//     //     while ((ent = readdir (dir)) != NULL)
//     //     {
//     //         sprintf(files[i++],"%s \\ ",ent->d_name); 
//     //         //printf("%s \n",ent->d_name);  
//     //     }
//     //     closedir (dir);
//     // }
//     // else
//     // {
//     //     cout<<"could not open directory";
//     //     perror ("");
//     // }

//     getch();
// }

int main()
{
    //directory();
    char line[50]; 
    char cmd[70];
    system("DIR .\\*.jpg /B > file.txt");
    fstream file;
    file.open("fil.txt",ios::in);
    // while(file)
    // {   
        strcpy(cmd," python test_image.py  ");
        file>>line;
        //cout<<line<<endl;
        strcat(cmd,line);
        cout<<cmd<<endl;
        system(cmd);
    // }
    file.close();

}

