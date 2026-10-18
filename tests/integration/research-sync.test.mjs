import { describe, expect, it } from "vitest";
import { buildResearchRecord } from "../../scripts/research-metrics.mjs";

describe("research sync record", () => {
  it("produces a normalized record for downstream sync", () => {
    expect(buildResearchRecord({
      category: "Classroom Kits",
      source: "Partner Interview",
      score: 11,
    })).toEqual({
      category: "Classroom Kits",
      source: "partner interview",
      score: 11,
    });
  });
});
