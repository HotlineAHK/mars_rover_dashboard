from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    battery = 68  # Уровень заряда батареи в процентах
    subsystems = [
        {"name": "Навигационный модуль", "status": "ok", "value": 45},
        {"name": "Силовая установка", "status": "warning", "value": 82},
        {"name": "Детектор радиации", "status": "critical", "value": 94},
        {"name": "Бортовой компьютер", "status": "ok", "value": 35},
        {"name": "Манипулятор-бур", "status": "warning", "value": 92}
    ]
    return render_template("index.html", battery=battery, subsystems=subsystems)

if __name__ == "__main__":
    app.run(debug=True)
