conv = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
def get_answer(key, dict):
	key.lower()
	return dict.get(key)
print(get_answer("пока", conv))

