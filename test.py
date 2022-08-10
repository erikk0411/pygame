if typ == 1:
    if 550 > hindery > 480:
        if hinderfil == spelarefil:
            return True
if typ == 2:
    if 550 > hindery > 480:
        if spelarefil == 1:
            return True
    if 550 > hindery - 50 > 480:
        if spelarefil == 2:
            return True
if typ == 3:
    if 550 > hindery + 28 > 480:
        if spelarefil == 1 or spelarefil == 2:
            return True
if typ == 4:
    if 550 > hindery > 480:
        if spelarefil == 3:
            return True
    if 550 > hindery - 50 > 480:
        if spelarefil == 2:
            return True
if typ == 5:
    if 550 > hindery > 480:
        if spelarefil == 3:
            return True
    if 550 > hindery - 28 > 480:
        if spelarefil == 2 or spelarefil == 3:
            return True
if typ == 6:
    if 550 > hindery > 480:
        if spelarefil == 3 or spelarefil == 1:
            return True
    if 550 > hindery - 400 > 480:
        if spelarefil == 2:
            return True
if typ == 7:
    if 550 > hindery > 480:
        if spelarefil == 3 or spelarefil == 1:
            return True
