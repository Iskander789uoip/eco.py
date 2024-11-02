# Импорт необходимых библиотек
from flask import Flask, render_template

app = Flask(__name__)

# Функция для расчета энергозатратности
def result_calculate(size, lights, device):
    # Коэффициенты для расчета энергопотребления
    home_coef = 100    # Энергозатраты на размер дома
    light_coef = 0.04  # Энергозатраты на количество ламп
    devices_coef = 5   # Энергозатраты на количество устройств
    return size * home_coef + lights * light_coef + device * devices_coef 

# Первая страница (главная)
@app.route('/')
def index():
    return render_template('index.html')

# Вторая страница - выбор количества осветительных приборов
@app.route('/<int:size>')
def lights(size):
    return render_template('lights.html', size=size)

# Третья страница - выбор количества электронных устройств
@app.route('/<int:size>/<int:lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

# Финальная страница с расчетом результата
@app.route('/<int:size>/<int:lights>/<int:device>')
def end(size, lights, device):
    result = result_calculate(size, lights, device)
    return render_template('end.html', result=result)

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
