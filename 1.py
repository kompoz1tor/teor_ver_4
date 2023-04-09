'''
1) Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].

Найдите ее среднее значение и дисперсию.
'''
def average_value_and_dispersion(a,b):
    M = (a+b)/2
    D = ((b-a)**2)/12
    return f'На промежутке ({a};{b}]\nСреднее значение: {M}\nДисперсия: {D}'

print(average_value_and_dispersion(200,800))