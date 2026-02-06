// Card Component Template
// Reusable card component with Tailwind CSS styling

interface CardProps {
  title: string
  description?: string
  children?: React.ReactNode
  className?: string
  onClick?: () => void
}

export function Card({ title, description, children, className = '', onClick }: CardProps) {
  return (
    <div
      className={`bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300 ${className}`}
      onClick={onClick}
    >
      <div className="p-6">
        <h3 className="text-xl font-bold text-gray-900 mb-2">{title}</h3>
        {description && <p className="text-gray-600 mb-4">{description}</p>}
        {children && <div className="mt-4">{children}</div>}
      </div>
    </div>
  )
}

// Usage Example:
// <Card title="My Card" description="Card description">
//   <button className="bg-blue-600 text-white px-4 py-2 rounded">Action</button>
// </Card>
