# Common Patterns and Best Practices

Essential patterns, best practices, and responsive design techniques for Tailwind CSS.

## Responsive Design

### Breakpoint Prefixes
Apply styles conditionally at different screen sizes using breakpoint prefixes:

- `sm:` - 640px and above
- `md:` - 768px and above
- `lg:` - 1024px and above
- `xl:` - 1280px and above
- `2xl:` - 1536px and above

### Example:
```html
<div class="text-center md:text-left lg:text-center">
  Responsive text alignment
</div>
```

## Dark Mode

### Configuration
Set up dark mode in `tailwind.config.js`:
```javascript
module.exports = {
  darkMode: 'class', // or 'media'
  // ...
}
```

### Usage
Use the `dark:` prefix to apply styles in dark mode:
```html
<div class="bg-white text-black dark:bg-gray-900 dark:text-white">
  Dark mode compatible
</div>
```

## Hover, Focus, and Other States

### State Prefixes
- `hover:` - Applies on hover
- `focus:` - Applies on focus
- `active:` - Applies when active
- `focus-within:` - Applies when element or child is focused
- `focus-visible:` - Applies when element is focused via keyboard
- `disabled:` - Applies when disabled

### Example:
```html
<button class="bg-blue-600 text-white hover:bg-blue-700 focus:ring-2 focus:ring-blue-500">
  Interactive button
</button>
```

## Best Practices

### 1. Use Consistent Spacing Scale
```html
<!-- Good: Use standard spacing scale -->
<div class="space-y-4">
  <div class="p-4">Item 1</div>
  <div class="p-4">Item 2</div>
</div>

<!-- Avoid: Arbitrary values unless necessary -->
<div class="space-y-[17px]">...</div>
```

### 2. Leverage Responsive Utilities
```html
<!-- Good: Mobile-first responsive design -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  ...
</div>

<!-- Avoid: Fixed layouts -->
<div class="grid grid-cols-3 gap-4">...</div>
```

### 3. Extract Repeated Patterns
```html
<!-- Good: Create reusable component -->
function PrimaryButton({ children }) {
  return (
    <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
      {children}
    </button>
  )
}

<!-- Avoid: Repeating same classes everywhere -->
```

### 4. Use Semantic Color Names
```javascript
// Good: Define semantic colors in config
colors: {
  primary: '#0ea5e9',
  danger: '#ef4444',
  success: '#22c55e',
}

// Then use: bg-primary, text-danger, border-success
```

### 5. Group Related Utilities
```html
<!-- Good: Organized and readable -->
<div class="
  flex items-center justify-between
  p-4 rounded-lg
  bg-white shadow-md
  hover:shadow-lg transition-shadow
">
  ...
</div>
```

## Common Component Patterns

### Card Component
```html
<div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
  <div class="p-6">
    <h3 class="text-xl font-bold text-gray-900">Card Title</h3>
    <p class="text-gray-600">Card content</p>
  </div>
</div>
```

### Button Variants
```html
<!-- Primary -->
<button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
  Primary
</button>

<!-- Secondary -->
<button class="bg-gray-200 text-gray-900 px-4 py-2 rounded-lg hover:bg-gray-300">
  Secondary
</button>

<!-- Outline -->
<button class="border-2 border-blue-600 text-blue-600 px-4 py-2 rounded-lg hover:bg-blue-50">
  Outline
</button>
```

### Form Elements
```html
<div>
  <label class="block text-sm font-medium text-gray-700 mb-2" for="email">
    Email
  </label>
  <input
    type="email"
    id="email"
    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
    placeholder="you@example.com" />
</div>
```

## Performance Optimization

### Purge Unused CSS
Ensure your `tailwind.config.js` has proper content paths to remove unused styles in production:

```javascript
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
    // Add all paths where classes are used
  ],
  // ...
}
```

## Troubleshooting

**Issue**: Styles not applying
- Solution: Verify Tailwind is scanning your files (check `content` in config)
- Ensure you're importing Tailwind directives in your CSS

**Issue**: Custom colors not working
- Solution: Restart dev server after config changes
- Verify color definition syntax in tailwind.config.js

**Issue**: Responsive classes not working
- Solution: Check screen size breakpoints
- Ensure you're testing at correct viewport width

## Example Usage

```html
<div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center gap-4 hover:shadow-xl transition-shadow duration-300">
  <img class="h-12 w-12 rounded-full" src="avatar.jpg" alt="Avatar" />
  <div>
    <h3 class="text-xl font-semibold text-gray-900">John Doe</h3>
    <p class="text-gray-500">Software Developer</p>
  </div>
</div>
```

## Performance Optimization

### Purge Unused CSS
Ensure your `tailwind.config.js` has proper content paths to remove unused styles in production:

```javascript
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
    // Add all paths where classes are used
  ],
  // ...
}
```

## Common Component Patterns

### Card Component
```html
<div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
  <div class="p-6">
    <h3 class="text-xl font-bold text-gray-900">Card Title</h3>
    <p class="text-gray-600">Card content</p>
  </div>
</div>
```

### Button Variants
```html
<!-- Primary -->
<button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
  Primary
</button>

<!-- Secondary -->
<button class="bg-gray-200 text-gray-900 px-4 py-2 rounded-lg hover:bg-gray-300">
  Secondary
</button>

<!-- Outline -->
<button class="border-2 border-blue-600 text-blue-600 px-4 py-2 rounded-lg hover:bg-blue-50">
  Outline
</button>
```

### Form Elements
```html
<div>
  <label class="block text-sm font-medium text-gray-700 mb-2" for="email">
    Email
  </label>
  <input
    type="email"
    id="email"
    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
    placeholder="you@example.com" />
</div>
```