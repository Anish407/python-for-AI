# NumPy Broadcasting

## 1. What is Broadcasting?

**Broadcasting** is a NumPy feature that allows mathematical operations between arrays of different shapes without explicitly using loops or manually repeating elements.

For example:

```python
import numpy as np

a = np.array([10, 20, 30])
b = 5

result = a + b
# [15, 25, 35]
```

NumPy conceptually expands `5` to `[5, 5, 5]` and performs element-wise addition.

**Important:** NumPy does not necessarily create a physically expanded array in memory. Broadcasting avoids unnecessary copies where possible.

---

## 2. Rules of Broadcasting

NumPy compares the shapes of two arrays **from right to left**, starting with the last (trailing) dimension.

Two dimensions are compatible when:

1. **Both dimensions have the same size.**
2. **One of the dimensions has size `1`.**
3. **If an array has fewer dimensions, its missing leading dimensions are treated as `1`.**

If any pair of aligned dimensions violates these rules, NumPy raises a `ValueError`.

### Rule 1: Dimensions Are Equal

```text
Array A: (3, 4)
Array B: (3, 4)
----------------
Result:  (3, 4) ✅
```

Both dimensions match exactly. NumPy performs element-wise operations.

### Rule 2: One Dimension Is 1

```text
Array A: (3, 4)
Array B: (1, 4)
----------------
Result:  (3, 4) ✅
```

The dimension with size `1` is broadcast to match size `3`.

Another example:

```text
Array A: (3, 4)
Array B: (3, 1)
----------------
Result:  (3, 4) ✅
```

The second dimension of B expands conceptually from `1` to `4`.

### Rule 3: Missing Leading Dimensions Are Treated as 1

```text
Array A: (3, 4)
Array B:    (4)
```

Align dimensions from the right:

```text
Array A: (3, 4)
Array B: (1, 4)
----------------
Result:  (3, 4) ✅
```

The 1D array is broadcast across all three rows.

### Rule 4: Incompatible Dimensions Cause an Error

```text
Array A: (3, 4)
Array B:    (3)
```

Align dimensions from the right:

```text
Array A: (3, 4)
Array B: (1, 3)
               ❌
```

The trailing dimensions `4` and `3` are incompatible because they are different and neither equals `1`.

**Result:** `ValueError: operands could not be broadcast together`

---

## 3. How to Calculate the Resulting Shape

Follow these steps:

1. Write the shapes of both arrays.
2. Align their dimensions from the **right**.
3. Add leading dimensions of size `1` where necessary.
4. Compare each pair of aligned dimensions.
5. If compatible, take the larger size of each pair to determine the resulting shape.

**Example:**

```text
Array A: (5, 1, 4)
Array B: (1, 3, 1)
------------------
Result:  (5, 3, 4) ✅
```

Dimension-by-dimension comparison:

| Dimension | Array A | Array B | Result |
|---|---|---|---|
| First | 5 | 1 | 5 |
| Second | 1 | 3 | 3 |
| Third | 4 | 1 | 4 |

Final shape: `(5, 3, 4)`

---

## 4. Row Broadcasting vs Column Broadcasting

Consider this matrix:

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

### A. Broadcasting Across Rows (Adding to Each Column)

```python
b = np.array([10, 20, 30])

result = a + b
```

Shapes:

```text
a: (3, 3)
b:    (3)
------------
   (3, 3)
```

Output:

```text
[[11 22 33]
 [14 25 36]
 [17 28 39]]
```

The vector `[10, 20, 30]` is added to every row.

### B. Broadcasting Down Columns (Adding to Each Row)

```python
b = np.array([
    [10],
    [20],
    [30]
])

result = a + b
```

Shapes:

```text
a: (3, 3)
b: (3, 1)
------------
   (3, 3)
```

Output:

```text
[[11 12 13]
 [24 25 26]
 [37 38 39]]
```

Each value in `b` is added to the corresponding row.

**Key difference:**

- `(3,)` — 1D array, aligned with the last dimension.
- `(1, 3)` — 2D row vector, broadcast down rows.
- `(3, 1)` — 2D column vector, broadcast across columns.

Although `(3,)` and `(1, 3)` behave similarly when added to a `(3, 3)` matrix, they are not the same shape.

---

## 5. Using `np.newaxis` to Control Broadcasting

`np.newaxis` (or `None`) inserts an additional dimension into an array.

```python
b = np.array([10, 20, 30])

b.shape                # (3,)
b[np.newaxis, :].shape # (1, 3)
b[:, np.newaxis].shape # (3, 1)
```

Example:

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = np.array([10, 20, 30])

a + b                 # Add to each column
a + b[:, np.newaxis]  # Add to each row
```

`np.newaxis` is particularly useful when broadcasting vectors against matrices and higher-dimensional arrays.

---

## 6. Broadcasting Compatibility Cheat Sheet

| Array A | Array B | Result | Valid? |
|---|---|---|---|
| `(3, 4)` | `(3, 4)` | `(3, 4)` | ✅ |
| `(3, 4)` | `(4,)` | `(3, 4)` | ✅ |
| `(3, 4)` | `(3,)` | Error | ❌ |
| `(3, 4)` | `(3, 1)` | `(3, 4)` | ✅ |
| `(3, 4)` | `(1, 4)` | `(3, 4)` | ✅ |
| `(5, 1)` | `(1, 4)` | `(5, 4)` | ✅ |
| `(2, 3, 4)` | `(3, 1)` | `(2, 3, 4)` | ✅ |
| `(2, 3, 4)` | `(2, 4)` | Error | ❌ |

---

## 7. Broadcasting in Machine Learning

Broadcasting is commonly used for feature normalization, neural network bias addition, and other vectorized mathematical operations.

### Example: Feature Standardization

```python
X = np.array([
    [25, 50000, 2],
    [30, 60000, 5],
    [35, 70000, 8]
])

mean = X.mean(axis=0)
std = X.std(axis=0)

X_scaled = (X - mean) / std
```

Shapes:

```text
X:       (3, 3)
mean:       (3,)
std:        (3,)
----------------
X_scaled: (3, 3)
```

Each column is normalized using its corresponding feature mean and standard deviation.

### Example: Neural Network Bias Addition

```python
outputs = np.array([
    [0.2, 0.5, 0.8],
    [0.1, 0.4, 0.7]
])

bias = np.array([0.1, 0.2, 0.3])

result = outputs + bias
```

Shapes:

```text
outputs: (2, 3)
bias:       (3,)
----------------
result:  (2, 3)
```

The same bias vector is added to every sample in the batch.

---

## 8. Key Takeaways

- Broadcasting allows operations on arrays with different but compatible shapes.
- **Always compare dimensions from right to left.**
- Dimensions are compatible if they match or if one equals `1`.
- Missing leading dimensions are treated as `1`.
- The resulting shape uses the maximum size of each aligned dimension.
- Broadcasting does not necessarily allocate repeated copies of the smaller array.
- `np.newaxis`, `None`, and `reshape()` help control broadcasting.
- Broadcasting is fundamental to efficient NumPy operations and PyTorch tensor computations.

**Golden Rule:**

> Align shapes from the right. For each dimension, the sizes must be equal or one must be `1`. Otherwise, broadcasting fails.

## 9. How NumPy Expands the Smaller Array During Broadcasting

Broadcasting works by **conceptually expanding an array's dimensions** so its shape is compatible with the larger array.

There are two important mechanisms:

1. **Adding missing dimensions to the left (head) of the shape.**
2. **Expanding dimensions whose size is `1` to match the other array.**

### Rule 1: Add Missing Dimensions of Size 1 to the Left

When two arrays have different numbers of dimensions (`ndim`), NumPy conceptually adds `1`s to the **left side** of the shape with fewer dimensions.

Example:

```text
Array A: (3, 4)
Array B:    (4)
```

Array B has one dimension, while A has two dimensions.

NumPy treats the shapes as:

```text
Array A: (3, 4)
Array B: (1, 4)  ← Added 1 to the left
```

Now both arrays have two dimensions.

Because the dimensions are compatible, broadcasting succeeds.

Another example:

```text
Array A: (2, 3, 4)
Array B:       (4)
```

NumPy conceptually adds two leading dimensions of size `1`:

```text
Array A: (2, 3, 4)
Array B: (1, 1, 4)
```

The final broadcast shape is `(2, 3, 4)`.

**Important:** Adding leading `1`s is a conceptual alignment rule. NumPy does not need to reshape or copy the original array explicitly.

---

### Rule 2: Expand Dimensions of Size 1

After aligning dimensions, NumPy can broadcast a dimension of size `1` to match the corresponding dimension of the other array.

Example:

```text
Array A: (3, 4)
Array B: (1, 4)
```

Array B has only one row.

Consider:

```python
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

b = np.array([[10, 20, 30, 40]])
```

Conceptually, NumPy broadcasts B as:

```text
Original B:

[[10, 20, 30, 40]]

Broadcasted B:

[[10, 20, 30, 40],
 [10, 20, 30, 40],
 [10, 20, 30, 40]]
```

Then element-wise addition happens:

```text
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12]]

           +

[[10, 20, 30, 40],
 [10, 20, 30, 40],
 [10, 20, 30, 40]]

           =

[[11, 22, 33, 44],
 [15, 26, 37, 48],
 [19, 30, 41, 52]]
```

**The row is repeated conceptually, not necessarily physically in memory.**

---

### Rule 3: A Dimension of Size 1 Can Expand in Any Position

Broadcasting is not restricted to the first or last dimension.

Example:

```text
Array A: (3, 4)
Array B: (3, 1)
```

Here, the last dimension of B is `1`.

```python
b = np.array([
    [10],
    [20],
    [30]
])
```

NumPy conceptually expands B horizontally:

```text
Original B:

[[10],
 [20],
 [30]]

Broadcasted B:

[[10, 10, 10, 10],
 [20, 20, 20, 20],
 [30, 30, 30, 30]]
```

Now it can perform element-wise addition with the `(3, 4)` array.

---

### Rule 4: Both Arrays Can Be Broadcast Simultaneously

It is not always only the smaller array that gets broadcast.

Example:

```text
Array A: (3, 1)
Array B: (1, 4)
```

NumPy compares each dimension:

```text
             Dimension 1   Dimension 2
Array A:         3             1
Array B:         1             4
Result:          3             4
```

Both arrays expand conceptually to `(3, 4)`.

```python
a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([[10, 20, 30, 40]])

result = a + b
```

Conceptually:

```text
A becomes:             B becomes:

[[1, 1, 1, 1],         [[10, 20, 30, 40],
 [2, 2, 2, 2],          [10, 20, 30, 40],
 [3, 3, 3, 3]]          [10, 20, 30, 40]]
```

Result:

```text
[[11, 21, 31, 41],
 [12, 22, 32, 42],
 [13, 23, 33, 43]]
```

---

### Rule 5: Dimensions Other Than 1 Cannot Be Expanded Arbitrarily

Example:

```text
Array A: (3, 4)
Array B: (3, 2)
```

Compare the trailing dimensions:

```text
4 vs 2 ❌
```

Neither value is `1`, so NumPy cannot broadcast these shapes.

It raises a `ValueError`.

NumPy does **not** repeat a dimension of size `2` to make it size `4`, even though `4` is divisible by `2`.

---

## 10. Broadcasting: Summary of Expansion Rules

| Operation | Rule |
|---|---|
| Add dimensions | Missing dimensions are treated as `1` on the left |
| Expand dimensions | Dimensions of size `1` can expand to match another dimension |
| Matching dimensions | Equal sizes require no expansion |
| Incompatible dimensions | Different sizes where neither is `1` cause an error |
| Expand both arrays | Both operands may broadcast simultaneously |
| Memory | Broadcasting generally avoids explicitly copying repeated values |

### Mental Model

Given two shapes:

```text
A: (2, 1, 4)
B:    (3, 1)
```

**Step 1 — Add missing leading dimensions:**

```text
A: (2, 1, 4)
B: (1, 3, 1)
```

**Step 2 — Compare from right to left:**

```text
4 vs 1 → 4
1 vs 3 → 3
2 vs 1 → 2
```

**Step 3 — Determine the final shape:**

```text
Result: (2, 3, 4)
```

**Remember:**

> First align the shapes by adding missing `1`s to the left. Then expand dimensions of size `1` wherever necessary. NumPy applies the operation element by element using the resulting broadcast shape.