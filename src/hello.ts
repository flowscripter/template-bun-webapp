import * as bunLib from "@flowscripter/template-bun-library";
import * as wasmLib from "@flowscripter/template-bun-wasm-rust-library";

/**
 * Logs out some greetings.
 */
export async function hello(): Promise<void> {
  console.info("Hello");
  bunLib.world();
  console.info("Hello");
  await wasmLib.world();
}
