import { createContext } from 'react'
import type { useNodesState, useEdgesState } from '@xyflow/react'
import type { Edge, Node } from '@xyflow/react'
import type { ServiceNode, ServiceNodeData } from '@/types'

export interface GraphContextValue {
  nodes: ServiceNode[]
  edges: Edge[]
  selectedNode: ServiceNode | null
  updateNodeData: (partial: Partial<ServiceNodeData>) => void
  onNodesChange: ReturnType<typeof useNodesState<Node<ServiceNodeData>>>[2]
  onEdgesChange: ReturnType<typeof useEdgesState<Edge>>[2]
  setNodes: ReturnType<typeof useNodesState<Node<ServiceNodeData>>>[1]
  setEdges: ReturnType<typeof useEdgesState<Edge>>[1]
  isLoading: boolean
  isError: boolean
  error: Error | null
  refetch: () => void
  hasApp: boolean
}

export const GraphContext = createContext<GraphContextValue | null>(null)
