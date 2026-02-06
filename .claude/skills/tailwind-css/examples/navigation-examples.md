# Navigation Examples

Various navigation patterns using Tailwind CSS.

## Horizontal Navigation

```html
<nav class="flex justify-center space-x-4">
  <a href="/dashboard" class="font-medium px-3 py-2 text-slate-700 rounded-lg hover:bg-slate-100 hover:text-slate-900">
    Home
  </a>
  <a href="/team" class="font-medium px-3 py-2 text-slate-700 rounded-lg hover:bg-slate-100 hover:text-slate-900">
    Team
  </a>
  <a href="/projects" class="font-medium px-3 py-2 text-slate-700 rounded-lg hover:bg-slate-100 hover:text-slate-900">
    Projects
  </a>
  <a href="/reports" class="font-medium px-3 py-2 text-slate-700 rounded-lg hover:bg-slate-100 hover:text-slate-900">
    Reports
  </a>
</nav>
```

## Navigation Bar with Logo

```html
<nav class="bg-white shadow-sm">
  <div class="max-w-7xl mx-auto px-4">
    <div class="flex items-center justify-between h-16">
      <div class="flex items-center">
        <img class="h-8 w-8" src="/logo.svg" alt="Logo" />
        <span class="ml-2 text-xl font-bold">Brand</span>
      </div>
      <div class="hidden md:flex gap-6">
        <a href="#" class="text-gray-700 hover:text-blue-600 transition-colors">Home</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 transition-colors">About</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 transition-colors">Services</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 transition-colors">Contact</a>
      </div>
      <div>
        <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
          Sign In
        </button>
      </div>
    </div>
  </div>
</nav>
```

## Sidebar Navigation

```html
<aside class="w-64 bg-gray-800 text-white min-h-screen p-4">
  <div class="mb-8">
    <h2 class="text-2xl font-bold">Dashboard</h2>
  </div>
  <nav class="space-y-2">
    <a href="#" class="flex items-center px-4 py-3 rounded-lg bg-gray-700 hover:bg-gray-600 transition-colors">
      <span>Home</span>
    </a>
    <a href="#" class="flex items-center px-4 py-3 rounded-lg hover:bg-gray-700 transition-colors">
      <span>Analytics</span>
    </a>
    <a href="#" class="flex items-center px-4 py-3 rounded-lg hover:bg-gray-700 transition-colors">
      <span>Settings</span>
    </a>
    <a href="#" class="flex items-center px-4 py-3 rounded-lg hover:bg-gray-700 transition-colors">
      <span>Profile</span>
    </a>
  </nav>
</aside>
```

## Mobile Responsive Navigation

```html
<nav class="bg-white shadow-md">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex items-center">
        <div class="flex-shrink-0 flex items-center">
          <img class="h-8 w-auto" src="/logo.svg" alt="Logo" />
        </div>
        <div class="hidden md:ml-6 md:flex md:space-x-8">
          <a href="#" class="border-b-2 border-blue-500 text-gray-900 inline-flex items-center px-1 pt-1 text-sm font-medium">
            Dashboard
          </a>
          <a href="#" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 text-sm font-medium">
            Team
          </a>
          <a href="#" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 text-sm font-medium">
            Projects
          </a>
          <a href="#" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 text-sm font-medium">
            Calendar
          </a>
        </div>
      </div>
      <div class="flex items-center md:hidden">
        <button type="button" class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500" aria-controls="mobile-menu" aria-expanded="false">
          <span class="sr-only">Open main menu</span>
          <svg class="block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile menu -->
  <div class="md:hidden" id="mobile-menu">
    <div class="pt-2 pb-3 space-y-1">
      <a href="#" class="bg-blue-50 border-blue-500 text-blue-700 block pl-3 pr-4 py-2 border-l-4 text-base font-medium">
        Dashboard
      </a>
      <a href="#" class="border-transparent text-gray-500 hover:bg-gray-50 hover:border-gray-300 hover:text-gray-700 block pl-3 pr-4 py-2 border-l-4 text-base font-medium">
        Team
      </a>
      <a href="#" class="border-transparent text-gray-500 hover:bg-gray-50 hover:border-gray-300 hover:text-gray-700 block pl-3 pr-4 py-2 border-l-4 text-base font-medium">
        Projects
      </a>
      <a href="#" class="border-transparent text-gray-500 hover:bg-gray-50 hover:border-gray-300 hover:text-gray-700 block pl-3 pr-4 py-2 border-l-4 text-base font-medium">
        Calendar
      </a>
    </div>
  </div>
</nav>
```

## Breadcrumb Navigation

```html
<nav class="flex" aria-label="Breadcrumb">
  <ol class="inline-flex items-center space-x-1 md:space-x-3">
    <li class="inline-flex items-center">
      <a href="#" class="inline-flex items-center text-sm font-medium text-gray-700 hover:text-blue-600">
        <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path>
        </svg>
        Home
      </a>
    </li>
    <li>
      <div class="flex items-center">
        <svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
        </svg>
        <a href="#" class="ml-1 text-sm font-medium text-gray-700 hover:text-blue-600 md:ml-2">Projects</a>
      </div>
    </li>
    <li aria-current="page">
      <div class="flex items-center">
        <svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
        </svg>
        <span class="ml-1 text-sm font-medium text-gray-500 md:ml-2">Website redesign</span>
      </div>
    </li>
  </ol>
</nav>
```

## E-commerce Category Navigation

```html
<nav class="bg-gray-100 py-4">
  <div class="max-w-7xl mx-auto px-4">
    <div class="flex flex-wrap gap-4 justify-center">
      <a href="#" class="inline-flex items-center px-4 py-2 bg-white rounded-lg shadow-sm hover:bg-gray-50">
        <svg class="w-5 h-5 mr-2 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"></path>
        </svg>
        Electronics
      </a>
      <a href="#" class="inline-flex items-center px-4 py-2 bg-white rounded-lg shadow-sm hover:bg-gray-50">
        <svg class="w-5 h-5 mr-2 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
        </svg>
        Clothing
      </a>
      <a href="#" class="inline-flex items-center px-4 py-2 bg-white rounded-lg shadow-sm hover:bg-gray-50">
        <svg class="w-5 h-5 mr-2 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
        </svg>
        Bags
      </a>
      <a href="#" class="inline-flex items-center px-4 py-2 bg-white rounded-lg shadow-sm hover:bg-gray-50">
        <svg class="w-5 h-5 mr-2 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        Watches
      </a>
      <a href="#" class="inline-flex items-center px-4 py-2 bg-white rounded-lg shadow-sm hover:bg-gray-50">
        <svg class="w-5 h-5 mr-2 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path>
        </svg>
        Accessories
      </a>
    </div>
  </div>
</nav>
```

## Dashboard Navigation with Badges

```html
<aside class="bg-gray-800 text-white w-64 min-h-screen">
  <div class="p-4 border-b border-gray-700">
    <h2 class="text-xl font-bold">Dashboard</h2>
  </div>
  <nav class="p-4 space-y-2">
    <a href="#" class="flex items-center px-4 py-3 rounded-lg bg-blue-600 text-white">
      <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
      </svg>
      Dashboard
    </a>
    <a href="#" class="flex items-center px-4 py-3 rounded-lg hover:bg-gray-700">
      <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
      </svg>
      Users
      <span class="ml-auto bg-red-500 text-white text-xs font-medium px-2 py-1 rounded-full">12</span>
    </a>
    <a href="#" class="flex items-center px-4 py-3 rounded-lg hover:bg-gray-700">
      <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
      </svg>
      Orders
      <span class="ml-auto bg-blue-500 text-white text-xs font-medium px-2 py-1 rounded-full">3</span>
    </a>
    <a href="#" class="flex items-center px-4 py-3 rounded-lg hover:bg-gray-700">
      <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
      </svg>
      Analytics
    </a>
    <a href="#" class="flex items-center px-4 py-3 rounded-lg hover:bg-gray-700">
      <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
      </svg>
      Settings
    </a>
  </nav>
</aside>
```

## Sticky Navigation Bar

```html
<nav class="sticky top-0 z-50 bg-white shadow-md">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex items-center">
        <div class="flex-shrink-0 flex items-center">
          <img class="h-8 w-auto" src="/logo.svg" alt="Logo" />
        </div>
        <div class="hidden md:ml-6 md:flex md:space-x-8">
          <a href="#" class="border-b-2 border-blue-500 text-gray-900 inline-flex items-center px-1 pt-1 text-sm font-medium">
            Home
          </a>
          <a href="#" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 text-sm font-medium">
            Products
          </a>
          <a href="#" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 text-sm font-medium">
            Solutions
          </a>
          <a href="#" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 text-sm font-medium">
            Pricing
          </a>
        </div>
      </div>
      <div class="flex items-center">
        <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 text-sm font-medium">
          Get Started
        </button>
      </div>
    </div>
  </div>
</nav>
```

## Mega Menu Navigation

```html
<nav class="bg-white shadow-lg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex">
        <div class="flex-shrink-0 flex items-center">
          <img class="h-8 w-auto" src="/logo.svg" alt="Logo" />
        </div>
        <div class="hidden md:ml-6 md:flex md:space-x-8">
          <div class="relative group">
            <button class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 hover:text-blue-600">
              Products
              <svg class="ml-1 h-5 w-5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>

            <!-- Mega Menu -->
            <div class="absolute z-50 mt-2 w-screen max-w-4xl left-0 transform -translate-x-1/2">
              <div class="bg-white rounded-lg shadow-lg">
                <div class="grid grid-cols-4 gap-4 p-4">
                  <div>
                    <h3 class="text-sm font-medium text-gray-900 mb-2">Development</h3>
                    <ul class="space-y-2">
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">API Platform</a></li>
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">SDKs</a></li>
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">Documentation</a></li>
                    </ul>
                  </div>
                  <div>
                    <h3 class="text-sm font-medium text-gray-900 mb-2">Security</h3>
                    <ul class="space-y-2">
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">Authentication</a></li>
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">Encryption</a></li>
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">Compliance</a></li>
                    </ul>
                  </div>
                  <div>
                    <h3 class="text-sm font-medium text-gray-900 mb-2">Analytics</h3>
                    <ul class="space-y-2">
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">Real-time</a></li>
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">Reports</a></li>
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">Dashboard</a></li>
                    </ul>
                  </div>
                  <div>
                    <h3 class="text-sm font-medium text-gray-900 mb-2">Enterprise</h3>
                    <ul class="space-y-2">
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">SSO</a></li>
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">Audit Logs</a></li>
                      <li><a href="#" class="text-sm text-gray-500 hover:text-blue-600">Teams</a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <a href="#" class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 hover:text-blue-600">
            Solutions
          </a>
          <a href="#" class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 hover:text-blue-600">
            Pricing
          </a>
          <a href="#" class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 hover:text-blue-600">
            Resources
          </a>
        </div>
      </div>
      <div class="flex items-center">
        <a href="#" class="text-sm font-medium text-gray-500 hover:text-blue-600 mr-4">Sign in</a>
        <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 text-sm font-medium">
          Get Started
        </button>
      </div>
    </div>
  </div>
</nav>
```