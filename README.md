# Aho–Corasick Algorithm for Efficient Multi-Pattern Searching in Cybersecurity Logs

## Project Overview

Cybersecurity logs contain a mix of routine events, warnings, and possible threats. Finding useful information in these logs becomes harder as the amount of data grows. Searching for each keyword separately also means reading the same text repeatedly.

This project uses the **Aho–Corasick algorithm in Python** to search for multiple keywords in a single pass. It builds a Trie to store the patterns and uses failure links to keep the search moving when a character does not match the current path.

The project demonstrates how data structures and algorithms can support a practical security task: locating keywords in logs so that relevant entries can be reviewed.

## Objectives

The project aims to:

- Build a working implementation of the Aho–Corasick algorithm.
- Explain how Tries, failure links, and output lists work together.
- Search cybersecurity logs for several keywords at once.
- Detect overlapping patterns.
- Display match positions and occurrence counts.
- Explore the algorithm’s time and space requirements.
- Demonstrate its behaviour through interactive examples.

## How the Algorithm Works

### 1. Storing Keywords in a Trie

The first step is to insert the keywords into a Trie. Each path through the Trie represents a pattern, with one character stored at each step.

Patterns with the same beginning share part of their path. For example, **he** and **hers** share the nodes for **h** and **e**. This keeps common prefixes together and provides the structure used during searching.

### 2. Building Failure Links

A search will sometimes reach a character that cannot continue the current path. Failure links tell the algorithm where to continue from that point.

Each link leads to the longest suffix of the current path that is also a prefix of a stored pattern. This allows the algorithm to reuse what it has already matched without scanning earlier text again.

### 3. Recording Matches

Output lists identify the patterns that end at each state. They also include relevant matches reached through failure links.

This matters when several patterns end at the same position. For example, matching **she** can also produce a match for **he**.

### 4. Using Breadth-First Search

Failure links are constructed level by level using breadth-first search.

The program uses Python’s `collections.deque` as a queue for this process. Processing shallower nodes first ensures that the fallback information needed by deeper nodes is already available.

## Features

The program supports:

- **Multiple keywords:** Enter several patterns separated by commas.
- **Flexible input:** Search the sample cybersecurity log or provide custom text.
- **Case options:** Choose whether matching should ignore letter case.
- **Overlapping matches:** Find patterns that share characters or occur within other patterns.
- **Match positions:** View where each occurrence begins and ends.
- **Occurrence summaries:** See how often each keyword appears.
- **Input handling:** Handle duplicate and empty pattern entries.
- **Complexity information:** Review the main time and space costs.

## Technologies Used

The project is written in **Python 3** and uses the **Aho–Corasick string-matching algorithm**.

Its main data structures are a Trie, dictionaries, lists, sets, and a queue. The queue is provided by Python’s standard library through `collections.deque`.

**No external Python packages are required.**

## Getting Started

Make sure Python 3 is installed on your computer.

### Step 1: Clone the Repository

Replace `YOUR-USERNAME` with the GitHub username of the repository owner:

```bash
git clone https://github.com/YOUR-USERNAME/aho-corasic-cybersecurity-scanner.git
```

### Step 2: Open the Project Folder

```bash
cd aho-corasic-cybersecurity-scanner
```

The repository and folder names should match the actual project.

### Step 3: Run the Program

```bash
python aho_corasick_cybersecurity_demo.py
```

### Step 4: Try a Search

Once the program starts:

1. Enter your keywords, separated by commas.
2. Choose the sample log or enter your own text.
3. Select whether to ignore letter case.
4. Review the matches and occurrence summary.

## Example 1: Searching a Cybersecurity Log

Suppose we want to check a log for these keywords:

```text
malware, attack, login, virus, bad
```

The sample log contains:

```text
INFO user login successful; WARNING suspicious login detected;
ALERT malware found; blocked attack from unknown host;
INFO system scan complete.
```

### What the Scanner Found

The scanner detects **4 matches across 3 keywords**.

- **login** appears twice, at positions **10–15** and **47–52**.
- **malware** appears once, at positions **69–76**.
- **attack** appears once, at positions **92–98**.

No matches are found for **virus** or **bad**.

*Positions start at zero, and the end position is excluded from each range. These values assume that each displayed line break is represented by one newline character.*

### Understanding the Results

The matches help identify entries worth reviewing, but their meaning depends on the surrounding text.

For example, **login** appears in both a successful login message and a suspicious login warning. The keyword search locates both entries; further analysis is needed to decide which events require attention.

## Example 2: Finding Overlapping Patterns

Some patterns overlap or appear inside other patterns. To demonstrate this, consider the following keywords:

```text
he, she, hers
```

The input text is:

```text
ushers
```

### What the Scanner Found

The scanner detects **3 matches**:

- **she** at positions **1–4**.
- **he** at positions **2–4**.
- **hers** at positions **2–6**.

The same position convention applies: the start is included, and the end is excluded.

### Why This Example Matters

The pattern **he** appears within **she**, while **hers** begins at the same position as **he** and continues further.

Failure links and output information allow the algorithm to report all three matches during the same scan.

## Time and Space Complexity

The analysis uses three values:

- **P:** The total number of characters across all patterns.
- **N:** The number of characters in the input text.
- **Z:** The number of matches reported.

### Preparing the Patterns

Building the Trie takes **O(P)** expected time when dictionary-based transitions are used.

Under the standard bounded-alphabet analysis, failure-link construction also takes **O(P)** time. The exact preprocessing cost depends on how transitions and inherited output information are represented.

### Searching the Text

Searching takes **O(N + Z)** time. The algorithm scans the text and reports each match it finds.

Under the standard construction assumptions, this gives a total core running time of:

```text
O(P + N + Z)
```

### Formatting the Results

The implementation sorts matches before displaying them. This can add **O(Z log Z)** time.

Copying inherited output lists can also add preprocessing work, depending on the implementation.

### Memory Usage

The Trie structure requires **O(P)** space. Storing the reported matches requires another **O(Z)**.

Output information can require additional memory, particularly when inherited pattern lists are copied between nodes.

## Applications

Aho–Corasick is useful when many known patterns need to be found in the same text. Its applications include:

- Scanning cybersecurity logs.
- Detecting suspicious keywords.
- Matching text-based malware signatures.
- Filtering spam.
- Supporting text search systems.
- Finding patterns in DNA sequences.

This project is an educational keyword scanner. It demonstrates multi-pattern matching, but interpreting security events requires additional context and analysis.

## Team Contributions

The work is divided into four technical responsibilities.

### Member 1: Trie Construction

Builds the Trie nodes, inserts patterns, and handles shared prefixes. This member explains how the keywords are stored before searching begins.

### Member 2: Failure Links

Constructs failure links using breadth-first search and manages inherited output information. This member explains how the algorithm continues after a mismatch.

### Member 3: Pattern Matching

Implements text scanning, follows failure transitions, detects matches, and calculates their positions.

### Member 4: Integration and Output

Connects the components and handles user input, sample logs, case options, occurrence summaries, and result formatting.

Each member should understand their assigned component and explain how it contributes to the complete program.

## References

1. Aho, A. V., and Corasick, M. J. (1975). *Efficient String Matching: An Aid to Bibliographic Search.* Communications of the ACM, 18(6), 333–340. [Read the paper](https://doi.org/10.1145/360825.360855).

2. National Institute of Standards and Technology. *Aho-Corasick Algorithm.* Dictionary of Algorithms and Data Structures. [View the reference](https://xlinux.nist.gov/dads/HTML/ahoCorasick.html).

## License

A license has not yet been added to this repository. Reuse permissions should be clarified with the project owner.

---

*Developed as a Data Structures and Algorithms case study on efficient multi-pattern searching.*
