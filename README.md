# 🔍 String Matching Algorithms in Python

This repository contains Python implementations of different **String Matching Algorithms** used in **Design and Analysis of Algorithms (DAA)**.  

The programs demonstrate how pattern searching works using:
- Naive String Matching
- Rabin-Karp Algorithm
- Knuth-Morris-Pratt (KMP) Algorithm
- Additional pattern matching implementations

These algorithms are widely used in:
- Text processing
- Search engines
- DNA sequence matching
- Compiler design
- Cybersecurity
- Intrusion detection systems

---

# 📂 Repository Structure

```text
.
├── input1.txt
├── pattern.txt
├── sample1.py
├── sample2.py
├── sample3.py
├── sample4.py
├── sample5.py
└── README.md
```

---

# 📄 File Description

| File Name | Description |
|---|---|
| `input1.txt` | Contains the input text |
| `pattern.txt` | Contains the pattern to search |
| `sample1.py` | Naive String Matching Algorithm |
| `sample2.py` | Rabin-Karp Algorithm |
| `sample3.py` | KMP Algorithm |
| `sample4.py` | Additional string matching implementation |
| `sample5.py` | Additional pattern searching program |

---

# 🧠 Algorithms Implemented

---

## 1️⃣ Naive String Matching Algorithm

### 📌 Description
The Naive String Matching algorithm checks for the pattern at every possible position in the text.

### ⚙️ Working
- Compare pattern characters with text characters one by one
- Shift pattern by one position after mismatch

### ✅ Advantages
- Easy to implement
- Good for small inputs

### ❌ Disadvantages
- Inefficient for large text

### ⏱ Time Complexity

| Case | Complexity |
|---|---|
| Best Case | `O(n)` |
| Worst Case | `O(nm)` |

Where:
- `n` = length of text
- `m` = length of pattern

---

## 2️⃣ Rabin-Karp Algorithm

### 📌 Description
Rabin-Karp uses **hashing** to search patterns efficiently.

### ⚙️ Working
- Compute hash value for pattern
- Compute hash value for text window
- Compare hash values first
- If hashes match, compare actual characters

### ✅ Advantages
- Efficient for multiple pattern searching
- Faster average performance

### ❌ Disadvantages
- Hash collisions may occur

### ⏱ Time Complexity

| Case | Complexity |
|---|---|
| Average Case | `O(n + m)` |
| Worst Case | `O(nm)` |

---

## 3️⃣ Knuth-Morris-Pratt (KMP) Algorithm

### 📌 Description
KMP improves searching efficiency using an **LPS array** (Longest Prefix Suffix).

### ⚙️ Working
- Preprocess pattern
- Avoid unnecessary comparisons
- Reuse previous matching information

### ✅ Advantages
- Very efficient
- No repeated comparisons

### ❌ Disadvantages
- Slightly complex implementation

### ⏱ Time Complexity

| Case | Complexity |
|---|---|
| Best Case | `O(n + m)` |
| Average Case | `O(n + m)` |
| Worst Case | `O(n + m)` |

---

# 🛠 Technologies Used

- Python 3
- File Handling
- Time Module
- String Processing

---

# ▶️ How to Run the Programs

---

## Step 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

---

## Step 2️⃣ Navigate to the Folder

```bash
cd your-repository-name
```

---

## Step 3️⃣ Run Python Programs

Example:

```bash
python sample1.py
```

or

```bash
python3 sample1.py
```

---

# 📄 Input Files

---

## input1.txt

Contains the input text.

### Example

```text
hello world
```

---

## pattern.txt

Contains the pattern to search.

### Example

```text
world
```

---

# 📌 Sample Output

```text
Found pattern at index 6
Length of Text: 11
Length of Pattern: 5
Execution Time: 0.0001
```

---

# 📊 Comparison of Algorithms

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Naive | `O(n)` | `O(nm)` | `O(nm)` |
| Rabin-Karp | `O(n+m)` | `O(n+m)` | `O(nm)` |
| KMP | `O(n+m)` | `O(n+m)` | `O(n+m)` |

---

# 🎯 Learning Objectives

This project helps in understanding:

- Pattern Matching Techniques
- String Searching Algorithms
- Hashing Concepts
- LPS Array Construction
- Time Complexity Analysis
- Efficient Searching Methods

---

# 📚 Applications

These algorithms are used in:

- Search Engines
- Text Editors
- Cybersecurity
- DNA Pattern Matching
- Data Mining
- Compiler Design
- Network Security

---

# 👩‍💻 Author

## Farisha KR

Assistant Professor  
Department of Computer Science and Engineering  
Chennai Institute of Technology


# ⭐ Support

If you found this repository useful, please consider giving it a ⭐ on GitHub.

---

# 📜 License

This project is created for educational and learning purposes.
