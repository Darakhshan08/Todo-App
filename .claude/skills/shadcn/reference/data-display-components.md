# Data Display Components Reference

## Card

Displays a card with header, content, and footer.

**Installation:**
```bash
npx shadcn@latest add card
```

**Props:**
- `className`: string - Additional CSS classes

**Card Props:**
- None specific - accepts all div props

**CardHeader Props:**
- None specific - accepts all div props

**CardTitle Props:**
- None specific - accepts all heading props

**CardDescription Props:**
- None specific - accepts all paragraph props

**CardContent Props:**
- None specific - accepts all div props

**CardFooter Props:**
- None specific - accepts all div props

**Example:**
```tsx
<Card>
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Card Description</CardDescription>
  </CardHeader>
  <CardContent>
    <p>Card Content</p>
  </CardContent>
  <CardFooter>
    <p>Card Footer</p>
  </CardFooter>
</Card>
```

## Table

A responsive table component for displaying tabular data.

**Installation:**
```bash
npx shadcn@latest add table
```

**Props:**
- `className`: string - Additional CSS classes

**Table Props:**
- None specific - accepts all table props

**TableHeader Props:**
- None specific - accepts all thead props

**TableBody Props:**
- None specific - accepts all tbody props

**TableFooter Props:**
- None specific - accepts all tfoot props

**TableRow Props:**
- None specific - accepts all tr props

**TableHead Props:**
- None specific - accepts all th props

**TableCell Props:**
- None specific - accepts all td props

**TableCaption Props:**
- None specific - accepts all caption props

**Example:**
```tsx
<Table>
  <TableCaption>A list of your recent invoices.</TableCaption>
  <TableHeader>
    <TableRow>
      <TableHead className="w-[100px]">Invoice</TableHead>
      <TableHead>Status</TableHead>
      <TableHead>Method</TableHead>
      <TableHead className="text-right">Amount</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    <TableRow>
      <TableCell className="font-medium">INV001</TableCell>
      <TableCell>Paid</TableCell>
      <TableCell>Credit Card</TableCell>
      <TableCell className="text-right">$250.00</TableCell>
    </TableRow>
  </TableBody>
</Table>
```

## Progress

Displays an indicator showing the completion progress of a task.

**Installation:**
```bash
npx shadcn@latest add progress
```

**Props:**
- `value`: number - The current value of the progress bar
- `max`: number - The maximum value of the progress bar (default: 100)
- `indicatorColor`: string - Color of the progress indicator

**Example:**
```tsx
<Progress value={33} />
<Progress value={66} className="h-2" />
<Progress value={100} className="h-4" />
```

## Badge

Displays a badge or a component that looks like a badge.

**Installation:**
```bash
npx shadcn@latest add badge
```

**Props:**
- `variant`: "default" | "secondary" | "destructive" | "outline" - The visual style of the badge

**Example:**
```tsx
<Badge>Default</Badge>
<Badge variant="secondary">Secondary</Badge>
<Badge variant="destructive">Destructive</Badge>
<Badge variant="outline">Outline</Badge>
```

## Alert

An alert displays a prominent message to the user.

**Installation:**
```bash
npx shadcn@latest add alert
```

**Props:**
- `variant`: "default" | "destructive" - The visual style of the alert

**AlertTitle Props:**
- None specific - accepts all heading props

**AlertDescription Props:**
- None specific - accepts all paragraph props

**Example:**
```tsx
<Alert>
  <TerminalIcon className="h-4 w-4" />
  <AlertTitle>Heads up!</AlertTitle>
  <AlertDescription>
    You can add components to your app using the cli.
  </AlertDescription>
</Alert>
```

## Calendar

A calendar component for selecting dates.

**Installation:**
```bash
npx shadcn@latest add calendar
```

**Props:**
- `mode`: "single" | "multiple" | "range" - The selection mode (default: "single")
- `selected`: Date | Date[] | { from: Date; to: Date } | undefined - The selected date(s)
- `onSelect`: (date: Date | Date[] | { from: Date; to: Date } | undefined) => void - Event handler for when a date is selected
- `initialFocus`: boolean - Whether to focus the calendar when mounted
- `defaultMonth`: Date - The month to display initially when no date is selected
- `fromMonth`: Date - The earliest month to allow selection
- `toMonth`: Date - The latest month to allow selection
- `fromYear`: number - The earliest year to allow selection
- `toYear`: number - The latest year to allow selection
- `captionLayout`: "label" | "dropdown-buttons" | "dropdown" - The layout of the calendar caption
- `disabled`: boolean | { from: Date; to: Date } | ((date: Date) => boolean) - Whether the calendar is disabled
- `fixedWeeks`: boolean - Whether to always show 6 weeks
- `showOutsideDays`: boolean - Whether to show days outside the current month

**Example:**
```tsx
<Calendar
  mode="single"
  selected={date}
  onSelect={setDate}
  className="rounded-md border"
/>
```

## Avatar

An image element with a fallback for representing the user.

**Installation:**
```bash
npx shadcn@latest add avatar
```

**Props:**
- `alt`: string - Alternative text for the image
- `src`: string - The source of the avatar image
- `onError`: () => void - Event handler for when the image fails to load

**AvatarImage Props:**
- Same as Avatar props

**AvatarFallback Props:**
- None specific - accepts all span props

**Example:**
```tsx
<Avatar>
  <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
  <AvatarFallback>CN</AvatarFallback>
</Avatar>
```

## Separator

A separator or divider between elements.

**Installation:**
```bash
npx shadcn@latest add separator
```

**Props:**
- `orientation`: "horizontal" | "vertical" - The orientation of the separator (default: "horizontal")
- `decorative`: boolean - Whether the separator is decorative (default: false)

**Example:**
```tsx
<div>
  <div>Section 1</div>
  <Separator />
  <div>Section 2</div>
</div>
<Separator orientation="vertical" />
```

## Skeleton

A placeholder component that mimics the layout of content while it's loading.

**Installation:**
```bash
npx shadcn@latest add skeleton
```

**Props:**
- None specific - accepts all div props

**Example:**
```tsx
<Skeleton className="h-4 w-[250px]" />
<Skeleton className="h-10 w-10 rounded-full" />
<div className="flex items-center space-x-4">
  <Skeleton className="h-12 w-12 rounded-full" />
  <div className="space-y-2">
    <Skeleton className="h-4 w-[250px]" />
    <Skeleton className="h-4 w-[200px]" />
  </div>
</div>
```

## AspectRatio

Displays content within a desired ratio.

**Installation:**
```bash
npx shadcn@latest add aspect-ratio
```

**Props:**
- `ratio`: number - The desired aspect ratio (default: 1)

**Example:**
```tsx
<AspectRatio ratio={16 / 9}>
  <img
    src="https://example.com/image.jpg"
    alt="Example image"
    className="rounded-md object-cover"
  />
</AspectRatio>
```

## Pagination

Pagination component for navigating through multiple pages of content.

**Installation:**
```bash
npx shadcn@latest add pagination
```

**Props:**
- `disabled`: boolean - Whether the pagination is disabled

**PaginationContent Props:**
- None specific - accepts all div props

**PaginationItem Props:**
- None specific - accepts all div props

**PaginationLink Props:**
- `isActive`: boolean - Whether the link is active
- `disabled`: boolean - Whether the link is disabled

**Example:**
```tsx
<Pagination>
  <PaginationContent>
    <PaginationItem>
      <PaginationPrevious href="#" />
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#">1</PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationEllipsis />
    </PaginationItem>
    <PaginationItem>
      <PaginationNext href="#" />
    </PaginationItem>
  </PaginationContent>
</Pagination>
```