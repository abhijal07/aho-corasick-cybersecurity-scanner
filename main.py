def read_patterns():
    # Time Complexity: O(L), where L is the total input length
    # Space Complexity: O(L)
    raw = input("Patterns: ")

    # Split the input using commas and remove extra spaces.
    patterns = [item.strip() for item in raw.split(",") if item.strip()]

    return patterns


def main():
    # Time Complexity: O(P + N + Z), under standard assumptions
    # Space Complexity: O(P + N + Z)
    # P = total pattern length; N = text length; Z = total matches

    patterns = read_patterns()

    # Stop if no valid patterns were entered.
    if not patterns:
        print("No valid patterns entered.")
        return

    # Allow the user to choose the input text.
    print("1. Use sample cybersecurity log")
    print("2. Enter custom text")
    choice = input("Choice (1 or 2): ").strip()

    sample_text = (
        "INFO user login successful; WARNING suspicious login detected; "
        "ALERT malware found; blocked attack from unknown host; "
        "INFO system scan complete."
    )

    # Select the sample log or read custom text.
    if choice == "2":
        text = input("Enter text to scan: ")
    else:
        text = sample_text
        print(text)

    # Ask whether uppercase and lowercase should be treated equally.
    case_choice = input("Ignore letter case? (y/n): ").strip().lower()
    ignore_case = case_choice == "y"

    # Convert patterns and text to lowercase when ignoring case.
    scan_patterns = [p.lower() for p in patterns] if ignore_case else patterns
    scan_text = text.lower() if ignore_case else text

    # Build the Aho-Corasick automaton using the given patterns.
    scanner = AhoCorasick(scan_patterns)

    # Search the text and collect all pattern matches.
    matches = scanner.search(scan_text)

    # Handle the case where no patterns were found.
    if not matches:
        print("No suspicious keywords found.")

    else:
        # Display the keyword and its starting and ending positions.
        print(f"{'Keyword':<20} {'Start':>8} {'End (exclusive)':>17}")

        # Sort matches by starting position and then by keyword.
        for pattern, start, end in sorted(
            matches, key=lambda m: (m[1], m[0])
        ):
            print(f"{pattern:<20} {start:>8} {end:>17}")

        # Time Complexity: O(Z + K log K), expected
        # Space Complexity: O(K)
        # Z = total matches; K = number of distinct matched patterns

        counts = {}

        # Count the occurrences of each matched keyword.
        for pattern, _, _ in matches:
            counts[pattern] = counts.get(pattern, 0) + 1

        # Display the count for each keyword.
        for pattern in sorted(counts):
            print(f"{pattern}: {counts[pattern]} match(es)")

        # Display the total number of matches.
        print(f"Total matches: {len(matches)}")


if __name__ == "__main__":
    main()
