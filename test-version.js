const lodash = require("lodash/package.json");

if (lodash.version !== "4.17.20") {
  console.error(`Functional contract changed: expected lodash 4.17.20, got ${lodash.version}`);
  process.exit(1);
}

console.log(`Functional contract OK for lodash ${lodash.version}`);
