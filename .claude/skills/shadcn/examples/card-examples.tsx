import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export function FeatureCards() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
      <Card>
        <CardHeader>
          <CardTitle>Basic Plan</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold">$0<span className="text-sm font-normal">/month</span></div>
          <ul className="mt-4 space-y-2">
            <li className="flex items-center">
              <Badge variant="secondary" className="mr-2">✓</Badge>
              <span>Up to 3 projects</span>
            </li>
            <li className="flex items-center">
              <Badge variant="secondary" className="mr-2">✓</Badge>
              <span>1GB storage</span>
            </li>
            <li className="flex items-center text-muted-foreground">
              <Badge variant="outline" className="mr-2">✗</Badge>
              <span>Advanced analytics</span>
            </li>
          </ul>
          <Button className="w-full mt-4">Get Started</Button>
        </CardContent>
      </Card>

      <Card className="border-2 border-primary">
        <CardHeader>
          <Badge variant="default" className="w-fit mb-2">POPULAR</Badge>
          <CardTitle>Pro Plan</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold">$15<span className="text-sm font-normal">/month</span></div>
          <ul className="mt-4 space-y-2">
            <li className="flex items-center">
              <Badge variant="secondary" className="mr-2">✓</Badge>
              <span>Unlimited projects</span>
            </li>
            <li className="flex items-center">
              <Badge variant="secondary" className="mr-2">✓</Badge>
              <span>10GB storage</span>
            </li>
            <li className="flex items-center">
              <Badge variant="secondary" className="mr-2">✓</Badge>
              <span>Advanced analytics</span>
            </li>
          </ul>
          <Button className="w-full mt-4 bg-primary hover:bg-primary/90">Upgrade Now</Button>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Enterprise</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold">Custom</div>
          <ul className="mt-4 space-y-2">
            <li className="flex items-center">
              <Badge variant="secondary" className="mr-2">✓</Badge>
              <span>Unlimited everything</span>
            </li>
            <li className="flex items-center">
              <Badge variant="secondary" className="mr-2">✓</Badge>
              <span>Dedicated support</span>
            </li>
            <li className="flex items-center">
              <Badge variant="secondary" className="mr-2">✓</Badge>
              <span>Custom integrations</span>
            </li>
          </ul>
          <Button variant="outline" className="w-full mt-4">Contact Sales</Button>
        </CardContent>
      </Card>
    </div>
  )
}