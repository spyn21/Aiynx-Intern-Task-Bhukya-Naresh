import { memo } from 'react'
import { Handle, Position, type NodeProps } from '@xyflow/react'
import { cn } from '@/lib/utils'
import type { ServiceNodeData } from '@/types'

const statusDot: Record<ServiceNodeData['status'], string> = {
  healthy: 'bg-emerald-500',
  degraded: 'bg-amber-500',
  down: 'bg-red-500',
}

function ServiceNodeComponent({ data, selected }: NodeProps) {
  const nodeData = data as ServiceNodeData

  return (
    <div
      className={cn(
        'min-w-[160px] rounded-lg border-2 bg-white px-4 py-3 shadow-sm transition-shadow',
        selected
          ? 'border-[var(--color-primary)] shadow-md'
          : 'border-[var(--color-border)]',
      )}
    >
      <Handle type="target" position={Position.Left} className="!bg-[var(--color-primary)]" />
      <div className="flex items-center gap-2">
        <span
          className={cn('h-2 w-2 shrink-0 rounded-full', statusDot[nodeData.status])}
        />
        <span className="text-sm font-semibold">{nodeData.label}</span>
      </div>
      {nodeData.description && (
        <p className="mt-1 text-xs text-[var(--color-muted-foreground)] line-clamp-2">
          {nodeData.description}
        </p>
      )}
      <Handle type="source" position={Position.Right} className="!bg-[var(--color-primary)]" />
    </div>
  )
}

export const ServiceNode = memo(ServiceNodeComponent)
