#include <bits/stdc++.h>
#include <SFML/Audio.hpp>
using namespace std;

bool sig = true;

void error(int code) {
    cerr << "Error! Code: " << code << endl;
    exit(code);
}

int main() {
    signal(SIGINT, [](int) {
        sig = false;
    });

    // generate the heart
    if (system("python3 generate_heart.py > heart.txt && clear")) error(1);
    ifstream f("heart.txt");
    if (!f) error(2);

    // display the music
    sf::Music music;
    if (!music.openFromFile("Funky_Town.ogg")) error(3);
    music.setLooping(true);
    music.play();

    cout << "\033[?25l";  // hide the cursor

    vector<string> lines;
    string str;
    int cnt;
    for (cnt = 0; getline(f, str); cnt++) {
        if (str[0] != '0') break;
        lines.push_back(str);
    }
    int len = lines[0].size();
    
    int theta, mid = len / 2, loc;
    for (theta = 0; sig; theta = (theta + 1) % 360) {
        cout << "\t\t\t\t   Happy Valentine's Day!\n";
        for (int i = 0; i < round(3 + 3 * cos(theta * M_PI / 180)); i++) {
            cout << '\n';
        }
        for (int i = 0; i < cnt; i++) {
            str.assign(len, ' ');
            for (int j = 1; j < len; j++) {
                loc = round((j - mid) * cos(theta * M_PI / 180)) + mid;
                if (str[loc] != '#') {
                    str[loc] = lines[i][j];
                }
            }
            cout << str << '\n';
        }
        cout << endl;
        usleep(10000);
        system("clear");
    }

    cout << "\033[?25h";  // show the cursor
    cout << "Thanks for watching! ❤️\n";
    return 0;
}
