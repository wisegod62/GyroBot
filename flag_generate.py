from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET
import io


def generate_flag(svg_string, width=900, height=600):
	root = ET.fromstring(svg_string)

	img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
	draw = ImageDraw.Draw(img)

	for el in root:
		tag = el.tag.split("}")[-1]

		if tag == "rect":
			draw.rectangle([
				float(el.get("x", 0)),
				float(el.get("y", 0)),
				float(el.get("x", 0)) + float(el.get("width", 0)),
				float(el.get("y", 0)) + float(el.get("height", 0))
			], fill=el.get("fill"))

		elif tag == "polygon":
			points = []
			for p in el.get("points").split():
				x, y = p.split(",")
				points.append((float(x), float(y)))

			draw.polygon(points, fill=el.get("fill"))

	buf = io.BytesIO()
	img.save(buf, format="PNG")
	buf.seek(0)
	return buf
