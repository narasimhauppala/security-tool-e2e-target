const http = require("http");
const lodash = require("lodash/package.json");

const payload = () => JSON.stringify({
  service: "security-tool-e2e-target",
  lodash: lodash.version,
  status: "ok"
});

const server = http.createServer((req, res) => {
  if (["/", "/livez", "/readyz", "/version"].includes(req.url)) {
    const body = payload();
    res.writeHead(200, {
      "content-type": "application/json",
      "content-length": Buffer.byteLength(body)
    });
    res.end(body);
    return;
  }

  const body = JSON.stringify({ status: "not_found", path: req.url });
  res.writeHead(404, {
    "content-type": "application/json",
    "content-length": Buffer.byteLength(body)
  });
  res.end(body);
});

server.listen(Number(process.env.PORT || 8080), "0.0.0.0");
