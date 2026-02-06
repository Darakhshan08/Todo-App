# Typography Utilities Reference

Complete reference for Tailwind CSS typography utility classes.

## Font Family

| Class | Properties |
|-------|------------|
| `font-sans` | font-family: ui-sans-serif, system-ui, ... |
| `font-serif` | font-family: ui-serif, Georgia, ... |
| `font-mono` | font-family: ui-monospace, Menlo, ... |

## Font Size

| Class | Properties |
|-------|------------|
| `text-xs` | font-size: 0.75rem; line-height: 1rem |
| `text-sm` | font-size: 0.875rem; line-height: 1.25rem |
| `text-base` | font-size: 1rem; line-height: 1.5rem |
| `text-lg` | font-size: 1.125rem; line-height: 1.75rem |
| `text-xl` | font-size: 1.25rem; line-height: 1.75rem |
| `text-2xl` | font-size: 1.5rem; line-height: 2rem |
| `text-3xl` | font-size: 1.875rem; line-height: 2.25rem |
| `text-4xl` | font-size: 2.25rem; line-height: 2.5rem |
| `text-5xl` | font-size: 3rem; line-height: 1 |
| `text-6xl` | font-size: 3.75rem; line-height: 1 |

## Font Weight

| Class | Properties |
|-------|------------|
| `font-thin` | font-weight: 100 |
| `font-extralight` | font-weight: 200 |
| `font-light` | font-weight: 300 |
| `font-normal` | font-weight: 400 |
| `font-medium` | font-weight: 500 |
| `font-semibold` | font-weight: 600 |
| `font-bold` | font-weight: 700 |
| `font-extrabold` | font-weight: 800 |
| `font-black` | font-weight: 900 |

## Line Height

| Class | Properties |
|-------|------------|
| `leading-none` | line-height: 1 |
| `leading-tight` | line-height: 1.25 |
| `leading-snug` | line-height: 1.375 |
| `leading-normal` | line-height: 1.5 |
| `leading-relaxed` | line-height: 1.625 |
| `leading-loose` | line-height: 2 |

## Letter Spacing

| Class | Properties |
|-------|------------|
| `tracking-tighter` | letter-spacing: -0.05em |
| `tracking-tight` | letter-spacing: -0.025em |
| `tracking-normal` | letter-spacing: 0 |
| `tracking-wide` | letter-spacing: 0.025em |
| `tracking-wider` | letter-spacing: 0.05em |
| `tracking-widest` | letter-spacing: 0.1em |

## Text Alignment

| Class | Properties |
|-------|------------|
| `text-left` | text-align: left |
| `text-center` | text-align: center |
| `text-right` | text-align: right |
| `text-justify` | text-align: justify |

## Text Color

| Class | Properties |
|-------|------------|
| `text-transparent` | color: transparent |
| `text-current` | color: currentColor |
| `text-black` | color: rgb(0 0 0) |
| `text-white` | color: rgb(255 255 255) |
| `text-slate-50` to `text-slate-900` | Various slate shades |
| `text-gray-50` to `text-gray-900` | Various gray shades |
| `text-red-500`, `text-blue-500`, etc. | Color shades from 50 to 900 |

## Text Decoration

| Class | Properties |
|-------|------------|
| `underline` | text-decoration: underline |
| `line-through` | text-decoration: line-through |
| `no-underline` | text-decoration: none |

## Text Transform

| Class | Properties |
|-------|------------|
| `uppercase` | text-transform: uppercase |
| `lowercase` | text-transform: lowercase |
| `capitalize` | text-transform: capitalize |
| `normal-case` | text-transform: none |

## Sizing

### Width

| Class | Properties |
|-------|------------|
| `w-0` | width: 0 |
| `w-px` | width: 1px |
| `w-1` | width: 0.25rem (4px) |
| `w-2` | width: 0.5rem (8px) |
| `w-4` | width: 1rem (16px) |
| `w-8` | width: 2rem (32px) |
| `w-16` | width: 4rem (64px) |
| `w-32` | width: 8rem (128px) |
| `w-auto` | width: auto |
| `w-full` | width: 100% |
| `w-screen` | width: 100vw |
| `w-1/2` | width: 50% |
| `w-1/3` | width: 33.333333% |
| `w-2/3` | width: 66.666667% |
| `w-1/4` | width: 25% |
| `w-3/4` | width: 75% |

### Min/Max Width

| Class | Properties |
|-------|------------|
| `min-w-0` | min-width: 0 |
| `min-w-full` | min-width: 100% |
| `max-w-xs` | max-width: 20rem |
| `max-w-sm` | max-width: 24rem |
| `max-w-md` | max-width: 28rem |
| `max-w-lg` | max-width: 32rem |
| `max-w-xl` | max-width: 36rem |
| `max-w-2xl` | max-width: 42rem |
| `max-w-4xl` | max-width: 56rem |
| `max-w-7xl` | max-width: 80rem |
| `max-w-full` | max-width: 100% |

### Height

| Class | Properties |
|-------|------------|
| `h-0` | height: 0 |
| `h-1` | height: 0.25rem (4px) |
| `h-4` | height: 1rem (16px) |
| `h-8` | height: 2rem (32px) |
| `h-16` | height: 4rem (64px) |
| `h-32` | height: 8rem (128px) |
| `h-auto` | height: auto |
| `h-full` | height: 100% |
| `h-screen` | height: 100vh |

### Min/Max Height

| Class | Properties |
|-------|------------|
| `min-h-0` | min-height: 0 |
| `min-h-full` | min-height: 100% |
| `min-h-screen` | min-height: 100vh |
| `max-h-full` | max-height: 100% |
| `max-h-screen` | max-height: 100vh |