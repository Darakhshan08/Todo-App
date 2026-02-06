# Form Examples

Complete form structures with various input types using Tailwind CSS.

## Basic Form

```html
<form class="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md space-y-4">
  <div>
    <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Name</label>
    <input
      type="text"
      id="name"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="Enter your name"
    />
  </div>

  <div>
    <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
    <input
      type="email"
      id="email"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="you@example.com"
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

  <div class="flex items-center">
    <input
      id="terms"
      type="checkbox"
      class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
    />
    <label for="terms" class="ml-2 block text-sm text-gray-900">
      I agree to the terms and conditions
    </label>
  </div>

  <div>
    <button
      type="submit"
      class="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
    >
      Submit
    </button>
  </div>
</form>
```

## Registration Form

```html
<form class="max-w-lg mx-auto bg-white p-8 rounded-lg shadow-md space-y-6">
  <h2 class="text-2xl font-bold text-gray-900 mb-6">Create Account</h2>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div>
      <label for="first-name" class="block text-sm font-medium text-gray-700 mb-1">First Name</label>
      <input
        type="text"
        id="first-name"
        class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        placeholder="John"
      />
    </div>

    <div>
      <label for="last-name" class="block text-sm font-medium text-gray-700 mb-1">Last Name</label>
      <input
        type="text"
        id="last-name"
        class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        placeholder="Doe"
      />
    </div>
  </div>

  <div>
    <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
    <input
      type="email"
      id="email"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="you@example.com"
    />
  </div>

  <div>
    <label for="phone" class="block text-sm font-medium text-gray-700 mb-1">Phone Number</label>
    <input
      type="tel"
      id="phone"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="(555) 123-4567"
    />
  </div>

  <div>
    <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password</label>
    <input
      type="password"
      id="password"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="At least 8 characters"
    />
  </div>

  <div>
    <label for="confirm-password" class="block text-sm font-medium text-gray-700 mb-1">Confirm Password</label>
    <input
      type="password"
      id="confirm-password"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="Re-enter your password"
    />
  </div>

  <div class="flex items-center">
    <input
      id="marketing"
      type="checkbox"
      class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
    />
    <label for="marketing" class="ml-2 block text-sm text-gray-900">
      I want to receive marketing emails
    </label>
  </div>

  <div>
    <button
      type="submit"
      class="w-full bg-blue-600 text-white py-3 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 font-medium"
    >
      Create Account
    </button>
  </div>
</form>
```

## Contact Form

```html
<form class="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-md space-y-6">
  <h2 class="text-2xl font-bold text-gray-900 mb-4">Contact Us</h2>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div>
      <label for="full-name" class="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
      <input
        type="text"
        id="full-name"
        class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        placeholder="Your name"
      />
    </div>

    <div>
      <label for="contact-email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
      <input
        type="email"
        id="contact-email"
        class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        placeholder="your.email@example.com"
      />
    </div>
  </div>

  <div>
    <label for="subject" class="block text-sm font-medium text-gray-700 mb-1">Subject</label>
    <input
      type="text"
      id="subject"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="What is this regarding?"
    />
  </div>

  <div>
    <label for="message" class="block text-sm font-medium text-gray-700 mb-1">Message</label>
    <textarea
      id="message"
      rows="5"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="Please describe your inquiry in detail..."
    ></textarea>
  </div>

  <div>
    <label for="attachment" class="block text-sm font-medium text-gray-700 mb-1">Attachments (Optional)</label>
    <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md">
      <div class="space-y-1 text-center">
        <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48">
          <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        <div class="flex text-sm text-gray-600">
          <label for="file-upload" class="relative cursor-pointer bg-white rounded-md font-medium text-blue-600 hover:text-blue-500">
            <span>Upload a file</span>
            <input id="file-upload" name="file-upload" type="file" class="sr-only" />
          </label>
          <p class="pl-1">or drag and drop</p>
        </div>
        <p class="text-xs text-gray-500">PDF, DOC, XLS up to 10MB</p>
      </div>
    </div>
  </div>

  <div>
    <button
      type="submit"
      class="w-full bg-blue-600 text-white py-3 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 font-medium"
    >
      Send Message
    </button>
  </div>
</form>
```

## Newsletter Subscription Form

```html
<div class="max-w-md mx-auto bg-gradient-to-r from-blue-500 to-purple-600 rounded-xl p-8 text-center">
  <h3 class="text-2xl font-bold text-white mb-2">Stay Updated</h3>
  <p class="text-blue-100 mb-6">Subscribe to our newsletter for the latest news and updates</p>

  <form class="space-y-4">
    <div>
      <input
        type="email"
        placeholder="Enter your email"
        class="w-full px-4 py-3 rounded-lg text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-white"
      />
    </div>

    <div class="flex items-center">
      <input
        id="privacy-policy"
        type="checkbox"
        class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
        required
      />
      <label for="privacy-policy" class="ml-2 block text-sm text-blue-100">
        I agree to the <a href="#" class="text-white underline">Privacy Policy</a>
      </label>
    </div>

    <button
      type="submit"
      class="w-full bg-white text-blue-600 py-3 px-4 rounded-lg font-semibold hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-white"
    >
      Subscribe Now
    </button>
  </form>
</div>
```

## E-commerce Product Review Form

```html
<form class="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-md space-y-6">
  <h2 class="text-2xl font-bold text-gray-900 mb-4">Leave a Review</h2>

  <div>
    <label class="block text-sm font-medium text-gray-700 mb-2">Rating</label>
    <div class="flex space-x-1">
      <button type="button" class="text-yellow-400 hover:text-yellow-500 focus:outline-none">
        <svg class="h-8 w-8 fill-current" viewBox="0 0 24 24">
          <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" />
        </svg>
      </button>
      <button type="button" class="text-yellow-400 hover:text-yellow-500 focus:outline-none">
        <svg class="h-8 w-8 fill-current" viewBox="0 0 24 24">
          <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" />
        </svg>
      </button>
      <button type="button" class="text-yellow-400 hover:text-yellow-500 focus:outline-none">
        <svg class="h-8 w-8 fill-current" viewBox="0 0 24 24">
          <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" />
        </svg>
      </button>
      <button type="button" class="text-yellow-400 hover:text-yellow-500 focus:outline-none">
        <svg class="h-8 w-8 fill-current" viewBox="0 0 24 24">
          <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" />
        </svg>
      </button>
      <button type="button" class="text-gray-300 hover:text-yellow-500 focus:outline-none">
        <svg class="h-8 w-8 fill-current" viewBox="0 0 24 24">
          <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" />
        </svg>
      </button>
    </div>
  </div>

  <div>
    <label for="review-title" class="block text-sm font-medium text-gray-700 mb-1">Review Title</label>
    <input
      type="text"
      id="review-title"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="Summarize your review in a few words"
    />
  </div>

  <div>
    <label for="review-body" class="block text-sm font-medium text-gray-700 mb-1">Review</label>
    <textarea
      id="review-body"
      rows="4"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="Share your detailed experience with this product..."
    ></textarea>
  </div>

  <div>
    <label class="block text-sm font-medium text-gray-700 mb-2">Would you recommend this product?</label>
    <div class="flex space-x-4">
      <label class="inline-flex items-center">
        <input type="radio" name="recommend" value="yes" class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500">
        <span class="ml-2 text-gray-700">Yes</span>
      </label>
      <label class="inline-flex items-center">
        <input type="radio" name="recommend" value="no" class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500">
        <span class="ml-2 text-gray-700">No</span>
      </label>
      <label class="inline-flex items-center">
        <input type="radio" name="recommend" value="maybe" class="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500">
        <span class="ml-2 text-gray-700">Maybe</span>
      </label>
    </div>
  </div>

  <div>
    <button
      type="submit"
      class="w-full bg-blue-600 text-white py-3 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 font-medium"
    >
      Submit Review
    </button>
  </div>
</form>
```

## Contact Form

```html
<form class="max-w-lg mx-auto bg-white p-8 rounded-lg shadow-md space-y-6">
  <h2 class="text-2xl font-bold text-gray-900 mb-4">Contact Us</h2>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div>
      <label for="first-name" class="block text-sm font-medium text-gray-700 mb-1">First Name</label>
      <input
        type="text"
        id="first-name"
        class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        placeholder="John"
      />
    </div>

    <div>
      <label for="last-name" class="block text-sm font-medium text-gray-700 mb-1">Last Name</label>
      <input
        type="text"
        id="last-name"
        class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        placeholder="Doe"
      />
    </div>
  </div>

  <div>
    <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
    <input
      type="email"
      id="email"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="you@example.com"
    />
  </div>

  <div>
    <label for="subject" class="block text-sm font-medium text-gray-700 mb-1">Subject</label>
    <input
      type="text"
      id="subject"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="Subject"
    />
  </div>

  <div>
    <label for="message" class="block text-sm font-medium text-gray-700 mb-1">Message</label>
    <textarea
      id="message"
      rows="4"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      placeholder="Your message here..."
    ></textarea>
  </div>

  <div>
    <button
      type="submit"
      class="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
    >
      Send Message
    </button>
  </div>
</form>
```

## Select and Checkbox Form

```html
<form class="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md space-y-4">
  <div>
    <label for="country" class="block text-sm font-medium text-gray-700 mb-1">Country</label>
    <select
      id="country"
      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
    >
      <option>United States</option>
      <option>Canada</option>
      <option>Mexico</option>
      <option>United Kingdom</option>
      <option>Germany</option>
    </select>
  </div>

  <div>
    <label class="block text-sm font-medium text-gray-700 mb-1">Preferences</label>
    <div class="space-y-2">
      <div class="flex items-center">
        <input
          id="email-notifications"
          type="checkbox"
          class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
        />
        <label for="email-notifications" class="ml-2 block text-sm text-gray-900">
          Email notifications
        </label>
      </div>

      <div class="flex items-center">
        <input
          id="sms-notifications"
          type="checkbox"
          class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
        />
        <label for="sms-notifications" class="ml-2 block text-sm text-gray-900">
          SMS notifications
        </label>
      </div>

      <div class="flex items-center">
        <input
          id="newsletter"
          type="checkbox"
          class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
        />
        <label for="newsletter" class="ml-2 block text-sm text-gray-900">
          Subscribe to newsletter
        </label>
      </div>
    </div>
  </div>

  <div>
    <button
      type="submit"
      class="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
    >
      Save Preferences
    </button>
  </div>
</form>
```