


import pickle

# Example object
data = {'name': 'John', 'age': 30, 'is_student': False}

# Serialization (pickling)
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialization (unpickling)
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

''''wb' (Write Binary): Opens a file for writing in binary mode. It creates the file if it doesn't exist 
and truncates it if it does.
'rb' (Read Binary): Opens a file for reading in binary mode. The file must exist.
These modes are particularly useful when dealing with non-text files, such as images, videos,
 or serialized Python objects, ensuring that the data is written and read in the correct format without any
 encoding/decoding issues.'''


'''By understanding serialization and the role of the pickle module, you can efficiently manage data transformation
 processes, ensuring that data can be preserved, transmitted, and reconstructed as needed across different parts 
 of your applications or systems.'''