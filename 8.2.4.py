def sort_anagrams(list_of_strings):
    # יצירת מבנה נתונים set ריק
    anagram_set = set()

    # רשימה ריקה לאחזור את התוצאה
    result = []

    # לעבור על רשימת המחרוזות ולסדר אותן לפי אנגרמות
    for word in list_of_strings:
        # יצירת אנגרמה - המילה מסודרת לפי האותיות שבה
        sorted_word = ''.join(sorted(word))

        # בדיקה האם המילה היא אנגרמה שכבר נמצאה במבנה הנתונים set
        # אם כן, נמצא את הרשימה המתאימה למילה ונוסיף את המילה לתוך הרשימה
        if sorted_word in anagram_set:
            for anagram_group in result:
                if sorted_word in anagram_group:
                    anagram_group.append(word)
        else:
            # אם לא נמצאה האנגרמה במבנה הנתונים, נוסיף אותה בפורמט של רשימה
            anagram_set.add(sorted_word)
            result.append([word])

    return result


# דוגמאות הרצה
list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless',
                 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
result = sort_anagrams(list_of_words)
print(result)
