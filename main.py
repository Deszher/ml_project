# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("translation", model="WelfCrozzo/T5-L128-belarusian")

text = "Не ищи счастье – оно всегда у тебя внутри"
print(f"'{text}' в переводе на белорусский язык означает - '{pipe(text, max_length=50)[0]['translation_text']}'")
