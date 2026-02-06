# Backgrounds & Borders Utilities Reference

Complete reference for Tailwind CSS backgrounds and borders utility classes.

## Background Color

| Class | Properties |
|-------|------------|
| `bg-transparent` | background-color: transparent |
| `bg-current` | background-color: currentColor |
| `bg-black` | background-color: rgb(0 0 0) |
| `bg-white` | background-color: rgb(255 255 255) |
| `bg-slate-100` to `bg-slate-900` | Various slate shades |
| `bg-red-500`, `bg-blue-600`, etc. | Color shades from 50 to 900 |

## Gradient

| Class | Properties |
|-------|------------|
| `bg-gradient-to-t` | background-image: linear-gradient(to top, ...) |
| `bg-gradient-to-tr` | background-image: linear-gradient(to top right, ...) |
| `bg-gradient-to-r` | background-image: linear-gradient(to right, ...) |
| `bg-gradient-to-br` | background-image: linear-gradient(to bottom right, ...) |
| `bg-gradient-to-b` | background-image: linear-gradient(to bottom, ...) |
| `bg-gradient-to-bl` | background-image: linear-gradient(to bottom left, ...) |
| `bg-gradient-to-l` | background-image: linear-gradient(to left, ...) |
| `bg-gradient-to-tl` | background-image: linear-gradient(to top left, ...) |

### Gradient Color Stops

| Class | Properties |
|-------|------------|
| `from-purple-500` | --tw-gradient-from: rgb(168 85 247) |
| `via-pink-500` | --tw-gradient-via: rgb(236 72 153) |
| `to-red-500` | --tw-gradient-to: rgb(239 68 68) |

## Border Width

| Class | Properties |
|-------|------------|
| `border` | border-width: 1px |
| `border-0` | border-width: 0 |
| `border-2` | border-width: 2px |
| `border-4` | border-width: 4px |
| `border-8` | border-width: 8px |
| `border-t` | border-top-width: 1px |
| `border-r` | border-right-width: 1px |
| `border-b` | border-bottom-width: 1px |
| `border-l` | border-left-width: 1px |

## Border Color

| Class | Properties |
|-------|------------|
| `border-transparent` | border-color: transparent |
| `border-current` | border-color: currentColor |
| `border-black` | border-color: rgb(0 0 0) |
| `border-white` | border-color: rgb(255 255 255) |
| `border-slate-300` to `border-slate-900` | Various slate shades |
| `border-red-500`, `border-blue-600`, etc. | Color shades from 50 to 900 |

## Border Radius

| Class | Properties |
|-------|------------|
| `rounded-none` | border-radius: 0 |
| `rounded-sm` | border-radius: 0.125rem (2px) |
| `rounded` | border-radius: 0.25rem (4px) |
| `rounded-md` | border-radius: 0.375rem (6px) |
| `rounded-lg` | border-radius: 0.5rem (8px) |
| `rounded-xl` | border-radius: 0.75rem (12px) |
| `rounded-2xl` | border-radius: 1rem (16px) |
| `rounded-3xl` | border-radius: 1.5rem (24px) |
| `rounded-full` | border-radius: 9999px |

### Individual Corners

| Class | Properties |
|-------|------------|
| `rounded-t-lg` | border-top-left-radius, border-top-right-radius |
| `rounded-r-lg` | border-top-right-radius, border-bottom-right-radius |
| `rounded-b-lg` | border-bottom-left-radius, border-bottom-right-radius |
| `rounded-l-lg` | border-top-left-radius, border-bottom-left-radius |
| `rounded-tl-lg` | border-top-left-radius |
| `rounded-tr-lg` | border-top-right-radius |
| `rounded-br-lg` | border-bottom-right-radius |
| `rounded-bl-lg` | border-bottom-left-radius |

## Filters

| Class | Properties |
|-------|------------|
| `blur-none` | filter: blur(0) |
| `blur-sm` | filter: blur(4px) |
| `blur` | filter: blur(8px) |
| `blur-md` | filter: blur(12px) |
| `blur-lg` | filter: blur(16px) |
| `blur-xl` | filter: blur(24px) |
| `blur-2xl` | filter: blur(40px) |
| `blur-3xl` | filter: blur(64px) |
| `brightness-0` | filter: brightness(0) |
| `brightness-50` | filter: brightness(.5) |
| `brightness-75` | filter: brightness(.75) |
| `brightness-90` | filter: brightness(.9) |
| `brightness-95` | filter: brightness(.95) |
| `brightness-100` | filter: brightness(1) |
| `brightness-105` | filter: brightness(1.05) |
| `brightness-110` | filter: brightness(1.1) |
| `brightness-125` | filter: brightness(1.25) |
| `brightness-150` | filter: brightness(1.5) |
| `brightness-200` | filter: brightness(2) |
| `contrast-0` | filter: contrast(0) |
| `contrast-50` | filter: contrast(.5) |
| `contrast-75` | filter: contrast(.75) |
| `contrast-100` | filter: contrast(1) |
| `contrast-125` | filter: contrast(1.25) |
| `contrast-150` | filter: contrast(1.5) |
| `contrast-200` | filter: contrast(2) |
| `drop-shadow-sm` | filter: drop-shadow(0 1px 1px rgb(0 0 0 / 0.05)) |
| `drop-shadow` | filter: drop-shadow(0 1px 2px rgb(0 0 0 / 0.1)) drop-shadow(0 1px 1px rgb(0 0 0 / 0.06)) |
| `drop-shadow-md` | filter: drop-shadow(0 4px 3px rgb(0 0 0 / 0.07)) drop-shadow(0 2px 2px rgb(0 0 0 / 0.06)) |
| `drop-shadow-lg` | filter: drop-shadow(0 10px 8px rgb(0 0 0 / 0.04)) drop-shadow(0 4px 3px rgb(0 0 0 / 0.1)) |
| `drop-shadow-xl` | filter: drop-shadow(0 20px 13px rgb(0 0 0 / 0.03)) drop-shadow(0 8px 5px rgb(0 0 0 / 0.08)) |
| `drop-shadow-2xl` | filter: drop-shadow(0 25px 25px rgb(0 0 0 / 0.15)) |
| `grayscale-0` | filter: grayscale(0) |
| `grayscale` | filter: grayscale(100%) |
| `hue-rotate-0` | filter: hue-rotate(0deg) |
| `hue-rotate-15` | filter: hue-rotate(15deg) |
| `hue-rotate-30` | filter: hue-rotate(30deg) |
| `hue-rotate-60` | filter: hue-rotate(60deg) |
| `hue-rotate-90` | filter: hue-rotate(90deg) |
| `hue-rotate-180` | filter: hue-rotate(180deg) |
| `invert-0` | filter: invert(0) |
| `invert` | filter: invert(100%) |
| `saturate-0` | filter: saturate(0) |
| `saturate-50` | filter: saturate(.5) |
| `saturate-100` | filter: saturate(1) |
| `saturate-150` | filter: saturate(1.5) |
| `saturate-200` | filter: saturate(2) |
| `sepia-0` | filter: sepia(0) |
| `sepia` | filter: sepia(100%) |