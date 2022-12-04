#include <iostream>
using namespace std;

class base
{
public:
    int id;
    float balance;
    char name[];
};

class savings : public base
{
public:
    int age;
    long int ATM;
};

class current : public base
{
public:
    int amount;
    int overdraft;
};

class B
{
private:
    int m1;

public:
    int m2;

protected:
    int m3;

public:
    void start()
    {
        cin >> m1;
        cin >> m2;
        cin >> m3;
    }
};

class D1 : public B
{
private:
    int x1;

public:
    int x2;

protected:
    int x3;

public:
    void f1()
    {
        cin >> x1;
        cin >> x2;
        cin >> x3;
        return;
    }
    // void f2()
    // {
    //     cin >> m1;
    //     cin >> m2;
    //     cin >> m3;
    //     return;
    // }
};

int main()
{
    savings s;
    s.id = 1;
    s.age = 20;
    cout << "s.id is " << s.id << endl;
    cout << "s.age is " << s.age << endl;
    current c;
    c.id = 2;
    c.amount = 10000;
    cout << "c.id is " << c.id << endl;
    cout << "c.amount is " << c.amount << endl;
    cout << "-------------------------------------------" << endl;
    D1 d;
    cout << "d.m1 gives error since m1 is private " << endl;
    cout << d.m2 << endl; // can be accessed since it's public
    cout << "d.m3 error since m3 is protected it can be only accessed inside d1 not inside main " << endl;
    cout << "-------------------------------------------" << endl;
    return 0;
}