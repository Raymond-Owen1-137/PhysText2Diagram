# SESSION_LOG_2025-05-15

| Clock Time | Action | Details / Artifacts | Issues & Fixes | Token‑Cost |
|-----------|--------|---------------------|---------------|-----------|
| **18:05** | Problem framing | Defined auto‑diagram pipeline; chose JSON scene graph | — | — |
| **18:12** | Multi‑file MVP scaffold | Created llm_scene_parser.py, mutator.py, renderer_svg.py, text_writer.py, main.py | — | — |
| **18:18** | Repo zipped | Generated ai_diagram_pipeline.zip | — | — |
| **18:20** | First run | UTF‑8 decode error | Added encoding fix | — |
| **18:24** | Dependency miss | svgwrite missing | pip install svgwrite | — |
| **18:26** | Quota hit | GPT‑4 RateLimitError | Switched to GPT‑3.5 | — |
| **18:28** | Billing | Added $20 credits | — | — |
| **18:30** | Successful run | Created variant_1‑3.svg/.txt | Verified data | ≈$0.00065 |
| **18:33** | Cost audit | $20 ≈ 10 M tokens | — | — |
| **18:35** | JSON sanity | Uploaded diagram → JSON OK | — | negligible |
| **18:39** | Single‑file script | quick_diagram_gen.py delivered | — | ≈$0.0005 |
| **18:45** | Detailed log | Current log generated | — | — |

## Artifacts
- `ai_diagram_pipeline.zip`
- `quick_diagram_gen.py`
- `outputs/variant_*.svg/.txt`

## Model & Cost
GPT‑3.5‑Turbo‑0125 @ $0.002 / 1k tokens
Session ≈1.4 k tokens → ~$0.0028

## Capabilities
1. Parse ramp problem to JSON with GPT‑3.5
2. Mutate angle, mass, arrow colors, add friction arrow
3. Option A: SVG + rewritten text
4. Option B: DALL·E prompts

## TODO
- Add pulleys, springs
- QC module
- Batch multiple problems
- Optional ControlNet style

## Reproduce
```bash
# single‑file
python quick_diagram_gen.py "A 5 kg block on a 30° incline…" 3

# multi‑file
cd ai_diagram_pipeline
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
set OPENAI_API_KEY=sk-...
python main.py examples\base_problem.txt -n 3
```
