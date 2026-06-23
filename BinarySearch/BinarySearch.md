# Binary Search

## What is Binary Search?

Imagine you are looking for a person's name in a phone book.

Suppose you want to find a name that starts with the letter **K**.

Would you start reading from the first page and check every name one by one?

Probably not.

A faster approach would be to open the phone book somewhere in the middle. If the names on that page start with letters before **K**, you know the name must be in the second half of the book. If they start with letters after **K**, you know it must be in the first half.

By repeatedly dividing the search area in half, you can find the desired name much faster.

This is exactly how **Binary Search** works.

---

## Definition

Binary Search is an algorithm used to find an element in a **sorted list**.

Instead of checking each element one by one, it:

1. Looks at the middle element.
2. Compares it with the target value.
3. Discards half of the remaining elements.
4. Repeats the process until the target is found or the search space becomes empty.

Because it eliminates half of the data at each step, Binary Search is much more efficient than a linear search.

---

## Example

Consider the following sorted list:

```text
[1, 3, 5, 7, 9, 11, 13]
```

Let's search for the number **11**.

### Step 1

Check the middle element:

```text
[1, 3, 5, 7, 9, 11, 13]
          ^
          7
```

Since `11 > 7`, we can ignore everything on the left side.

### Step 2

Search only in:

```text
[9, 11, 13]
     ^
     11
```

The middle element is `11`.

Target found!

---

## Time Complexity

### Linear Search

A linear search checks each element one by one.

```text
O(n)
```

### Binary Search

Binary Search cuts the search space in half on every step.

```text
O(log n)
```

This makes it significantly faster for large datasets.

For example:

| Number of Elements | Maximum Checks |
| ------------------ | -------------- |
| 1,000              | ~10            |
| 1,000,000          | ~20            |
| 1,000,000,000      | ~30            |

---

## Requirements

Binary Search only works correctly if the data is **sorted**.

For example:

✅ Sorted

```text
[1, 3, 5, 7, 9, 11]
```

❌ Unsorted

```text
[7, 1, 11, 3, 9, 5]
```

If the list is not sorted, Binary Search cannot determine which half should be discarded.

---
