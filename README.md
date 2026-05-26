# Pattern Matching Algorithms in Python

This repository contains implementations of various **String Pattern Matching Algorithms** using Python.  
The programs are developed for understanding the working, efficiency, and performance comparison of different pattern searching techniques used in **Design and Analysis of Algorithms (DAA)**.

---

# Repository Structure

```bash
📂 Pattern-Matching-Algorithms
│
├── input1.txt
├── pattern.txt
│
├── sample1.py
├── sample2.py
├── sample3.py
├── sample4.py
├── sample5.py
│
└── README.md
```

---

# Programs Included

| File Name | Description |
|-----------|-------------|
| sample1.py | Naive String Matching using User Input |
| sample2.py | Naive String Matching using File Input |
| sample3.py | Rabin-Karp Algorithm using User Input |
| sample4.py | Rabin-Karp Algorithm using Large Text |
| sample5.py | Knuth-Morris-Pratt (KMP) Algorithm |

---

# Algorithms Implemented

## 1. Naive String Matching Algorithm

The Naive Pattern Matching Algorithm compares the pattern with every possible position in the text until a match is found.

### Time Complexity

Worst Case:

:contentReference[oaicite:0]{index=0}

Average Case:

:contentReference[oaicite:1]{index=1}

---

## 2. Rabin-Karp Algorithm

The Rabin-Karp Algorithm uses hashing to search for patterns efficiently in a text.

### Time Complexity

Average Case:

:contentReference[oaicite:2]{index=2}

Worst Case:

:contentReference[oaicite:3]{index=3}

---

## 3. Knuth-Morris-Pratt (KMP) Algorithm

The KMP Algorithm improves pattern searching efficiency using the LPS (Longest Prefix Suffix) array.

### Time Complexity

:contentReference[oaicite:4]{index=4}

---

# Features

- Pattern Matching Techniques
- File Handling in Python
- User Input Based Searching
- Large Text Pattern Searching
- Execution Time Calculation
- Performance Analysis of Algorithms
- LPS Array Generation in KMP
- Rolling Hash Technique in Rabin-Karp

---

# Requirements

- Python 3.x

---

# How to Run

## Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

## Open Repository Folder

```bash
cd your-repository-name
```

## Run Any Program

```bash
python sample1.py
```

Example:

```bash
python sample5.py
```

---

# Sample Inputs

## Sample Input for User-Based Programs

```text
Enter Text: hello world
Enter Pattern: world
```

---

# Output

The programs display:
- Pattern matching index
- Text length
- Pattern length
- Execution time

---

# Concepts Covered

- String Matching
- Pattern Searching
- Hashing
- Rolling Hash Function
- LPS Array
- Time Complexity Analysis
- File Handling
- Algorithm Comparison

---

# Algorithm Comparison

| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|-------------|
| Naive String Matching | O(n) | O((n-m+1)m) | O(nm) |
| Rabin-Karp | O(n+m) | O(n+m) | O(nm) |
| KMP | O(n+m) | O(n+m) | O(n+m) |

---

# Applications

- Text Editors
- Search Engines
- DNA Sequence Matching
- Plagiarism Detection
- Data Retrieval Systems
- Information Search Systems

---

# Author

**Farisha KR**  
M.Tech — Network and Information Security  
Assistant Professor — Department of Computer Science and Engineering

---

# License

This project is developed for educational and academic purposes.
