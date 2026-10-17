from cs50 import get_string
text = get_string("Text: ")






























def main():
    x = count_word()
    y = count_sentence()
    z = count_alphabet()
    l = float((z/x)*100)
    s = float((y/x)*100)
    index_coleman_liau = int(round(0.0588 * l - 0.296 * s - 15.8))
    if index_coleman_liau >= 16:
        print("Grade 16+")
    elif index_coleman_liau < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index_coleman_liau}")

def count_word():
    c_word = 1
    for character in text:
        if character == " ":
            c_word +=1
    return c_word

def count_alphabet():
    c_alphabet = 0
    for character in text:
        if character.isalpha():
            c_alphabet +=1
    return c_alphabet

def count_sentence():
    c_sentence = 0
    for character in text:
        if character == "!" or character == "." or character == "?":
            c_sentence +=1
    return c_sentence


main()
