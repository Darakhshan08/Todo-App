# Common Patterns and Best Practices

## Component Organization

### File Structure
```
components/
├── ui/                 # Shadcn UI components
│   ├── button.tsx
│   ├── card.tsx
│   ├── dialog.tsx
│   └── ...
├── theme-provider.tsx  # Theme provider
└── mode-toggle.tsx     # Theme toggle
```

### Naming Conventions
- Use PascalCase for component names: `UserProfile`, `DataTable`
- Use camelCase for utility functions: `cn`, `formatDate`
- Use kebab-case for file names: `user-profile.tsx`, `data-table.tsx`

## Theming and Styling

### CSS Variables
Define theme colors using CSS variables in your globals.css:

```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;
    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 222.2 84% 4.9%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --card: 222.2 84% 4.9%;
    --card-foreground: 210 40% 98%;
    --popover: 222.2 84% 4.9%;
    --popover-foreground: 210 40% 98%;
    --primary: 210 40% 98%;
    --primary-foreground: 222.2 47.4% 11.2%;
    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;
    --accent: 217.2 32.6% 17.5%;
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;
    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 212.7 26.8% 83.9%;
  }
}
```

### Dark Mode Implementation
Use next-themes for theme switching:

```tsx
// components/theme-provider.tsx
"use client"

import * as React from "react"
import { ThemeProvider as NextThemesProvider } from "next-themes"
import { type ThemeProviderProps } from "next-themes/dist/types"

export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

## Accessibility Best Practices

### Semantic HTML
Always use semantic HTML elements when possible:
- Use `<button>` for buttons instead of `<div>`
- Use `<label>` for form inputs
- Use proper heading hierarchy (h1, h2, h3, etc.)

### Keyboard Navigation
Ensure all interactive elements are keyboard accessible:
- Use `tabIndex` appropriately
- Implement focus management in modals
- Follow proper focus order

### ARIA Labels
Provide appropriate ARIA labels for accessibility:
```tsx
<Button aria-label="Close dialog">
  <XIcon />
</Button>
```

## Responsive Design

### Breakpoints
Use Tailwind's responsive prefixes:
- `sm:` - 640px and above
- `md:` - 768px and above
- `lg:` - 1024px and above
- `xl:` - 1280px and above
- `2xl:` - 1536px and above

### Responsive Components
```tsx
// Responsive card grid
<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
  <Card>...</Card>
  <Card>...</Card>
  <Card>...</Card>
</div>
```

## Form Handling

### Form Validation
Use react-hook-form with Zod for validation:

```tsx
const formSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
})
```

### Loading States
Always provide loading states for form submissions:

```tsx
<Button type="submit" disabled={isLoading}>
  {isLoading ? "Submitting..." : "Submit"}
</Button>
```

## Common Workflows

### Adding a New Component
1. Identify required components (e.g., form with input, button, card)
2. Add components: `npx shadcn@latest add card input button label`
3. Import and compose components in your page/component
4. Customize styling using Tailwind classes
5. Add interactivity with client-side logic if needed

### Customizing a Component
1. Locate component in `components/ui/`
2. Modify directly - add variants, change styles, extend functionality
3. Component changes are isolated to your project
4. Update types if adding new props

## Performance Optimization

### Code Splitting
Use React.lazy for heavy components:
```tsx
const HeavyComponent = lazy(() => import('./HeavyComponent'))
```

### Image Optimization
Use Next.js Image component for all images:
```tsx
<Image
  src="/image.jpg"
  alt="Description"
  width={300}
  height={200}
/>
```

## Testing Components

### Unit Testing
Test components with Jest and React Testing Library:
```tsx
import { render, screen } from '@testing-library/react'

test('renders button with correct text', () => {
  render(<Button>Click me</Button>)
  expect(screen.getByText('Click me')).toBeInTheDocument()
})
```

### Visual Regression Testing
Consider using tools like Storybook for visual regression testing.

## Common Troubleshooting

### Components not found after adding
- Solution: Check `components.json` aliases match your import paths
- Verify components were added to correct directory

### Styles not applying
- Solution: Ensure Tailwind CSS is properly configured
- Check `globals.css` has CSS variables defined
- Verify Tailwind config includes component paths

### Dark mode not working
- Solution: Ensure `next-themes` is installed
- Verify ThemeProvider wraps your app in layout
- Check `suppressHydrationWarning` on `<html>` tag

## Internationalization (i18n)
For multilingual apps, consider using next-i18next with Shadcn UI components:

```tsx
import { useTranslation } from 'next-i18next'

export function TranslatedButton() {
  const { t } = useTranslation('common')

  return <Button>{t('click-me')}</Button>
}
```