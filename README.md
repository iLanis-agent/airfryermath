# Air Fryer Math

Air fryer capacity honesty. The basket says eight quarts, and the fries were always going to
need one layer.

- Landing: `index.html`
- App: `app.html` (loads `engine.js`)

## What it does

Quarts measure a pile, and nothing in an air fryer cooks in a pile. The honest unit is the
single layer: the square inches the hot air can actually see. Once the layer is full, the
rest of the servings join a queue, and the recipe's minutes were never written for a queue.
Three panels of honest arithmetic:

- **The layer truth** - basket width x depth at a labeled 80% usable footprint: the honest
  layer area.
- **The batch truth** - layer area divided by the per-serving spacing: servings per layer,
  and the batches behind a serving count.
- **The time truth** - batches x minutes plus the preheat, against the recipe's
  one-layer assumption.

## Norms used (labeled, illustrative)

- Usable layer: 80% of the basket footprint (the edges need airflow).
- Spacing is entered per food - about 20 square inches a serving is a common starting norm.

Every figure is hypothetical arithmetic on labeled norms, not a statement about any real
fryer, food or recipe. Follow the fryer's manual and the recipe, and let a thermometer call
the doneness.

## Tests

`oracle.py` generates `expected.json` from a Python mirror of the engine (same operation
order, same rounding). `node test.js` checks the JavaScript engine against it:

```
python3 oracle.py
node test.js
```
