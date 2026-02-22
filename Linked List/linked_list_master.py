# ============================================================
# ================== SINGLY LINKED LIST ======================
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ---------- Basic Operations ----------

def insert_at_beginning(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node


def insert_at_end(head, val):
    new_node = Node(val)
    if not head:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head


def delete_value(head, key):
    if not head:
        return None

    if head.data == key:
        return head.next

    temp = head
    while temp.next and temp.next.data != key:
        temp = temp.next

    if temp.next:
        temp.next = temp.next.next

    return head


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# ---------- Reverse Linked List ----------

def reverse_iterative(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def reverse_recursive(head):
    if not head or not head.next:
        return head

    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# ---------- Middle of Linked List ----------

def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# ---------- Detect Cycle (Floyd) ----------

def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# ---------- Merge Two Sorted Lists ----------

def merge_sorted(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


# ---------- Remove Nth Node From End ----------

def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next


# ---------- Intersection of Two Linked Lists ----------

def get_intersection(headA, headB):
    a = headA
    b = headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a


# ---------- Palindrome Linked List ----------

def reverse_helper(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


def is_palindrome(head):
    if not head or not head.next:
        return True

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = reverse_helper(slow)
    first_half = head

    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


# ---------- Rotate Linked List ----------

def rotate_right(head, k):
    if not head or not head.next:
        return head

    temp = head
    length = 1

    while temp.next:
        temp = temp.next
        length += 1

    temp.next = head  # make circular

    k = k % length
    steps = length - k

    while steps:
        temp = temp.next
        steps -= 1

    new_head = temp.next
    temp.next = None
    return new_head


# ============================================================
# ================= DOUBLY LINKED LIST =======================
# ============================================================

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def insert_doubly_at_head(head, val):
    new_node = DNode(val)
    if head:
        head.prev = new_node
        new_node.next = head
    return new_node


# ============================================================
# ================= MULTILEVEL FLATTEN =======================
# ============================================================

class MultiNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


def flatten(head):
    if not head:
        return head

    curr = head
    while curr:
        if curr.child:
            next_node = curr.next
            curr.next = flatten(curr.child)

            temp = curr.next
            while temp.next:
                temp = temp.next

            temp.next = next_node
            curr.child = None

        curr = curr.next

    return head


# ============================================================
# ====================== LRU CACHE ===========================
# ============================================================

class LRUCache:

    class CacheNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = self.CacheNode(0, 0)
        self.tail = self.CacheNode(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove_node(node)
        self._add_node(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            self._remove_node(self.cache[key])
            del self.cache[key]

        if len(self.cache) == self.capacity:
            lru = self.tail.prev
            self._remove_node(lru)
            del self.cache[lru.key]

        new_node = self.CacheNode(key, value)
        self._add_node(new_node)
        self.cache[key] = new_node


# ============================================================
# ========================== MAIN =============================
# ============================================================

if __name__ == "__main__":

    print("Singly Linked List Demo:")

    head = None
    head = insert_at_end(head, 1)
    head = insert_at_end(head, 2)
    head = insert_at_end(head, 3)

    print_list(head)

    head = reverse_iterative(head)
    print("After Reverse:")
    print_list(head)

    middle = find_middle(head)
    print("Middle:", middle.data)

    print("Program executed successfully.")
