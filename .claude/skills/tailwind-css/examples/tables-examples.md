# Table Examples

Table components using Tailwind CSS.

## Basic Table

```html
<div class="overflow-x-auto">
  <table class="min-w-full bg-white">
    <thead class="bg-gray-100">
      <tr>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Name</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Email</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Role</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Status</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr class="hover:bg-gray-50">
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="text-sm font-medium text-gray-900">John Doe</div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="text-sm text-gray-500">john@example.com</div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="text-sm text-gray-500">Admin</div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
            Active
          </span>
        </td>
      </tr>
      <tr class="hover:bg-gray-50">
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="text-sm font-medium text-gray-900">Jane Smith</div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="text-sm text-gray-500">jane@example.com</div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="text-sm text-gray-500">User</div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
            Active
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

## Striped Table

```html
<div class="overflow-x-auto">
  <table class="min-w-full bg-white">
    <thead class="bg-gray-100">
      <tr>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">ID</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Product</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Price</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Stock</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr class="bg-white">
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">#001</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">Wireless Headphones</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">$99.99</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
            In Stock
          </span>
        </td>
      </tr>
      <tr class="bg-gray-50">
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">#002</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">Smart Watch</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">$199.99</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
            Low Stock
          </span>
        </td>
      </tr>
      <tr class="bg-white">
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">#003</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">Phone Charger</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">$19.99</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
            Out of Stock
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

## Responsive Table

```html
<div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
  <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
    <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-100">
          <tr>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
              Name
            </th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
              Title
            </th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
              Email
            </th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
              Role
            </th>
            <th scope="col" class="relative px-6 py-3">
              <span class="sr-only">Edit</span>
            </th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="flex items-center">
                <div class="flex-shrink-0 h-10 w-10">
                  <img class="h-10 w-10 rounded-full" src="https://via.placeholder.com/40x40" alt="">
                </div>
                <div class="ml-4">
                  <div class="text-sm font-medium text-gray-900">Jane Cooper</div>
                  <div class="text-sm text-gray-500">Regional Paradigm Technician</div>
                </div>
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">Paradigm Representative</div>
              <div class="text-sm text-gray-500">Optimization</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
              jane.cooper@example.com
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
              Admin
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <a href="#" class="text-blue-600 hover:text-blue-900">Edit</a>
            </td>
          </tr>
          <tr>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="flex items-center">
                <div class="flex-shrink-0 h-10 w-10">
                  <img class="h-10 w-10 rounded-full" src="https://via.placeholder.com/40x40" alt="">
                </div>
                <div class="ml-4">
                  <div class="text-sm font-medium text-gray-900">John Doe</div>
                  <div class="text-sm text-gray-500">Dynamic Assurance Specialist</div>
                </div>
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">Forward Metrics Orchestrator</div>
              <div class="text-sm text-gray-500">Implementation</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
              john.doe@example.com
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
              Owner
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <a href="#" class="text-blue-600 hover:text-blue-900">Edit</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
```

## Sortable Table Headers

```html
<div class="overflow-x-auto">
  <table class="min-w-full bg-white">
    <thead class="bg-gray-100">
      <tr>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
          <div class="flex items-center">
            Name
            <button class="ml-1">
              <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4h13M3 8h9m-9 4h9m5-4v12m0 0l-4-4m4 4l4-4"></path>
              </svg>
            </button>
          </div>
        </th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
          <div class="flex items-center">
            Email
            <button class="ml-1">
              <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4h13M3 8h9m-9 4h9m5-4v12m0 0l-4-4m4 4l4-4"></path>
              </svg>
            </button>
          </div>
        </th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
          <div class="flex items-center">
            Status
            <button class="ml-1">
              <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4h13M3 8h9m-9 4h9m5-4v12m0 0l-4-4m4 4l4-4"></path>
              </svg>
            </button>
          </div>
        </th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">John Smith</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">john@example.com</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
            Active
          </span>
        </td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">Sarah Johnson</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">sarah@example.com</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
            Inactive
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

## E-commerce Order Table

```html
<div class="overflow-x-auto">
  <table class="min-w-full bg-white">
    <thead class="bg-gray-50">
      <tr>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Order</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Customer</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Amount</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">#12345</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">John Smith</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Jan 12, 2024</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">$249.99</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
            Paid
          </span>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
          <a href="#" class="text-blue-600 hover:text-blue-900 mr-3">View</a>
          <a href="#" class="text-gray-600 hover:text-gray-900">Invoice</a>
        </td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">#12344</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Jane Doe</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Jan 11, 2024</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">$129.99</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
            Pending
          </span>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
          <a href="#" class="text-blue-600 hover:text-blue-900 mr-3">View</a>
          <a href="#" class="text-gray-600 hover:text-gray-900">Invoice</a>
        </td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">#12343</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Bob Johnson</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Jan 10, 2024</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">$89.99</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
            Cancelled
          </span>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
          <a href="#" class="text-blue-600 hover:text-blue-900 mr-3">View</a>
          <a href="#" class="text-gray-600 hover:text-gray-900">Invoice</a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

## Financial Data Table

```html
<div class="overflow-x-auto">
  <table class="min-w-full bg-white">
    <thead class="bg-gray-50">
      <tr>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Symbol</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Change</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">% Change</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Volume</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">AAPL</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Apple Inc.</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">$182.52</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-green-600">+1.24</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-green-600">+0.68%</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">45.2M</td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">MSFT</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Microsoft Corp.</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">$340.54</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-green-600">+2.15</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-green-600">+0.64%</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">28.7M</td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">GOOGL</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Alphabet Inc.</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">$138.21</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-red-600">-0.87</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-red-600">-0.63%</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">22.1M</td>
      </tr>
    </tbody>
  </table>
</div>
```

## User Management Table

```html
<div class="overflow-x-auto">
  <table class="min-w-full bg-white">
    <thead class="bg-gray-50">
      <tr>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">User</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Role</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Last Active</th>
        <th scope="col" class="relative px-6 py-3">
          <span class="sr-only">Actions</span>
        </th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="flex items-center">
            <div class="flex-shrink-0 h-10 w-10">
              <img class="h-10 w-10 rounded-full" src="https://via.placeholder.com/40x40" alt="">
            </div>
            <div class="ml-4">
              <div class="text-sm font-medium text-gray-900">Jane Cooper</div>
              <div class="text-sm text-gray-500">jane.cooper@example.com</div>
            </div>
          </div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          Admin
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
            Active
          </span>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          2 hours ago
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
          <a href="#" class="text-blue-600 hover:text-blue-900 mr-3">Edit</a>
          <a href="#" class="text-red-600 hover:text-red-900">Deactivate</a>
        </td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="flex items-center">
            <div class="flex-shrink-0 h-10 w-10">
              <img class="h-10 w-10 rounded-full" src="https://via.placeholder.com/40x40" alt="">
            </div>
            <div class="ml-4">
              <div class="text-sm font-medium text-gray-900">John Doe</div>
              <div class="text-sm text-gray-500">john.doe@example.com</div>
            </div>
          </div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          Editor
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
            Pending
          </span>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          1 day ago
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
          <a href="#" class="text-blue-600 hover:text-blue-900 mr-3">Edit</a>
          <a href="#" class="text-green-600 hover:text-green-900">Activate</a>
        </td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="flex items-center">
            <div class="flex-shrink-0 h-10 w-10">
              <img class="h-10 w-10 rounded-full" src="https://via.placeholder.com/40x40" alt="">
            </div>
            <div class="ml-4">
              <div class="text-sm font-medium text-gray-900">Alice Smith</div>
              <div class="text-sm text-gray-500">alice.smith@example.com</div>
            </div>
          </div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          Viewer
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
            Deactivated
          </span>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          2 weeks ago
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
          <a href="#" class="text-blue-600 hover:text-blue-900 mr-3">Edit</a>
          <a href="#" class="text-green-600 hover:text-green-900">Reactivate</a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

## Inventory Tracking Table

```html
<div class="overflow-x-auto">
  <table class="min-w-full bg-white">
    <thead class="bg-gray-50">
      <tr>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">SKU</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Product</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Category</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Stock</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">WHP-001</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">Wireless Headphones Pro</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Electronics</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">$129.99</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">42</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
            In Stock
          </span>
        </td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">SMW-002</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">Smart Watch Series 5</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Wearables</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">$249.99</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">5</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
            Low Stock
          </span>
        </td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">PCH-003</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">USB-C Phone Charger</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Accessories</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">$24.99</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">0</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
            Out of Stock
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

## Interactive Table with Actions

```html
<div class="overflow-x-auto">
  <table class="min-w-full bg-white">
    <thead class="bg-gray-50">
      <tr>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
          <input type="checkbox" class="h-4 w-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500">
        </th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Project</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Manager</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Progress</th>
        <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
        <th scope="col" class="relative px-6 py-3">
          <span class="sr-only">Actions</span>
        </th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="px-6 py-4 whitespace-nowrap">
          <input type="checkbox" class="h-4 w-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500">
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Website Redesign</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">John Smith</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="w-full bg-gray-200 rounded-full h-2.5">
            <div class="bg-blue-600 h-2.5 rounded-full" style="width: 75%"></div>
          </div>
          <div class="text-xs text-gray-500 mt-1">75%</div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
            In Progress
          </span>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
          <a href="#" class="text-blue-600 hover:text-blue-900 mr-3">View</a>
          <a href="#" class="text-gray-600 hover:text-gray-900">Edit</a>
        </td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap">
          <input type="checkbox" class="h-4 w-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500">
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Mobile App Development</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Jane Doe</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="w-full bg-gray-200 rounded-full h-2.5">
            <div class="bg-yellow-500 h-2.5 rounded-full" style="width: 45%"></div>
          </div>
          <div class="text-xs text-gray-500 mt-1">45%</div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
            Behind Schedule
          </span>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
          <a href="#" class="text-blue-600 hover:text-blue-900 mr-3">View</a>
          <a href="#" class="text-gray-600 hover:text-gray-900">Edit</a>
        </td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap">
          <input type="checkbox" class="h-4 w-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500">
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Marketing Campaign</td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Bob Johnson</td>
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="w-full bg-gray-200 rounded-full h-2.5">
            <div class="bg-green-600 h-2.5 rounded-full" style="width: 100%"></div>
          </div>
          <div class="text-xs text-gray-500 mt-1">Completed</div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap">
          <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
            Completed
          </span>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
          <a href="#" class="text-blue-600 hover:text-blue-900 mr-3">View</a>
          <a href="#" class="text-gray-600 hover:text-gray-900">Edit</a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```