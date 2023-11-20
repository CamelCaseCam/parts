import yaml
import hashlib
import base64

# Function to compute the hash of a sequence
def compute_hash(sequence):
    hash_obj = hashlib.sha256(sequence.encode())  # Compute SHA-256 hash (256 bits)
    truncated_bytes = hash_obj.digest()[:16]  # Truncate to 128 bits (16 bytes)
    return base64.b64encode(truncated_bytes).decode()  # Convert to base64

# Load the collections.yaml file
with open('collections.yaml', 'r') as file:
    collections = yaml.safe_load(file)

# Process each collection
for collection in collections.values():
    collection_file = collection['file']
    
    # Load the individual collection YAML file
    with open(collection_file, 'r') as file:
        parts = yaml.safe_load(file)
    
    # Iterate over the parts and replace the sequence with its base64 truncated hash
    for part in parts.values():
        part['sequence'] = compute_hash(part['sequence'])
    
    # Add the processed parts under a new key 'parts'
    collection['parts'] = parts

# Print the updated collections content
print(yaml.dump(collections, default_flow_style=False))

