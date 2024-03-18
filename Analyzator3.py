"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Veronika Pindíková
email: veronika.pindikova@gmail.com
discord: Veronika77
"""
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

username = ["Bob", "Ann", "Mike", "Liz"]
password = ["123", "pass123", "password123", "pass123"]
users = dict(zip(username, password))
username_input = input("Username: ")
password_input = input("Password: ")
user_password = users.get(username_input)
if user_password == password_input:
    print("-" * 45)
    input(f"Welcome to the app, {username_input}!\nWe have 3 texts to be analyzed.")
    print("-" * 45)
else:
    print("Unregistered user. Terminating program.")
    exit()
for index, text in enumerate(texts, start=1):
    print(index, text)
    print("-" * 45)
enter = input("Enter a number between 1 and 3 to select: ")
print("-" * 45)    
if not enter.isdigit():
    print("Invalid input. Please enter a valid number.")
    exit()
elif not 1<= int(enter)<=3: 
    print("Invalid input. Please enter a number between 1 and 3.")
    exit()
if 1 <= int(enter) <= 3:
        enter = int(enter)
        selected_text = texts [enter - 1]
        cleaned_words = selected_text.strip(",.").split()
        sum_of_words = len(cleaned_words)       
        title_words = []
        upper_words = []
        lower_words = []
        count_of_numbers = []          
        for word in cleaned_words:      
            if word.isupper() and not any(x.isdigit() for x in word):
                upper_words.append(word)
            elif word.istitle():
                title_words.append(word)
            elif word.islower():
                lower_words.append(word)
            elif word.isdigit():
                count_of_numbers.append(int(word))   
        sum_numbers = sum(count_of_numbers)
        print(f"There are {sum_of_words} words in the selected text.")
        print(f"There are {len(title_words)} titlecase words.")
        print(f"There are {len(upper_words)} uppercase words.")
        print(f"There are {len(lower_words)} lowercase words.")
        print(f"There are {len(count_of_numbers)} numeric strings.")
        print(f"The sum of all the numbers: {sum_numbers}")               
        def analyze_text(texts):
            words = texts.split()
            word_lengths = {}
            for word in words:
                cleaned_word = word.strip(".,")
                word_length = len(cleaned_word)
                word_lengths[word_length] = word_lengths.get(word_length, 0) + 1
            print("-" * 45)
            print(f"LEN:|\tOCCURRENCES\t|NR. ")
            print("-" * 45)
            for length, frequency in sorted(word_lengths.items()):
                print(f"{length:^4}|{'*' * frequency:17}\t|{frequency:}")
         analyze_text(texts[enter - 1]) 
