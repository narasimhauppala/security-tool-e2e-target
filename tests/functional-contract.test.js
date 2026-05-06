const assert = require("assert");
const lodash = require("lodash/package.json");

assert.strictEqual(
  lodash.version,
  "4.17.20",
  `Expected lodash runtime contract to stay on 4.17.20, got ${lodash.version}`
);

console.log("lodash runtime contract passed");
