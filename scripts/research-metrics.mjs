export function normalizeSource(value) {
  return String(value ?? "").trim().toLowerCase();
}

export function categoryScore({ demand = 0, margin = 0, supportLoad = 0 }) {
  return demand * 2 + margin - supportLoad;
}

export function riskBucket(score) {
  if (score >= 12) return "low";
  if (score >= 7) return "medium";
  return "high";
}

export function buildResearchRecord({ category, source, score }) {
  return {
    category: String(category).trim(),
    source: normalizeSource(source),
    score: Number(score),
  };
}
