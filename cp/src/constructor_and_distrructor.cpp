#include<iostream>
using namespace std;
class point{
    private:
        double x,y;
    public:
        point(double p , double q){x = p ; y = q;}
};
class disk {
    private :
        point centre ; double radius ;
    public :
        disk(double x ,double y,double r):
            centre(point(x,y)),radius(r){;}
};
int main(){
    int a;
    cout<<"happy"<<endl;
    cin>>a;
    return 0;
}