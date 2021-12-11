def get_announcement(x: int, y: str, z: float) -> str:
    return f'{x}時の{y}は{z}'


x = 12
y = '気温'
z = 22.4
print(get_announcement(x, y, z))
