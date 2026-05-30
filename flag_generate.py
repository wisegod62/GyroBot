from PIL import Image, ImageDraw
import io


def hex_to_rgb(hex_color):
	hex_color = hex_color.lstrip("#")
	return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def lerp(a, b, t):
	return int(a + (b - a) * t)


def generate_flag(spec, width=900, height=600):
	img = Image.new("RGB", (width, height))
	draw = ImageDraw.Draw(img)

	flag_type = spec.get("type")

	if flag_type == "stripes":
		_render_stripes(draw, spec, width, height)

	elif flag_type == "gradient":
		_render_gradient(img, spec, width, height)

	elif flag_type == "composite":
		for layer in spec.get("layers", []):
			_apply_layer(img, draw, layer, width, height)

	buffer = io.BytesIO()
	img.save(buffer, format="PNG")
	buffer.seek(0)
	return buffer


# -------------------------
# STRIPES
# -------------------------
def _render_stripes(draw, spec, width, height):
	colors = spec["colors"]
	ratios = spec.get("ratios")

	if not ratios:
		ratios = [1 / len(colors)] * len(colors)

	y = 0

	for color, ratio in zip(colors, ratios):
		h = int(height * ratio)
		draw.rectangle([(0, y), (width, y + h)], fill=color)
		y += h


# -------------------------
# GRADIENT
# -------------------------
def _render_gradient(img, spec, width, height):
	colors = [hex_to_rgb(c) for c in spec["colors"]]
	direction = spec.get("direction", "horizontal")

	base = Image.new("RGB", (width, height))
	pixels = base.load()

	steps = width if direction == "horizontal" else height

	for i in range(steps):
		t = i / max(steps - 1, 1)
		seg = t * (len(colors) - 1)
		idx = int(seg)
		local_t = seg - idx

		c1 = colors[idx]
		c2 = colors[min(idx + 1, len(colors) - 1)]

		r = lerp(c1[0], c2[0], local_t)
		g = lerp(c1[1], c2[1], local_t)
		b = lerp(c1[2], c2[2], local_t)

		if direction == "horizontal":
			for y in range(height):
				pixels[i, y] = (r, g, b)
		else:
			for x in range(width):
				pixels[x, i] = (r, g, b)

	img.paste(base)


# -------------------------
# LAYERS
# -------------------------
def _apply_layer(img, draw, layer, width, height):
	t = layer.get("type")

	if t == "overlay":
		_render_overlay(draw, layer, width, height)


def _render_overlay(draw, layer, width, height):
	kind = layer.get("kind")
	color = layer.get("color", "#000000")

	if kind == "triangle_left":
		points = [
			(0, 0),
			(int(width * layer.get("width_ratio", 0.4)), height // 2),
			(0, height)
		]
		draw.polygon(points, fill=color)

	elif kind == "circle_center":
		r = layer.get("radius", min(width, height) // 6)
		draw.ellipse(
			[
				(width // 2 - r, height // 2 - r),
				(width // 2 + r, height // 2 + r)
			],
			fill=color
		)
