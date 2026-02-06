# Alerts & Badges Examples

Alert and badge components using Tailwind CSS.

## Alert Variants

### Success Alert

```html
<div class="bg-green-50 border-l-4 border-green-500 p-4 mb-4">
  <div class="flex">
    <div class="flex-shrink-0">
      <svg class="h-5 w-5 text-green-400" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
      </svg>
    </div>
    <div class="ml-3">
      <p class="text-sm text-green-700">
        <strong class="font-medium">Success!</strong> Your changes have been saved.
      </p>
    </div>
  </div>
</div>
```

### Error Alert

```html
<div class="bg-red-50 border-l-4 border-red-500 p-4 mb-4">
  <div class="flex">
    <div class="ml-3">
      <p class="text-sm text-red-700">
        <strong class="font-medium">Error!</strong> There was a problem with your request.
      </p>
    </div>
  </div>
</div>
```

### Warning Alert

```html
<div class="bg-yellow-50 border-l-4 border-yellow-500 p-4 mb-4">
  <div class="flex">
    <div class="ml-3">
      <p class="text-sm text-yellow-700">
        <strong class="font-medium">Warning!</strong> Please review your information.
      </p>
    </div>
  </div>
</div>
```

### Info Alert

```html
<div class="bg-blue-50 border-l-4 border-blue-500 p-4 mb-4">
  <div class="flex">
    <div class="ml-3">
      <p class="text-sm text-blue-700">
        <strong class="font-medium">Info:</strong> This is an informational message.
      </p>
    </div>
  </div>
</div>
```

## Badge Variants

### Default Badge

```html
<span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
  Default
</span>
```

### Success Badge

```html
<span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800">
  Success
</span>
```

### Error Badge

```html
<span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800">
  Error
</span>
```

### Warning Badge

```html
<span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-yellow-100 text-yellow-800">
  Warning
</span>
```

### Neutral Badge

```html
<span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800">
  Neutral
</span>
```

## Pill Badges

### Small Pill Badge

```html
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
  Small
</span>
```

### Large Pill Badge

```html
<span class="inline-flex items-center px-3 py-1 rounded-full text-base font-medium bg-purple-100 text-purple-800">
  Large
</span>
```

## Icon Badges

### Badge with Left Icon

```html
<span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
  <svg class="-ml-0.5 mr-1.5 h-2 w-2 text-blue-400" fill="currentColor" viewBox="0 0 8 8">
    <circle cx="4" cy="4" r="3" />
  </svg>
  Active
</span>
```

### Badge with Right Icon

```html
<span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800">
  Completed
  <svg class="ml-1.5 h-4 w-4 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
  </svg>
</span>
```

## Outline Badges

```html
<span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium border border-blue-500 text-blue-700">
  Outline
</span>
```

## Dot Badges

```html
<span class="relative inline-block">
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
    Notifications
  </span>
  <span class="absolute -top-1 -right-1 flex h-4 w-4">
    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
    <span class="relative inline-flex rounded-full h-4 w-4 bg-red-500"></span>
  </span>
</span>
```

## Real-World Alert Examples

### Order Confirmation Alert

```html
<div class="bg-green-50 border-l-4 border-green-500 p-4 mb-4">
  <div class="flex">
    <div class="flex-shrink-0">
      <svg class="h-5 w-5 text-green-400" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
      </svg>
    </div>
    <div class="ml-3">
      <p class="text-sm text-green-700">
        <strong class="font-medium">Order Confirmed!</strong> Your order #12345 has been placed successfully. Expected delivery: March 15, 2024.
      </p>
    </div>
  </div>
</div>
```

### Payment Error Alert

```html
<div class="bg-red-50 border-l-4 border-red-500 p-4 mb-4">
  <div class="flex">
    <div class="flex-shrink-0">
      <svg class="h-5 w-5 text-red-400" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"></path>
      </svg>
    </div>
    <div class="ml-3">
      <p class="text-sm text-red-700">
        <strong class="font-medium">Payment Failed!</strong> Your card was declined. Please update your payment method.
      </p>
      <div class="mt-2">
        <button class="text-sm font-medium text-red-800 hover:text-red-900">
          Update payment method
        </button>
      </div>
    </div>
  </div>
</div>
```

### Security Warning Alert

```html
<div class="bg-yellow-50 border-l-4 border-yellow-500 p-4 mb-4">
  <div class="flex">
    <div class="flex-shrink-0">
      <svg class="h-5 w-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path>
      </svg>
    </div>
    <div class="ml-3">
      <p class="text-sm text-yellow-700">
        <strong class="font-medium">Security Alert!</strong> Unusual activity detected on your account from a new device. Please verify this login.
      </p>
      <div class="mt-2 flex space-x-3">
        <button class="text-sm font-medium text-yellow-800 hover:text-yellow-900">
          Verify Device
        </button>
        <button class="text-sm font-medium text-yellow-800 hover:text-yellow-900">
          Secure Account
        </button>
      </div>
    </div>
  </div>
</div>
```

## E-commerce Badges

### Product Availability Badges

```html
<div class="flex flex-wrap gap-2">
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800">
    <svg class="-ml-0.5 mr-1.5 h-2 w-2 text-green-400" fill="currentColor" viewBox="0 0 8 8">
      <circle cx="4" cy="4" r="3" />
    </svg>
    In Stock
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-yellow-100 text-yellow-800">
    <svg class="-ml-0.5 mr-1.5 h-2 w-2 text-yellow-400" fill="currentColor" viewBox="0 0 8 8">
      <circle cx="4" cy="4" r="3" />
    </svg>
    Low Stock
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800">
    <svg class="-ml-0.5 mr-1.5 h-2 w-2 text-red-400" fill="currentColor" viewBox="0 0 8 8">
      <circle cx="4" cy="4" r="3" />
    </svg>
    Out of Stock
  </span>
</div>
```

### Sale and Discount Badges

```html
<div class="flex flex-wrap gap-2">
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-500 text-white">
    SALE!
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-orange-500 text-white">
    20% OFF
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-purple-500 text-white">
    NEW
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-500 text-white">
    BEST SELLER
  </span>
</div>
```

### User Status Badges

```html
<div class="flex flex-wrap gap-2">
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800">
    Online
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800">
    Offline
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-yellow-100 text-yellow-800">
    Away
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800">
    Do Not Disturb
  </span>
</div>
```

### Social Media Badges

```html
<div class="flex flex-wrap gap-2">
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
    <svg class="mr-1 h-4 w-4 text-blue-500" fill="currentColor" viewBox="0 0 24 24">
      <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
    </svg>
    Verified
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800">
    <svg class="mr-1 h-4 w-4 text-gray-500" fill="currentColor" viewBox="0 0 24 24">
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
    </svg>
    GitHub
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-600 text-white">
    <svg class="mr-1 h-4 w-4" fill="currentColor" viewBox="0 0 24 24">
      <path d="M22.46 6c-.77.35-1.6.58-2.46.69.88-.53 1.56-1.37 1.88-2.38-.83.5-1.75.85-2.72 1.05C18.37 4.5 17.26 4 16 4c-2.35 0-4.27 1.92-4.27 4.29 0 .34.04.67.11.98C8.28 9.09 5.11 7.38 3 4.79c-.37.63-.58 1.37-.58 2.15 0 1.49.75 2.81 1.91 3.56-.71 0-1.37-.2-1.95-.5v.03c0 2.08 1.48 3.82 3.44 4.21a4.22 4.22 0 0 1-1.93.07 4.28 4.28 0 0 0 4 2.98 8.521 8.521 0 0 1-5.33 1.84c-.34 0-.68-.02-1.02-.06C3.44 20.29 5.7 21 8.12 21 16 21 20.33 14.46 20.33 8.79c0-.19 0-.37-.01-.56.84-.6 1.56-1.36 2.14-2.23z"/>
    </svg>
    Twitter
  </span>
</div>
```

## Notification Badges

```html
<div class="flex flex-wrap gap-4 items-center">
  <div class="relative">
    <button class="text-gray-700 hover:text-blue-600">
      <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path>
      </svg>
    </button>
    <span class="absolute -top-1 -right-1 flex h-4 w-4">
      <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
      <span class="relative inline-flex rounded-full h-4 w-4 bg-red-500 text-xs text-white flex items-center justify-center">3</span>
    </span>
  </div>

  <div class="relative">
    <button class="text-gray-700 hover:text-blue-600">
      <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
      </svg>
    </button>
    <span class="absolute -top-1 -right-1 flex h-4 w-4">
      <span class="relative inline-flex rounded-full h-4 w-4 bg-green-500 text-xs text-white flex items-center justify-center">1</span>
    </span>
  </div>
</div>
```

## Status Indicator Badges

```html
<div class="flex flex-wrap gap-4">
  <div class="flex items-center">
    <div class="w-3 h-3 rounded-full bg-green-500 mr-2"></div>
    <span class="text-sm">Online</span>
  </div>
  <div class="flex items-center">
    <div class="w-3 h-3 rounded-full bg-yellow-500 mr-2"></div>
    <span class="text-sm">Away</span>
  </div>
  <div class="flex items-center">
    <div class="w-3 h-3 rounded-full bg-red-500 mr-2"></div>
    <span class="text-sm">Do Not Disturb</span>
  </div>
  <div class="flex items-center">
    <div class="w-3 h-3 rounded-full bg-gray-400 mr-2"></div>
    <span class="text-sm">Offline</span>
  </div>
</div>
```