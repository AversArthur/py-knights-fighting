from app.knight import Knight


def result(first: Knight, second: Knight) -> None:
    first.hp -= second.power - first.protection
    second.hp -= first.power - second.protection

    if first.hp < 0:
        first.hp = 0
    if second.hp < 0:
        second.hp = 0
