import { describe, expect, it } from "vitest";
import { categoryScore } from "../../scripts/research-metrics.mjs";

describe("categoryScore", () => {
  it("rewards demand and margin while accounting for support load", () => {
    expect(categoryScore({ demand: 5, margin: 4, supportLoad: 2 })).toBe(12);
  });
});
