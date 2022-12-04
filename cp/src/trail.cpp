#include <iostream>
#include <typeinfo>

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
    int chida(){
        return this->x;
    }
    ~point(){
        std::cout << "X-coordinate is " << this->x << std::endl;
        std::cout << "Y-coordinate is " << this->y << std::endl;
        std::cout << "Type of the variable this is " << typeid(this).name() << std::endl;
        return;
    }
};

int main()
{
    int a = 2;
    int *p = new int[4];
    for (int i = 0; i < 4; i++)
    {
        p[i] = i * 10;
    }
    std::cout << "Type of a is " << typeid(a).name() << std::endl;
    std::cout << "Tyoe of &a is " << typeid(&a).name() << std::endl;
    std::cout << "Type of p is " << typeid(p).name() << std::endl;
    std::cout << "Type of *p is " << typeid(*p).name() << std::endl;
    std::cout << "Value of p is " << p << std::endl;
    std::cout << "Value of *p is " << *p << std::endl;
    std::cout << "Value of p+1 is " << p + 1 << std::endl;
    std::cout << "Value of *(p+1) is " << *(p + 1) << std::endl;
    std::cout << "Value of *p+1 is " << *p + 1 << std::endl;
    std::cout << "------------------------------------------------------------------" << std::endl;

    point X(1.0,2.0);
    point *Y = new point(3.0,4.0);
    point &Z = X;
    point A = X;
    std::cout << "Type of X is " << typeid(X).name() << std::endl;
    std::cout << "Type of &X is " << typeid(&X).name() << std::endl;
    std::cout << "Type of *&X is " << typeid(*&X).name() << std::endl;
    std::cout << "Type of Y is " << typeid(Y).name() << std::endl;
    std::cout << "Type of *Y is " << typeid(*Y).name() << std::endl;
    std::cout << "------------------------------------------------------------------" << std::endl;
    std::cout << "Type of Z is " << typeid(Z).name() << std::endl;
    std::cout << "Size of class point is " << sizeof(point) << std::endl;
    std::cout << "Size of Z is " << sizeof(Z) << std::endl;
    std::cout << "The Value of address of X is " << &X << std::endl;
    std::cout << "The Value of address of Z is " << &Z << std::endl;
    std::cout << "The Value of address of A is " << &A << std::endl;
    std::cout << "The Value of X-cordinate in X,Z,A are " << X.chida() << " " << Z.chida()  << " " << A.chida() << std::endl;
    std::cout << "------------------------------------------------------------------" << std::endl;
    delete Y;
    delete p;
    return 0;
}