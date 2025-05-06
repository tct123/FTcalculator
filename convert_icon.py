import re
from cairosvg import svg2png


def correct_svg(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Korrigiere die Dezimaltrennzeichen für stroke-opacity und fill-opacity
    content = re.sub(
        r'stroke-opacity="([\d,]+)"', lambda m: m.group(0).replace(",", "."), content
    )
    content = re.sub(
        r'fill-opacity="([\d,]+)"', lambda m: m.group(0).replace(",", "."), content
    )

    corrected_file_path = "corrected_icon.svg"
    with open(corrected_file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return corrected_file_path


svg_path = "icon.svg"
corrected_svg_path = correct_svg(svg_path)

svg2png(
    url=corrected_svg_path,
    write_to="src/assets/icon.png",
    output_width=1024,
    parent_height=1024,
)

svg2png(
    url=corrected_svg_path,
    write_to="src/assets/splash_android.png",
    output_width=1152,
    parent_height=1152,
)
