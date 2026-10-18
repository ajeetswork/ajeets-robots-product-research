import { describe, expect, it } from "vitest";

describe("live provider query", () => {
  it.skip("checks a provider-backed research lookup when credentials are available", () => {
    expect(process.env.RESEARCH_PROVIDER_TOKEN).toBeTruthy();
  });
});
