Here's a polished English version in Markdown format:

# Observations

## Logarithms

Logarithms are the opposite of exponentials.

What does that mean?

For example, if we want to calculate `log₁₀(100)`, we are asking:

> "How many times do we multiply 10 by itself to get 100?"

Since:

```text
10 × 10 = 100
```

we multiplied 10 by itself **2 times**, so:

```text
log₁₀(100) = 2
```

In other words, a logarithm tells us the exponent needed to reach a certain number.

---

### Log Base 2

In this book, we will use only **base-2 logarithms** (`log₂`).

To keep the notation simple, whenever we write **log**, we mean **log₂**.

For example:

```text
log₂(8) = 3
```

because:

```text
2³ = 8
```

---

### Why Is This Important?

Logarithms are commonly used when analyzing algorithms that repeatedly divide a problem in half.

Consider a binary search on an array with 8 elements:

```text
[1, 2, 3, 4, 5, 6, 7, 8]
```

At each step, binary search eliminates half of the remaining elements.

The number of times we can divide 8 by 2 until only one element remains is:

```text
log₂(8) = 3
```

This means binary search needs at most **3 steps** to find an element in an array of 8 sorted items.

As the array grows larger, the number of required steps grows very slowly, which is why binary search is so efficient.
