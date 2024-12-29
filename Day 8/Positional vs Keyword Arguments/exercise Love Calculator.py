def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()
    word1 = "true"
    word2 = "love"

    count_TRUE = 0
    count_LOVE = 0

    for letter in word1:
        count_TRUE += combined_names.count(letter)

    for letter in word2:
        count_LOVE += combined_names.count(letter)

    print(f"{count_TRUE}{count_LOVE}")

calculate_love_score("Angela Yu", "Jack Bauer")