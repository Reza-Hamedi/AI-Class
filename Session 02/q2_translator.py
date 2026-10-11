# Global Scop
dictionary = {
    "hello": "سلام", "goodbye": "خداحافظ", "book": "کتاب", "water": "آب", "food": "غذا", "name": "اسم",
    "house": "خانه", "school": "مدرسه", "friend": "دوست", "computer": "کامپیوتر", "music": "موسیقی",
    "car": "ماشین", "phone": "تلفن", "table": "میز", "chair": "صندلی", "door": "در", "and": "و",
    "window": "پنجره", "teacher": "معلم", "student": "دانش‌آموز", "city": "شهر", "country": "کشور",
    "family": "خانواده", "mother": "مادر", "father": "پدر", "brother": "برادر", "sister": "خواهر",
    "morning": "صبح", "night": "شب", "happy": "خوشحال", "beautiful": "زیبا", "strong": "قوی", "is": "هست",
    "i": "من", "love": "عاشق", "python": "پایتون", "AI": "هوش مصنوعی", "am": "هستم", "or": "یا"
}

# تابع جدا کننده
def convertTolist():
    sentence = input("Write your sentence. \n")
    sentence = "I love python and AI" if not sentence else sentence    
    wordList = sentence.split(" ")
    return wordList


# تابع مترجم
def translator():
    wordList = convertTolist()
    Translated_Words = 0
    Untranslated_words = 0
    Translated_sentence = []
    for word in wordList:
        if word.lower() in dictionary.keys():
            Translated_sentence.append(dictionary.get(word.lower()))
            Translated_Words += 1
        else:
            Translated_sentence.append(f"[{word}]")
            Untranslated_words += 1
    return Translated_sentence, Untranslated_words, Translated_Words

# تابع فراخوان
def main():
    Translated_sentence, Untranslated_words, Translated_Words = translator()
    print("Translated_sentence: ")
    print(" ".join(Translated_sentence))
    print(f"{Translated_Words} words were translated :)\n {Untranslated_words} words were not translated :( ")

main()