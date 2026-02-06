---
name: react-components
description: Generate reusable React components in Next.js with TypeScript. Creates functional components with proper props typing, hooks (useState, useEffect), and composition patterns. Use when building React components for Next.js App Router.
---

# React Components for Next.js

This skill helps you create reusable, well-typed React components in Next.js projects with TypeScript and App Router patterns.

## Overview

Modern React development focuses on functional components with hooks, strong TypeScript typing, and composition over inheritance. In Next.js App Router, components are Server Components by default, with Client Components used only when needed for interactivity.

## Prerequisites

- Next.js project with App Router
- TypeScript enabled
- React 18+

## Component Fundamentals

### Basic Functional Component

```typescript
export default function Welcome() {
  return <h1>Hello, World!</h1>
}
```

### Component with Props (Interface)

```typescript
interface MyButtonProps {
  /** The text to display inside the button */
  title: string
  /** Whether the button can be interacted with */
  disabled: boolean
}

function MyButton({ title, disabled }: MyButtonProps) {
  return <button disabled={disabled}>{title}</button>
}

export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton title="Click me" disabled={false} />
      <MyButton title="I'm disabled" disabled={true} />
    </div>
  )
}
```

### Component with Optional Props

```typescript
interface CardProps {
  title: string
  description?: string // Optional
  children: React.ReactNode
  onClick?: () => void // Optional function
}

export function Card({ title, description, children, onClick }: CardProps) {
  return (
    <div className="card" onClick={onClick}>
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      <div>{children}</div>
    </div>
  )
}
```

## Server vs Client Components

### Server Component (Default)

Server Components render on the server and send HTML to the client. Use for:
- Data fetching
- Accessing backend resources
- Keeping sensitive information on server
- Large dependencies that don't need client-side JavaScript

```typescript
// app/blog/page.tsx
// Server Component by default - no "use client" directive

interface Post {
  id: number
  title: string
  content: string
}

async function getPosts(): Promise<Post[]> {
  const res = await fetch('https://api.example.com/posts')
  return res.json()
}

export default async function BlogPage() {
  const posts = await getPosts()

  return (
    <div>
      <h1>Blog Posts</h1>
      {posts.map((post) => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
        </article>
      ))}
    </div>
  )
}
```

### Client Component

Client Components render on the client and require the `"use client"` directive. Use for:
- Interactive elements (onClick, onChange)
- State management (useState, useReducer)
- Effects (useEffect)
- Browser APIs (localStorage, window)
- Custom hooks

```typescript
"use client"

import { useState } from 'react'

interface CounterProps {
  initialValue?: number
}

export default function Counter({ initialValue = 0 }: CounterProps) {
  const [count, setCount] = useState(initialValue)

  const increment = () => setCount(count + 1)
  const decrement = () => setCount(count - 1)

  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={increment}>+1</button>
      <button onClick={decrement}>-1</button>
    </div>
  )
}
```

## React Hooks

### useState - State Management

```typescript
"use client"

import { useState } from 'react'

export default function Form() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)

    try {
      await fetch('/api/submit', {
        method: 'POST',
        body: JSON.stringify({ name, email }),
      })
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Name"
      />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Submitting...' : 'Submit'}
      </button>
    </form>
  )
}
```

### useEffect - Side Effects

```typescript
"use client"

import { useState, useEffect } from 'react'

export default function Timer() {
  const [seconds, setSeconds] = useState(0)

  useEffect(() => {
    // Setup: Start interval
    const intervalId = setInterval(() => {
      setSeconds((s) => s + 1)
    }, 1000)

    // Cleanup: Clear interval when component unmounts
    return () => clearInterval(intervalId)
  }, []) // Empty array = run once on mount

  return <h1>Seconds elapsed: {seconds}</h1>
}
```

### useEffect with Dependencies

```typescript
"use client"

import { useState, useEffect } from 'react'

interface ChatRoomProps {
  roomId: string
}

export default function ChatRoom({ roomId }: ChatRoomProps) {
  const [serverUrl, setServerUrl] = useState('https://localhost:1234')
  const [isConnected, setIsConnected] = useState(false)

  useEffect(() => {
    // Connect when roomId or serverUrl changes
    setIsConnected(true)
    console.log(`Connecting to ${roomId} at ${serverUrl}`)

    // Cleanup on unmount or before next effect
    return () => {
      setIsConnected(false)
      console.log(`Disconnecting from ${roomId}`)
    }
  }, [roomId, serverUrl]) // Re-run when these change

  return (
    <div>
      <label>
        Server URL:{' '}
        <input
          value={serverUrl}
          onChange={(e) => setServerUrl(e.target.value)}
        />
      </label>
      <h1>Welcome to {roomId}!</h1>
      <p>Status: {isConnected ? 'Connected' : 'Disconnected'}</p>
    </div>
  )
}
```

## Custom Hooks

Extract reusable logic into custom hooks. Hooks must start with "use" and can call other hooks.

### Simple Custom Hook

```typescript
"use client"

import { useState, useEffect } from 'react'

// Custom hook for window size
function useWindowSize() {
  const [size, setSize] = useState({ width: 0, height: 0 })

  useEffect(() => {
    function handleResize() {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight,
      })
    }

    handleResize() // Set initial size
    window.addEventListener('resize', handleResize)
    return () => window.removeEventListener('resize', handleResize)
  }, [])

  return size
}

// Usage
export default function Component() {
  const { width, height } = useWindowSize()

  return (
    <div>
      Window size: {width} x {height}
    </div>
  )
}
```

### Custom Hook with Parameters

```typescript
"use client"

import { useState, useEffect } from 'react'

// Custom hook for data fetching
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    let cancelled = false

    async function fetchData() {
      try {
        setLoading(true)
        const response = await fetch(url)
        const json = await response.json()

        if (!cancelled) {
          setData(json)
          setError(null)
        }
      } catch (err) {
        if (!cancelled) {
          setError(err as Error)
        }
      } finally {
        if (!cancelled) {
          setLoading(false)
        }
      }
    }

    fetchData()

    return () => {
      cancelled = true
    }
  }, [url])

  return { data, loading, error }
}

// Usage
interface User {
  id: number
  name: string
  email: string
}

export default function UserProfile({ userId }: { userId: number }) {
  const { data: user, loading, error } = useFetch<User>(
    `/api/users/${userId}`
  )

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>
  if (!user) return <div>No user found</div>

  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  )
}
```

### Reusable List Selection Hook

```typescript
"use client"

import { useState } from 'react'

// Custom hook for list item selection
function useList<T>(items: T[]) {
  const [selectedIndex, setSelectedIndex] = useState(0)

  function onNext() {
    setSelectedIndex((i) => (i + 1) % items.length)
  }

  function onPrevious() {
    setSelectedIndex((i) => (i - 1 + items.length) % items.length)
  }

  const selected = items[selectedIndex]

  return { selected, onNext, onPrevious, selectedIndex }
}

// Usage
interface Product {
  id: number
  name: string
  price: number
}

export default function ProductCarousel({ products }: { products: Product[] }) {
  const { selected, onNext, onPrevious } = useList(products)

  return (
    <div>
      <h2>{selected.name}</h2>
      <p>${selected.price}</p>
      <button onClick={onPrevious}>Previous</button>
      <button onClick={onNext}>Next</button>
    </div>
  )
}
```

## Component Composition

### Children Prop

```typescript
interface ContainerProps {
  children: React.ReactNode
}

export function Container({ children }: ContainerProps) {
  return (
    <div className="max-w-7xl mx-auto px-4">
      {children}
    </div>
  )
}

// Usage
<Container>
  <h1>Title</h1>
  <p>Content goes here</p>
</Container>
```

### Render Props Pattern

```typescript
interface DataProviderProps<T> {
  data: T[]
  render: (item: T, index: number) => React.ReactNode
}

export function DataProvider<T>({ data, render }: DataProviderProps<T>) {
  return (
    <div>
      {data.map((item, index) => render(item, index))}
    </div>
  )
}

// Usage
<DataProvider
  data={users}
  render={(user, index) => (
    <div key={index}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  )}
/>
```

### Compound Components

```typescript
interface TabsProps {
  children: React.ReactNode
  defaultTab?: string
}

interface TabProps {
  id: string
  label: string
  children: React.ReactNode
}

export function Tabs({ children, defaultTab }: TabsProps) {
  const [activeTab, setActiveTab] = useState(defaultTab || '')

  return (
    <div>
      <div className="tabs-header">
        {React.Children.map(children, (child) => {
          if (React.isValidElement<TabProps>(child)) {
            return (
              <button
                onClick={() => setActiveTab(child.props.id)}
                className={activeTab === child.props.id ? 'active' : ''}
              >
                {child.props.label}
              </button>
            )
          }
        })}
      </div>
      <div className="tabs-content">
        {React.Children.map(children, (child) => {
          if (React.isValidElement<TabProps>(child) && child.props.id === activeTab) {
            return child.props.children
          }
        })}
      </div>
    </div>
  )
}

export function Tab({ children }: TabProps) {
  return <>{children}</>
}

// Usage
<Tabs defaultTab="profile">
  <Tab id="profile" label="Profile">
    <ProfileForm />
  </Tab>
  <Tab id="settings" label="Settings">
    <SettingsForm />
  </Tab>
</Tabs>
```

## Advanced Typing Patterns

### Generic Components

```typescript
interface ListProps<T> {
  items: T[]
  renderItem: (item: T) => React.ReactNode
  keyExtractor: (item: T) => string | number
}

export function List<T>({ items, renderItem, keyExtractor }: ListProps<T>) {
  return (
    <ul>
      {items.map((item) => (
        <li key={keyExtractor(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  )
}

// Usage with type inference
<List
  items={products}
  renderItem={(product) => <div>{product.name}</div>}
  keyExtractor={(product) => product.id}
/>
```

### Event Handlers

```typescript
interface ButtonProps {
  onClick: (event: React.MouseEvent<HTMLButtonElement>) => void
  children: React.ReactNode
}

export function Button({ onClick, children }: ButtonProps) {
  return <button onClick={onClick}>{children}</button>
}

// Usage
<Button onClick={(e) => console.log('Clicked!', e)}>
  Click Me
</Button>
```

### Form Events

```typescript
interface SearchBarProps {
  onSearch: (query: string) => void
}

export function SearchBar({ onSearch }: SearchBarProps) {
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const formData = new FormData(e.currentTarget)
    const query = formData.get('query') as string
    onSearch(query)
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="query" type="text" placeholder="Search..." />
      <button type="submit">Search</button>
    </form>
  )
}
```

## Best Practices

### 1. Prefer Server Components

```typescript
// Good: Server Component for static content
export default function AboutPage() {
  return (
    <div>
      <h1>About Us</h1>
      <p>We are a company...</p>
    </div>
  )
}

// Only use Client Component when needed
"use client"
export default function InteractiveFeature() {
  const [state, setState] = useState(false)
  return <button onClick={() => setState(!state)}>Toggle</button>
}
```

### 2. Keep Components Small and Focused

```typescript
// Good: Single responsibility
function UserAvatar({ url, name }: { url: string; name: string }) {
  return <img src={url} alt={name} />
}

function UserName({ name }: { name: string }) {
  return <h3>{name}</h3>
}

function UserCard({ user }: { user: User }) {
  return (
    <div>
      <UserAvatar url={user.avatarUrl} name={user.name} />
      <UserName name={user.name} />
    </div>
  )
}
```

### 3. Use Descriptive Prop Names

```typescript
// Good
interface ModalProps {
  isOpen: boolean
  onClose: () => void
  title: string
  children: React.ReactNode
}

// Avoid
interface ModalProps {
  open: boolean
  close: () => void
  text: string
  content: React.ReactNode
}
```

### 4. Document Complex Props

```typescript
interface DataTableProps<T> {
  /** The array of data items to display */
  data: T[]
  /** Function to render each row */
  renderRow: (item: T) => React.ReactNode
  /** Optional loading state */
  isLoading?: boolean
  /** Optional empty state message */
  emptyMessage?: string
}
```

### 5. Handle Loading and Error States

```typescript
"use client"

export default function DataComponent() {
  const { data, loading, error } = useFetch('/api/data')

  if (loading) {
    return <div>Loading...</div>
  }

  if (error) {
    return <div>Error: {error.message}</div>
  }

  if (!data || data.length === 0) {
    return <div>No data available</div>
  }

  return (
    <div>
      {data.map((item) => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  )
}
```

## Common Patterns

### Modal Component

```typescript
"use client"

interface ModalProps {
  isOpen: boolean
  onClose: () => void
  title: string
  children: React.ReactNode
}

export function Modal({ isOpen, onClose, title, children }: ModalProps) {
  if (!isOpen) return null

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <div className="bg-white rounded-lg p-6 max-w-md w-full">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-bold">{title}</h2>
          <button onClick={onClose}>×</button>
        </div>
        <div>{children}</div>
      </div>
    </div>
  )
}
```

### Dropdown Component

```typescript
"use client"

import { useState } from 'react'

interface DropdownProps {
  label: string
  options: string[]
  onSelect: (option: string) => void
}

export function Dropdown({ label, options, onSelect }: DropdownProps) {
  const [isOpen, setIsOpen] = useState(false)
  const [selected, setSelected] = useState(label)

  const handleSelect = (option: string) => {
    setSelected(option)
    onSelect(option)
    setIsOpen(false)
  }

  return (
    <div className="relative">
      <button onClick={() => setIsOpen(!isOpen)}>
        {selected}
      </button>
      {isOpen && (
        <div className="absolute top-full left-0 bg-white shadow-lg">
          {options.map((option) => (
            <button
              key={option}
              onClick={() => handleSelect(option)}
              className="block w-full text-left px-4 py-2 hover:bg-gray-100"
            >
              {option}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}
```

## Troubleshooting

**Issue**: "use client" error
- Solution: Add `"use client"` directive at top of file for components using hooks or event handlers

**Issue**: Hydration errors
- Solution: Ensure server and client render the same initial content
- Avoid using browser APIs (localStorage, window) during initial render

**Issue**: Props not updating
- Solution: Check that you're not mutating state directly
- Use proper state updates with setState functions

**Issue**: useEffect running too often
- Solution: Check dependency array
- Add all variables used inside useEffect to dependencies

## Resources

- React Official Docs: https://react.dev
- Next.js App Router: https://nextjs.org/docs/app
- TypeScript with React: https://react.dev/learn/typescript
- React Hooks Reference: https://react.dev/reference/react/hooks
