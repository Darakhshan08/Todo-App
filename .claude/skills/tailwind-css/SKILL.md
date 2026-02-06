---
name: tailwind-css
description: Apply Tailwind CSS styling patterns in Next.js. Creates responsive layouts with utility classes, custom color schemes, and consistent spacing/typography. Use when styling Next.js components or creating responsive designs.
---

# Tailwind CSS Styling Patterns

This skill helps you set up and apply Tailwind CSS styling patterns in Next.js projects with proper utility usage, responsive design, and theme customization.

## Overview

Tailwind CSS is a utility-first CSS framework that provides pre-designed classes for rapid UI development. It scans your files to generate optimized CSS with zero runtime overhead.

## Prerequisites

- Node.js and npm/pnpm/yarn
- Next.js project with App Router

## Installation and Setup

### Install Tailwind CSS

Run the following commands to install Tailwind CSS and initialize the configuration:

```bash
npm install -D tailwindcss@3
npx tailwindcss init
```

Or with pnpm:
```bash
pnpm add -D tailwindcss@3
npx tailwindcss init
```

### Configure Tailwind CSS

Update your `tailwind.config.js` (or `tailwind.config.ts`) to include your project files:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### Add Tailwind Directives to CSS

Create or update your main CSS file (typically `app/globals.css` or `styles/globals.css`) and add the Tailwind directives:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

These directives inject Tailwind's base styles, component classes, and utility classes into your CSS.

## Core Concepts

### Utility-First Approach

Style elements by composing utility classes directly in HTML/JSX instead of writing custom CSS:

```tsx
// Traditional CSS approach
<div className="chat-notification">
  <div className="chat-notification-logo-wrapper">
    <img className="chat-notification-logo" src="/img/logo.svg" alt="Logo" />
  </div>
  <div className="chat-notification-content">
    <h4 className="chat-notification-title">ChitChat</h4>
    <p className="chat-notification-message">You have a new message!</p>
  </div>
</div>

// Tailwind CSS utility-first approach
<div className="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center gap-x-4">
  <div className="shrink-0">
    <img className="size-12" src="/img/logo.svg" alt="ChitChat Logo" />
  </div>
  <div>
    <div className="text-xl font-medium text-black">ChitChat</div>
    <p className="text-slate-500">You have a new message!</p>
  </div>
</div>
```

## Responsive Design

### Mobile-First Breakpoints

Tailwind uses a mobile-first breakpoint system. Styles apply to all screen sizes unless overridden:

```tsx
// Default breakpoints:
// sm: 640px
// md: 768px
// lg: 1024px
// xl: 1280px
// 2xl: 1536px

// Example: Different widths at different screen sizes
<img className="w-16 md:w-32 lg:w-48" src="..." />
// Width 16 (default), 32 on medium screens, 48 on large screens
```

### Responsive Layout Example

```tsx
<div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
  <div className="md:flex">
    <div className="md:shrink-0">
      <img
        className="h-48 w-full object-cover md:h-full md:w-48"
        src="/img/building.jpg"
        alt="Modern building"
      />
    </div>
    <div className="p-8">
      <div className="uppercase tracking-wide text-sm text-indigo-500 font-semibold">
        Company retreats
      </div>
      <a href="#" className="block mt-1 text-lg leading-tight font-medium text-black hover:underline">
        Incredible accommodation for your team
      </a>
      <p className="mt-2 text-slate-500">
        Looking to take your team away on a retreat to enjoy awesome food and sunshine?
        We have a list of places to do just that.
      </p>
    </div>
  </div>
</div>
```

### Responsive Text and Colors

```tsx
// Responsive text sizes
<h1 className="text-2xl md:text-4xl lg:text-6xl">Responsive Heading</h1>

// Responsive colors
<p className="text-blue-600 md:text-green-600 lg:text-purple-600">
  Changes color at different breakpoints
</p>

// Responsive padding
<div className="p-4 md:p-6 lg:p-8">
  Padding increases on larger screens
</div>
```

## Layout Utilities

### Flexbox

```tsx
// Horizontal flex layout
<div className="flex items-center justify-between gap-4">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>

// Vertical flex layout
<div className="flex flex-col gap-2">
  <div>Item 1</div>
  <div>Item 2</div>
</div>

// Responsive flex direction
<div className="flex flex-col md:flex-row gap-4">
  Stacked on mobile, horizontal on desktop
</div>

// Center content
<div className="flex items-center justify-center min-h-screen">
  <div>Centered content</div>
</div>
```

### Grid

```tsx
// Basic grid
<div className="grid grid-cols-3 gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

// Responsive grid
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <div>Card 1</div>
  <div>Card 2</div>
  <div>Card 3</div>
</div>

// Grid with different column spans
<div className="grid grid-cols-6 gap-4">
  <div className="col-span-6 md:col-span-4">Main content</div>
  <div className="col-span-6 md:col-span-2">Sidebar</div>
</div>
```

## Spacing

### Padding and Margin

```tsx
// Padding all sides
<div className="p-4">Padding 1rem (16px)</div>

// Padding specific sides
<div className="pt-4 pb-2 px-6">
  Top padding 1rem, bottom 0.5rem, horizontal 1.5rem
</div>

// Margin
<div className="mt-4 mb-6 mx-auto">
  Top margin 1rem, bottom 1.5rem, horizontal auto (center)
</div>

// Gap for flex/grid
<div className="flex gap-4">Spacing between flex items</div>
<div className="grid grid-cols-3 gap-x-4 gap-y-2">
  Horizontal gap 1rem, vertical gap 0.5rem
</div>
```

### Spacing Scale

```
0   = 0px
1   = 0.25rem (4px)
2   = 0.5rem (8px)
3   = 0.75rem (12px)
4   = 1rem (16px)
6   = 1.5rem (24px)
8   = 2rem (32px)
12  = 3rem (48px)
16  = 4rem (64px)
```

## Typography

### Font Families

```tsx
<p className="font-sans">Sans-serif font</p>
<p className="font-serif">Serif font</p>
<p className="font-mono">Monospace font</p>
```

### Font Sizes

```tsx
<p className="text-xs">Extra small (0.75rem)</p>
<p className="text-sm">Small (0.875rem)</p>
<p className="text-base">Base (1rem)</p>
<p className="text-lg">Large (1.125rem)</p>
<p className="text-xl">Extra large (1.25rem)</p>
<p className="text-2xl">2XL (1.5rem)</p>
<p className="text-4xl">4XL (2.25rem)</p>
```

### Font Weights and Styles

```tsx
<p className="font-light">Light (300)</p>
<p className="font-normal">Normal (400)</p>
<p className="font-medium">Medium (500)</p>
<p className="font-semibold">Semibold (600)</p>
<p className="font-bold">Bold (700)</p>

<p className="italic">Italic text</p>
<p className="uppercase">Uppercase text</p>
<p className="lowercase">Lowercase text</p>
<p className="capitalize">Capitalized text</p>
```

### Line Height and Letter Spacing

```tsx
<p className="leading-tight">Tight line height</p>
<p className="leading-normal">Normal line height</p>
<p className="leading-relaxed">Relaxed line height</p>

<p className="tracking-tight">Tight letter spacing</p>
<p className="tracking-wide">Wide letter spacing</p>
```

## Colors

### Text Colors

```tsx
<p className="text-slate-900">Very dark slate</p>
<p className="text-gray-600">Medium gray</p>
<p className="text-blue-500">Blue</p>
<p className="text-red-600">Red</p>
<p className="text-green-500">Green</p>
```

### Background Colors

```tsx
<div className="bg-white">White background</div>
<div className="bg-slate-100">Light slate background</div>
<div className="bg-blue-500">Blue background</div>
<div className="bg-gradient-to-r from-blue-500 to-purple-600">Gradient</div>
```

### Border Colors

```tsx
<div className="border border-gray-300">Gray border</div>
<div className="border-2 border-blue-500">Thick blue border</div>
```

## Custom Theme Configuration

### Extend Default Theme in `tailwind.config.ts`

```typescript
import type { Config } from "tailwindcss"

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/**/*.{js,ts,jsx,tsx,mdx}", // Additional path for src directory
  ],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    colors: {
      'blue': '#1fb6ff',
      'purple': '#7e5bef',
      'pink': '#ff49db',
      'orange': '#ff7849',
      'green': '#13ce66',
      'yellow': '#ffc82c',
      'gray-dark': '#273444',
      'gray': '#8492a6',
      'gray-light': '#d3dce6',
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {
      colors: {
        // Custom color palette
        primary: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          500: '#0ea5e9',
          600: '#0284c7',
          900: '#0c4a6e',
        },
        secondary: {
          500: '#8b5cf6',
          600: '#7c3aed',
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        heading: ['Poppins', 'sans-serif'],
      },
      spacing: {
        '128': '32rem',
        '144': '36rem',
      },
      borderRadius: {
        '4xl': '2rem',
      },
    },
  },
  plugins: [],
}

export default config
```

### Replace Default Colors

```typescript
const config: Config = {
  theme: {
    colors: {
      'blue': '#1fb6ff',
      'purple': '#7e5bef',
      'pink': '#ff49db',
      'orange': '#ff7849',
      'green': '#13ce66',
      'yellow': '#ffc82c',
      'gray-dark': '#273444',
      'gray': '#8492a6',
      'gray-light': '#d3dce6',
    },
    // ... rest of config
  },
}
```

### Custom Breakpoints

```typescript
const config: Config = {
  theme: {
    screens: {
      'sm': '480px',
      'md': '768px',
      'lg': '976px',
      'xl': '1440px',
    },
  },
}
```

## Component Patterns

### Card Component

```tsx
export function Card({ children }: { children: React.ReactNode }) {
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      <div className="p-6">
        {children}
      </div>
    </div>
  )
}
```

### Button Variants

```tsx
export function Button({
  variant = 'primary',
  children
}: {
  variant?: 'primary' | 'secondary' | 'outline'
  children: React.ReactNode
}) {
  const baseClasses = "px-4 py-2 rounded-lg font-medium transition-colors"

  const variantClasses = {
    primary: "bg-blue-600 text-white hover:bg-blue-700",
    secondary: "bg-gray-200 text-gray-900 hover:bg-gray-300",
    outline: "border-2 border-blue-600 text-blue-600 hover:bg-blue-50",
  }

  return (
    <button className={`${baseClasses} ${variantClasses[variant]}`}>
      {children}
    </button>
  )
}
```

### Container with Max Width

```tsx
export function Container({ children }: { children: React.ReactNode }) {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      {children}
    </div>
  )
}
```

## Best Practices

### 1. Use Consistent Spacing Scale

```tsx
// Good: Use standard spacing scale
<div className="space-y-4">
  <div className="p-4">Item 1</div>
  <div className="p-4">Item 2</div>
</div>

// Avoid: Arbitrary values unless necessary
<div className="space-y-[17px]">...</div>
```

### 2. Leverage Responsive Utilities

```tsx
// Good: Mobile-first responsive design
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  ...
</div>

// Avoid: Fixed layouts
<div className="grid grid-cols-3 gap-4">...</div>
```

### 3. Extract Repeated Patterns

```tsx
// Good: Create reusable component
function PrimaryButton({ children }: { children: React.ReactNode }) {
  return (
    <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
      {children}
    </button>
  )
}

// Avoid: Repeating same classes everywhere
```

### 4. Use Semantic Color Names

```tsx
// Good: Define semantic colors in config
colors: {
  primary: '#0ea5e9',
  danger: '#ef4444',
  success: '#22c55e',
}

// Then use: bg-primary, text-danger, border-success
```

### 5. Group Related Utilities

```tsx
// Good: Organized and readable
<div className="
  flex items-center justify-between
  p-4 rounded-lg
  bg-white shadow-md
  hover:shadow-lg transition-shadow
">
  ...
</div>
```

## Dark Mode

### Configure Dark Mode in `tailwind.config.ts`

```typescript
const config: Config = {
  darkMode: 'class', // or 'media'
  // ... rest of config
}
```

### Apply Dark Mode Styles

```tsx
<div className="bg-white dark:bg-gray-900 text-gray-900 dark:text-white">
  <h1 className="text-2xl font-bold">
    Light and Dark Mode Support
  </h1>
  <p className="text-gray-600 dark:text-gray-400">
    This text adapts to the theme
  </p>
</div>
```

## Common Patterns

### Hero Section

```tsx
<section className="bg-gradient-to-r from-blue-600 to-purple-600 text-white">
  <div className="max-w-7xl mx-auto px-4 py-20 text-center">
    <h1 className="text-5xl font-bold mb-4">Welcome to Our Site</h1>
    <p className="text-xl mb-8">Build amazing things with Tailwind CSS</p>
    <button className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100">
      Get Started
    </button>
  </div>
</section>
```

### Navigation Bar

```tsx
<nav className="bg-white shadow-sm">
  <div className="max-w-7xl mx-auto px-4">
    <div className="flex items-center justify-between h-16">
      <div className="text-xl font-bold">Logo</div>
      <div className="hidden md:flex gap-6">
        <a href="#" className="text-gray-700 hover:text-blue-600">Home</a>
        <a href="#" className="text-gray-700 hover:text-blue-600">About</a>
        <a href="#" className="text-gray-700 hover:text-blue-600">Contact</a>
      </div>
    </div>
  </div>
</nav>
```

### Grid Gallery

```tsx
<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 p-4">
  {images.map((img, i) => (
    <div key={i} className="aspect-square bg-gray-200 rounded-lg overflow-hidden hover:scale-105 transition-transform">
      <img src={img} alt="" className="w-full h-full object-cover" />
    </div>
  ))}
</div>
```

## Troubleshooting

**Issue**: Styles not applying
- Solution: Verify Tailwind is scanning your files (check `content` in config)
- Ensure you're importing Tailwind directives in globals.css

**Issue**: Custom colors not working
- Solution: Restart dev server after config changes
- Verify color definition syntax in tailwind.config.ts

**Issue**: Responsive classes not working
- Solution: Check screen size breakpoints
- Ensure you're testing at correct viewport width

## Resources

- Official Documentation: https://tailwindcss.com
- Official Documentation v3: https://v3.tailwindcss.com
- Playground: https://play.tailwindcss.com
- Components: https://tailwindui.com
- Cheat Sheet: https://nerdcave.com/tailwind-cheat-sheet

## Included Templates

This skill includes comprehensive templates for common UI patterns organized in the templates/ directory:

- **Button Component Template**: Reusable button component with variant support (`templates/button-component.tsx`)
- **Card Component Template**: Flexible card component with title, description, and content slots (`templates/card-component.tsx`)
- **Form Template**: Complete form structure with validation patterns (`templates/form-template.tsx`)
- **Modal Component**: Accessible modal component with backdrop and content (`templates/modal-component.tsx`)

## Included Examples

Practical, production-ready examples of Tailwind CSS components organized in the examples/ directory:

- **Button Examples**: Various button styles and variants with different states (`examples/button-examples.md`)
- **Form Examples**: Complete form structures with various input types and validation patterns (`examples/form-examples.md`)
- **Navigation Examples**: Horizontal nav, navbar with logo, and sidebar navigation components (`examples/navigation-examples.md`)
- **Alerts & Badges Examples**: Alert and badge components with different variants (`examples/alerts-badges-examples.md`)
- **Table Examples**: Data table and striped table components (`examples/tables-examples.md`)
- **Hero & Footer Examples**: Hero sections and footer components (`examples/hero-footer-examples.md`)
- **Modal Examples**: Accessible modal components with different configurations (`examples/modal-examples.md`)

## Reference Documentation

Complete API reference for all Tailwind CSS utility classes organized in the reference/ directory:

- **Overview**: Core concepts, installation, configuration, and utility functions (`reference/reference-overview.md`)
- **Layout Utilities**: Display, position, overflow, z-index, and other layout properties (`reference/layout-utilities.md`)
- **Flexbox & Grid**: Flexbox and grid system utilities (`reference/flexbox-grid-utilities.md`)
- **Typography Utilities**: Font family, size, weight, line height, and text properties (`reference/typography-utilities.md`)
- **Backgrounds & Borders**: Background colors, gradients, border styles, and radius (`reference/backgrounds-borders-utilities.md`)
- **Effects & Animations**: Shadows, opacity, transitions, transforms, and animations (`reference/effects-animations-utilities.md`)
- **Common Patterns**: Best practices, responsive design, dark mode, and troubleshooting (`reference/common-patterns.md`)
