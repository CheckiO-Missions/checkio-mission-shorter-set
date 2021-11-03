"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [set([7, 8, 9, 18]), 1],
            "answer": set([8, 9]),
        },
        {
            "input": [set([7, 8, 9]), 0],
            "answer": set([7, 8, 9]),
        },
        {
            "input": [set([7, 8, 9]), 2],
            "answer": set([]),
        },
        {
            "input": [set([1, 2, 7, 8, 9]), 2],
            "answer": set([7]),
        },
        {
            "input": [set([]), 1],
            "answer": set([]),
        },
    ],
    "Extra": [
        {
            "input": [set([1, 2, 3, 4, 8]), 2],
            "answer": set([3]),
        }
    ]
}
