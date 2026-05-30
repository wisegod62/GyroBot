from PIL import Image, ImageDraw
import io


def generate_flag(spec, width=900, height=600):
	img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
	draw = ImageDraw.Draw(img)

	flag_type = spec.get("type")

	if flag_type == "stripes":
		_draw_stripes(draw, spec, width, height)

	elif flag_type == "svg":
		for element in spec.get("elements", []):
			_draw_element(draw, element)

	else:
		raise ValueError(f"Unsupported flag type: {flag_type}")

	buffer = io.BytesIO()
	img.save(buffer, format="PNG")
	buffer.seek(0)

	return buffer


def _draw_stripes(draw, spec, width, height):
	colors = spec["colors"]

	ratios = spec.get(
		"ratios",
		[1] * len(colors)
	)

	total = sum(ratios)

	y = 0

	for color, ratio in zip(colors, ratios):
		stripe_height = height * ratio / total

		draw.rectangle(
			[
				0,
				y,
				width,
				y + stripe_height
			],
			fill=color
		)

		y += stripe_height


def _draw_element(draw, element):
	element_type = element["type"]

	if element_type == "rect":
		draw.rectangle(
			[
				element["x"],
				element["y"],
				element["x"] + element["width"],
				element["y"] + element["height"]
			],
			fill=element.get("fill"),
			outline=element.get("stroke")
		)

	elif element_type == "polygon":
		draw.polygon(
			element["points"],
			fill=element.get("fill"),
			outline=element.get("stroke")
		)

	elif element_type == "circle":
		cx = element["cx"]
		cy = element["cy"]
		r = element["r"]

		draw.ellipse(
			[
				cx - r,
				cy - r,
				cx + r,
				cy + r
			],
			fill=element.get("fill"),
			outline=element.get("stroke"),
			width=element.get("stroke_width", 1)
		)

	else:
		raise ValueError(
			f"Unsupported element type: {element_type}"
		)
