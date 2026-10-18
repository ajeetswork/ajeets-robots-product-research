import { describe, expect, it } from "vitest";
import { riskBucket } from "../../scripts/research-metrics.mjs";

describe("riskBucket", () => {
  it("marks high-scoring categories as low risk", () => {
    expect(riskBucket(14)).toBe("low");
  });
});
