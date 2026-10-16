import math, json

def plural(n, one, many):
    return one if n == 1 else many

def article(n):
    s = math.floor(n)
    return "An" if (s == 8 or s == 11 or s == 18 or (80 <= s < 90)) else "A"

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def layer_truth(w, d):
    if not (w > 0):
        raise ValueError("the basket width must be above zero")
    if not (d > 0):
        raise ValueError("the basket depth must be above zero")
    area = w * d * 0.8
    return f"{article(w)} {w} by {d} inch basket keeps {fixed1(area)} square inches of honest layer; the quarts never mentioned the layer honestly."

def batch_truth(area, norm, servings):
    if not (area > 0):
        raise ValueError("the layer area must be above zero")
    if not (norm > 0):
        raise ValueError("the per-serving area must be above zero")
    if not (servings > 0):
        raise ValueError("the servings must be above zero")
    per_layer = math.floor(area / norm + 1e-9)
    if per_layer == 0:
        return "The layer cannot hold even one serving at that spacing honestly."
    batches = math.ceil(servings / per_layer - 1e-9)
    return f"The layer holds {per_layer} {plural(per_layer, 'serving', 'servings')} at a time; {servings} {plural(servings, 'serving', 'servings')} take {batches} {plural(batches, 'batch', 'batches')} honestly."

def time_truth(batches, mins, pre):
    if not (batches > 0):
        raise ValueError("the batches must be above zero")
    if not (mins > 0):
        raise ValueError("the batch minutes must be above zero")
    if not (pre >= 0):
        raise ValueError("the preheat must be zero or more")
    total = batches * mins + pre
    pre_part = "plus no preheat" if pre == 0 else f"plus a {pre}-minute preheat"
    verb = plural(batches, "makes", "make")
    tail = "one batch, no queue honestly" if batches == 1 else "the recipe was counting one layer honestly"
    return f"{batches} {plural(batches, 'batch', 'batches')} of {mins} minutes each {pre_part} {verb} {total} minutes honestly - {tail}."

FNS = {"layerTruth": layer_truth, "batchTruth": batch_truth, "timeTruth": time_truth}

CASES = [
    ("layerTruth", [8, 10]),
    ("layerTruth", [9, 9]),
    ("layerTruth", [5, 5]),
    ("layerTruth", [18, 10]),
    ("layerTruth", [12, 14]),
    ("layerTruth", [0, 10]),
    ("layerTruth", [8, 0]),
    ("batchTruth", [64, 20, 6]),
    ("batchTruth", [64, 20, 3]),
    ("batchTruth", [64, 20, 64]),
    ("batchTruth", [20, 20, 5]),
    ("batchTruth", [10, 20, 4]),
    ("batchTruth", [134.4, 20, 10]),
    ("batchTruth", [100, 12, 30]),
    ("batchTruth", [50, 20, 2]),
    ("batchTruth", [40, 20, 40]),
    ("batchTruth", [0, 20, 6]),
    ("batchTruth", [64, 0, 6]),
    ("batchTruth", [64, 20, 0]),
    ("timeTruth", [2, 18, 3]),
    ("timeTruth", [1, 18, 3]),
    ("timeTruth", [3, 12, 0]),
    ("timeTruth", [4, 15, 3]),
    ("timeTruth", [22, 15, 3]),
    ("timeTruth", [1, 25, 0]),
    ("timeTruth", [2, 18, 1]),
    ("timeTruth", [0, 18, 3]),
    ("timeTruth", [2, 0, 3]),
]

out = []
for fn, args in CASES:
    rec = {"fn": fn, "args": args}
    try:
        rec["out"] = FNS[fn](*args)
    except ValueError as e:
        rec["err"] = str(e)
    out.append(rec)
    print(fn, args, "->", rec.get("out") or ("ERR: " + rec["err"]))

with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(f"{len(out)} cases written to expected.json")
