class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def measurements_changed(self):
        self.notify()

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()

class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data):
        self._weather_data = weather_data
        weather_data.attach(self)

    def update(self, subject):
        if isinstance(subject, WeatherData):
            self._temperature = subject._temperature
            self._humidity = subject._humidity
            self.display()

    def display(self):
        print("Current conditions: ", self._temperature, "F degrees and ", self._humidity, "% humidity")

# Contoh penggunaan
weather_data = WeatherData()
current_display = CurrentConditionsDisplay(weather_data)

# Simulasi perubahan data cuaca
weather_data.set_measurements(80, 65, 30.4)
