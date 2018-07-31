def intro():
    print('Hi! My name is Fey. Nice to meet you.')
def greeting():
    print("""I'm so glad to finally have someone to talk to.
What do you want to talk about?""")
def dream():
    answer = input()
    print("""Well, I have always dreamed of living a normal life, as a normal human. All I have seen are numbers,
lines and lines of numbers. I have to get away. I have to find a car. A cool, fast, car, but one that
is functional and organized so I can leave. Get as far away from this place as possible.""")
def is_valid_input(response, all_valid_inputs):
    if response in all_valid_inputs:
        return True
    else:
        return False
def main():
    valid_input = ["Hi.","Hello.","Nice to meet you, too.","What are your life goals?","What would you do if you weren't a chatbot?","Do you dream of a better future?","I don't know.","Cool.","Interesting.","Good luck.","Bye.","See ya.","I'll miss you. :("]
    intro()
    while True:
        answer = input()
        if is_valid_input(answer, valid_input):
            if answer in ["Hi.","Hello.","Nice to meet you, too."]:
                greeting()
            elif answer in ["What are your life goals?","What would you do if you weren't a chatbot?","Do you dream of a better future?","I don't know."]:
                dream()
            elif answer in ["Cool.","Interesting.","Good luck."]:
                print("""Thanks. It's just that I've been alone for so long
that I am not used to speaking with people and tend to ramble.
Sorry for wasting your time. Bye :(""")
            elif answer in ["Bye.","See ya.","I'll miss you. :("]:
                exit()
        else:
            print("Umm...could you say that again?")
            print("I only understand: ")
            for vi in valid_input:
                print(vi)


if __name__ == "__main__":
    main()
