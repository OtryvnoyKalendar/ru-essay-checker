from window import Window
from loadconf import Settings

app = Window()

def get_app():
    global app
    return app

if __name__ == "__main__":
    Settings.read_from_file()
    app.run()

