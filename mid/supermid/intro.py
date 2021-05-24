from tkinter import *
class intro():
    def __init__(self, window):

        T = Text(window, height=5, width=52)



        Fact = """This system can help users easily manage citizen and business information, it makes public service management easier."""

        T.pack(fill=BOTH, expand=True)

        # Insert The Fact.
        T.insert(END, Fact)
