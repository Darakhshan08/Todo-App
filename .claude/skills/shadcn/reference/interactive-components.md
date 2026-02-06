# Interactive Components Reference

## Button

Displays a button or a component that looks like a button.

**Installation:**
```bash
npx shadcn@latest add button
```

**Props:**
- `variant`: "default" | "destructive" | "outline" | "secondary" | "ghost" | "link" - The visual style of the button
- `size`: "default" | "sm" | "lg" | "icon" - The size of the button
- `asChild`: boolean - Change the default rendered element for the one passed as a child

**Example:**
```tsx
<Button>Default</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="destructive">Destructive</Button>
<Button variant="outline">Outline</Button>
<Button variant="ghost">Ghost</Button>
<Button variant="link">Link</Button>
```

## Dialog

A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

**Installation:**
```bash
npx shadcn@latest add dialog
```

**Props:**
- `open`: boolean - Whether the dialog is open
- `onOpenChange`: (open: boolean) => void - Event handler for when the open state changes
- `modal`: boolean - Whether the dialog should be modal (default: true)

**DialogTrigger Props:**
- None specific - accepts all button props

**DialogContent Props:**
- `forceMount`: boolean - Whether to force mounting when more control is needed
- `trapFocus`: boolean - Whether to trap focus inside the dialog
- `disableOutsidePointerEvents`: boolean - Whether to disable pointer events outside the dialog

**DialogHeader Props:**
- None specific - accepts all div props

**DialogFooter Props:**
- None specific - accepts all div props

**DialogTitle Props:**
- None specific - accepts all heading props

**DialogDescription Props:**
- None specific - accepts all paragraph props

**Example:**
```tsx
<Dialog>
  <DialogTrigger asChild>
    <Button variant="outline">Edit Profile</Button>
  </DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Edit profile</DialogTitle>
      <DialogDescription>
        Make changes to your profile here. Click save when you're done.
      </DialogDescription>
    </DialogHeader>
    <div className="grid gap-4 py-4">
      <div className="grid grid-cols-4 items-center gap-4">
        <Label htmlFor="name" className="text-right">
          Name
        </Label>
        <Input id="name" value="Pedro Duarte" className="col-span-3" />
      </div>
      <div className="grid grid-cols-4 items-center gap-4">
        <Label htmlFor="username" className="text-right">
          Username
        </Label>
        <Input id="username" value="@peduarte" className="col-span-3" />
      </div>
    </div>
    <DialogFooter>
      <Button type="submit">Save changes</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

## AlertDialog

A modal dialog that interrupts the user with important content and expects a response.

**Installation:**
```bash
npx shadcn@latest add alert-dialog
```

**Props:**
- `open`: boolean - Whether the dialog is open
- `onOpenChange`: (open: boolean) => void - Event handler for when the open state changes

**AlertDialogTrigger Props:**
- None specific - accepts all button props

**AlertDialogContent Props:**
- None specific - accepts all dialog props

**AlertDialogHeader Props:**
- None specific - accepts all div props

**AlertDialogFooter Props:**
- None specific - accepts all div props

**AlertDialogTitle Props:**
- None specific - accepts all heading props

**AlertDialogDescription Props:**
- None specific - accepts all paragraph props

**AlertDialogAction Props:**
- None specific - accepts all button props

**AlertDialogCancel Props:**
- None specific - accepts all button props

**Example:**
```tsx
<AlertDialog>
  <AlertDialogTrigger asChild>
    <Button variant="outline">Show Dialog</Button>
  </AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
      <AlertDialogDescription>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction>Continue</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

## DropdownMenu

Displays a menu to the user — such as a set of actions or functions.

**Installation:**
```bash
npx shadcn@latest add dropdown-menu
```

**Props:**
- `modal`: boolean - Whether the dropdown menu should be modal (default: true)

**DropdownMenuTrigger Props:**
- None specific - accepts all button props

**DropdownMenuContent Props:**
- `forceMount`: boolean - Whether to force mounting when more control is needed

**DropdownMenuItem Props:**
- `inset`: boolean - Whether the item is inset
- `disabled`: boolean - Whether the item is disabled
- `onSelect`: (event: Event) => void - Event handler for when the item is selected

**DropdownMenuSeparator Props:**
- None specific - accepts all div props

**DropdownMenuLabel Props:**
- `inset`: boolean - Whether the label is inset

**Example:**
```tsx
<DropdownMenu>
  <DropdownMenuTrigger asChild>
    <Button variant="outline">Open</Button>
  </DropdownMenuTrigger>
  <DropdownMenuContent>
    <DropdownMenuLabel>My Account</DropdownMenuLabel>
    <DropdownMenuSeparator />
    <DropdownMenuItem>Profile</DropdownMenuItem>
    <DropdownMenuItem>Billing</DropdownMenuItem>
    <DropdownMenuSeparator />
    <DropdownMenuItem>Log out</DropdownMenuItem>
  </DropdownMenuContent>
</DropdownMenu>
```

## ContextMenu

A context menu that displays a list of actions when triggered by a right-click.

**Installation:**
```bash
npx shadcn@latest add context-menu
```

**Props:**
- `modal`: boolean - Whether the context menu should be modal (default: true)

**ContextMenuTrigger Props:**
- None specific - accepts all div props

**ContextMenuContent Props:**
- None specific - accepts all div props

**ContextMenuItem Props:**
- `inset`: boolean - Whether the item is inset
- `disabled`: boolean - Whether the item is disabled
- `onSelect`: (event: Event) => void - Event handler for when the item is selected

**ContextMenuSeparator Props:**
- None specific - accepts all div props

**Example:**
```tsx
<ContextMenu>
  <ContextMenuTrigger>Right click here</ContextMenuTrigger>
  <ContextMenuContent>
    <ContextMenuItem>Profile</ContextMenuItem>
    <ContextMenuItem>Billing</ContextMenuItem>
    <ContextMenuSeparator />
    <ContextMenuItem>Log out</ContextMenuItem>
  </ContextMenuContent>
</ContextMenu>
```

## Combobox

A combobox component with autocomplete and filtering capabilities.

**Installation:**
```bash
npx shadcn@latest add combobox
```

**Props:**
- `open`: boolean - Whether the combobox is open
- `onOpenChange`: (open: boolean) => void - Event handler for when the open state changes
- `value`: string - The controlled value of the selected item
- `onValueChange`: (value: string) => void - Event handler for when the value changes

**ComboboxInput Props:**
- None specific - accepts all input props

**ComboboxItem Props:**
- `value`: string - The value of the item
- `disabled`: boolean - Whether the item is disabled

**Example:**
```tsx
<Combobox>
  <ComboboxInput placeholder="Search framework..." />
  <ComboboxContent>
    <ComboboxItem value="next">Next.js</ComboboxItem>
    <ComboboxItem value="svelte">SvelteKit</ComboboxItem>
  </ComboboxContent>
</Combobox>
```

## Command

A command palette component for quickly searching and selecting options.

**Installation:**
```bash
npx shadcn@latest add command
```

**Props:**
- `shouldFilter`: boolean - Whether to filter items automatically (default: true)
- `filter`: (value: string, search: string) => number - Custom filtering function
- `loop`: boolean - Whether to loop through items (default: false)

**CommandInput Props:**
- None specific - accepts all input props

**CommandList Props:**
- None specific - accepts all div props

**CommandEmpty Props:**
- None specific - accepts all div props

**CommandGroup Props:**
- `heading`: string - Heading for the group
- `value`: string - Value for the group

**CommandItem Props:**
- `value`: string - The value of the item
- `disabled`: boolean - Whether the item is disabled
- `onSelect`: (value: string) => void - Event handler for when the item is selected

**Example:**
```tsx
<Command>
  <CommandInput placeholder="Type a command or search..." />
  <CommandList>
    <CommandEmpty>No results found.</CommandEmpty>
    <CommandGroup heading="Suggestions">
      <CommandItem>Calendar</CommandItem>
      <CommandItem>Search Emoji</CommandItem>
      <CommandItem>Calculator</CommandItem>
    </CommandGroup>
  </CommandList>
</Command>
```

## Popover

A popover component that displays content in a floating container.

**Installation:**
```bash
npx shadcn@latest add popover
```

**Props:**
- `open`: boolean - Whether the popover is open
- `onOpenChange`: (open: boolean) => void - Event handler for when the open state changes
- `modal`: boolean - Whether the popover should be modal (default: false)

**PopoverTrigger Props:**
- None specific - accepts all button props

**PopoverContent Props:**
- `forceMount`: boolean - Whether to force mounting when more control is needed
- `align`: "start" | "center" | "end" - Alignment of the popover content
- `side`: "top" | "right" | "bottom" | "left" - Side where the popover appears

**Example:**
```tsx
<Popover>
  <PopoverTrigger>Open popover</PopoverTrigger>
  <PopoverContent>
    <div className="grid gap-4">
      <div className="space-y-2">
        <h4 className="font-medium leading-none">Dimensions</h4>
        <p className="text-sm text-muted-foreground">
          Set the dimensions for the layer.
        </p>
      </div>
    </div>
  </PopoverContent>
</Popover>
```

## Tooltip

A tooltip component that displays additional information on hover.

**Installation:**
```bash
npx shadcn@latest add tooltip
```

**Props:**
- `open`: boolean - Whether the tooltip is open
- `onOpenChange`: (open: boolean) => void - Event handler for when the open state changes
- `delayDuration`: number - Delay before the tooltip appears (default: 700)
- `disableHoverableContent`: boolean - Whether to disable hoverable content (default: false)

**TooltipTrigger Props:**
- None specific - accepts all button props

**TooltipContent Props:**
- `forceMount`: boolean - Whether to force mounting when more control is needed
- `side`: "top" | "right" | "bottom" | "left" - Side where the tooltip appears
- `align`: "start" | "center" | "end" - Alignment of the tooltip content

**Example:**
```tsx
<TooltipProvider>
  <Tooltip>
    <TooltipTrigger asChild>
      <Button variant="outline" className="w-10 rounded-full">
        <PlusCircledIcon className="h-4 w-4" />
      </Button>
    </TooltipTrigger>
    <TooltipContent>
      <p>Add to library</p>
    </TooltipContent>
  </Tooltip>
</TooltipProvider>
```

## Hover Card

A popup that displays information related to an element when hovering over it.

**Installation:**
```bash
npx shadcn@latest add hover-card
```

**Props:**
- `open`: boolean - Whether the hover card is open
- `onOpenChange`: (open: boolean) => void - Event handler for when the open state changes
- `delayDuration`: number - Delay before the hover card opens (default: 700)

**HoverCardTrigger Props:**
- None specific - accepts all anchor props

**HoverCardContent Props:**
- `forceMount`: boolean - Whether to force mounting when more control is needed

**Example:**
```tsx
<HoverCard>
  <HoverCardTrigger asChild>
    <Button variant="link">@nextjs</Button>
  </HoverCardTrigger>
  <HoverCardContent>
    The React Framework – created and maintained by @vercel.
  </HoverCardContent>
</HoverCard>
```

## Slider

An input where the user selects a value from within a given range.

**Installation:**
```bash
npx shadcn@latest add slider
```

**Props:**
- `value`: number[] - The controlled value of the slider
- `onValueChange`: (value: number[]) => void - Event handler for when the value changes
- `min`: number - The minimum value of the slider (default: 0)
- `max`: number - The maximum value of the slider (default: 100)
- `step`: number - The step value of the slider (default: 1)
- `minStepsBetweenThumbs`: number - The minimum steps between thumbs (default: 0)
- `disabled`: boolean - Whether the slider is disabled

**Example:**
```tsx
<Slider defaultValue={[50]} max={100} step={1} />
<Slider defaultValue={[25, 75]} max={100} step={1} />
```

## Toggle

A toggle component that can be switched between two states.

**Installation:**
```bash
npx shadcn@latest add toggle
```

**Props:**
- `pressed`: boolean - Whether the toggle is pressed
- `onPressedChange`: (pressed: boolean) => void - Event handler for when the pressed state changes
- `disabled`: boolean - Whether the toggle is disabled
- `variant`: "default" | "outline" - The visual style of the toggle
- `size`: "default" | "sm" | "lg" - The size of the toggle

**Example:**
```tsx
<Toggle aria-label="Toggle italic">
  <ItalicIcon className="h-4 w-4" />
</Toggle>
<Toggle variant="outline" aria-label="Toggle bold">
  <BoldIcon className="h-4 w-4" />
</Toggle>
```

## Collapsible

An interactive component which expands/collapses a panel.

**Installation:**
```bash
npx shadcn@latest add collapsible
```

**Props:**
- `open`: boolean - Whether the collapsible is open
- `onOpenChange`: (open: boolean) => void - Event handler for when the open state changes
- `disabled`: boolean - Whether the collapsible is disabled

**Example:**
```tsx
<Collapsible>
  <CollapsibleTrigger>Can I use this in my project?</CollapsibleTrigger>
  <CollapsibleContent>
    Yes. Free to use for personal and commercial projects. No attribution required.
  </CollapsibleContent>
</Collapsible>
```

## Sheet

A sheet component that slides in from the edge of the screen.

**Installation:**
```bash
npx shadcn@latest add sheet
```

**Props:**
- `open`: boolean - Whether the sheet is open
- `onOpenChange`: (open: boolean) => void - Event handler for when the open state changes
- `side`: "top" | "right" | "bottom" | "left" - Side where the sheet appears (default: "right")

**SheetTrigger Props:**
- None specific - accepts all button props

**SheetContent Props:**
- `forceMount`: boolean - Whether to force mounting when more control is needed

**SheetHeader Props:**
- None specific - accepts all div props

**SheetFooter Props:**
- None specific - accepts all div props

**SheetTitle Props:**
- None specific - accepts all heading props

**SheetDescription Props:**
- None specific - accepts all paragraph props

**Example:**
```tsx
<Sheet>
  <SheetTrigger>Open</SheetTrigger>
  <SheetContent>
    <SheetHeader>
      <SheetTitle>Are you sure absolutely sure?</SheetTitle>
      <SheetDescription>
        This action cannot be undone.
      </SheetDescription>
    </SheetHeader>
  </SheetContent>
</Sheet>
```

## Drawer

A drawer component that slides in from the edge of the screen.

**Installation:**
```bash
npx shadcn@latest add drawer
```

**Props:**
- `open`: boolean - Whether the drawer is open
- `onOpenChange`: (open: boolean) => void - Event handler for when the open state changes
- `shouldScaleBackground`: boolean - Whether to scale the background when open (default: true)

**DrawerTrigger Props:**
- None specific - accepts all button props

**DrawerContent Props:**
- None specific - accepts all div props

**DrawerHeader Props:**
- None specific - accepts all div props

**DrawerFooter Props:**
- None specific - accepts all div props

**DrawerTitle Props:**
- None specific - accepts all heading props

**DrawerDescription Props:**
- None specific - accepts all paragraph props

**Example:**
```tsx
<Drawer>
  <DrawerTrigger>Open Drawer</DrawerTrigger>
  <DrawerContent>
    <DrawerHeader>
      <DrawerTitle>Are you sure absolutely sure?</DrawerTitle>
      <DrawerDescription>
        This action cannot be undone.
      </DrawerDescription>
    </DrawerHeader>
    <DrawerFooter>
      <Button>Submit</Button>
      <DrawerClose asChild>
        <Button variant="outline">Cancel</Button>
      </DrawerClose>
    </DrawerFooter>
  </DrawerContent>
</Drawer>
```

## Toast

A toast component for displaying notifications.

**Installation:**
```bash
npx shadcn@latest add toast
```

**Props:**
- `open`: boolean - Whether the toast is open
- `onOpenChange`: (open: boolean) => void - Event handler for when the open state changes
- `duration`: number - Duration in milliseconds (default: 5000)

**ToastProps:**
- `type`: "foreground" | "background" - The type of toast (default: "background")

**ToastAction Props:**
- `altText`: string - Alternative text for the action

**Example:**
```tsx
// To use toasts, you need to wrap your app with ToastProvider
<ToastProvider>
  <Button
    onClick={() => {
      toast({
        title: "Scheduled: Catch up",
        description: "Friday, February 10, 2023 at 5:57 PM",
      })
    }}
  >
    Add to calendar
  </Button>
  <ToastViewport />
</ToastProvider>
```