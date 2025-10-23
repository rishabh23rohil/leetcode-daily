import java.util.*;

class GraphValidTree {
    public boolean validTree(int n, int[][] edges) {
        // 1) Must have exactly n-1 edges
        if (edges.length != n - 1) return false;

        // 2) Use DSU to ensure no cycles and single component
        int[] parent = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        for (int[] e : edges) {
            int a = e[0], b = e[1];
            if (!union(a, b, parent, rank)) {
                // union returns false if a and b already connected => cycle
                return false;
            }
        }
        // If edges == n-1 and we never found a cycle, graph is connected => tree
        return true;
    }

    private int find(int x, int[] parent) {
        if (parent[x] != x) parent[x] = find(parent[x], parent);
        return parent[x];
    }

    private boolean union(int a, int b, int[] parent, int[] rank) {
        int ra = find(a, parent), rb = find(b, parent);
        if (ra == rb) return false; // cycle
        if (rank[ra] < rank[rb]) parent[ra] = rb;
        else if (rank[rb] < rank[ra]) parent[rb] = ra;
        else { parent[rb] = ra; rank[ra]++; }
        return true;
    }
}
