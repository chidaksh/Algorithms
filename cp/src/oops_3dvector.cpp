#include <iostream>
#include <cmath>
using namespace std;
int sum(int a, int b);
class V3
{
private:
    double x, y, z;
public:
    V3(){
        x=5;
        y=2;
        z=3;
    }
    V3(double vx,double vy,double vz){
        x = vx;
        y = vy;
        z = vz;
    }
    void printlength()
    {
        cout << length() << endl;
    }
    void sum(V3 const b)
    {
        x = x + b.x;
        y = y + b.y;
        z = z + b.z;
    }
    V3 scale(double const factor)
    {
        V3 v;
        v.x = x * factor;
        v.y = y * factor;
        v.z = z * factor;
        return v;
    }
    void print()
    {
        cout << " x: " << x << " y: " << y << " z: " << z << endl;
    }

private:
    double length() { return sqrt(x * x + y * y + z * z); }
};
int main()
{   
    V3 a(1.0,1.0,1.0);
    a.print();
    //V3 b = a.sum(V3(0,0,0));
    //b.print();
    //a = b;
    a.print();
}
