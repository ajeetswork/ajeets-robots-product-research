import { describe, expect, it } from "vitest";
import { normalizeSource } from "../../scripts/research-metrics.mjs";

describe("supplier sync source", () => {
  it("normalizes supplier intake labels", () => {
    expect(normalizeSource(" Supplier Intake ")).toBe("supplier intake");
  });
});
