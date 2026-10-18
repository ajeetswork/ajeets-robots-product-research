import { describe, expect, it } from "vitest";
import { buildResearchRecord } from "../../scripts/research-metrics.mjs";

describe("research record contract", () => {
  it("keeps the fields consumed by reporting", () => {
    const record = buildResearchRecord({ category: "Accessories", source: "Survey", score: 8 });
    expect(Object.keys(record).sort()).toEqual(["category", "score", "source"]);
  });
});
