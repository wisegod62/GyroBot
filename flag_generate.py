from PIL import Image, ImageDraw
import io


def generate_flag(colors: list[str], width: int = 600, height: int = 400):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    stripe_height = height // len(colors)

    for i, color in enumerate(colors):
        draw.rectangle(
            [
                (0, i * stripe_height),
                (width, (i + 1) * stripe_height)
            ],
            fill=color
        )

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer
