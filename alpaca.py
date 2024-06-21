import ollama

response = ollama.generate(model='llama3',
prompt='what is a qubit? respond under 100 characters')
print(response['response'])