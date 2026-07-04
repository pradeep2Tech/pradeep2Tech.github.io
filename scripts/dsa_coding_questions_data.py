"""DSA & Coding curriculum — problem registry and module metadata."""
from __future__ import annotations

from typing import NamedTuple


class Problem(NamedTuple):
    num: int
    slug: str
    title: str
    pattern: str
    source_url: str
    source_label: str


class Module(NamedTuple):
    id: int
    focus: str
    folder: str
    primer_desc: str
    problems: tuple[Problem, ...]


MODULES: tuple[Module, ...] = (
    Module(
        1,
        "Arrays, HashMap & Two Pointers",
        "01-arrays-hashmap-two-pointers",
        "HashMap lookups, two-pointer scans, and expand-around-center for palindromes.",
        (
            Problem(1, "two-sum", "Two Sum", "HashMap", "https://leetcode.com/problems/two-sum/", "LeetCode 1"),
            Problem(2, "valid-anagram", "Valid Anagram", "HashMap", "https://leetcode.com/problems/valid-anagram/", "LeetCode 242"),
            Problem(3, "group-anagrams", "Group Anagrams", "HashMap", "https://leetcode.com/problems/group-anagrams/", "LeetCode 49"),
            Problem(
                4,
                "count-pairs-absolute-difference-k",
                "Count Pairs With Absolute Difference K",
                "HashMap",
                "https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/",
                "LeetCode 2006",
            ),
            Problem(
                5,
                "count-nice-pairs-in-an-array",
                "Count Nice Pairs in an Array",
                "HashMap",
                "https://leetcode.com/problems/count-nice-pairs-in-an-array/",
                "LeetCode 1814",
            ),
            Problem(6, "valid-palindrome", "Valid Palindrome", "Two Pointers", "https://leetcode.com/problems/valid-palindrome/", "LeetCode 125"),
            Problem(7, "3sum", "3Sum", "Two Pointers", "https://leetcode.com/problems/3sum/", "LeetCode 15"),
            Problem(8, "3sum-closest", "3Sum Closest", "Two Pointers", "https://leetcode.com/problems/3sum-closest/", "LeetCode 16"),
            Problem(9, "4sum", "4Sum", "Two Pointers", "https://leetcode.com/problems/4sum/", "LeetCode 18"),
            Problem(10, "merge-sorted-array", "Merge Sorted Array", "Two Pointers", "https://leetcode.com/problems/merge-sorted-array/", "LeetCode 88"),
            Problem(
                11,
                "meeting-schedule",
                "Meeting Schedule",
                "Two Arrays + Sorting",
                "https://leetcode.com/problems/meeting-rooms/",
                "LeetCode 252",
            ),
            Problem(
                12,
                "longest-palindromic-substring",
                "Longest Palindromic Substring",
                "Expand Around Center",
                "https://leetcode.com/problems/longest-palindromic-substring/",
                "LeetCode 5",
            ),
        ),
    ),
    Module(
        2,
        "Sliding Window & Prefix Sum",
        "02-sliding-window-prefix-sum",
        "Fixed and variable sliding windows, prefix sums, and suffix arrays.",
        (
            Problem(
                13,
                "max-sum-subarray-size-k",
                "Max Sum Subarray of Size K",
                "Fixed Window",
                "https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1",
                "GFG",
            ),
            Problem(
                14,
                "longest-substring-without-repeating-characters",
                "Longest Substring Without Repeating Characters",
                "Variable Window",
                "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
                "LeetCode 3",
            ),
            Problem(
                15,
                "longest-substring-k-distinct-characters",
                "Longest Substring with At Most K Distinct Characters",
                "Variable Window",
                "https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/",
                "LeetCode 340",
            ),
            Problem(
                16,
                "max-consecutive-ones-iii",
                "Max Consecutive Ones III",
                "Variable Window",
                "https://leetcode.com/problems/max-consecutive-ones-iii/",
                "LeetCode 1004",
            ),
            Problem(
                17,
                "maximum-points-from-cards",
                "Maximum Points You Can Obtain from Cards",
                "Sliding Window",
                "https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/",
                "LeetCode 1423",
            ),
            Problem(
                18,
                "equal-left-right-subarray-sum",
                "Equal Left and Right Subarray Sum",
                "Prefix Sum",
                "https://leetcode.com/problems/find-pivot-index/",
                "LeetCode 724",
            ),
            Problem(
                19,
                "trapping-rain-water",
                "Trapping Rain Water",
                "Prefix/Suffix",
                "https://leetcode.com/problems/trapping-rain-water/",
                "LeetCode 42",
            ),
            Problem(
                20,
                "subdomain-visit-count",
                "Subdomain Visit Count",
                "HashMap",
                "https://leetcode.com/problems/subdomain-visit-count/",
                "LeetCode 811",
            ),
        ),
    ),
    Module(
        3,
        "Binary Search",
        "03-binary-search",
        "Classic binary search, rotated arrays, matrices, and search on answer space.",
        (
            Problem(21, "binary-search", "Binary Search", "Classic", "https://leetcode.com/problems/binary-search/", "LeetCode 704"),
            Problem(
                22,
                "search-in-rotated-sorted-array",
                "Search in Rotated Sorted Array",
                "Modified Binary Search",
                "https://leetcode.com/problems/search-in-rotated-sorted-array/",
                "LeetCode 33",
            ),
            Problem(
                23,
                "search-a-2d-matrix",
                "Search a 2D Matrix",
                "Matrix Binary Search",
                "https://leetcode.com/problems/search-a-2d-matrix/",
                "LeetCode 74",
            ),
            Problem(
                24,
                "missing-number-in-sorted-array",
                "Missing Number in Sorted Array",
                "Binary Search",
                "https://leetcode.com/problems/missing-number/",
                "LeetCode 268",
            ),
            Problem(
                25,
                "koko-eating-bananas",
                "Koko Eating Bananas",
                "Binary Search on Answer",
                "https://leetcode.com/problems/koko-eating-bananas/",
                "LeetCode 875",
            ),
            Problem(
                26,
                "aggressive-cows",
                "Aggressive Cows",
                "Binary Search on Answer",
                "https://www.geeksforgeeks.org/problems/aggressive-cows/1",
                "GFG",
            ),
        ),
    ),
    Module(
        4,
        "Recursion & Backtracking",
        "04-recursion-backtracking",
        "Stack-based thinking, subset generation, and constraint-satisfaction search.",
        (
            Problem(
                27,
                "valid-parentheses",
                "Valid Parentheses",
                "Stack / Recursion Thinking",
                "https://leetcode.com/problems/valid-parentheses/",
                "LeetCode 20",
            ),
            Problem(28, "subset-sum-recursion", "Subset Sum", "Recursion", "https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1", "GFG"),
            Problem(
                29,
                "letter-combinations-of-phone-number",
                "Letter Combinations of a Phone Number",
                "Backtracking",
                "https://leetcode.com/problems/letter-combinations-of-a-phone-number/",
                "LeetCode 17",
            ),
            Problem(
                30,
                "generate-parentheses",
                "Generate Parentheses",
                "Backtracking",
                "https://leetcode.com/problems/generate-parentheses/",
                "LeetCode 22",
            ),
            Problem(31, "word-search", "Word Search", "Backtracking", "https://leetcode.com/problems/word-search/", "LeetCode 79"),
            Problem(32, "n-queens", "N-Queens", "Backtracking", "https://leetcode.com/problems/n-queens/", "LeetCode 51"),
        ),
    ),
    Module(
        5,
        "Trees",
        "05-trees",
        "DFS and BFS traversals on binary trees and BSTs.",
        (
            Problem(33, "path-sum", "Path Sum", "DFS", "https://leetcode.com/problems/path-sum/", "LeetCode 112"),
            Problem(
                34,
                "validate-binary-search-tree",
                "Validate Binary Search Tree",
                "DFS",
                "https://leetcode.com/problems/validate-binary-search-tree/",
                "LeetCode 98",
            ),
            Problem(
                35,
                "lowest-common-ancestor-bst",
                "Lowest Common Ancestor of a BST",
                "DFS",
                "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/",
                "LeetCode 235",
            ),
            Problem(
                36,
                "binary-tree-right-side-view",
                "Binary Tree Right Side View",
                "BFS",
                "https://leetcode.com/problems/binary-tree-right-side-view/",
                "LeetCode 199",
            ),
            Problem(
                37,
                "binary-tree-zigzag-level-order",
                "Binary Tree Zigzag Level Order Traversal",
                "BFS",
                "https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/",
                "LeetCode 103",
            ),
            Problem(
                38,
                "maximum-width-of-binary-tree",
                "Maximum Width of Binary Tree",
                "BFS",
                "https://leetcode.com/problems/maximum-width-of-binary-tree/",
                "LeetCode 662",
            ),
            Problem(
                39,
                "maximum-level-sum-binary-tree",
                "Maximum Level Sum of a Binary Tree",
                "BFS",
                "https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/",
                "LeetCode 1161",
            ),
        ),
    ),
    Module(
        6,
        "Graphs",
        "06-graphs",
        "DFS/BFS on grids and adjacency structures; multi-source BFS.",
        (
            Problem(40, "rotten-oranges", "Rotten Oranges", "Multi-Source BFS", "https://leetcode.com/problems/rotten-oranges/", "LeetCode 994"),
            Problem(41, "number-of-islands", "Number of Islands", "DFS", "https://leetcode.com/problems/number-of-islands/", "LeetCode 200"),
            Problem(42, "number-of-provinces", "Number of Provinces", "DFS", "https://leetcode.com/problems/number-of-provinces/", "LeetCode 547"),
            Problem(43, "graph-valid-tree", "Graph Valid Tree", "DFS/BFS", "https://leetcode.com/problems/graph-valid-tree/", "LeetCode 261"),
            Problem(
                44,
                "shortest-path-in-binary-matrix",
                "Shortest Path in Binary Matrix",
                "BFS",
                "https://leetcode.com/problems/shortest-path-in-binary-matrix/",
                "LeetCode 1091",
            ),
            Problem(
                45,
                "nearest-exit-from-maze",
                "Nearest Exit from Entrance in Maze",
                "BFS",
                "https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/",
                "LeetCode 490",
            ),
            Problem(
                46,
                "time-needed-to-inform-employees",
                "Time Needed to Inform All Employees",
                "BFS/DFS on Tree",
                "https://leetcode.com/problems/time-needed-to-inform-all-employees/",
                "LeetCode 1376",
            ),
            Problem(
                47,
                "number-of-closed-islands",
                "Number of Closed Islands",
                "DFS",
                "https://leetcode.com/problems/number-of-closed-islands/",
                "LeetCode 1254",
            ),
        ),
    ),
    Module(
        7,
        "Advanced Graphs",
        "07-advanced-graphs",
        "Topological ordering and graph modeling from tree structures.",
        (
            Problem(
                48,
                "alien-dictionary",
                "Alien Dictionary",
                "Topological Sort",
                "https://leetcode.com/problems/alien-dictionary/",
                "LeetCode 269",
            ),
            Problem(
                49,
                "all-nodes-distance-k-in-binary-tree",
                "All Nodes Distance K in Binary Tree",
                "Graph + BFS",
                "https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/",
                "LeetCode 863",
            ),
        ),
    ),
    Module(
        8,
        "Dynamic Programming",
        "08-dynamic-programming",
        "1D DP, grid paths, coin change, and unbounded knapsack.",
        (
            Problem(50, "climbing-stairs", "Climbing Stairs", "Fibonacci DP", "https://leetcode.com/problems/climbing-stairs/", "LeetCode 70"),
            Problem(51, "house-robber", "House Robber", "Include/Exclude", "https://leetcode.com/problems/house-robber/", "LeetCode 198"),
            Problem(52, "subset-sum-dp", "Subset Sum", "DP", "https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1", "GFG"),
            Problem(53, "unique-paths", "Unique Paths", "Grid DP", "https://leetcode.com/problems/unique-paths/", "LeetCode 62"),
            Problem(54, "coin-change", "Coin Change", "DP", "https://leetcode.com/problems/coin-change/", "LeetCode 322"),
            Problem(
                55,
                "rod-cutting",
                "Rod Cutting",
                "Unbounded Knapsack",
                "https://www.geeksforgeeks.org/problems/rod-cutting0840/1",
                "GFG",
            ),
        ),
    ),
)

SUPPORT_MODULES: tuple[tuple[int, str, str, tuple[str, ...]], ...] = (
    (
        9,
        "Interview Guide",
        "09-interview-guide",
        (
            "interview-problem-solving-framework",
            "pattern-recognition-table",
            "pattern-selection-matrix",
            "complexity-decision-framework",
            "60-second-pattern-recognition",
            "top-55-interview-questions",
            "top-30-must-solve",
            "binary-search-template",
            "sliding-window-template",
            "graph-cheatsheet",
            "tree-cheatsheet",
            "dp-cheatsheet",
        ),
    ),
    (
        10,
        "Learning Paths",
        "10-learning-paths",
        ("dsa-senior-engineer-path", "dsa-interview-revision-path"),
    ),
    (
        11,
        "Interview Pattern Cheat Sheets",
        "11-interview-pattern-cheatsheets",
        (
            "01-two-pointers-cheatsheet",
            "02-sliding-window-cheatsheet",
            "03-prefix-sum-cheatsheet",
            "04-binary-search-cheatsheet",
            "05-backtracking-cheatsheet",
            "06-tree-cheatsheet",
            "07-graph-cheatsheet",
            "08-dp-cheatsheet",
        ),
    ),
)

GUIDE_TITLES: dict[str, str] = {
    "09-interview-guide/interview-problem-solving-framework": "Interview Problem-Solving Framework",
    "09-interview-guide/pattern-recognition-table": "Pattern Recognition Table",
    "09-interview-guide/pattern-selection-matrix": "Pattern Selection Matrix",
    "09-interview-guide/complexity-decision-framework": "Complexity Decision Framework",
    "09-interview-guide/60-second-pattern-recognition": "60-Second Pattern Recognition",
    "09-interview-guide/top-55-interview-questions": "Top 55 Interview Questions",
    "09-interview-guide/top-30-must-solve": "Top 30 Must-Solve",
    "09-interview-guide/binary-search-template": "Binary Search Template",
    "09-interview-guide/sliding-window-template": "Sliding Window Template",
    "09-interview-guide/graph-cheatsheet": "Graph Cheat Sheet",
    "09-interview-guide/tree-cheatsheet": "Tree Cheat Sheet",
    "09-interview-guide/dp-cheatsheet": "DP Cheat Sheet",
    "10-learning-paths/dsa-senior-engineer-path": "Senior Engineer Path",
    "10-learning-paths/dsa-interview-revision-path": "Interview Revision Path",
    "11-interview-pattern-cheatsheets/01-two-pointers-cheatsheet": "Two Pointers Cheat Sheet",
    "11-interview-pattern-cheatsheets/02-sliding-window-cheatsheet": "Sliding Window Cheat Sheet",
    "11-interview-pattern-cheatsheets/03-prefix-sum-cheatsheet": "Prefix Sum Cheat Sheet",
    "11-interview-pattern-cheatsheets/04-binary-search-cheatsheet": "Binary Search Cheat Sheet",
    "11-interview-pattern-cheatsheets/05-backtracking-cheatsheet": "Backtracking Cheat Sheet",
    "11-interview-pattern-cheatsheets/06-tree-cheatsheet": "Tree Cheat Sheet",
    "11-interview-pattern-cheatsheets/07-graph-cheatsheet": "Graph Cheat Sheet",
    "11-interview-pattern-cheatsheets/08-dp-cheatsheet": "DP Cheat Sheet",
}


def all_problem_topics() -> list[str]:
    topics: list[str] = []
    for mod in MODULES:
        topics.append(f"{mod.folder}/_index")
        topics.extend(f"{mod.folder}/{p.slug}" for p in mod.problems)
    return topics


def all_topics() -> list[str]:
    topics = all_problem_topics()
    for _mod_id, _focus, folder, slugs in SUPPORT_MODULES:
        topics.extend(f"{folder}/{slug}" for slug in slugs)
    return topics


def topic_title(rel: str) -> str:
    for mod in MODULES:
        if rel == f"{mod.folder}/_index":
            return mod.focus
        for p in mod.problems:
            if rel == f"{mod.folder}/{p.slug}":
                return p.title
    return GUIDE_TITLES.get(rel, rel.split("/")[-1].replace("-", " ").title())
