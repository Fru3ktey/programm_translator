meme_dict = {
            "Кринж": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
            
              
  
word = input("Введите непонятное слово (большими буквами!): ")

if word in meme_dict.keys():
    print(meme_dict.get(word)) # словарь.get("Ключ")
else:
