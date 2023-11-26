import json

# Load the original JSON file
with open('ise-dsc01-private-test-offcial.json', 'r',encoding="utf8") as file:
    original_data = json.load(file)

# Define the new object to add
with open('Private_result_khang.json', 'r',encoding="utf8") as new_data_file:
    new_data = json.load(new_data_file)

# Add the new object to the existing data
original_data.update(new_data)

# Write the updated data back to the original JSON file
with open('ise-dsc01-private-test-offcial.json', 'w',encoding="utf8") as file:
    json.dump(original_data, file, indent=4)  # Use indent for pretty formatting if needed

# The new object has been added to your original JSON file.
