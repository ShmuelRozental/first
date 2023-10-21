nethur_strings = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
def sort_anagrams(list_of_strings):
    sorted_strings =[]
    short_list = []
    result = []

# יצירת לולאה העוברת על הרשימה המלאה ומסדרת מחרוזת אחרי מחרוזת ע"י מתודת SORTED
# ואח"כ מחזירה את המחרוזת למחרוזת שלמה ע"י JOIN

    for i in list_of_strings:
        a =  ''.join(sorted(i))
        sorted_strings.append(a)

#יצירת רשימה חדשה קצרה עם הופעה אחת לכל מילה שאין לה היפוך אותיות
#  היה ניתן לבצע זאת ע"י פונקציית ()SET אבל הפונקצייה תחזיר רשימה קצרה אומנם ללא סדר מסויים

    for i in sorted_strings:
        if i not in short_list:
            short_list.append(i)
# כעת יש לנו את הרשימה המקורית - LIST_OF_STRINGS
# רשימה באורך הרשימה המקורית אך כל מחרוזת ממויינת לפי הסדר - SORTED_STRINGS
#ועוד רשימה המכילה מופע אחד בלבד של כל מילה אנאגרמית - SHORT_LIST



#(UNIQ)מה שנשאר לעשות הוא רק לעבור איבר איבר ברשימה הקצרה
#לפתוח לו רשימה בפני עצמה(NEW_ARRY) ולעבור בלולאה שנייה (לולאה בתוך לולאה)
 #על הרשימה המקורית מחרוזת מחרוזת, עם מיון לפי סדר והחזרת המיון למחרוזת (JOIN)
#אם המחרוזת בלולאה הפנימית = = למחרוזת מהלולאה החיצונית נכניס את המחרוזת שפתחנו עבור אותה מחרוזת (UNIQ)
#את כל זה נכניס לתוך רשימה שהגדרנו מראש - RESULT
    for uniqe in short_list:
        new_arry = []
        for word in list_of_strings:
            if ''.join(sorted(word)) == uniqe:
                 new_arry.append(word)
        result.append(new_arry)
    return result




print(sort_anagrams(nethur_strings))
