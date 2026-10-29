# Publication Plane

The `render/` area contains deterministic generation logic and presentation templates for human- and AI-consumable views of canonical repository content.

## Authority boundary

Generated publications do not create or modify normative authority. Canonical JSON remains the governed source. If generated output disagrees with canonical content, the canonical content governs and the renderer must be corrected.

## Direction of travel

```text
canonical JSON
  ↓
renderer
  ↓
dist/
  ├─ human Markdown / HTML / PDF
  ├─ role-specific views
  ├─ AI context packages
  └─ reports
```

Generated files should be reproducible and should not become an independent editing surface.

## First publication pilot

`scripts/render_standards.py` renders canonical `type: standard` JSON objects into deterministic Markdown under `dist/human/standards/`.

The pilot intentionally favors semantic fidelity over visual polish. Its job is to prove that the human-readable standard can be generated from the governed machine-readable source. Later renderers may add templates, navigation, role-specific views, HTML, or PDF without changing the underlying authority model.
