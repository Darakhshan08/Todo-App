# Flexbox & Grid Reference

Complete reference for Tailwind CSS flexbox and grid utility classes.

## Flex Direction

| Class | Properties |
|-------|------------|
| `flex-row` | flex-direction: row |
| `flex-row-reverse` | flex-direction: row-reverse |
| `flex-col` | flex-direction: column |
| `flex-col-reverse` | flex-direction: column-reverse |

## Flex Wrap

| Class | Properties |
|-------|------------|
| `flex-wrap` | flex-wrap: wrap |
| `flex-wrap-reverse` | flex-wrap: wrap-reverse |
| `flex-nowrap` | flex-wrap: nowrap |

## Flex

| Class | Properties |
|-------|------------|
| `flex-1` | flex: 1 1 0% |
| `flex-auto` | flex: 1 1 auto |
| `flex-initial` | flex: 0 1 auto |
| `flex-none` | flex: none |

## Flex Grow / Shrink

| Class | Properties |
|-------|------------|
| `grow` | flex-grow: 1 |
| `grow-0` | flex-grow: 0 |
| `shrink` | flex-shrink: 1 |
| `shrink-0` | flex-shrink: 0 |

## Justify Content

| Class | Properties |
|-------|------------|
| `justify-start` | justify-content: flex-start |
| `justify-end` | justify-content: flex-end |
| `justify-center` | justify-content: center |
| `justify-between` | justify-content: space-between |
| `justify-around` | justify-content: space-around |
| `justify-evenly` | justify-content: space-evenly |

## Align Items

| Class | Properties |
|-------|------------|
| `items-start` | align-items: flex-start |
| `items-end` | align-items: flex-end |
| `items-center` | align-items: center |
| `items-baseline` | align-items: baseline |
| `items-stretch` | align-items: stretch |

## Align Content

| Class | Properties |
|-------|------------|
| `content-start` | align-content: flex-start |
| `content-end` | align-content: flex-end |
| `content-center` | align-content: center |
| `content-between` | align-content: space-between |
| `content-around` | align-content: space-around |
| `content-evenly` | align-content: space-evenly |

## Align Self

| Class | Properties |
|-------|------------|
| `self-auto` | align-self: auto |
| `self-start` | align-self: flex-start |
| `self-end` | align-self: flex-end |
| `self-center` | align-self: center |
| `self-stretch` | align-self: stretch |

## Gap

| Class | Properties |
|-------|------------|
| `gap-0` | gap: 0 |
| `gap-1` | gap: 0.25rem (4px) |
| `gap-2` | gap: 0.5rem (8px) |
| `gap-4` | gap: 1rem (16px) |
| `gap-6` | gap: 1.5rem (24px) |
| `gap-8` | gap: 2rem (32px) |
| `gap-x-4` | column-gap: 1rem |
| `gap-y-4` | row-gap: 1rem |

## Grid Template Columns

| Class | Properties |
|-------|------------|
| `grid-cols-1` | grid-template-columns: repeat(1, minmax(0, 1fr)) |
| `grid-cols-2` | grid-template-columns: repeat(2, minmax(0, 1fr)) |
| `grid-cols-3` | grid-template-columns: repeat(3, minmax(0, 1fr)) |
| `grid-cols-4` | grid-template-columns: repeat(4, minmax(0, 1fr)) |
| `grid-cols-6` | grid-template-columns: repeat(6, minmax(0, 1fr)) |
| `grid-cols-12` | grid-template-columns: repeat(12, minmax(0, 1fr)) |
| `grid-cols-none` | grid-template-columns: none |

## Grid Column Span

| Class | Properties |
|-------|------------|
| `col-auto` | grid-column: auto |
| `col-span-1` | grid-column: span 1 / span 1 |
| `col-span-2` | grid-column: span 2 / span 2 |
| `col-span-3` | grid-column: span 3 / span 3 |
| `col-span-6` | grid-column: span 6 / span 6 |
| `col-span-12` | grid-column: span 12 / span 12 |
| `col-span-full` | grid-column: 1 / -1 |

## Grid Template Rows

| Class | Properties |
|-------|------------|
| `grid-rows-1` | grid-template-rows: repeat(1, minmax(0, 1fr)) |
| `grid-rows-2` | grid-template-rows: repeat(2, minmax(0, 1fr)) |
| `grid-rows-3` | grid-template-rows: repeat(3, minmax(0, 1fr)) |
| `grid-rows-6` | grid-template-rows: repeat(6, minmax(0, 1fr)) |

## Spacing

### Padding

| Class | Properties |
|-------|------------|
| `p-0` | padding: 0 |
| `p-1` | padding: 0.25rem (4px) |
| `p-2` | padding: 0.5rem (8px) |
| `p-3` | padding: 0.75rem (12px) |
| `p-4` | padding: 1rem (16px) |
| `p-6` | padding: 1.5rem (24px) |
| `p-8` | padding: 2rem (32px) |
| `pt-4` | padding-top: 1rem |
| `pr-4` | padding-right: 1rem |
| `pb-4` | padding-bottom: 1rem |
| `pl-4` | padding-left: 1rem |
| `px-4` | padding-left: 1rem; padding-right: 1rem |
| `py-4` | padding-top: 1rem; padding-bottom: 1rem |

### Margin

| Class | Properties |
|-------|------------|
| `m-0` | margin: 0 |
| `m-1` | margin: 0.25rem (4px) |
| `m-2` | margin: 0.5rem (8px) |
| `m-4` | margin: 1rem (16px) |
| `m-auto` | margin: auto |
| `mt-4` | margin-top: 1rem |
| `mr-4` | margin-right: 1rem |
| `mb-4` | margin-bottom: 1rem |
| `ml-4` | margin-left: 1rem |
| `mx-4` | margin-left: 1rem; margin-right: 1rem |
| `my-4` | margin-top: 1rem; margin-bottom: 1rem |
| `mx-auto` | margin-left: auto; margin-right: auto |

### Space Between

| Class | Properties |
|-------|------------|
| `space-x-4` | margin-left: 1rem (for children except first) |
| `space-y-4` | margin-top: 1rem (for children except first) |