def generate_acronym(user_input):
    acronym = ""
    for word in user_input.split():
        if word:
            acronym += word[0].upper()
    return acronym

def main():
    user_input = input("Enter a phrase to generate its acronym: ")
    acronym = generate_acronym(user_input)
    print(f"The acronym for '{user_input}' is: {acronym}")

main()