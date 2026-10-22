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

  
