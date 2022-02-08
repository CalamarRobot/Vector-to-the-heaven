import tkinter as tk


class Apllication(tk.Tk):
    """
    Contain the frame of the application
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Vector to the Heaven")
        self.iconbitmap("star.ico")
        self.config(bg="#ffdf00")
    
    def long_vector(self):
        """
        Contain the long vector frame of the application
        """
        self.frame = tk.LabelFrame(self, text="Vecteur 2 points", bg="#ffdf00")
        self.first_letter = tk.Entry(self.frame, width=3, bg="#ffdf00")
        self.first_indice = tk.Entry(self.frame, width=3, bg="#ffdf00")
        self.second_letter = tk.Entry(self.frame, width=3, bg="#ffdf00")
        self.second_indice = tk.Entry(self.frame, width=3, bg="#ffdf00")

if __name__ == "__main__":
    app = Apllication()
    app.mainloop()
# vecteur 2 points avec indice, qui peut etre vide,
# simple vecteur, ou vecteur avec indice
# produit scalaire, produit vectoriel
