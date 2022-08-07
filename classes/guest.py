class Guest:
    def __init__(self, name, wallet, song):
        self.name = name
        self.wallet = wallet
        self.song = song
        
    def reduce_wallet(self, amount):
        self.wallet -= amount