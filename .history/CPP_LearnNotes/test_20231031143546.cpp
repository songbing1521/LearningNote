#include<iostream>
using namespace std;
class Person{
    private:
        int age;
    public:
        string name;
        Person(string name, int age){
            this->name = name;
            this->age = age;
        }
        void show(){
            cout << "name: " << name << " age: " << age << endl;
        }
};
int main(){
   Person p1 = Person("p1", 12);
   p1
}