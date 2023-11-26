import json
def read_and_iterate_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:  # Specify the encoding
            data = json.load(file)
            
            for item in data:
                # Do something with each item in the JSON data
                print(item)  # You can replace this with your desired processing

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{filename}'")

# Replace 'your_json_file.json' with the actual filename of your JSON file
json_file = 'D:\DSC2023\Private_Test\ise-dsc01-private_new.json'
#read_and_iterate_json_file(json_file)
with open(json_file, 'r', encoding='utf-8') as file:

    data = json.load(file)

# Initialize a variable to store the maximum evidence length
max_evidence_length = 0
max_evidence_sentence = ""
max_context_length = 0
max_evidence_sentence = ""
# Iterate through the JSON data and find the maximum evidence length
for item in data.values():
    evidence = item.get('evidence')
    context = item.get('context')
    if evidence is not None:  # Check if the "evidence" field is not None
        evidence_length = len(evidence)
        if evidence_length > max_evidence_length:
            max_evidence_length = evidence_length
            max_evidence_sentence = item.get('evidence', '') 

    if context is not None:  # Check if the "evidence" field is not None
        context_length = len(context)
        if context_length > max_context_length:
            max_context_length = context_length
            max_context_sentence = item.get('context', '')        

# Print the maximum evidence length
print("Maximum evidence length:", max_evidence_length)
#print("Corresponding sentence:")
#print(max_evidence_sentence)

print("Maximum context length:", max_context_length)
#print("Corresponding sentence:")
#print(max_context_sentence)