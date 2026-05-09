HINGLISH_DICT = {
    "bekar": "bad",
    "acha": "good",
    "bahut": "very",
    "bakwas": "nonsense",
    "faltu": "useless",
    "ghatiya": "worst",
    "bhai": "bro",
    "yaar": "friend",
    "pareshan": "troubled",
    "gussa": "angry"
}

def normalize_hinglish(text):

    words = str(text).split()

    normalized_words = []

    for word in words:

        word_lower = word.lower()

        if word_lower in HINGLISH_DICT:
            normalized_words.append(
                HINGLISH_DICT[word_lower]
            )

        else:
            normalized_words.append(word)

    return " ".join(normalized_words)