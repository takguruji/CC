#include <iostream>
#include <queue>
using namespace std;

// Node structure
struct Node {
    char ch;
    int freq;

    Node *left, *right;

    Node(char c, int f) {
        ch = c;
        freq = f;
        left = right = NULL;
    }
};

// Compare nodes based on frequency
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

// Print Huffman codes
void printCodes(Node* root, string code) {
    if (root == NULL)
        return;

    if (root->left == NULL && root->right == NULL) {
        cout << root->ch << " : " << code << endl;
    }

    printCodes(root->left, code + "0");
    printCodes(root->right, code + "1");
}

// Build Huffman Tree
void huffman(char chars[], int freq[], int n) {

    priority_queue<Node*, vector<Node*>, Compare> pq;

    // Insert all characters
    for (int i = 0; i < n; i++) {
        pq.push(new Node(chars[i], freq[i]));
    }

    // Build tree
    while (pq.size() > 1) {

        Node* left = pq.top();
        pq.pop();

        Node* right = pq.top();
        pq.pop();

        Node* parent = new Node('$',
                                left->freq + right->freq);

        parent->left = left;
        parent->right = right;

        pq.push(parent);
    }

    // Print codes
    cout << "Huffman Codes:\n";
    printCodes(pq.top(), "");
}

int main() {

    int n;

    cout << "Enter number of characters: ";
    cin >> n;

    char chars[n];
    int freq[n];

    cout << "Enter characters:\n";
    for (int i = 0; i < n; i++) {
        cin >> chars[i];
    }

    cout << "Enter frequencies:\n";
    for (int i = 0; i < n; i++) {
        cin >> freq[i];
    }

    huffman(chars, freq, n);

    return 0;
}
