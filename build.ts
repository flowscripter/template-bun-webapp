await Bun.build({
  entrypoints: ["html/index.html"],
  outdir: "dist",
  minify: true,
});

export {};
