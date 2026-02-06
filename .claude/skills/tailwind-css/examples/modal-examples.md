# Modal Examples

Modal components using Tailwind CSS.

## Basic Modal

```html
<!-- Modal Backdrop -->
<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
  <!-- Modal Container -->
  <div class="bg-white rounded-lg max-w-md w-full p-6 shadow-xl">
    <!-- Modal Header -->
    <div class="flex items-center justify-between mb-4">
      <h3 class="text-xl font-bold text-gray-900">Modal Title</h3>
      <button class="text-gray-400 hover:text-gray-600">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>

    <!-- Modal Body -->
    <div class="mb-6">
      <p class="text-gray-600">
        This is the modal content. You can put any content here including forms, images, or text.
      </p>
    </div>

    <!-- Modal Footer -->
    <div class="flex gap-3 justify-end">
      <button class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
        Cancel
      </button>
      <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
        Confirm
      </button>
    </div>
  </div>
</div>
```

## Alert Modal

```html
<!-- Alert Modal Backdrop -->
<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
  <div class="bg-white rounded-lg max-w-sm w-full p-6 shadow-xl">
    <div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-red-100">
      <svg class="h-6 w-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
      </svg>
    </div>
    <div class="mt-4 text-center">
      <h3 class="text-lg font-medium text-gray-900 mb-2">Delete Item</h3>
      <p class="text-sm text-gray-500">
        Are you sure you want to delete this item? This action cannot be undone.
      </p>
    </div>
    <div class="mt-6 flex gap-3 justify-center">
      <button class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
        Cancel
      </button>
      <button class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors">
        Delete
      </button>
    </div>
  </div>
</div>
```

## Full Screen Modal

```html
<!-- Full Screen Modal Backdrop -->
<div class="fixed inset-0 bg-white z-50 flex flex-col">
  <!-- Modal Header -->
  <div class="border-b border-gray-200 px-6 py-4 flex items-center justify-between">
    <h3 class="text-lg font-medium text-gray-900">Full Screen Modal</h3>
    <button class="text-gray-400 hover:text-gray-600">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
      </svg>
    </button>
  </div>

  <!-- Modal Body -->
  <div class="flex-1 overflow-y-auto p-6">
    <p class="text-gray-600">
      This is a full screen modal. It takes up the entire viewport and is useful for displaying detailed content or complex forms.
    </p>

    <div class="mt-6 bg-gray-100 p-4 rounded-lg">
      <h4 class="font-medium text-gray-900 mb-2">Additional Content</h4>
      <p class="text-sm text-gray-600">
        You can add any kind of content inside a full screen modal, including forms, images, or detailed information.
      </p>
    </div>
  </div>

  <!-- Modal Footer -->
  <div class="border-t border-gray-200 px-6 py-4 flex justify-end gap-3">
    <button class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
      Close
    </button>
    <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
      Save Changes
    </button>
  </div>
</div>
```

## Form Modal

```html
<!-- Form Modal Backdrop -->
<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
  <div class="bg-white rounded-lg max-w-lg w-full shadow-xl">
    <!-- Modal Header -->
    <div class="border-b border-gray-200 px-6 py-4">
      <h3 class="text-lg font-medium text-gray-900">Create New Account</h3>
    </div>

    <!-- Modal Body -->
    <div class="p-6">
      <form class="space-y-4">
        <div>
          <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
          <input
            type="text"
            id="name"
            class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            placeholder="John Doe"
          />
        </div>

        <div>
          <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
          <input
            type="email"
            id="email"
            class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            placeholder="john@example.com"
          />
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password</label>
          <input
            type="password"
            id="password"
            class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            placeholder="••••••••"
          />
        </div>
      </form>
    </div>

    <!-- Modal Footer -->
    <div class="border-t border-gray-200 px-6 py-4 flex justify-end gap-3">
      <button class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
        Cancel
      </button>
      <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
        Create Account
      </button>
    </div>
  </div>
</div>
```

## Media Modal

```html
<!-- Media Modal Backdrop -->
<div class="fixed inset-0 bg-black bg-opacity-90 flex items-center justify-center z-50">
  <div class="max-w-4xl w-full">
    <!-- Media Modal Content -->
    <div class="relative">
      <img
        src="https://via.placeholder.com/800x600"
        alt="Modal Image"
        class="w-full h-auto max-h-[80vh] object-contain"
      />

      <button class="absolute top-4 right-4 bg-black bg-opacity-50 text-white rounded-full p-2 hover:bg-opacity-75">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>

      <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent p-6 text-white">
        <h3 class="text-xl font-medium">Image Caption</h3>
        <p class="text-sm opacity-80">Description of the image goes here</p>
      </div>
    </div>
  </div>
</div>
```

## Centered Modal with Animation

```html
<!-- Modal Backdrop with Fade Animation -->
<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
  <!-- Modal Container with Scale Animation -->
  <div class="bg-white rounded-lg max-w-md w-full p-6 shadow-xl transform transition-all duration-300 scale-95 opacity-0 animate-in fade-in-90 zoom-in-90">
    <div class="flex items-center justify-between mb-4">
      <h3 class="text-xl font-bold text-gray-900">Animated Modal</h3>
      <button class="text-gray-400 hover:text-gray-600">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>

    <div class="mb-6">
      <p class="text-gray-600">
        This modal includes entrance animations for a smoother user experience.
      </p>
    </div>

    <div class="flex gap-3 justify-end">
      <button class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
        Cancel
      </button>
      <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
        Confirm
      </button>
    </div>
  </div>
</div>
```