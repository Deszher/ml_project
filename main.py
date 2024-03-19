from transformers import pipeline

# Создаем объект pipeline для перевода текста
pipe = pipeline("translation", model="WelfCrozzo/T5-L128-belarusian")

# Текст для перевода
TEXT = "Не ищи счастье – оно всегда у тебя внутри"

# Выводим оригинальный текст и его перевод на белорусский язык
print(f"'{TEXT}' в переводе на белорусский язык означает - "
      f"'{pipe(TEXT, max_length=50)[0]['translation_text']}'")
