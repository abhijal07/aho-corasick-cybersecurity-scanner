# Aho–Corasick Algorithm for Efficient Multi-Pattern Searching in Cybersecurity Systems

## 📌 Project Overview

This project implements the **Aho–Corasick algorithm in Python** to efficiently search for multiple suspicious keywords in cybersecurity logs. Security systems often need to analyze large volumes of text to identify potential threats, malware signatures, and suspicious activities. Searching for each keyword separately can be inefficient because the same text may need to be scanned multiple times.

The Aho–Corasick algorithm addresses this problem by constructing a pattern-matching automaton using a Trie and failure links, enabling multiple patterns to be detected during a single scan of the input text.

This project demonstrates the practical application of advanced data structures and algorithms in cybersecurity.

## 🎯 Objectives

- Implement the Aho–Corasick algorithm using Python.
- Understand the role of Tries and failure links in multi-pattern searching.
- Detect multiple keywords in cybersecurity logs efficiently.
- Identify overlapping pattern matches.
- Analyze time and space complexity.
- Demonstrate the algorithm through interactive test cases.

## 🧠 Data Structures and Algorithms Used

### 1. Trie

A Trie stores patterns character by character. Common prefixes are shared between patterns, reducing redundant storage and providing the structure for efficient pattern matching.

### 2. Failure Links

Failure links connect each state to an appropriate fallback state. When a character cannot continue the current path, the algorithm follows these links instead of restarting the search from the root.

### 3. Output Lists

Each Trie node maintains a list of patterns that end at that state. Patterns inherited through failure links allow the algorithm to identify suffix matches and overlapping occurrences.

### 4. Queue and Breadth-First Search (BFS)

Python's `deque` is used as a queue to construct failure links level by level.

## ⚙️ Features

- Interactive input for multiple suspicious keywords.
- Predefined cybersecurity log or custom text input.
- Trie construction with duplicate and empty-pattern handling.
- Failure-link construction using BFS.
- Multi-pattern searching in a single text scan.
- Detection of overlapping matches.
- Optional case-insensitive searching.
- Reporting of matched keywords and their start and end positions.
- Occurrence counting and summary generation.
- Time-complexity information.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Data Structures:** Trie, queue, dictionaries, lists, and sets
- **Algorithm:** Aho–Corasick string matching
- **Libraries:** Python standard library (`collections.deque`)

No external Python packages are required.

## 🚀 How to Run

### Prerequisites

Install Python 3 on your computer.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/aho-corasic-cybersecurity-scanner.git
   ```

2. Navigate to the project directory:

   ```bash
   cd aho-corasic-cybersecurity-scanner
   ```

3. Run the Python program:

   ```bash
   python aho_corasick_cybersecurity_demo.py
   ```

4. Enter suspicious keywords separated by commas.

5. Choose either the sample cybersecurity log or custom text.

6. Select whether to ignore letter case and view the matching results.

Replace `YOUR-USERNAME` with the GitHub account that owns the repository. Ensure the repository name in the commands matches the actual name.

## 🧪 Example Demonstration

### Test Case 1: Cybersecurity Log

**Patterns:**

```text
malware, attack, login, virus, bad
```

**Sample input text:**

```text
INFO user login successful; WARNING suspicious login detected;
ALERT malware found; blocked attack from unknown host;
INFO system scan complete.
```

**Expected matches:**

| Keyword | Start index | End index (exclusive) | Occurrences |
|---|---:|---:|---:|
| login | 10 | 15 | 1 |
| login | 47 | 52 | 1 |
| malware | 69 | 76 | 1 |
| attack | 92 | 98 | 1 |

The program reports four total matches: two occurrences of `login`, one of `malware`, and one of `attack`.

### Test Case 2: Overlapping Patterns

**Patterns:**

```text
he, she, hers
```

**Input text:**

```text
ushers
```

**Expected matches:**

| Pattern | Start index | End index (exclusive) |
|---|---:|---:|
| she | 1 | 4 |
| he | 2 | 4 |
| hers | 2 | 6 |

This test demonstrates how failure links and inherited output lists enable overlapping patterns to be detected.

## ⏱️ Complexity Analysis

Let:

- **P** = Total number of characters across all patterns.
- **N** = Number of characters in the input text.
- **Z** = Total number of matches reported.

| Operation | Time Complexity |
|---|---|
| Trie construction | O(P), expected |
| Failure-link construction | O(P) under standard bounded-alphabet analysis |
| Text searching | O(N + Z) |
| Overall algorithm | O(P + N + Z) |

The overall bound excludes additional sorting of the results. The implementation sorts reported matches before displaying them, which can add O(Z log Z) time.

The Trie and automaton require O(P) space. Storing the reported matches requires O(Z) additional space.

## 🌐 Applications

The algorithm can be applied to:

- Cybersecurity log scanning.
- Suspicious keyword detection.
- Malware signature matching.
- Spam filtering.
- Text search engines.
- DNA sequence pattern matching.

**Note:** This project is an educational prototype for literal keyword detection. It is not a complete production-grade intrusion-detection system.

## 👥 Team Contributions

The project is divided into four technical responsibilities:

- **Member 1 — Trie Construction:** Implements Trie nodes, pattern insertion, and shared-prefix handling.
- **Member 2 — Failure Links:** Implements BFS-based failure-link construction and inherited output lists.
- **Member 3 — Pattern Matching:** Implements text scanning, failure transitions, match detection, and position calculation.
- **Member 4 — Integration and Output:** Implements interactive input, sample logs, case handling, occurrence summaries, and output formatting.

Each member is responsible for understanding and demonstrating their assigned implementation.

## 📚 References

1. Aho, A. V., and Corasick, M. J. (1975). *Efficient String Matching: An Aid to Bibliographic Search.* Communications of the ACM, 18(6), 333–340. https://doi.org/10.1145/360825.360855
2. National Institute of Standards and Technology (NIST). *Aho-Corasick Algorithm.* Dictionary of Algorithms and Data Structures. https://xlinux.nist.gov/dads/HTML/ahoCorasick.html

## 📄 License

No license has been selected for this repository. Unless a license is added, others generally do not have permission to reuse, modify, or distribute the project beyond applicable legal exceptions.

---

**Developed as a Data Structures and Algorithms (DSA) case study demonstrating efficient multi-pattern searching using the Aho–Corasick algorithm.**
