def letters_a_count(text: str) -> int:
    return(len([word for word in text.split(" ") if "a" in word]))
print(letters_a_count("Laba diena kaip jums sekasi"))


def separate(text: str) -> str:
    return text.replace(" ", "|")
print(separate("Mano vardas yra Sarunas"))