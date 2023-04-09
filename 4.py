
'''
4) Рост взрослого населения города X имеет нормальное распределение.

Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.

Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:

а). больше 182 см

б). больше 190 см

в). от 166 см до 190 см

г). от 166 см до 182 см

д). от 158 см до 190 см

е). не выше 150 см или не ниже 190 см

ё). не выше 150 см или не ниже 198 см

ж). ниже 166 см.
'''
from statistics import NormalDist

def z_value(height):
    return (height-174)/8


print(z_value(182))
print(z_value(190))
NormalDist().cdf(z_value(182))

# Больше 182
P=1-NormalDist().cdf(z_value(182))
print(P)

z=z_value(190)
# Больше 190
P=1-NormalDist().cdf(z)
print(P)

# от 166 до 190
z1=z_value(166)
z2=z_value(190)
P=NormalDist().cdf(z2)-NormalDist().cdf(z1)
print(P)

# от 166 до 182
z1=z_value(166)
z2=z_value(182)
P=NormalDist().cdf(z2)-NormalDist().cdf(z1)
print(P)

# от 158 до 190
z1=z_value(158)
z2=z_value(190)
P=NormalDist().cdf(z2)-NormalDist().cdf(z1)
print(P)

# не выше 150 см или не ниже 190 см
z1=z_value(150)
z2=z_value(190)
P=NormalDist().cdf(z1)+(1-NormalDist().cdf(z2))

# не выше 150 см или не ниже 198 см
z1=z_value(150)
z2=z_value(198)
P=NormalDist().cdf(z1)+(1-NormalDist().cdf(z2))

# ниже 166 см.
z=z_value(166)
P=NormalDist().cdf(z)
