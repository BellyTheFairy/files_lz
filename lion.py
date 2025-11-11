import matplotlib
import docx


doc = docx.Document("lion.docx")    #открываем документ 


word = input("Введите слово - ")     #импортируем слово и букву для полсчета
letter = input("Введите букву - ")
count1 = 0    #считчик для упоминаний слова
count2 = 0    #счетчик для буквы

text = ""
for para in doc.paragraphs:
    text += para.text + " "

text = text.lower()    #приводим текст к нижнему регистру для удобства

a = text.split()     #считаем количество упоминаний слова

for w in a:
    if w == word.lower():
        count1 += 1

for ch in text:
    if ch == letter.lower():
        count2 += 1


total_words = len(words)    #количество слов в тексте 
total_letters = len(text)    #количество букв в тексте

word_percent = (word_count / total_words * 100) 
letter_percent = (letter_count / total_letters * 100) 

data = [                                                     # Таблица для matplotlib
    ["Слово", word, word_count, f"{word_percent:.2f}%"]
]

fig, ax = plt.subplots()
ax.axis("off")

table = ax.table(
    cellText=data,
    colLabels=["Слово", "Частота встречи, раз", "Частота встречи, в %"],
)

table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.5)
plt.show()
