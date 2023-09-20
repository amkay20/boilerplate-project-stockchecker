def read_json_file(file_path):
  """Reads data from a JSON file.

  Args:
    file_path: The path to the JSON file.

  Returns:
    A Python dictionary containing the data from the JSON file.
  """

  with open(file_path, "r") as f:
    data = json.load(f)
  return data