import tkinter as tk
 
class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Währungsrechner")
        self.root.geometry("300x300")
 
        self.label = tk.Label(root, text="Geben Sie den Betrag in EUR ein:")
        self.label.pack(pady=5)
 
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
 
        self.button_usd = tk.Button(root, text="USD ", command=lambda: self.convert("USD"))
        self.button_usd.pack(pady=5)
 
        self.button_yen = tk.Button(root, text="Yen", command=lambda: self.convert("JPY"))
        self.button_yen.pack(pady=5)
 
        self.button_sek = tk.Button(root, text="Schwedische Kronen", command=lambda: self.convert("SEK"))
        self.button_sek.pack(pady=5)
 
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)
 
    def convert(self, currency):
        try:
            amount_eur = float(self.entry.get())
            if currency == "USD":
                amount = amount_eur * 1.1  # 1 EUR = 1.1 USD
                self.result_label.config(text=f"{amount_eur:.2f} EUR = {amount:.2f} USD")
            elif currency == "JPY":
                amount = amount_eur * 130.0  # 1 EUR = 130 JPY
                self.result_label.config(text=f"{amount_eur:.2f} EUR = {amount:.2f} JPY")
            elif currency == "SEK":
                amount = amount_eur * 10.5  # 1 EUR = 10.5 SEK
                self.result_label.config(text=f"{amount_eur:.2f} EUR = {amount:.2f} SEK")
        except ValueError:
            self.result_label.config(text="Ungültige Eingabe!")
 
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
 