# Layout Utilities Reference

Complete reference for Tailwind CSS layout utility classes.

## Display

| Class | Properties |
|-------|------------|
| `block` | display: block |
| `inline-block` | display: inline-block |
| `inline` | display: inline |
| `flex` | display: flex |
| `inline-flex` | display: inline-flex |
| `grid` | display: grid |
| `inline-grid` | display: inline-grid |
| `hidden` | display: none |

## Position

| Class | Properties |
|-------|------------|
| `static` | position: static |
| `fixed` | position: fixed |
| `absolute` | position: absolute |
| `relative` | position: relative |
| `sticky` | position: sticky |

## Top / Right / Bottom / Left

| Class | Properties |
|-------|------------|
| `inset-0` | top: 0; right: 0; bottom: 0; left: 0 |
| `inset-x-0` | left: 0; right: 0 |
| `inset-y-0` | top: 0; bottom: 0 |
| `top-0` | top: 0 |
| `right-0` | right: 0 |
| `bottom-0` | bottom: 0 |
| `left-0` | left: 0 |
| `top-1` | top: 0.25rem (4px) |
| `right-1` | right: 0.25rem (4px) |
| `bottom-1` | bottom: 0.25rem (4px) |
| `left-1` | left: 0.25rem (4px) |

Values: `0`, `0.5`, `1`, `2`, `3`, `4`, `6`, `8`, `12`, `16`, etc.

## Overflow

| Class | Properties |
|-------|------------|
| `overflow-auto` | overflow: auto |
| `overflow-hidden` | overflow: hidden |
| `overflow-visible` | overflow: visible |
| `overflow-scroll` | overflow: scroll |
| `overflow-x-auto` | overflow-x: auto |
| `overflow-y-auto` | overflow-y: auto |

## Z-Index

| Class | Properties |
|-------|------------|
| `z-0` | z-index: 0 |
| `z-10` | z-index: 10 |
| `z-20` | z-index: 20 |
| `z-30` | z-index: 30 |
| `z-40` | z-index: 40 |
| `z-50` | z-index: 50 |
| `z-auto` | z-index: auto |

## Responsive Design

All utilities can be prefixed with breakpoint modifiers:

| Prefix | Screen Size |
|--------|-------------|
| `sm:` | 640px and above |
| `md:` | 768px and above |
| `lg:` | 1024px and above |
| `xl:` | 1280px and above |
| `2xl:` | 1536px and above |

Example: `sm:text-center` applies text-center on small screens and above.

## Hover, Focus, and Other States

| Prefix | Purpose |
|--------|---------|
| `hover:` | Apply on hover |
| `focus:` | Apply on focus |
| `active:` | Apply when active |
| `focus-within:` | Apply when element or child is focused |
| `focus-visible:` | Apply when element is focused via keyboard |
| `disabled:` | Apply when disabled |
| `dark:` | Apply in dark mode |