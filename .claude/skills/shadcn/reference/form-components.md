# Form Components Reference

## Form

Form components with validation using react-hook-form.

**Installation:**
```bash
npx shadcn@latest add form
```

**Props:**
- `control`: Control - The control object from react-hook-form
- `name`: string - The name of the form field
- `rules`: ValidationRule - Validation rules for the field
- `defaultValue`: any - Default value for the field
- `disabled`: boolean - Whether the field is disabled
- `children`: ReactNode - Children of the form field

**Form Props:**
- None specific - accepts all form props

**FormField Props:**
- `control`: Control - The control object from react-hook-form
- `name`: string - The name of the form field
- `render`: (props: { field: FieldProps; fieldState: FieldError; formState: FormState }) => ReactElement - Render function for the form field

**FormItem Props:**
- None specific - accepts all div props

**FormLabel Props:**
- None specific - accepts all label props

**FormControl Props:**
- None specific - accepts all div props

**FormDescription Props:**
- None specific - accepts all p props

**FormMessage Props:**
- None specific - accepts all p props

**Example:**
```tsx
<Form {...form}>
  <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
    <FormField
      control={form.control}
      name="email"
      render={({ field }) => (
        <FormItem>
          <FormLabel>Email</FormLabel>
          <FormControl>
            <Input placeholder="your@email.com" {...field} />
          </FormControl>
          <FormDescription>
            Enter your email address to login.
          </FormDescription>
          <FormMessage />
        </FormItem>
      )}
    />
  </form>
</Form>
```

## Input

Displays a form input field or a component that looks like an input field.

**Installation:**
```bash
npx shadcn@latest add input
```

**Props:**
- `type`: string - The type of input (text, email, password, etc.)
- `disabled`: boolean - Whether the input is disabled
- `placeholder`: string - Placeholder text for the input
- `size`: "sm" | "md" | "lg" - The size of the input

**Example:**
```tsx
<Input type="email" placeholder="Email" />
<Input type="password" placeholder="Password" />
<Input disabled type="text" placeholder="Disabled input" />
```

## Textarea

Displays a form textarea or a component that looks like a textarea.

**Installation:**
```bash
npx shadcn@latest add textarea
```

**Props:**
- `disabled`: boolean - Whether the textarea is disabled
- `placeholder`: string - Placeholder text for the textarea
- `rows`: number - Number of visible text lines (default: 3)
- `autoResize`: boolean - Whether the textarea should automatically resize (default: false)

**Example:**
```tsx
<Textarea placeholder="Type your message here." />
<Textarea disabled placeholder="Type your message here." />
<Textarea rows={6} placeholder="Type your message here." />
```

## Label

Renders an accessible label associated with controls.

**Installation:**
```bash
npx shadcn@latest add label
```

**Props:**
- `htmlFor`: string - Associates the label with a form control
- `disabled`: boolean - Whether the label is disabled

**Example:**
```tsx
<Label htmlFor="email">Email</Label>
<Input id="email" type="email" />
```

## Select

A dropdown component that allows the user to select one option from a list.

**Installation:**
```bash
npx shadcn@latest add select
```

**Props:**
- `value`: string - The controlled value of the selected item
- `onValueChange`: (value: string) => void - Event handler for when the value changes
- `disabled`: boolean - Whether the select is disabled
- `required`: boolean - Whether the select is required

**SelectTrigger Props:**
- `disabled`: boolean - Whether the trigger is disabled

**SelectValue Props:**
- `placeholder`: string - Placeholder text for the select

**SelectContent Props:**
- `position`: "popper" | "item-aligned" - Position of the content
- `forceMount`: boolean - Whether to force mounting when more control is needed

**SelectItem Props:**
- `value`: string - The value of the item
- `disabled`: boolean - Whether the item is disabled

**Example:**
```tsx
<Select defaultValue="blue">
  <SelectTrigger className="w-[180px]">
    <SelectValue placeholder="Select a color" />
  </SelectTrigger>
  <SelectContent>
    <SelectItem value="red">Red</SelectItem>
    <SelectItem value="blue">Blue</SelectItem>
    <SelectItem value="green">Green</SelectItem>
  </SelectContent>
</Select>
```

## RadioGroup

A set of checkable buttons that allow the user to select one option from a group.

**Installation:**
```bash
npx shadcn@latest add radio-group
```

**Props:**
- `value`: string - The controlled value of the selected item
- `onValueChange`: (value: string) => void - Event handler for when the value changes
- `disabled`: boolean - Whether the radio group is disabled
- `required`: boolean - Whether the radio group is required

**RadioGroupItem Props:**
- `value`: string - The value of the item
- `disabled`: boolean - Whether the item is disabled
- `required`: boolean - Whether the item is required

**Example:**
```tsx
<RadioGroup defaultValue="comfortable">
  <div className="flex items-center space-x-2">
    <RadioGroupItem value="default" id="r1" />
    <Label htmlFor="r1">Default</Label>
  </div>
  <div className="flex items-center space-x-2">
    <RadioGroupItem value="comfortable" id="r2" />
    <Label htmlFor="r2">Comfortable</Label>
  </div>
  <div className="flex items-center space-x-2">
    <RadioGroupItem value="compact" id="r3" />
    <Label htmlFor="r3">Compact</Label>
  </div>
</RadioGroup>
```

## Checkbox

A control that allows the user to toggle between checked and not checked.

**Installation:**
```bash
npx shadcn@latest add checkbox
```

**Props:**
- `checked`: boolean | "indeterminate" - Whether the checkbox is checked
- `onCheckedChange`: (checked: boolean) => void - Event handler for when the checked state changes
- `disabled`: boolean - Whether the checkbox is disabled
- `required`: boolean - Whether the checkbox is required
- `id`: string - The id of the checkbox

**Example:**
```tsx
<Checkbox
  id="terms"
  onCheckedChange={(checked) => console.log(checked)}
/>
<label htmlFor="terms" className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
  Accept terms and conditions
</label>
```

## Switch

A switch that allows the user to toggle between checked and unchecked states.

**Installation:**
```bash
npx shadcn@latest add switch
```

**Props:**
- `checked`: boolean - Whether the switch is checked
- `onCheckedChange`: (checked: boolean) => void - Event handler for when the checked state changes
- `disabled`: boolean - Whether the switch is disabled
- `required`: boolean - Whether the switch is required

**Example:**
```tsx
<Switch id="airplane-mode" />
<Label htmlFor="airplane-mode">Airplane Mode</Label>
```