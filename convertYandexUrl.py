from os import path

work_directory = path.dirname(path.abspath(__file__))


def main():
    line = "https://yandex.ru/maps/?ll=29.684150%2C59.811507&z=8&mode=search&text=%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C&sll=34.042788%2C44.855022&sspn=4.136353%2C1.598069&rl=29.67316387%2C59.92475770~0.42846680%2C-0.11325035~-0.09887695%2C-0.07479101~0.11535645%2C-0.03329445~0.02197266%2C0.08594269~0.12084961%2C-0.01938703~-0.01647949%2C-0.11099999~0.20874023%2C0.00555878~0.26367188%2C0.08604288~-0.24169922%2C0.12450647~0.08789063%2C0.13779392~-0.26367187%2C0.11530338~-0.27465820%2C0.03834465~-0.28564453%2C0.07655481~-0.30761719%2C-0.06013512~-0.43945312%2C0.03828060~-0.49438477%2C0.24502160~0.14282227%2C0.30234503~-0.26367188%2C-0.10226284~-0.14282227%2C-0.12422929~-0.43945312%2C0.01623103~0.71411133%2C0.40312838~0.12084961%2C-0.00534166~0.23071289%2C0.18111226~0.43945313%2C0.16951217~0.12084961%2C-0.03700255~0.15380859%2C-0.07413648~0.35156250%2C-0.04244244~2.97729492%2C-0.45450261~0.26367187%2C0.05380897~0.05493164%2C0.12341780~0.21972656%2C0.06420252~-0.01098633%2C0.08540177~0.37353516%2C-0.09609318~0.14282227%2C0.17063105~-0.16479492%2C0.04251412~-0.18676758%2C-0.07443738~-0.17578125%2C0.10097958~0.17578125%2C0.06890498~0.68115234%2C0.01058735~0.15380859%2C-0.10072429~0.12084961%2C0.14303793~0.64819336%2C-0.03702131~0.17578125%2C0.04230649~0.00000000%2C-0.13239780~0.21972656%2C0.02122122~0.05493164%2C-0.10624947~-0.10986328%2C-0.14400631~-0.36254883%2C-0.12855648~0.10986328%2C-0.31824812~-0.09887695%2C-0.27764477~-0.01098633%2C-0.17542185~0.28564453%2C-0.04950656~-0.09887695%2C-0.09371547~0.05493164%2C-0.18267803~0.21972656%2C0.03328891~-0.03295898%2C-0.11109239~-0.14282227%2C0.01668743~0.02197266%2C-0.12256799~-0.19775391%2C0.00000000~0.15380859%2C-0.10061663~-0.26367188%2C-0.15992550~-0.30761719%2C-0.04502733~-0.10437012%2C-0.12695957~-0.44494629%2C0.11287629~-0.23620605%2C-0.05356966~-0.43395996%2C0.17449546~-0.00000000%2C0.05890035~-0.30761719%2C0.00560421~0.00000000%2C-0.06731190~-0.08789063%2C0.00280734~-0.25268555%2C0.10930478~-0.07690430%2C-0.08404921~-0.08239746%2C0.00841434~-0.10986328%2C-0.08704912~0.02746582%2C-0.05064735~-0.13732910%2C-0.10434578~-0.19226074%2C0.00282436~-0.15930176%2C0.08180483~0.04394531%2C0.06474019~-0.34057617%2C0.16271097~-0.20874023%2C-0.09809403~-0.20324707%2C0.03646817~0.01098633%2C-0.14892467~-0.09887695%2C-0.04226733~-0.01647949%2C-0.07621355~-0.18676758%2C-0.11605757~-0.17028809%2C0.11323158~-0.14831543%2C-0.06223104~0.02197266%2C-0.07369180~-0.27465820%2C-0.12507019~-0.01098633%2C-0.10266835~-0.54931641%2C0.01713256~-0.02197266%2C-0.22913150~-0.30761719%2C-0.09207562~-0.48339844%2C0.14950000~-0.32958984%2C0.25154711~-0.54931641%2C0.06260220~-0.17578125%2C-0.05690640~-0.09887695%2C0.13641770~-0.18676758%2C0.03968676~-0.26367187%2C-0.02834300~0.14282227%2C0.26550116~0.25268555%2C0.06184082~0.08239746%2C0.06453131~-0.17578125%2C0.10914168~0.07690430%2C0.11157367~-0.13183594%2C0.09454641~0.16479492%2C0.12749074~0.13732910%2C-0.13304489~0.15380859%2C-0.00833297~0.03295898%2C0.15520615~0.08789062%2C0.01382253~0.18676758%2C-0.07748036~0.18676758%2C0.01938703~0.15380859%2C0.09124390~-0.02746582%2C0.07997712~0.19226074%2C0.02753350"
    line = find_right_by_separator(line, 'rl=')
    line = line.replace('%2C', ' ')
    points_text = line.split('~')

    points = list()
    prev_point = {'x': 0., 'y': 0.}

    for point_text in points_text:
        print point_text

    print

    for point_text in points_text:
        coord = point_text.split(' ')
        x = prev_point['x'] + float(coord[1])
        y = prev_point['y'] + float(coord[0])
        prev_point = {'x': x, 'y': y}
        points.append(prev_point)

    if len(points) > 0:
        points.append(points[0])

    result = ''
    for point in points:
        x = point['x']
        y = point['y']
        show_x = x + 360. if x < -90. else x
        show_y = y + 360. if y < -90. else y
        result += "[{0:.3f}, {1:.3f}],".format(show_y, show_x)

    print result

def find_right_by_separator(line, separator):
    parts = line.split(separator)
    return parts[1]

if __name__ == "__main__":
    main()