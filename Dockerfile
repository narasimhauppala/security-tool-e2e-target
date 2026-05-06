FROM node:20-slim

LABEL org.opencontainers.image.source="https://github.com/narasimhauppala/security-tool-e2e-target"
LABEL org.opencontainers.image.description="Security Tool company-style E2E target image"
LABEL org.opencontainers.image.licenses="MIT"

ENV NODE_ENV=production

WORKDIR /app

COPY package.json /app/package.json
RUN npm install --omit=dev

COPY server.js /app/server.js

EXPOSE 8080

CMD ["node", "server.js"]
