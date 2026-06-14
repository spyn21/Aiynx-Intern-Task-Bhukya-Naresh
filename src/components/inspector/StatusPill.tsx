import { Badge } from '@/components/ui/badge'
import type { NodeStatus } from '@/types'

const statusConfig: Record<
  NodeStatus,
  { label: string; variant: 'healthy' | 'degraded' | 'down' }
> = {
  healthy: { label: 'Healthy', variant: 'healthy' },
  degraded: { label: 'Degraded', variant: 'degraded' },
  down: { label: 'Down', variant: 'down' },
}

interface StatusPillProps {
  status: NodeStatus
}

export function StatusPill({ status }: StatusPillProps) {
  const config = statusConfig[status]
  return <Badge variant={config.variant}>{config.label}</Badge>
}
