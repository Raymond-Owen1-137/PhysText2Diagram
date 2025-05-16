import argparse, pathlib, json
from llm_scene_parser import parse_problem
from mutator import mutate
from renderer_svg import render
from text_writer import rewrite

def pipeline(problem_path: str, n: int):
    base_text = pathlib.Path(problem_path).read_text()
    base_scene = parse_problem(base_text)
    variants = mutate(base_scene, n)
    out_dir = pathlib.Path("outputs")
    out_dir.mkdir(exist_ok=True)
    for i, sc in enumerate(variants, 1):
        svg_path = out_dir / f"variant_{i}.svg"
        render(sc, svg_path)
        new_text = rewrite(sc, base_text)
        (out_dir / f"variant_{i}.txt").write_text(new_text)
        print(f"Generated {svg_path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("problem", help="text file with base problem")
    ap.add_argument("-n", type=int, default=3, help="number of variants")
    args = ap.parse_args()
    pipeline(args.problem, args.n)