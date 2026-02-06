# Hero & Footer Examples

Hero and footer components using Tailwind CSS.

## Centered Hero with CTA

```html
<section class="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-20">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <h1 class="text-5xl md:text-6xl font-bold mb-6">
      Build Amazing Things
    </h1>
    <p class="text-xl md:text-2xl mb-8 text-blue-100">
      The modern way to build beautiful, responsive websites with Tailwind CSS
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors">
        Get Started
      </button>
      <button class="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-blue-600 transition-colors">
        Learn More
      </button>
    </div>
  </div>
</section>
```

## Hero with Image Background

```html
<section class="relative bg-cover bg-center bg-no-repeat" style="background-image: url('https://via.placeholder.com/1200x600');">
  <div class="absolute inset-0 bg-black bg-opacity-50"></div>
  <div class="relative max-w-7xl mx-auto px-4 py-32 text-center">
    <h1 class="text-4xl md:text-5xl font-bold text-white mb-6">
      Discover New Possibilities
    </h1>
    <p class="text-xl text-white mb-8 max-w-2xl mx-auto">
      Transform your ideas into reality with our powerful tools and resources.
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors">
        Start Free Trial
      </button>
      <button class="bg-transparent border-2 border-white text-white px-6 py-3 rounded-lg font-medium hover:bg-white hover:text-gray-900 transition-colors">
        View Demo
      </button>
    </div>
  </div>
</section>
```

## Split Hero Section

```html
<section class="py-20">
  <div class="max-w-7xl mx-auto px-4 flex flex-col md:flex-row items-center">
    <div class="md:w-1/2 mb-10 md:mb-0">
      <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
        The Future is Built with Code
      </h1>
      <p class="text-lg text-gray-600 mb-8">
        Build modern, responsive websites with our intuitive tools and frameworks. Focus on creativity while we handle the complexity.
      </p>
      <div class="flex flex-col sm:flex-row gap-4">
        <button class="bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors">
          Get Started
        </button>
        <button class="bg-gray-200 text-gray-800 px-6 py-3 rounded-lg font-medium hover:bg-gray-300 transition-colors">
          View Examples
        </button>
      </div>
    </div>
    <div class="md:w-1/2 flex justify-center">
      <img
        src="https://via.placeholder.com/600x400"
        alt="Hero Image"
        class="rounded-lg shadow-xl max-w-full h-auto"
      />
    </div>
  </div>
</section>
```

## Marketing Hero Section

```html
<section class="bg-gradient-to-br from-blue-50 to-indigo-100 py-16 md:py-24">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="lg:grid lg:grid-cols-12 lg:gap-8">
      <div class="sm:text-center md:max-w-2xl md:mx-auto lg:col-span-6 lg:text-left">
        <h1 class="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
          <span class="block">Transform Your Business</span>
          <span class="block text-blue-600">With Modern Solutions</span>
        </h1>
        <p class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
          Our platform helps businesses grow faster and reach more customers with innovative digital solutions tailored to your needs.
        </p>
        <div class="mt-8 sm:max-w-lg sm:mx-auto sm:text-center lg:text-left lg:mx-0">
          <div class="mt-5 sm:flex sm:justify-center lg:justify-start">
            <div class="rounded-md shadow">
              <a href="#" class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 md:py-4 md:text-lg md:px-10">
                Get started
              </a>
            </div>
            <div class="mt-3 rounded-md shadow sm:mt-0 sm:ml-3">
              <a href="#" class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-blue-600 bg-white hover:bg-gray-50 md:py-4 md:text-lg md:px-10">
                Live demo
              </a>
            </div>
          </div>
          <div class="mt-3 text-sm text-gray-500">
            Free 14-day trial • No credit card required
          </div>
        </div>
      </div>
      <div class="mt-12 relative sm:max-w-lg sm:mx-auto lg:mt-0 lg:max-w-none lg:mx-0 lg:col-span-6 lg:flex lg:items-center">
        <div class="relative mx-auto w-full rounded-lg shadow-lg lg:max-w-md">
          <div class="relative block w-full bg-white rounded-lg overflow-hidden">
            <div class="aspect-w-16 aspect-h-9 sm:aspect-none bg-gray-100 rounded-lg overflow-hidden">
              <img src="https://via.placeholder.com/600x400" alt="Dashboard preview" class="object-cover pointer-events-none">
              <div class="absolute inset-0 w-full h-full flex items-center justify-center">
                <svg class="h-20 w-20 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

## E-commerce Hero Section

```html
<section class="bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500 text-white py-16 md:py-24">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center">
      <h1 class="text-4xl font-extrabold tracking-tight sm:text-5xl md:text-6xl">
        Summer Sale is Live!
      </h1>
      <p class="mt-6 max-w-lg mx-auto text-xl text-pink-100">
        Up to 70% off on selected items. Limited time offer. Shop now before it's gone!
      </p>
      <div class="mt-10 max-w-sm mx-auto sm:max-w-none sm:flex sm:justify-center">
        <div class="space-y-4 sm:space-y-0 sm:mx-auto sm:inline-grid sm:grid-cols-2 sm:gap-5">
          <a href="#" class="flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-red-700 bg-white hover:bg-pink-50 md:py-4 md:text-lg md:px-10">
            Shop Sale
          </a>
          <a href="#" class="flex items-center justify-center px-8 py-3 border border-white text-base font-medium rounded-md text-white bg-transparent hover:bg-white hover:text-red-700 md:py-4 md:text-lg md:px-10">
            View Collection
          </a>
        </div>
      </div>
      <div class="mt-8 flex justify-center">
        <span class="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-black bg-opacity-30">
          Ends in: <span class="ml-1 font-bold">7 days</span>
        </span>
      </div>
    </div>
  </div>
</section>
```

## Simple Footer

```html
<footer class="bg-gray-900 text-white py-12">
  <div class="max-w-7xl mx-auto px-4">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
      <div>
        <h3 class="text-lg font-semibold mb-4">Company</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-400 hover:text-white">About</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Careers</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Press</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Blog</a></li>
        </ul>
      </div>
      <div>
        <h3 class="text-lg font-semibold mb-4">Resources</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-400 hover:text-white">Documentation</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Support</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Community</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Tutorials</a></li>
        </ul>
      </div>
      <div>
        <h3 class="text-lg font-semibold mb-4">Legal</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-400 hover:text-white">Privacy Policy</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Terms of Service</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Cookie Policy</a></li>
        </ul>
      </div>
      <div>
        <h3 class="text-lg font-semibold mb-4">Newsletter</h3>
        <p class="text-gray-400 mb-4">Subscribe to our newsletter</p>
        <div class="flex">
          <input
            type="email"
            placeholder="Your email"
            class="flex-1 px-4 py-2 rounded-l-lg text-gray-900"
          />
          <button class="bg-blue-600 px-4 py-2 rounded-r-lg hover:bg-blue-700">
            Subscribe
          </button>
        </div>
      </div>
    </div>
    <div class="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
      <p>&copy; 2024 Your Company. All rights reserved.</p>
    </div>
  </div>
</footer>
```

## Minimal Footer

```html
<footer class="bg-gray-100 py-8">
  <div class="max-w-7xl mx-auto px-4 text-center">
    <div class="mb-4">
      <a href="#" class="text-xl font-bold text-gray-900">Brand</a>
    </div>
    <nav class="mb-4">
      <ul class="flex flex-wrap justify-center gap-6">
        <li><a href="#" class="text-gray-600 hover:text-gray-900">Home</a></li>
        <li><a href="#" class="text-gray-600 hover:text-gray-900">Features</a></li>
        <li><a href="#" class="text-gray-600 hover:text-gray-900">Pricing</a></li>
        <li><a href="#" class="text-gray-600 hover:text-gray-900">Contact</a></li>
      </ul>
    </nav>
    <div class="flex justify-center space-x-4 mb-4">
      <a href="#" class="text-gray-600 hover:text-gray-900">
        <span class="sr-only">Twitter</span>
        <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
          <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/>
        </svg>
      </a>
      <a href="#" class="text-gray-600 hover:text-gray-900">
        <span class="sr-only">GitHub</span>
        <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
          <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/>
        </svg>
      </a>
    </div>
    <p class="text-gray-600 text-sm">
      &copy; 2024 Company Name. All rights reserved.
    </p>
  </div>
</footer>
```

## Footer with Social Links and App Downloads

```html
<footer class="bg-gray-900 text-white">
  <div class="max-w-7xl mx-auto px-4 py-12">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      <div>
        <h3 class="text-lg font-semibold mb-4">Company</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-400 hover:text-white">About Us</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Careers</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Contact</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Blog</a></li>
        </ul>
      </div>
      <div>
        <h3 class="text-lg font-semibold mb-4">Products</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-400 hover:text-white">Features</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Pricing</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Integrations</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Roadmap</a></li>
        </ul>
      </div>
      <div>
        <h3 class="text-lg font-semibold mb-4">Support</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-400 hover:text-white">Help Center</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Community</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Status</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Feedback</a></li>
        </ul>
      </div>
      <div>
        <h3 class="text-lg font-semibold mb-4">Download App</h3>
        <div class="space-y-3">
          <a href="#" class="block">
            <img src="https://placehold.co/150x40?text=App+Store" alt="Download on the App Store" class="h-10">
          </a>
          <a href="#" class="block">
            <img src="https://placehold.co/150x40?text=Google+Play" alt="Get it on Google Play" class="h-10">
          </a>
        </div>
      </div>
    </div>
  </div>
  <div class="border-t border-gray-800 py-6">
    <div class="max-w-7xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
      <div class="mb-4 md:mb-0">
        <p class="text-gray-400">&copy; 2024 Your Company. All rights reserved.</p>
      </div>
      <div class="flex space-x-6">
        <a href="#" class="text-gray-400 hover:text-white">
          <span class="sr-only">Facebook</span>
          <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
            <path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd"/>
          </svg>
        </a>
        <a href="#" class="text-gray-400 hover:text-white">
          <span class="sr-only">Instagram</span>
          <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
            <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd"/>
          </svg>
        </a>
        <a href="#" class="text-gray-400 hover:text-white">
          <span class="sr-only">Twitter</span>
          <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/>
          </svg>
        </a>
      </div>
    </div>
  </div>
</footer>
```

## E-commerce Footer

```html
<footer class="bg-white border-t border-gray-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-8 py-12">
      <div class="col-span-2">
        <h3 class="text-sm font-semibold text-gray-900 tracking-wider uppercase mb-4">Shop Categories</h3>
        <div class="grid grid-cols-2 gap-4">
          <ul class="space-y-2">
            <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Electronics</a></li>
            <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Clothing</a></li>
            <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Home & Garden</a></li>
            <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Beauty</a></li>
          </ul>
          <ul class="space-y-2">
            <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Sports</a></li>
            <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Books</a></li>
            <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Toys</a></li>
            <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Automotive</a></li>
          </ul>
        </div>
      </div>

      <div>
        <h3 class="text-sm font-semibold text-gray-900 tracking-wider uppercase mb-4">Customer Service</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Contact Us</a></li>
          <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Shipping Policy</a></li>
          <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Returns & Exchanges</a></li>
          <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">FAQ</a></li>
        </ul>
      </div>

      <div>
        <h3 class="text-sm font-semibold text-gray-900 tracking-wider uppercase mb-4">About Us</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Our Story</a></li>
          <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Careers</a></li>
          <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Press</a></li>
          <li><a href="#" class="text-base text-gray-500 hover:text-gray-900">Sustainability</a></li>
        </ul>
      </div>
    </div>

    <div class="border-t border-gray-200 pt-8 pb-4">
      <div class="flex flex-col md:flex-row justify-between items-center">
        <div class="mb-4 md:mb-0">
          <p class="text-base text-gray-400">&copy; 2024 Shop Name. All rights reserved.</p>
        </div>

        <div class="flex space-x-6">
          <a href="#" class="text-gray-400 hover:text-gray-500">
            <span class="sr-only">Facebook</span>
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd"/>
            </svg>
          </a>
          <a href="#" class="text-gray-400 hover:text-gray-500">
            <span class="sr-only">Instagram</span>
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd"/>
            </svg>
          </a>
          <a href="#" class="text-gray-400 hover:text-gray-500">
            <span class="sr-only">Twitter</span>
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/>
            </svg>
          </a>
          <a href="#" class="text-gray-400 hover:text-gray-500">
            <span class="sr-only">YouTube</span>
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path fill-rule="evenodd" d="M19.812 5.418c.861.23 1.538.907 1.768 1.768C21.998 8.746 22 12 22 12s0 3.255-.418 4.814a2.504 2.504 0 0 1-1.768 1.768c-1.56.419-7.814.419-7.814.419s-6.255 0-7.814-.419a2.505 2.505 0 0 1-1.768-1.768C2 15.255 2 12 2 12s0-3.255.417-4.814a2.507 2.507 0 0 1 1.768-1.768C5.744 5 11.998 5 11.998 5s6.255 0 7.814.418ZM15.194 12 10 15V9l5.194 3Z" clip-rule="evenodd"/>
            </svg>
          </a>
        </div>
      </div>

      <div class="mt-8 flex justify-center space-x-8">
        <div class="flex items-center">
          <svg class="h-6 w-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
          </svg>
          <span class="ml-2 text-sm text-gray-500">Secure Checkout</span>
        </div>
        <div class="flex items-center">
          <svg class="h-6 w-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path>
          </svg>
          <span class="ml-2 text-sm text-gray-500">Free Shipping</span>
        </div>
        <div class="flex items-center">
          <svg class="h-6 w-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
          </svg>
          <span class="ml-2 text-sm text-gray-500">Easy Returns</span>
        </div>
      </div>
    </div>
  </div>
</footer>
```

## Business Footer with Newsletter Signup

```html
<footer class="bg-gray-800 text-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      <div>
        <h3 class="text-lg font-semibold mb-4">Company</h3>
        <p class="text-gray-400 mb-4">
          Building innovative solutions for businesses worldwide since 2010. Our mission is to empower companies with cutting-edge technology.
        </p>
        <div class="flex space-x-4">
          <a href="#" class="text-gray-400 hover:text-white">
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-1.098-.957-2.694-1.343-4.032-1.343-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
            </svg>
          </a>
          <a href="#" class="text-gray-400 hover:text-white">
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
            </svg>
          </a>
          <a href="#" class="text-gray-400 hover:text-white">
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
            </svg>
          </a>
        </div>
      </div>

      <div>
        <h3 class="text-lg font-semibold mb-4">Quick Links</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-400 hover:text-white">Home</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">About Us</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Services</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Portfolio</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Contact</a></li>
        </ul>
      </div>

      <div>
        <h3 class="text-lg font-semibold mb-4">Services</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-400 hover:text-white">Web Development</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Mobile Apps</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">UI/UX Design</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Cloud Solutions</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Consulting</a></li>
        </ul>
      </div>

      <div>
        <h3 class="text-lg font-semibold mb-4">Newsletter</h3>
        <p class="text-gray-400 mb-4">Subscribe to our newsletter for the latest updates and offers.</p>
        <form class="space-y-2">
          <div>
            <input
              type="email"
              placeholder="Your email address"
              class="w-full px-4 py-2 rounded-md text-gray-900"
            />
          </div>
          <button
            type="submit"
            class="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition-colors"
          >
            Subscribe
          </button>
        </form>
      </div>
    </div>
  </div>

  <div class="border-t border-gray-700 py-6">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <p class="text-center text-gray-400">&copy; 2024 Company Name. All rights reserved.</p>
    </div>
  </div>
</footer>
```

## Blog Footer

```html
<footer class="bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      <div>
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Latest Posts</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-600 hover:text-gray-900">Getting Started with React</a></li>
          <li><a href="#" class="text-gray-600 hover:text-gray-900">CSS Grid vs Flexbox</a></li>
          <li><a href="#" class="text-gray-600 hover:text-gray-900">JavaScript ES6 Features</a></li>
          <li><a href="#" class="text-gray-600 hover:text-gray-900">Building APIs with Node.js</a></li>
        </ul>
      </div>

      <div>
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Categories</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-600 hover:text-gray-900">Web Development</a></li>
          <li><a href="#" class="text-gray-600 hover:text-gray-900">Mobile Development</a></li>
          <li><a href="#" class="text-gray-600 hover:text-gray-900">Design & UX</a></li>
          <li><a href="#" class="text-gray-600 hover:text-gray-900">Career Advice</a></li>
        </ul>
      </div>

      <div>
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Social Media</h3>
        <ul class="space-y-2">
          <li><a href="#" class="text-gray-600 hover:text-gray-900">Twitter</a></li>
          <li><a href="#" class="text-gray-600 hover:text-gray-900">LinkedIn</a></li>
          <li><a href="#" class="text-gray-600 hover:text-gray-900">GitHub</a></li>
          <li><a href="#" class="text-gray-600 hover:text-gray-900">Instagram</a></li>
        </ul>
      </div>

      <div>
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Subscribe</h3>
        <p class="text-gray-600 mb-4">Get the latest posts delivered straight to your inbox.</p>
        <form class="space-y-2">
          <input
            type="email"
            placeholder="Your email"
            class="w-full px-4 py-2 border border-gray-300 rounded-md"
          />
          <button
            type="submit"
            class="w-full bg-gray-900 text-white py-2 rounded-md hover:bg-gray-800 transition-colors"
          >
            Subscribe
          </button>
        </form>
      </div>
    </div>
  </div>

  <div class="border-t border-gray-200 py-6">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row justify-between items-center">
        <div class="text-gray-600">© 2024 Tech Blog. All rights reserved.</div>
        <div class="mt-4 md:mt-0 flex space-x-6">
          <a href="#" class="text-gray-400 hover:text-gray-500">Privacy Policy</a>
          <a href="#" class="text-gray-400 hover:text-gray-500">Terms of Service</a>
          <a href="#" class="text-gray-400 hover:text-gray-500">Contact</a>
        </div>
      </div>
    </div>
  </div>
</footer>
```

## Agency Footer

```html
<footer class="bg-gradient-to-r from-blue-900 to-indigo-900 text-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8">
      <div class="lg:col-span-2">
        <h3 class="text-xl font-bold mb-4">Agency Name</h3>
        <p class="text-blue-200 mb-4">
          We create digital experiences that help businesses grow and connect with their audience in meaningful ways.
        </p>
        <div class="flex space-x-4">
          <a href="#" class="text-blue-200 hover:text-white">
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-1.098-.957-2.694-1.343-4.032-1.343-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
            </svg>
          </a>
          <a href="#" class="text-blue-200 hover:text-white">
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M22.46 6c-.77.35-1.6.58-2.46.69.88-.53 1.56-1.37 1.88-2.38-.83.5-1.75.85-2.72 1.05C18.37 4.5 17.26 4 16 4c-2.35 0-4.27 1.92-4.27 4.29 0 .34.04.67.11.98C8.28 9.09 5.11 7.38 3 4.79c-.37.63-.58 1.37-.58 2.15 0 1.49.75 2.81 1.91 3.56-.71 0-1.37-.2-1.95-.5v.03c0 2.08 1.48 3.82 3.44 4.21a4.22 4.22 0 0 1-1.93.07 4.28 4.28 0 0 0 4 2.98 8.521 8.521 0 0 1-5.33 1.84c-.34 0-.68-.02-1.02-.06C3.44 20.29 5.7 21 8.12 21 16 21 20.33 14.46 20.33 8.79c0-.19 0-.37-.01-.56.84-.6 1.56-1.36 2.14-2.23z"/>
            </svg>
          </a>
          <a href="#" class="text-blue-200 hover:text-white">
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a.755.755 0 1 1 1.066-.016a.755.755 0 0 1-1.066.016zm-1.98 9.184h1.337V9H3.357v7.217zm1.926-8.16a1.2 1.2 0 1 1-1.2 1.2a1.2 1.2 0 0 1 1.2-1.2z"/>
            </svg>
          </a>
        </div>
      </div>

      <div>
        <h4 class="text-lg font-semibold mb-4">Services</h4>
        <ul class="space-y-2">
          <li><a href="#" class="text-blue-200 hover:text-white">Web Design</a></li>
          <li><a href="#" class="text-blue-200 hover:text-white">Development</a></li>
          <li><a href="#" class="text-blue-200 hover:text-white">Branding</a></li>
          <li><a href="#" class="text-blue-200 hover:text-white">SEO</a></li>
        </ul>
      </div>

      <div>
        <h4 class="text-lg font-semibold mb-4">Company</h4>
        <ul class="space-y-2">
          <li><a href="#" class="text-blue-200 hover:text-white">About</a></li>
          <li><a href="#" class="text-blue-200 hover:text-white">Team</a></li>
          <li><a href="#" class="text-blue-200 hover:text-white">Careers</a></li>
          <li><a href="#" class="text-blue-200 hover:text-white">Contact</a></li>
        </ul>
      </div>

      <div>
        <h4 class="text-lg font-semibold mb-4">Contact</h4>
        <address class="not-italic text-blue-200">
          <p class="mb-2">123 Business Street</p>
          <p class="mb-2">New York, NY 10001</p>
          <p class="mb-2">hello@agency.com</p>
          <p>(123) 456-7890</p>
        </address>
      </div>
    </div>
  </div>

  <div class="border-t border-blue-800 py-6">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row justify-between items-center">
        <p class="text-blue-200">© 2024 Agency Name. All rights reserved.</p>
        <div class="mt-4 md:mt-0">
          <a href="#" class="text-blue-200 hover:text-white mx-3">Privacy Policy</a>
          <a href="#" class="text-blue-200 hover:text-white mx-3">Terms</a>
          <a href="#" class="text-blue-200 hover:text-white mx-3">Sitemap</a>
        </div>
      </div>
    </div>
  </div>
</footer>
```