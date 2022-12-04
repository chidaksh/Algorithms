#include <iostream>
#include <cmath>
using namespace std;
class V3
{
private:
    double x, y, z;

public:
    V3(double vx, double vy, double vz)
    {
        x = vx;
        y = vy;
        z = vz;
    }
    V3() { x = y = z = 0.0; }
    V3(const V3 &src)
    {
        x = src.x;
        y = src.y;
        z = src.z;
    }
    ~V3()
    {
        if (length() == 0.0)
        {
            cout << "Zero Vector!" << endl;
        }
        return;
    }
    void printLength()
    {
        cout << length() << endl;
        return;
    }
    V3 operator*(double const factor) const
    {
        return V3(factor * x, factor * y, factor * z);
    }
    V3 operator+(V3 const &b) const
    { // denotes that member function can't change receiver object
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
    point(double p, double q)
    {
        x = p;
        y = q;
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

int main()
{
    V3 a, *ptr;
    a.printLength();
    ptr = new V3;
    if (ptr == NULL)
    {
        cout << "memory allocation error" << endl;
        return -1;
    }
    ptr->printLength();
    delete ptr;
    return 0;
    /*V3 a(0.0, 0.0, 0.0);
    V3 b;
    V3 *p, *q;
    p = new V3(1.0, 2.0, 3.0);
    q = new V3();
    delete p, q;
    return 0;*/
}