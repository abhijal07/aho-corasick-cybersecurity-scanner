class TrieNode:
    """One node in the Trie."""

    def __init__(self):
        self.children = {}
        self.fail = None
        self.outputs = []


class AhoCorasick:
    def __init__(self, patterns):
        self.root = TrieNode()
        self.patterns = []

        self._build_trie(patterns)
        self._build_failure_links()  # Method supplied by Member 2.

    def _build_trie(self, patterns):
        """Insert distinct, non-empty patterns into the Trie."""
        seen = set()

        for pattern in patterns:
            # Skip empty patterns and duplicates.
            if not pattern or pattern in seen:
                continue

            seen.add(pattern)
            self.patterns.append(pattern)

            # Every pattern starts from the root.
            node = self.root

            for char in pattern:
                # Create a branch only when it does not already exist.
                if char not in node.children:
                    node.children[char] = TrieNode()

                # Follow the new or existing branch.
                node = node.children[char]

            # Record the complete pattern at its final node.
            node.outputs.append(pattern)

    # Keep Member 2's _build_failure_links() method below.
    # Keep Member 3's search methods below.
