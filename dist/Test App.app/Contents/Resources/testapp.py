import rumps # pip install rumps

class TimerApp(rumps.App):
    def __init__(self):
        self.app = rumps.App("TimerApp" , "🧋")

    def run(self):
        self.app.run()

if __name__ == "__main__":
    app = TimerApp()
    app.run()