start = '''
It's the final day of your training.
Pico's mentor, a flying hippo, is sending him off to embark on an adventure
to discover who you truly are.

Pico is standing on a hill awaiting the arrival of his mentor.
When he arrives, this discussion ensues:

Hippo Mentor: Pico, you have done a very good job on your training.
I believe you are now ready to go off on your own...and "find yourself".
Do me proud, son.

Oh, and try not to die.

Pico: I will Hippo Mentor!

Pico begins his adventure and stumbles upon a four forked road.
'''

print(start)

print("""Should Pico take path one, path two, path three, or path four?
      Type one, two, three, or four.""")
user_input = input()
if user_input == "one":
    print("""Pico decided to go down path one. After much time spent walking it turned out
          that Pico didn't actually learn anything from his Hippo Mentor. So in the end,
          Pico died from falling off a cliff.""")

elif user_input == "two":

    print("""Pico decided to go down path two. After much time spent walking Pico stumbles upon a Sphinx.
          The Sphinx was guarding a box and told Pico that the box held something very valuable. If Pico
          wanted its contents, he would have to answer the Sphinx's riddle in three tries or less.
          Otherwise, he would die.

          Should Pico try to win the box? y/n? """)

    response = input()
    if response == "y":
        print("""Sphinx: It has a long neck, A name of a bird, Feeds on cargo ships, It's not alive.
        What is it?""")

        Ans = "a crane" and "crane"
        correct = False
        for tries in range (1,4):
            guess = input()
            if guess == Ans:
                correct = True
                print("""Sphinx: You are correct. Therefore you recieve the box. Congradulations!

                    Inside the box, Pico finds many riches and leaves the woods to live a happy life
                    in Beverly Hills with his wife, two and a half kids, and his dog all wrapped inside
                    a white picket fence.""")
                break
            elif guess != Ans:
                print("You are incorrect, guess again.")
        if not correct:
            print("""Sphinx: Pico you have answered incorrectly three times, now you die!

              Sadly Pico wasn't as great at riddles as he thought. In the end he died a tragic
              death at the hands of the Sphinx.""")

    if response == "n":
        print("""Pico continued on without obtaining the box, but somehow ended up dying anyway.""")

elif user_input == "three":
    print("""Pico decided to go down path three. After much time spent walking it turned out
          that Pico didn't actually learn anything from his Hippo Mentor. So in the end,
          Pico died from hitting his head on a tree limb then falling off a cliff.""")

elif user_input == "four":
    print("""Pico decided to go down path fourth. After much time spent walking it turned out
          that Pico didn't actually learn anything from his Hippo Mentor. So in the end,
          Pico died from getting attacked by a swarm of bees then falling off a cliff while
          attempting to escape the bees.""")
