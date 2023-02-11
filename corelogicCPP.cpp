#include <bits/stdc++.h>
using namespace std;
const int v = 5;
;

int mat[5][5] = {{0, 3, 0, 0, 4}, {3, 0, 2, 0, 5}, {0, 2, 0, 6, 1}, {0, 0, 6, 0, 0}, {4, 5, 1, 0, 0}};
int count2;
void printPathUtil(int u, int d, int visited[v], int path[v], int pi, int count)
{
    //count2++;
    // if(count>20){return 1;}
    visited[u] = 1;
    path[pi] = u;
    pi++;

    if (u == d)
    {
        cout << "path length" << count << endl;
        for (int j = 0; j < pi; j++)
        {
            cout << path[j] << ' ';
        }
        cout << "" << endl;
    }
    else
    {
        int temp[5];

        for (int h = 0; h < v; h++)
        {
            temp[h] = mat[u][h];
        }

        for (int i = 0; i < v; i++)
        {
            // cout << i << endl;
            int temp2 = temp[i];
            if (temp2 != 0 && visited[i] == 0)
            {
                count = count + temp2;
                // cout << i << " " << d << " " << visited[i] << " " << path[pi] << " " << pi << " " << count << " " << endl;
                printPathUtil(i, d, visited, path, pi, count);
                count = count - temp2;
            }
        };
    }
    pi--;
    visited[u] = 0;
}

void printPath(int s, int d)
{
    int count = 0;
    int visited[v];
    int path[v];
    int pi = 0;
    // console.log("entered driver")
    for (int t = 0; t < v; t++)
    {
        visited[t] = 0;
    }
    printPathUtil(s, d, visited, path, pi, count);
}

int main()
{
    // cout << mat[2][3] << endl;
    printPath(0, 3);
}
