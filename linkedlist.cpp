#include <iostream>
#include <cstdlib>
#include <string>
#include <typeinfo>
using namespace std;
using std::string;

template <typename E>
class DNode;

template <typename E>
class GDLinkedList{
    public:
        GDLinkedList();
        ~GDLinkedList();
        bool empty() const;
        const E& front() const;
        void addFront(const E& e);
        void removeBack();
        void printList() const;
        
    private:
        DNode<E>* header;
        DNode<E>* trailer;
};

template <typename E>
class DNode {
    private:
        E elem;
        DNode<E>* next;
        DNode<E>* prev;
        friend class GDLinkedList<E>;
};

// template <typename E>
// GDLinkedList<E>::GDLinkedList(): header(NULL), trailer(NULL) {}
template <typename E>
GDLinkedList<E>::GDLinkedList(){
    header = new DNode<E>;
    trailer = new DNode<E>;
    header->next = trailer;
    trailer->prev = header;
}
template <typename E>
GDLinkedList<E>::~GDLinkedList() { while (!empty()) removeBack(); }
template <typename E>
bool GDLinkedList<E>::empty() const { return header == NULL; }
template <typename E>
const E& GDLinkedList<E>::front() const { return header->elem; }

template <typename E>
void GDLinkedList<E>::addFront(const E& e){
    DNode<E>* u = new DNode<E>;
    u->elem = e;
    u->next = header->next;
    u->prev = header;
    u->prev->next = u;
    u->next->prev = u;
}

template <typename E>
void GDLinkedList<E>::removeBack(){
    if (header->next == trailer){
        return;
    }
    DNode<E>* v = trailer->prev;
    DNode<E>* u = v->prev;
    DNode<E>* w = v->next;
    u->next = w;
    w->prev = u;
    delete v;
}

template <typename E>
void GDLinkedList<E>::printList() const {
        DNode<E>* current = header->next;
        while (current != trailer){
            cout << current->elem << "->";
            
            current = current->next;
        }
        cout << "END" << endl;
    }

int main() {
    string input_type;
    string calc_type;

    string num;

    GDLinkedList<int> intll;
    GDLinkedList<string> stringll;

    while (true){
        cin >> input_type;
        if (input_type == "end"){
            // return 0;
            exit(0);
        }
        else if (input_type == "int"){
            cin >> calc_type;
            int intNum;
            if (calc_type == "add"){
                cin >> num;
                intNum = stoi(num);
                intll.addFront(intNum);
            }
            else if (calc_type == "del"){
                intll.removeBack();
            }
            intll.printList();
        }
        else if (input_type == "str") {
            cin >> calc_type;
            if (calc_type == "add"){
                cin >> num;
                stringll.addFront(num);
            }
            else if (calc_type == "del"){
                stringll.removeBack();
            }
            stringll.printList();
        }
        
    }
    
}