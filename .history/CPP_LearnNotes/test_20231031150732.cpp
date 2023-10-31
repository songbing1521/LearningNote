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
        int getAge() { return this->age; }
        void show(){
            cout << "name: " << name << " age: " << age << endl;
        }
        friendly int getPerson
};
class student:public Person{
    private:
        string ID;
    public:
    student(string name, int age, string ID):Person(name, age){
        this->ID = ID;
    }
    void show(){
        cout << "name: " << name << " age: " << getAge() << " ID: " << ID << endl;
    }
};
int main(){
   Person p1 = Person("p1", 12);
   p1.show();
   student stu1 = student("stu1", 13, "123456");
   stu1.show();
}