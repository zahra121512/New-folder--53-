from collections import Counter

def count_value_frequencies(test_dict):
  """
  Counts the frequency of each value in the given dictionary.

  Args:
    test_dict: The dictionary to analyze.
  Returns:
    A dictionary where keys are values from the input dictionary 
    and values are their respective frequencies.
  """
  value_counts = Counter(test_dict.values())
  return value_counts
# Example usage:
test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
value_frequencies = count_value_frequencies(test_dict)

print("Value frequencies:", value_frequencies)