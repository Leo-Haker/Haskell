#include <stdio.h>
#include <stdlib.h>

/*
kruskal_CSR.c 10 körningar:
real    0m 35.599s
user    0m 23.165s
sys     0m 3.518s

kruskal_v2.c 10 körningar:
real    0m 42.634s
user    0m 5.448s
sys     0m 3.469s

jarnik.c 10 körningar:
real    0m 53.785s
user    0m 23.765s
sys     0m 3.923s

pypy jarnik.py 10 körningar:
real    6m 43.237s
user    5m 54.661s
sys     0m 20.619s



*/


typedef struct {
    int w, u, v
} Edge;

Edge* heap;
int heap_size = 0;

void swap(int i, int j) {
    Edge tmp = heap[i];
    heap[i] = heap[j];
    heap[j] = tmp;
}

void heappush(int w, int u, int v) {
    heap[heap_size] = (Edge){w, u, v};
    int i = heap_size++;
    while (i > 0){
        int parent = (i - 1) /2; 
        if (heap[parent].w > heap[i].w) {
            swap(parent, i);
            i = parent;
        } else break;
    }
}

Edge heappop(){
    Edge min = heap[0];
    heap[0] = heap[--heap_size];
    int i = 0;
    while (1) {
        int left = 2*i+1, right = 2*i+2, smallest = i;
        if(left < heap_size && heap[left].w < heap[smallest].w) smallest = left;
        if(right < heap_size && heap[right].w < heap[smallest].w) smallest = right;
        if (smallest == i) break;
        swap(i, smallest);
        i = smallest;
    }
    return min;
}

int jarnik(int n, int* adj_w, int* adj_v, int* adj_next, int* head, int root){
    int visited[n+1];
    for (int i = 0; i <= n; i++) visited[i] = 0;
    visited[root] = 1;

    //lägger till alla kanter från root
    for(int e = head[root]; e != -1; e = adj_next[e])
        heappush(adj_w[e], root, adj_v[e]);

    int total = 0;

    while (heap_size > 0) {
        Edge edge = heappop();
        int w = edge.w, u = edge.u, v = edge.v;

        if (visited[v]) continue;
        visited[v] = 1;
        total += w;

        for (int e = head[v]; e != -1; e = adj_next[e])
            if (!visited[adj_v[e]])
                heappush(adj_w[e], v, adj_v[e]);
    }

    return total;
}

int main() {
    int n, m;
    (void)scanf("%d %d", &n, &m);

    int* head    = malloc((n+1) * sizeof(int));
    int* adj_v   = malloc(2*m  * sizeof(int));
    int* adj_w   = malloc(2*m  * sizeof(int));
    int* adj_next= malloc(2*m  * sizeof(int));
    Edge* heap_arr = malloc(2*m * sizeof(Edge));
    heap = malloc(2*m * sizeof(Edge));

    for (int i = 0; i <= n; i++) head[i] = -1;

    for (int i = 0; i < m; i++){
        int u, v, w;
        (void)scanf("%d %d %d", &u, &v, &w);

        //lägg till båda riktningarna
        adj_v[2*i] = v; adj_w[2*i] = w; adj_next[2*i] = head[u]; head[u] = 2*i;
        adj_v[2*i + 1] = u; adj_w[2*i +1] = w; adj_next[2*i+1] = head[v]; head[v] = 2*i+1;

    }

    printf("%d\n", jarnik(n, adj_w, adj_v, adj_next, head, 1));
    free(head); free(adj_v); free(adj_w); free(adj_next); free(heap_arr);
    return 0;
}