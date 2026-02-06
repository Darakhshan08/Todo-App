# Shadcn UI Reference Guide

This document provides a complete API reference for all Shadcn UI components with props, variants, and usage examples.

## Core Concepts

### Component Installation
Shadcn UI components are installed individually using the CLI:

```bash
npx shadcn@latest add [component-name]
```

Components are copied into your project and can be customized freely.

### Configuration File
The `components.json` file controls component installation and configuration:

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}
```

## Utility Functions

### cn Utility

The `cn` utility function combines class names and resolves conflicts using Tailwind Merge:

```tsx
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

This function is typically located in `lib/utils.ts` and is used throughout components to merge Tailwind classes safely.

## Styling and Theming

### CSS Variables

Shadcn UI uses CSS variables for theming, which are defined in your globals.css file:

```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    /* ... other color variables */
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    /* ... other color variables */
  }
}
```

### Dark Mode

Dark mode is implemented using `next-themes` and CSS variables. The theme provider should wrap your app:

```tsx
import { ThemeProvider as NextThemesProvider } from "next-themes"
import { type ThemeProviderProps } from "next-themes/dist/types"

export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

## Dependencies

Shadcn UI relies on several key dependencies:

- `@radix-ui/react-*` - Accessible component primitives
- `class-variance-authority` - Component variant utilities
- `clsx` - Class name utility
- `tailwind-merge` - Tailwind class merging
- `lucide-react` - Icon library (if using lucide icons)
- `@hookform/resolvers` - Form validation resolvers (for form components)
- `zod` - Schema validation library (often used with forms)