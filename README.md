# template-bun-webapp

[![version](https://img.shields.io/github/v/release/flowscripter/template-bun-webapp?sort=semver)](https://github.com/flowscripter/template-bun-webapp/releases)
[![build](https://img.shields.io/github/actions/workflow/status/flowscripter/template-bun-webapp/release-deno-webapp.yml)](https://github.com/flowscripter/template-bun-webapp/actions/workflows/release-deno-webapp.yml)
[![coverage](https://codecov.io/gh/flowscripter/template-bun-webapp/branch/main/graph/badge.svg?token=EMFT2938ZF)](https://codecov.io/gh/flowscripter/template-bun-webapp)
[![deno doc](https://doc.deno.land/badge.svg)](https://jsr.io/@flowscripter/template-bun-webapp/doc)
[![license: MIT](https://img.shields.io/github/license/flowscripter/template-bun-webapp)](https://github.com/flowscripter/template-bun-webapp/blob/main/LICENSE)

> Project template for a webapp with Bun and Rust compiled to WASM library dependencies.

## Hosted Webapp Demo

Go to: https://flowscripter.github.io/template-bun-webapp/

## Development

Run: `deno run --allow-net mod.ts`

Test: `deno test -A --unstable`

Lint: `deno fmt mod.ts deps.ts src/ tests/`

Bundle: `deno bundle mod.ts html/mod.bundle.js`

Serve: `cd html && python3 -m http.server 8000` and then...

Verify: Browse to http://127.0.0.1:8000/index.html and check that the browser console displays:

    INFO Hello
    INFO World
    INFO Hello
    INFO World 4

## Functional Tests

Refer to [functional_tests/README.md](functional_tests/README.md)

## Development

Install dependencies:

`bun install`

Test:

`bun test`

Run:

`bun run index.ts`

Bundle:

`bun build index.ts --outdir ./dist --entry-naming bundle.js --minify`

**NOTE**: The following tasks use Deno as it excels at these and Bun does not
currently provide such functionality:

Format:

`deno fmt`

Lint:

`deno lint index.ts src/ tests/`

## Documentation

### Overview

```mermaid
classDiagram
    Foo <|-- Bar
```

## License

MIT © Flowscripter

