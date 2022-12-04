#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
class V3
{
private:
    double x, y, z;

public:
    V3(double vx, double vy, double vz) // ordinary constructor
    {
        x = vx;
        y = vy;
        z = vz;
    }

    V3() { x = y = z = 0.0; } // default constructor

    V3(const V3 &src) // copy constructor
    {
        x = src.x;
        y = src.y;
        z = src.z;
        cout << "copy constructor called!" << endl;
    }

    ~V3()
    {
        if (length() == 0.0)
        {
            cout << "Zero Vector!" << endl;
        }
        return;
    }

    void sum(V3 const b)
    {
        x = x + b.x;
        y = y + b.y;
        z = z + b.z;
    }

    V3 scale(const double factor)
    {
        V3 v;
        v.x = factor * x;
        v.y = factor * y;
        v.z = factor * z;
        return v;
    }

    void printLength()
    {
        cout << length() << endl;
        return;
    }

    V3 operator*(const double factor) const
    {   // replaces the function scale
        return V3(factor * x, factor * y, factor * z);
    }

    V3 operator+(const V3 &b) const
    {   // replaces the function sum
        // denotes that member function can't change receiver object
        return V3(x + b.x, y + b.y, z + b.z);
    }

private:
    double length() { return sqrt(x * x + y * y + z * z); }
};

class point
{
private:
    double x, y;

public:
    static int count;
    point(){count ++; return;}
    point(double p, double q)
    {
        x = p;
        y = q;
        count++;
        return;
    }
};

class disk
{
private:
    point center;
    double radius;

public:
    disk(double x, double y, double r) : center(point(x, y)), radius(r) { return; }
};

class mystring
{

public:
    char *cArray;
    int length;

    mystring(const char initstring[])
    { // ordinary constructor
        int i = 0;
        while (initstring[i] != '\0')
        {
            i++;
        }
        length = i;
        cArray = new char[length + 1];
        if (cArray == NULL)
        {
            cout << "Unexpected Error Occured!" << endl;
            return;
        }
        for (int j = 0; j <= length; j++)
        {
            cArray[j] = initstring[j];
        }
        cout << "Your name is " << cArray << " of length " << length << endl;
    }

    ~mystring()
    { // destructor
        delete[] cArray;
        return;
    }

    mystring(const mystring &source) : length(source.length)
    { // copy constructor
        cArray = new char[length + 1];
        if (cArray == NULL)
        {
            cout << "Unexpected Error Occured!" << endl;
            return;
        }
        else
        {
            for (int i = 0; i <= length; i++)
            {
                cArray[i] = source.cArray[i];
            }
        }
        return;
    }
};

int main()
{   
    int point::count = 0;
    V3 a(1.0, 2.0, 3.0);
    V3 temp = a;
    V3 b = a.scale(4.0);
    b.printLength();
    V3 *p, *q;
    p = new V3(0.0, 0.0, 0.0);
    q = new V3();
    // q->printLength();
    delete p;
    delete q;
    string name;
    cout << "Enter name: " << endl;
    cin >> name;
    int len = name.length();
    char name_array[len + 1];
    strcpy(name_array, name.c_str());
    mystring z(name_array);
    return 0;
}