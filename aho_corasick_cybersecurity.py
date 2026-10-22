from collections import deque


class TrieNode:
    """One state in the Aho-Corasick automaton."""
    def __init__(self):
        self.children = {}
        self.fail = None
        self.outputs = []


class AhoCorasick:
    def __init__(self, patterns):
        self.root = TrieNode()
        self.patterns = []
        self._build_trie(patterns)
        self._build_failure_links()

    def _build_trie(self, patterns):
        # Insert each distinct, non-empty pattern into the trie.
        seen = set()
        for pattern in patterns:
            if not pattern:
                continue
            if pattern in seen:
                continue
            seen.add(pattern)
            self.patterns.append(pattern)

            node = self.root
            for char in pattern:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.outputs.append(pattern)

    def _build_failure_links(self):
        # The root fails to itself; its children fail to the root.
        self.root.fail = self.root
        queue = deque()

        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        while queue:
            current = queue.popleft()

            for char, child in current.children.items():
                fallback = current.fail

                while fallback is not self.root and char not in fallback.children:
                    fallback = fallback.fail

                if char in fallback.children and fallback.children[char] is not child:
                    child.fail = fallback.children[char]
                else:
                    child.fail = self.root

                # Patterns ending at the failure state also end here.
                child.outputs.extend(child.fail.outputs)
                queue.append(child)

    def search(self, text, case_insensitive=False):
        """Return (pattern, start_index, end_index) for every match."""
        if case_insensitive:
            scan_text = text.lower()
            # Case-fold patterns for this search while preserving the original text positions.
            patterns = [p.lower() for p in self.patterns]
            automaton = AhoCorasick(patterns)
            return automaton.search(text.lower(), case_insensitive=False)

        matches = []
        node = self.root

        for index, char in enumerate(text):
            while node is not self.root and char not in node.children:
                node = node.fail

            if char in node.children:
                node = node.children[char]
            else:
                node = self.root

            for pattern in node.outputs:
                start = index - len(pattern) + 1
                matches.append((pattern, start, index + 1))

        return matches


def read_patterns():
    print("Enter suspicious keywords separated by commas.")
    print("Example: malware, attack, login, virus, bad")
    raw = input("Patterns: ")
    patterns = [item.strip() for item in raw.split(",") if item.strip()]
    return patterns


def main():
    print("=" * 62)
    print(" AHO-CORASICK: CYBERSECURITY MULTI-PATTERN SCANNER")
    print("=" * 62)

    patterns = read_patterns()
    if not patterns:
        print("No valid patterns entered. Please run the program again.")
        return

    print("\nChoose input text:")
    print("1. Use sample cybersecurity log")
    print("2. Enter custom text")
    choice = input("Choice (1 or 2): ").strip()

    sample_text = (
        "INFO user login successful; WARNING suspicious login detected; "
        "ALERT malware found; blocked attack from unknown host; "
        "INFO system scan complete."
    )

    if choice == "2":
        text = input("\nEnter text to scan: ")
    else:
        text = sample_text
        print("\nSample log:")
        print(text)

    case_choice = input("\nIgnore letter case? (y/n): ").strip().lower()
    ignore_case = case_choice == "y"

    # If ignoring case, normalize patterns too so displayed matches are consistent.
    scan_patterns = [p.lower() for p in patterns] if ignore_case else patterns
    scanner = AhoCorasick(scan_patterns)
    matches = scanner.search(text.lower() if ignore_case else text)

    print("\n" + "-" * 62)
    print("SCAN RESULTS")
    print("-" * 62)

    if not matches:
        print("No suspicious keywords found.")
    else:
        print(f"{'Keyword':<20} {'Start':>8} {'End (exclusive)':>17}")
        print("-" * 48)
        for pattern, start, end in sorted(matches, key=lambda m: (m[1], m[0])):
            print(f"{pattern:<20} {start:>8} {end:>17}")

        counts = {}
        for pattern, _, _ in matches:
            counts[pattern] = counts.get(pattern, 0) + 1

        print("\nOccurrence summary:")
        for pattern in sorted(counts):
            print(f"  {pattern}: {counts[pattern]} match(es)")
        print(f"\nTotal matches: {len(matches)}")

    print("\nComplexity:")
    print("  Build: O(P) for trie insertion + failure-link construction")
    print("  Search: O(N + Z)")
    print("  P = total length of patterns, N = text length, Z = matches")
    print("=" * 62)


if __name__ == "__main__":
    main()
