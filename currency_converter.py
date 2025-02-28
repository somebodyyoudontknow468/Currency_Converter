import tkinter as tk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x300")  # Fenster breiter gemacht

        # Spracheinstellungen
        self.language = "de"  # Start mit Deutsch

        # Aktuelle Sprache Anzeige oben links
        self.language_label = tk.Label(root, text="Selected Language: Deutsch")
        self.language_label.pack(pady=5, anchor="w")

        self.label = tk.Label(root, text="Geben Sie den Betrag in EUR ein:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button_usd = tk.Button(root, text="USD", command=lambda: self.convert("USD"))
        self.button_usd.pack(pady=5)

        self.button_yen = tk.Button(root, text="Yen", command=lambda: self.convert("JPY"))
        self.button_yen.pack(pady=5)

        self.button_sek = tk.Button(root, text="Schwedische Kronen", command=lambda: self.convert("SEK"))
        self.button_sek.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)

        # Button für Sprachwechsel
        self.language_button = tk.Button(root, text="Change Language", command=self.change_language)
        self.language_button.place(relx=1.0, rely=0.0, anchor="ne")

        self.update_labels()

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
            self.result_label.config(text=self.get_text("invalid_input"))

    def change_language(self):
        languages = ["de", "en", "ja", "sv"]
        current_index = languages.index(self.language)
        self.language = languages[(current_index + 1) % len(languages)]
        self.update_labels()

    def update_labels(self):
        # Sprache oben links anzeigen (immer in Englisch)
        if self.language == "de":
            self.language_label.config(text="Selected Language: Deutsch")
            self.label.config(text="Geben Sie den Betrag in EUR ein:")
            self.button_usd.config(text="USD")
            self.button_yen.config(text="Yen")
            self.button_sek.config(text="Schwedische Kronen")
            self.language_button.config(text="Change Language")
            self.result_label.config(text="")
        elif self.language == "en":
            self.language_label.config(text="Selected Language: English")
            self.label.config(text="Enter the amount in EUR:")
            self.button_usd.config(text="USD")
            self.button_yen.config(text="Yen")
            self.button_sek.config(text="Swedish Krona")
            self.language_button.config(text="Change Language")
            self.result_label.config(text="")
        elif self.language == "ja":
            self.language_label.config(text="Selected Language: 日本語")
            self.label.config(text="EURの金額を入力してください:")
            self.button_usd.config(text="USD")
            self.button_yen.config(text="円")
            self.button_sek.config(text="スウェーデンクローナ")
            self.language_button.config(text="Change Language")
            self.result_label.config(text="")
        elif self.language == "sv":
            self.language_label.config(text="Selected Language: Svenska")
            self.label.config(text="Ange beloppet i EUR:")
            self.button_usd.config(text="USD")
            self.button_yen.config(text="Yen")
            self.button_sek.config(text="Svenska kronor")
            self.language_button.config(text="Change Language")
            self.result_label.config(text="")

    def get_text(self, key):
        texts = {
            "invalid_input": {
                "de": "Ungültige Eingabe!",
                "en": "Invalid input!",
                "ja": "無効な入力！",
                "sv": "Ogiltig inmatning!"
            }
        }
        return texts[key][self.language]

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
