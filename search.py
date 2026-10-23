
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
