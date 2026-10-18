import { describe, expect, it } from "vitest";
import { normalizeSource } from "../../scripts/research-metrics.mjs";

describe("normalizeSource", () => {
  it("normalizes source labels for comparison", () => {
    expect(normalizeSource("  Retail Survey  ")).toBe("retail survey");
  });
});
