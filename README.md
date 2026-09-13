# ComfyUI-Mochorong

Utility nodes for ComfyUI — conditional routing, audio control, and type conversion.

## Nodes

**Audio Gate** — Boolean toggle that passes audio through or outputs silence.

**Audio Selector** — Pick one audio stem from up to four inputs (Bass, Drums, Guitar, Vocals).

**Custom Gate** — Boolean switch for IMAGE + MASK pairs, with optional fallback inputs.

**Int and Float** — Single float input, outputs both INT and FLOAT.

**Load Image Optional** — Standard image loader with a "None" option that passes null — useful for optional reference image inputs.

## Install

Via ComfyUI Manager or:

```
comfy node install comfyui-mochorong
```
