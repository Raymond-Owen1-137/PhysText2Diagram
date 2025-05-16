import copy, random, math

def mutate(scene: dict, n_variants=3):
    """Return a list of mutated scene graphs."""
    variants = []
    for _ in range(n_variants):
        s = copy.deepcopy(scene)
        for obj in s.get("objects", []):
            if obj.get("type") == "inclined_plane":
                delta = random.choice([-15, -10, 10, 15])
                obj["angle_degrees"] = max(5, min(75, obj.get("angle_degrees",30)+delta))
            if obj.get("type") == "block" and "mass" in obj:
                try:
                    mass = float(str(obj["mass"]).split()[0])
                except:
                    mass = 5.0
                mass *= random.choice([0.5, 1.5, 2])
                mass = round(mass,1)
                obj["mass"] = mass
                obj["label"] = f"{mass} kg"
        variants.append(s)
    return variants