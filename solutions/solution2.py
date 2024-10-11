
# solution 2
# pip install scipy
from scipy.optimize import fsolve

# 수식 정의
def equations(vars):
    x, y, z = vars
    eq1 = x / (y + z) + y / (x + z) + z / (x + y) - 4  # 원래 주어진 수식
    eq2 = x - y - 1  # x와 y가 1 차이 난다고 가정한 추가 방정식
    eq3 = y - z - 1  # y와 z가 1 차이 난다고 가정한 추가 방정식
    return [eq1, eq2, eq3]

# 초기 추정값 설정
initial_guess = [1.0, 2.0, 3.0]  # x, y, z에 대한 초기 추정값

# fsolve로 방정식 풀기
solution = fsolve(equations, initial_guess)

# 결과 출력
# Solution found: x = 0.258380151290432, y = -0.741619848709568, z = -1.741619848709568
print(f"Solution found: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")


# 검산
x = 0.258380151290432
y = -0.741619848709568
z = -1.741619848709568

result = x/(y+z)+y/(x+z)+z/(x+y)
print(result)
