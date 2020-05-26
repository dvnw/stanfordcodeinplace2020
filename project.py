"""
Hello world, I'm Amed Ajibola Salaudeen and learner at Stanford Code in Place 2020.
My deepest gratitude to the staff, instructors and professors involved in this program.
My final project is the following program which displays random programming jokes through
the user of API. And at the exit, the program displays a quote.
"""

import requests
from bs4 import BeautifulSoup


def main():

    while True:
        page = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
        soup = BeautifulSoup(page.content, 'html.parser')
        soup = str(soup)

        print(" --- ")

        print(soup[31:-2])
        print(" ")
        user_choice = input("Press Enter for another joke or Type 'exit' to stop the flow> ")

        if user_choice == 'exit':
            print(
                "\"I'm gonna fix that last joke by taking out all the words and adding new ones.\" \n    --Mitch Hedberg")

            break


if __name__ == '__main__':
    main()