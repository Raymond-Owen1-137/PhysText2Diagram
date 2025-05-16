import svgwrite, math

def _draw_incline(dwg, angle, origin=(50,300), length=400):
    rad = math.radians(angle)
    ox, oy = origin
    dx = length*math.cos(rad)
    dy = -length*math.sin(rad)
    dwg.add(dwg.line(start=(ox,oy), end=(ox+length, oy), stroke="black", stroke_width=3))
    dwg.add(dwg.line(start=(ox,oy), end=(ox+dx, oy+dy), stroke="black", stroke_width=3))

def _block_coords(angle, offset_along=150, width=60, height=40):
    rad = math.radians(angle)
    base_x = 50 + offset_along*math.cos(rad)
    base_y = 300 - offset_along*math.sin(rad)
    return base_x, base_y-height  # bottom-left in screen coords

def render(scene: dict, out_path: str):
    plane = next(o for o in scene["objects"] if o["type"]=="inclined_plane")
    angle = plane["angle_degrees"]
    dwg = svgwrite.Drawing(out_path, size=("600px","400px"))
    _draw_incline(dwg, angle)
    # angle label
    dwg.add(dwg.text(f"θ = {angle}°", insert=(100, 330), font_size="16px"))
    # draw block
    block = next(o for o in scene["objects"] if o["type"]=="block")
    bx, by = _block_coords(angle)
    rect = dwg.rect(insert=(bx, by), size=(60,40),
                    fill="#cccccc", stroke="black")
    dwg.add(rect)
    if "label" in block:
        dwg.add(dwg.text(block["label"], insert=(bx+30, by+25),
                         text_anchor="middle", font_size="14px"))
    # force arrows
    for arrow in scene.get("arrows", []):
        if arrow["direction"]=="down":
            x = bx+30; y=by+20
            dwg.add(dwg.line(start=(x,y), end=(x, y+80), stroke="black"))
            dwg.add(dwg.text(arrow["label"], insert=(x+5, y+40), font_size="14px"))
        if arrow["direction"]=="perpendicular_to_plane":
            # crude perpendicular
            rad = math.radians(angle)
            vx = -60*math.sin(rad); vy = -60*math.cos(rad)
            x0 = bx+30; y0 = by+20
            dwg.add(dwg.line(start=(x0,y0), end=(x0+vx, y0+vy), stroke="black"))
            dwg.add(dwg.text(arrow["label"], insert=(x0+vx/2, y0+vy/2-5), font_size="14px"))
    dwg.save()