# Image prompts: how Claude makes a generated image

Ships with the plugin, read-only. conteudo-estatico reads it for any generated image; her own look lives in `departamentos/conteudo/estilo-de-foto.md`, which wins over this file wherever they differ.

This edition's clients are in Brazil: settings, people and details in a prompt fit her Brazilian audience unless her photo style says otherwise. Prompts themselves can stay in English.

## What a generated image may show

> "A generated image never stands in for her work, her customers, her results or her. It shows the reader's world, an object or an idea, and the post's notes say it was generated."

- **Yes:** the reader's situation (a contractor reading texts in a truck, a desk at 9 PM with unread emails), an object or tool, a place type, a mood, an idea made visible.
- **No:** "her" work, a before/after, a client, a team photo, her place, a screenshot of a result, any real person or brand. Those are her photos or nothing.
- **No text inside the image.** Words go in the caption or on a Canva template. Generated text comes out wrong.

## The prompt, always in this order

1. **Subject and action** — one subject, doing one thing. "A woman in her 40s reading her phone at a kitchen counter."
2. **Setting** — where, time of day, two or three concrete details.
3. **Camera** — how it was shot: "phone photo, eye level, 35mm, shallow depth of field", or the camera line from her photo style.
4. **Light** — one light source and its direction ("soft window light from the left, late afternoon").
5. **Color** — the palette from her photo style (it follows `estilo-da-marca.md`), as plain color words, never hex codes.
6. **Mood** — one or two words.
7. **Composition** — vertical 3:4, subject placement, room left for anything the post adds.
8. **Avoid** — the photo style's Never list, plus: text, logos, watermarks, extra fingers, warped faces, glossy "AI" skin, perfect symmetry.

Faces: prefer people seen from the side, from behind, at a distance, or hands only. Close-up faces are where generated images look fake first.

## Tool

- **Canva**, through her Canva connection: `generate-image` with `aspectRatio: PORTRAIT_3_4`, then `get-generate-image-job` until it's done. Canva hands back an image stored in her Canva (a media ID), not a file. To get the full-size file: copy her `TEMPLATE - Photo - full frame`, replace its one image with the generated media (`update_fill`), save, export JPG 1080x1440, and download it into the post's `photos/` folder. For text over the photo, a Photo template with a headline region does the same with the words filled in. Her Canva plan's monthly AI allowance applies; when it runs out, say so plainly and offer a photo from her library or the shot list instead.
- Other generators only if her photo style names one and she has set it up.

## Calibration: getting her look right

The first generated images are a calibration round, not a post:
1. Read `estilo-de-foto.md` (create it from the shape in conteudo-estatico if missing, with what's known: her brand colors, her audience, the strategy's topics).
2. Make 3 images of the same subject that differ in **one** thing (light, or camera, or color treatment). Say what differs.
3. She says what's right and wrong. Turn each remark into a parameter: "too polished" → "phone photo, natural light, slight grain"; "too dark" → the light line.
4. Show the change to `estilo-de-foto.md` and write it on her sim. Log the round.
5. Repeat until she says the look is right; then mark the style **settled**.

Once settled, each generated image starts from the base prompt in `estilo-de-foto.md`, with the post's subject added. A remark about the style (not this one image) goes back into `estilo-de-foto.md`, on her sim, so the next image starts better.
