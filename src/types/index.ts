import type { Edge, Node } from '@xyflow/react'

export type NodeStatus = 'healthy' | 'degraded' | 'down'

export type InspectorTab = 'config' | 'runtime'

export interface ServiceNodeData extends Record<string, unknown> {
  label: string
  description?: string
  status: NodeStatus
  loadPercent: number
}

export type ServiceNode = Node<ServiceNodeData, 'service'>

export interface AppSummary {
  id: string
  name: string
  description: string
}

export interface AppGraph {
  nodes: ServiceNode[]
  edges: Edge[]
}
