> https://github.com/serhanekicii/openclaw-helm

# openclaw-helm (149 stars)

## Problem and Solution

OpenClaw does not officially provide a Kubernetes deployment solution, requiring enterprise users to write their own Deployment/Service/ConfigMap and other resource manifests, which is complex and difficult to standardize. openclaw-helm provides a production-grade Helm Chart based on the bjw-s app-template, supporting single-instance deployment, Secret management, port mapping, and device pairing workflows, simplifying OpenClaw operations in K8s environments.

## Key Features

- **Production-grade Helm Chart** -- Based on bjw-s app-template v3, supporting Kubernetes >= 1.26
- **Clear Architecture** -- Gateway (18789) + Chromium CDP (9222, optional), single-instance deployment (not horizontally scalable)
- **Secret Management** -- Injects `ANTHROPIC_API_KEY` and `OPENCLAW_GATEWAY_TOKEN` via `envFrom.secretRef`
- **Device Pairing Workflow** -- Provides `kubectl port-forward` + `kubectl exec` command examples to simplify first-time pairing
- **Private Image Support** -- Supports custom `image.repository` and `image.tag`, compatible with enterprise internal image registries
- **Artifact Hub Publication** -- Hosted on the official Helm repository, installable via `helm repo add`
