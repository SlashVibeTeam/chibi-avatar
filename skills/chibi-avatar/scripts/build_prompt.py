#!/usr/bin/env python3
"""Build a local image-tool request. Standard library only; no image/API calls."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def image_path(raw):
    p = Path(raw).expanduser().resolve()
    if not p.is_file():
        raise argparse.ArgumentTypeError(f"Image not found: {p}")
    with p.open('rb') as f:
        head = f.read(16)
    if not (head.startswith(b'\x89PNG\r\n\x1a\n') or head.startswith(b'\xff\xd8\xff')
            or (head.startswith(b'RIFF') and head[8:12] == b'WEBP')):
        raise argparse.ArgumentTypeError("Use a PNG, JPEG, or WebP image.")
    return str(p)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--photo', required=True, type=image_path)
    ap.add_argument('--scene', choices=['office', 'home', 'floor'], default='home')
    ap.add_argument('--appearance', default='Preserve visible hair, skin tone, glasses and facial characteristics from the person photo.')
    ap.add_argument('--outfit', default='Follow the visible outfit in the person photo; use simple dark trousers and ordinary shoes where unseen.')
    ap.add_argument('--accessory', action='append', default=[])
    ap.add_argument('--pet-photo', type=image_path)
    ap.add_argument('--pet-description')
    ap.add_argument('--background', choices=['white', 'transparent'], default='white')
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    refs = [args.photo, str(ROOT / 'assets' / 'reference.png')]
    roles = ['Image 1: person identity and appearance only.', 'Image 2: illustration style and scene vocabulary only; this contact sheet does NOT request multiple people.']
    refs.append(str(ROOT / 'assets' / 'product-stand.png'))
    roles.append(f'Image {len(refs)}: mandatory SlashVibe shape and base extending ONLY to viewer-left, never mirrored.')
    refs.append(str(ROOT / 'assets' / 'product-scale-reference.png'))
    roles.append(f'Image {len(refs)}: approved small product SCALE ONLY; do not copy this person or accessories.')
    if args.pet_photo:
        refs.append(args.pet_photo)
        roles.append(f'Image {len(refs)}: requested pet appearance, coat pattern and iris color only.')
    try:
        for ref in refs:
            image_path(ref)
    except argparse.ArgumentTypeError as exc:
        ap.error(str(exc))
    scenes = {
        'office': 'Simple white desk and dark office swivel chair, working at a computer.',
        'home': 'Light natural wood desk, ordinary domestic chair, silver laptop.',
        'floor': 'Sitting cross-legged on a cushion at a low wooden table with a silver laptop. No office chair.',
    }
    pet = args.pet_description or ('Match the supplied pet photo.' if args.pet_photo else 'No pet.')
    product = ('MANDATORY in EVERY image: exactly ONE small silver SlashVibe product fully supported on the desktop beside the computer. '
               'Its total projected bounding-box width must be approximately 10% of the desktop projected width (acceptable 9-11%), about one quarter of laptop width, as in the approved scale reference. '
               'Preserve the reference rounded tilted silver plate, single black diagonal slash and connected low base extending ONLY to viewer/image-LEFT. '
               'Never omit, mirror, reverse, duplicate, deform, stretch, flatten, bend or redesign it. Uniform scaling only, with coherent natural tabletop perspective. '
               'No floating plate, missing base or base extending both directions. Keep product fixed when editing unrelated content.')
    prompt = '\n'.join([
        'Use case: stylized-concept',
        'Primary request: Create ONE standalone full-body chibi working avatar based on the person photo, matching the approved team illustration. Do not reproduce the team sheet.',
        'Input images: ' + ' '.join(roles),
        'Style: Clean flat chibi illustration with slight soft dimensional shading, oversized head, small body, smooth rounded face, simple white eye shapes and black oval pupils, minimal nose and mouth, large tidy hair shapes, crisp contours and calm solid colors. Not photorealistic, painted, plush or glossy 3D.',
        'Identity: ' + args.appearance,
        'Outfit: ' + args.outfit,
        'Scene: ' + scenes[args.scene],
        'Accessories requested: ' + ('; '.join(args.accessory) if args.accessory else
            'None beyond the specified desk, chair, computer and mandatory small SlashVibe product.'),
        'Pet: ' + pet,
        'Product: ' + product,
        'Composition: Square single-person PNG, target approximately 1024 x 1024. Complete head, hands, feet, chair, desk and all requested objects within the canvas, comfortable white space. No clipping and no stretching.',
        'Background: ' + ('Genuine transparent alpha; no painted checkerboard.' if args.background == 'transparent' else 'Plain solid white.'),
        'Text: No names, job titles or watermarks. Render only explicitly requested object text such as book titles; orient books and working papers toward the person.',
        'Geometry: One consistent rectangular tabletop perspective and correctly attached vertical legs. All objects fully supported within desktop boundaries. Laptop screen and keyboard face the person, never draw UI on back of lid.',
        'Quality: Preserve the photo/user-specified skin tone consistently on face, neck and hands; warm tan must not become gray-green. Preserve glasses, hair parting and requested accessories. Keep eyebrows harmonious with hair color. Smooth coherent face contour and distinct eye/skin boundary; no accidental white cheek flecks, mottled skin, speckled texture, blur or over-denoising. No extra props from other team members. Coherent simplified hands, clear pet paws and iris/pupil anatomy.',
    ])
    result = {'prompt': prompt, 'referenced_image_paths': refs,
              'transparent_background': args.background == 'transparent'}
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        try:
            with args.output.open('x', encoding='utf-8') as f:
                f.write(serialized)
        except FileExistsError:
            ap.error(f'Output already exists; choose a new filename: {args.output}')
        print(str(args.output.resolve()))
    else:
        print(serialized, end='')

if __name__ == '__main__':
    main()
