class LRUCache {
    private static class Node {
        int key, value;
        Node prev, next;
        Node(int k, int v) { key = k; value = v; }
    }

    private final int capacity;
    private int size = 0;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node(-1, -1); // dummy head
    private final Node tail = new Node(-1, -1); // dummy tail

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail; tail.prev = head;
    }

    public int get(int key) {
        Node n = map.get(key);
        if (n == null) return -1;
        moveToHead(n);
        return n.value;
    }

    public void put(int key, int value) {
        Node n = map.get(key);
        if (n != null) {
            n.value = value;
            moveToHead(n);
            return;
        }
        Node nn = new Node(key, value);
        map.put(key, nn);
        addAfterHead(nn);
        size++;
        if (size > capacity) {
            Node lru = popTail();
            map.remove(lru.key);
            size--;
        }
    }

    private void moveToHead(Node n) {
        removeNode(n);
        addAfterHead(n);
    }

    private void addAfterHead(Node n) {
        n.prev = head; n.next = head.next;
        head.next.prev = n; head.next = n;
    }

    private void removeNode(Node n) {
        n.prev.next = n.next;
        n.next.prev = n.prev;
    }

    private Node popTail() {
        Node n = tail.prev;
        removeNode(n);
        return n;
    }
}
