// Air Fryer Math engine - hypothetical arithmetic on labeled norms only.
// Basket areas, per-serving spacing and minutes are labeled norms, not
// measurements of your fryer, your food or your recipe.

function plural(n, one, many) { return n === 1 ? one : many; }
function article(n) {
  const s = Math.floor(n);
  return (s === 8 || s === 11 || s === 18 || (s >= 80 && s < 90)) ? "An" : "A";
}
function tenths(x) { return Math.floor(x * 10 + 0.5) / 10; }
function fixed1(x) { return tenths(x).toFixed(1); }

function layerTruth(w, d) {
  if (!(w > 0)) throw new Error("the basket width must be above zero");
  if (!(d > 0)) throw new Error("the basket depth must be above zero");
  const area = w * d * 0.8; // labeled norm: 80% of the footprint cooks in one layer
  return `${article(w)} ${w} by ${d} inch basket keeps ${fixed1(area)} square inches of honest layer; the quarts never mentioned the layer honestly.`;
}

function batchTruth(area, norm, servings) {
  if (!(area > 0)) throw new Error("the layer area must be above zero");
  if (!(norm > 0)) throw new Error("the per-serving area must be above zero");
  if (!(servings > 0)) throw new Error("the servings must be above zero");
  const perLayer = Math.floor(area / norm + 1e-9);
  if (perLayer === 0) return "The layer cannot hold even one serving at that spacing honestly.";
  const batches = Math.ceil(servings / perLayer - 1e-9);
  return `The layer holds ${perLayer} ${plural(perLayer, "serving", "servings")} at a time; ${servings} ${plural(servings, "serving", "servings")} take ${batches} ${plural(batches, "batch", "batches")} honestly.`;
}

function timeTruth(batches, mins, pre) {
  if (!(batches > 0)) throw new Error("the batches must be above zero");
  if (!(mins > 0)) throw new Error("the batch minutes must be above zero");
  if (!(pre >= 0)) throw new Error("the preheat must be zero or more");
  const total = batches * mins + pre;
  const prePart = pre === 0 ? "plus no preheat" : `plus a ${pre}-minute preheat`;
  const verb = plural(batches, "makes", "make");
  const tail = batches === 1 ? "one batch, no queue honestly" : "the recipe was counting one layer honestly";
  return `${batches} ${plural(batches, "batch", "batches")} of ${mins} minutes each ${prePart} ${verb} ${total} minutes honestly - ${tail}.`;
}

if (typeof module !== "undefined") {
  module.exports = { layerTruth, batchTruth, timeTruth };
}
