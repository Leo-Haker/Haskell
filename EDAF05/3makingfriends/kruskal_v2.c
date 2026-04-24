#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int w;
    int u;
    int v;
} Edge;

/* ───────────────────────── UNION-FIND ───────────────────────── */

int* parent;
int* rank_;

static inline int find(int x) {
    int root = x;

    while (parent[root] != root)
        root = parent[root];

    while (x != root) {
        int p = parent[x];
        parent[x] = root;
        x = p;
    }

    return root;
}

static inline int unite(int a, int b) {
    int pa = find(a);
    int pb = find(b);

    if (pa == pb) return 0;

    if (rank_[pa] < rank_[pb]) {
        int t = pa; pa = pb; pb = t;
    }

    parent[pb] = pa;

    if (rank_[pa] == rank_[pb])
        rank_[pa]++;

    return 1;
}

/* ───────────────────────── RADIX SORT ───────────────────────── */

#define BUCKETS 65536

static int count[BUCKETS];

static void radix_sort(Edge* a, Edge* tmp, int n) {
    memset(count, 0, sizeof(count));

    for (int i = 0; i < n; i++)
        count[a[i].w & 0xFFFF]++;

    for (int i = 1; i < BUCKETS; i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--)
        tmp[--count[a[i].w & 0xFFFF]] = a[i];

    memset(count, 0, sizeof(count));

    for (int i = 0; i < n; i++)
        count[(tmp[i].w >> 16) & 0xFFFF]++;

    for (int i = 1; i < BUCKETS; i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--)
        a[--count[(tmp[i].w >> 16) & 0xFFFF]] = tmp[i];
}

/* ───────────────────────── KRUSKAL ───────────────────────── */

static long long kruskal(Edge* edges, int n, int m) {
    Edge* tmp = (Edge*)malloc(m * sizeof(Edge));

    radix_sort(edges, tmp, m);
    free(tmp);

    parent = malloc((n + 1) * sizeof(int));
    rank_ = malloc((n + 1) * sizeof(int));

    for (int i = 0; i <= n; i++) {
    parent[i] = i;
    rank_[i] = 0;
}

    long long total = 0;
    int used = 0;

    for (int i = 0; i < m && used < n - 1; i++) {
        if (unite(edges[i].u, edges[i].v)) {
            total += edges[i].w;
            used++;
        }
    }

    free(parent);
    free(rank_);

    return total;
}

/* ───────────────────────── MAIN ───────────────────────── */

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    Edge* edges = (Edge*)malloc(m * sizeof(Edge));

    for (int i = 0; i < m; i++)
        scanf("%d %d %d", &edges[i].u, &edges[i].v, &edges[i].w);

    printf("%lld\n", kruskal(edges, n, m));

    free(edges);
    return 0;
}