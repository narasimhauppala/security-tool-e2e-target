# Security Tool E2E Target

Small Python container used as a realistic target for the security-tool company-style E2E flow.

It intentionally pins old Python dependencies so the scanner and planner have fixable findings, then Module 3 can update `requirements.txt`, build an upgraded image, and Module 5 can open a pull request.

## Local Image

```powershell
$IMAGE = "ghcr.io/narasimhauppala/security-tool-e2e-target:latest"
docker build -t $IMAGE .
docker run --rm $IMAGE
docker push $IMAGE
```

If you use GHCR for the first test, make the package public or configure registry credentials in the security-tool scanner.

## Security Tool E2E Config

Use these values in `.tmp/company-e2e.local.json` after pushing this repo to GitHub:

```json
{
  "image_ref": "ghcr.io/narasimhauppala/security-tool-e2e-target:latest",
  "source_repo": {
    "url": "https://github.com/narasimhauppala/security-tool-e2e-target.git",
    "branch": "main",
    "credential_id": null
  },
  "upgrade": {
    "target_registry": "ghcr.io/narasimhauppala/security-tool-e2e-target"
  }
}
```

