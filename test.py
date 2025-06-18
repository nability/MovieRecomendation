from config import model

response = model.generate_content("Berikan 3 film petualangan terbaik sepanjang masa.")
print(response.text)
