import wikipedia

print("Enter a wiki page")
user_input = input(""">>>""")
while user_input != "":
    try:
        page = wikipedia.page(user_input, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
        print("Enter a wiki page")
    except wikipedia.exceptions.DisambiguationError:
        print("Here are the top suggestions")
        print(wikipedia.search(user_input, results=5))
    user_input = input(""">>>""")
print("Finished")

