# 1. AI-Suggested Code (e.g., from GitHub Copilot, TabNine)

def sort_dicts_by_key(data, key):
    return sorted(data, key=lambda x: x[key])


# 2. Manual Implementation
def manual_sort_dicts_by_key(data, key):
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
# 3. Example usage
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

print(sort_dicts_by_key(people, "age"))
print(manual_sort_dicts_by_key(people, "age"))


# 4. Analysis 

The AI-generated code is concise, efficient, and leverages Python’s built-in sorted() function, which uses Timsort, an adaptive, hybrid sorting algorithm with an average and worst-case time complexity of O(n log n). The lambda function elegantly extracts the key for comparison, making the code both readable and performant.

In contrast, the manual implementation uses a bubble sort approach, which has a time complexity of O(n²). Although it achieves the same end result, it performs significantly worse on large datasets due to its nested loops and repeated comparisons. The manual version is also more error-prone and harder to maintain.

Therefore, the AI-suggested implementation is clearly superior in both performance and readability. This demonstrates one of the main advantages of AI-powered code completion tools — they not only save time by providing boilerplate solutions but also tend to suggest optimal, Pythonic code patterns based on best practices learned from large-scale code analysis.