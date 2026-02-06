# Button Examples

Various button styles and variants using Tailwind CSS.

## Primary Button

```html
<button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  Primary Button
</button>
```

## Secondary Button

```html
<button class="bg-gray-200 text-gray-900 px-4 py-2 rounded-lg hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2">
  Secondary Button
</button>
```

## Outline Button

```html
<button class="border-2 border-blue-600 text-blue-600 px-4 py-2 rounded-lg hover:bg-blue-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  Outline Button
</button>
```

## Disabled Button

```html
<button class="bg-gray-300 text-gray-500 px-4 py-2 rounded-lg cursor-not-allowed" disabled>
  Disabled Button
</button>
```

## Button Sizes

### Small Button

```html
<button class="bg-blue-600 text-white px-2 py-1 text-sm rounded hover:bg-blue-700">
  Small
</button>
```

### Large Button

```html
<button class="bg-blue-600 text-white px-6 py-3 text-lg rounded-lg hover:bg-blue-700">
  Large
</button>
```

## Icon Buttons

### Button with Left Icon

```html
<button class="bg-blue-600 text-white px-4 py-2 rounded-lg inline-flex items-center hover:bg-blue-700">
  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
    <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
  </svg>
  Add
</button>
```

### Button with Right Icon

```html
<button class="bg-blue-600 text-white px-4 py-2 rounded-lg inline-flex items-center hover:bg-blue-700">
  Download
  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
    <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" />
  </svg>
</button>
```

## Real-World Button Examples

### Call-to-Action Button

```html
<button class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-8 py-4 rounded-lg text-lg font-semibold shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition-all duration-200">
  Get Started
</button>
```

### Social Media Buttons

#### Twitter Button

```html
<button class="bg-blue-400 text-white px-6 py-3 rounded-full font-medium hover:bg-blue-500 flex items-center">
  <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24">
    <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z" />
  </svg>
  Share on Twitter
</button>
```

#### GitHub Button

```html
<button class="bg-gray-800 text-white px-6 py-3 rounded-lg font-medium hover:bg-gray-900 flex items-center">
  <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24">
    <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.65.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
  </svg>
  Sign in with GitHub
</button>
```

### E-commerce Buttons

#### Add to Cart Button

```html
<button class="bg-green-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-green-700 flex items-center justify-center">
  <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
  </svg>
  Add to Cart - $99.99
</button>
```

#### Like Button

```html
<button class="bg-white border-2 border-red-500 text-red-500 px-4 py-2 rounded-full hover:bg-red-50 flex items-center">
  <svg class="w-5 h-5 mr-1" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd" />
  </svg>
  Like
</button>
```

## Secondary Button

```html
<button class="bg-gray-200 text-gray-900 px-4 py-2 rounded-lg hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2">
  Secondary Button
</button>
```

## Outline Button

```html
<button class="border-2 border-blue-600 text-blue-600 px-4 py-2 rounded-lg hover:bg-blue-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  Outline Button
</button>
```

## Disabled Button

```html
<button class="bg-gray-300 text-gray-500 px-4 py-2 rounded-lg cursor-not-allowed" disabled>
  Disabled Button
</button>
```

## Button Sizes

### Small Button

```html
<button class="bg-blue-600 text-white px-2 py-1 text-sm rounded hover:bg-blue-700">
  Small
</button>
```

### Large Button

```html
<button class="bg-blue-600 text-white px-6 py-3 text-lg rounded-lg hover:bg-blue-700">
  Large
</button>
```

## Icon Buttons

### Button with Left Icon

```html
<button class="bg-blue-600 text-white px-4 py-2 rounded-lg inline-flex items-center hover:bg-blue-700">
  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
    <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
  </svg>
  Add
</button>
```

### Button with Right Icon

```html
<button class="bg-blue-600 text-white px-4 py-2 rounded-lg inline-flex items-center hover:bg-blue-700">
  Download
  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
    <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" />
  </svg>
</button>
```