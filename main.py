import spacy
import tkinter as tk
import tkinter

def tkinter():
    window = tk.Tk() 
    window.minsize(width="300",height="300")
    window.maxsize(width="900",height="500")

    def nltk_func():
        text = text_box.get("1.0",tk.END) 
        labelName.config(text = " ")
        
        analyze1 = []
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)

        # Analyze syntax
        analyze = ("Noun phrases:", [chunk.text for chunk in doc.noun_chunks],
        "Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

        # Find named entities, phrases and concepts
        for entity in doc.ents:
            analyze1.append(entity.text)
            analyze1.append(entity.label_)
            
        labelName.config(text = str(analyze)+str(analyze1))

    text_box = tk.Text()
    text_box.pack()

    buttonName = tk.Button(text="submit", command = nltk_func)
    buttonName.pack()


    labelName = tk.Label(text = "")
    labelName.pack()


    window.mainloop() 
tkinter()
