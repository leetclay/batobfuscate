from pyqcolor import Colorate, Colors


def display_banner():
    banner_text = """
    ____       _____    _   _        ___  _     _____           ____     _____
   | __ )  __ |_   _|__| | | |      / _ \| |__ |  ___|   _ ___ / ___|__ |_   _|__
   |  _ \ / _  || |/ __| |_| |_____| | | |  _ \| |_ | | | / __| |   / _  || |/ _ \`
   | |_) | (_| || | (__|  _  |_____| |_| | |_) |  _|| |_| \__ \ |__| (_| || |  __/
   |____/ \__,_||_|\___|_| |_|      \___/|_ __/|_|   \__,_|___/\____\__,_||_|\___|
                            \n\n
"""
    print(Colorate.Vertical(Colors.green_to_yellow, banner_text, 2))

display_banner()
