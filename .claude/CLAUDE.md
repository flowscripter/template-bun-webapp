# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Template for a browser webapp using Bun, with dependencies on a plain Bun library and a Rust-compiled-to-WASM library.

## Commands

```bash
# Install
bun install

# Test
bun test

# Serve dev version (check browser console for output)
bun html/index.html

# Bundle for production
bun run build

# Lint and format
bunx oxlint src/ tests/
bunx oxfmt
```

Functional tests use Python Behave + Selenium (geckodriver) against the bundled webapp -- see `functional_tests/README.md`.

## Architecture

- `html/index.html` -- entry point; loads `src/main.ts` as a module script
- `src/main.ts` -- browser bootstrap: patches `console.info` to mirror output into a `<textarea id="console">`, then calls `hello()`
- `src/hello.ts` -- core logic; calls into both library dependencies and logs greetings
- `build.ts` -- Bun.build config: bundles `html/index.html` -> `dist/` with minification
- `tests/hello_test.ts` -- unit test for `hello()` using `bun:test`

### Dependencies

- `@flowscripter/template-bun-library` -- plain Bun/TS library (`bunLib.world()`)
- `@flowscripter/template-bun-wasm-rust-library` -- async WASM library (`await wasmLib.world()`)

The WASM library call is async; `hello()` must be awaited.

## CI/CD

GitHub Actions:

- PR validation: `validate-bun-webapp-pr.yml`
- Release builds: `release-bun-webapp.yml`
- Daily dependency check: `check-bun-dependencies.yml`
