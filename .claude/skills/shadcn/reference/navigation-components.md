# Navigation Components Reference

## Accordion

The Accordion component allows users to expand and collapse sections of content.

**Installation:**
```bash
npx shadcn@latest add accordion
```

**Props:**
- `type`: "single" | "multiple" - Whether only one item can be opened at a time or multiple
- `collapsible`: boolean - Whether an open item can be closed
- `defaultValue`: string | string[] - The controlled value of the item(s) to expand
- `value`: string | string[] - The controlled value of the item(s) that are expanded
- `onValueChange`: (value: string | string[]) => void - Event handler for when the expanded item(s) change

**AccordionItem Props:**
- `value`: string - A unique value for the item
- `disabled`: boolean - Whether the item is disabled

**AccordionTrigger Props:**
- None specific - accepts all button props

**AccordionContent Props:**
- None specific - accepts all div props

**Example:**
```tsx
<Accordion type="single" collapsible>
  <AccordionItem value="item-1">
    <AccordionTrigger>Is it accessible?</AccordionTrigger>
    <AccordionContent>Yes. It adheres to the WAI-ARIA design pattern.</AccordionContent>
  </AccordionItem>
</Accordion>
```

## NavigationMenu

A navigation menu component for organizing links and navigation items.

**Installation:**
```bash
npx shadcn@latest add navigation-menu
```

**Props:**
- `value`: string - The controlled value of the selected item
- `onValueChange`: (value: string) => void - Event handler for when the value changes

**NavigationMenuList Props:**
- None specific - accepts all ul props

**NavigationMenuItem Props:**
- None specific - accepts all li props

**NavigationMenuTrigger Props:**
- None specific - accepts all button props

**NavigationMenuContent Props:**
- `forceMount`: boolean - Whether to force mounting when more control is needed

**NavigationMenuLink Props:**
- None specific - accepts all anchor props

**Example:**
```tsx
<NavigationMenu>
  <NavigationMenuList>
    <NavigationMenuItem>
      <NavigationMenuTrigger>Getting started</NavigationMenuTrigger>
      <NavigationMenuContent>
        <NavigationMenuLink>Introduction</NavigationMenuLink>
        <NavigationMenuLink>Installation</NavigationMenuLink>
      </NavigationMenuContent>
    </NavigationMenuItem>
  </NavigationMenuList>
</NavigationMenu>
```

## Tabs

A set of layered sections of content that are displayed one at a time.

**Installation:**
```bash
npx shadcn@latest add tabs
```

**Props:**
- `value`: string - The controlled value of the selected tab
- `onValueChange`: (value: string) => void - Event handler for when the value changes
- `activationMode`: "automatic" | "manual" - How tabs are activated (default: "automatic")

**TabsList Props:**
- None specific - accepts all div props

**TabsTrigger Props:**
- `value`: string - The value of the tab
- `disabled`: boolean - Whether the tab is disabled

**TabsContent Props:**
- `value`: string - The value of the tab
- `forceMount`: boolean - Whether to force mounting when more control is needed

**Example:**
```tsx
<Tabs defaultValue="account" className="w-[400px]">
  <TabsList>
    <TabsTrigger value="account">Account</TabsTrigger>
    <TabsTrigger value="password">Password</TabsTrigger>
  </TabsList>
  <TabsContent value="account">
    Make changes to your account here.
  </TabsContent>
  <TabsContent value="password">
    Change your password here.
  </TabsContent>
</Tabs>
```

## Menubar

A menubar component that provides access to app functionality.

**Installation:**
```bash
npx shadcn@latest add menubar
```

**Props:**
- `value`: string - The controlled value of the selected item
- `onValueChange`: (value: string) => void - Event handler for when the value changes

**MenubarTrigger Props:**
- None specific - accepts all button props

**MenubarContent Props:**
- `forceMount`: boolean - Whether to force mounting when more control is needed

**MenubarItem Props:**
- `inset`: boolean - Whether the item is inset
- `disabled`: boolean - Whether the item is disabled
- `onSelect`: (event: Event) => void - Event handler for when the item is selected

**Example:**
```tsx
<Menubar>
  <MenubarMenu>
    <MenubarTrigger>File</MenubarTrigger>
    <MenubarContent>
      <MenubarItem>New Tab</MenubarItem>
      <MenubarItem>New Window</MenubarItem>
      <MenubarSeparator />
      <MenubarItem>Share</MenubarItem>
    </MenubarContent>
  </MenubarMenu>
</Menubar>
```