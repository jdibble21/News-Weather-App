from weatherAPI import WeatherData
from newsAPI import NewsData
from PyQt5.QtWidgets import *

def getAppData():
    global NData
    global WData
    global weatherInput
    News = NewsData()
    News.getTopStories()
    NData.setText(News.top_stories)
    Weather = WeatherData()
    Weather.getData(weatherInput.text())
    WData.setText(Weather.currentWeather)

app = QApplication([])
window = QWidget()
Wlabel = QLabel("Weather Data")
WData = QLabel("")
Nlabel = QLabel("News Data")
NData = QLabel("")
weatherInput = QLineEdit()
weatherInput.setText("Enter a city and state to get weather for (separate by comma)")
getDataButton = QPushButton("Get Data")
getDataButton.clicked.connect(getAppData)

layout = QVBoxLayout()
layout.addWidget(Wlabel)
layout.addWidget(WData)
layout.addWidget(Nlabel)
layout.addWidget(NData)
layout.addWidget(weatherInput)
layout.addWidget(getDataButton)

window.setLayout(layout)
window.setWindowTitle("Weather and News Service")
window.resize(1100,1300)
window.show()
app.exec_()