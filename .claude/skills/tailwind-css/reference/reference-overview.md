# Tailwind CSS Reference Overview

Complete reference guide for Tailwind CSS including installation, configuration, and core concepts.

## Installation

### Install Tailwind CSS

```bash
npm install -D tailwindcss@3
npx tailwindcss init
```

### Configure Tailwind CSS

Update your `tailwind.config.js` to include your project files:

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

Add these directives to your main CSS file (typically `app/globals.css`):

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

## Core Concepts

### Utility-First Approach
Tailwind CSS is a utility-first CSS framework that provides low-level utility classes to build designs without writing custom CSS. Instead of predefined components, you compose classes directly in your HTML/JSX.

### Responsive Design
Use breakpoint prefixes to apply styles conditionally at different screen sizes:
- `sm:` - 640px and above
- `md:` - 768px and above
- `lg:` - 1024px and above
- `xl:` - 1280px and above
- `2xl:` - 1536px and above

### Dark Mode
Configure dark mode in your `tailwind.config.js`:
```javascript
module.exports = {
  darkMode: 'class', // or 'media'
  // ...
}
```

Then use the `dark:` prefix in your classes:
```html
<div class="bg-white text-black dark:bg-gray-900 dark:text-white">
```