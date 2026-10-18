import { describe, expect, it } from "vitest";
import { buildResearchRecord } from "../../scripts/research-metrics.mjs";

describe("category schema contract", () => {
  it("stores score as a number", () => {
    const record = buildResearchRecord({ category: "STEM Kits", source: "Pilot", score: "9" });
    expect(record.score).toBe(9);
  });
});
