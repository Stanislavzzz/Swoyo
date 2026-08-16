# Дан список слов
# Создайте новый список, содержащий только уникальные слова.
# Если слово встречается несколько раз, оно должно попасть в новый список только один раз.
# Порядок первого появления элементов нужно сохранить.
words = ["python", "java", "python", "go", "java", "javascript"]
new_words = []
for i in words:
    if i not in new_words:
        new_words.append(i)
print(new_words)
