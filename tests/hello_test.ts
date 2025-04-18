import { describe, expect, test } from "bun:test";
import { hello } from "../src/hello.ts";

describe("Hello Tests", () => {
  test("Simple Test", () => {
    hello();
    expect(true);
  });
});
