import pickle

user_data = {
    'name': 'Никика',
    'age': 19,
    'email': 'n@f.by'
}

with open('user_data.pickle', 'wb') as file:
    pickle.dump(user_data, file)

with open('user_data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
