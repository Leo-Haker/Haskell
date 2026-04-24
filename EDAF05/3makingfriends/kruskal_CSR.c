#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

typedef struct {
    int u, v, w;
} Edge;

// ── Union-Find ──────────────────────────────────────────────
int* parent;
int* rank_;

int find(int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];  // path compression (halving)
        x = parent[x];
    }
    return x;
}

int unite(int x, int y) {
    int px = find(x), py = find(y);
    if (px == py) return 0;
    if (rank_[px] < rank_[py]) { int t = px; px = py; py = t; }
    parent[py] = px;
    if (rank_[px] == rank_[py]) rank_[px]++;
    return 1;
}

// ── Parallel Merge Sort ─────────────────────────────────────
void merge(Edge* arr, Edge* tmp, int l, int m, int r) {
    int i = l, j = m, k = l;
    while (i < m && j < r)
        tmp[k++] = (arr[i].w <= arr[j].w) ? arr[i++] : arr[j++];
    while (i < m) tmp[k++] = arr[i++];
    while (j < r) tmp[k++] = arr[j++];
    for (int x = l; x < r; x++) arr[x] = tmp[x];
}

void mergesort(Edge* arr, Edge* tmp, int l, int r, int depth) {
    if (r - l <= 1) return;
    int m = (l + r) / 2;

    if (depth > 0) {
        #pragma omp task
        mergesort(arr, tmp, l, m, depth - 1);
        #pragma omp task
        mergesort(arr, tmp, m, r, depth - 1);
        #pragma omp taskwait
    } else {
        mergesort(arr, tmp, l, m, 0);
        mergesort(arr, tmp, m, r, 0);
    }
    merge(arr, tmp, l, m, r);
}

// ── Kruskal ─────────────────────────────────────────────────
int kruskal(Edge* edges, int n, int m) {
    // sortera kanter
    Edge* tmp = malloc(m * sizeof(Edge));

    #pragma omp parallel
    {
        #pragma omp single
        mergesort(edges, tmp, 0, m, 4);  // depth=4 → 16 trådar
    }
    free(tmp);

    // union-find
    parent = malloc((n+1) * sizeof(int));
    rank_  = malloc((n+1) * sizeof(int));
    for (int i = 0; i <= n; i++) { parent[i] = i; rank_[i] = 0; }

    int total = 0, added = 0;
    for (int i = 0; i < m && added < n-1; i++) {
        if (unite(edges[i].u, edges[i].v)) {
            total += edges[i].w;
            added++;
        }
    }

    free(parent);
    free(rank_);
    return total;
}

// ── Main ────────────────────────────────────────────────────
int main() {
    int n, m;
    (void)scanf("%d %d", &n, &m);

    // CSR — kanter i ett sammanhängande block = cache-vänligt
    Edge* edges = malloc(m * sizeof(Edge));

    for (int i = 0; i < m; i++)
        (void)scanf("%d %d %d", &edges[i].u, &edges[i].v, &edges[i].w);

    printf("%d\n", kruskal(edges, n, m));

    free(edges);
    return 0;
}