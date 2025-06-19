import { hello } from "./hello";

async function start() {
  const oldLog = console.info;

  console.info = (...args) => {
    oldLog(...args);
    const textarea = document.getElementById("console") as HTMLTextAreaElement;

    if (textarea) {
      args.forEach((arg) => textarea.value += `${JSON.stringify(arg)}\n`);
    }
  };

  await hello();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", start);
} else {
  start();
}
