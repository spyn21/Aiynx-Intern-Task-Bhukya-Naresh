import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  type ReactNode,
} from 'react'
import {
  ReactFlowProvider,
  useNodesState,
  useEdgesState,
  useReactFlow,
  type Node,
  type Edge,
} from '@xyflow/react'
import { GraphContext, type GraphContextValue } from './graph-context'
import { useAppStore } from '@/store/useAppStore'
import { useAppGraph } from '@/hooks/useAppGraph'
import type { ServiceNode, ServiceNodeData } from '@/types'

function GraphStateProvider({ children }: { children: ReactNode }) {
  const selectedAppId = useAppStore((s) => s.selectedAppId)
  const selectedNodeId = useAppStore((s) => s.selectedNodeId)
  const setSelectedNodeId = useAppStore((s) => s.setSelectedNodeId)

  const { data, isLoading, isError, error, refetch } = useAppGraph(selectedAppId)
  const { fitView } = useReactFlow()

  const [nodes, setNodes, onNodesChange] = useNodesState<Node<ServiceNodeData>>([])
  const [edges, setEdges, onEdgesChange] = useEdgesState<Edge>([])
  const hasFitView = useRef(false)

  useEffect(() => {
    if (data) {
      setNodes(data.nodes)
      setEdges(data.edges)
      hasFitView.current = false
    }
  }, [data, setNodes, setEdges])

  useEffect(() => {
    if (nodes.length > 0 && !hasFitView.current) {
      requestAnimationFrame(() => {
        fitView({ padding: 0.2 })
        hasFitView.current = true
      })
    }
  }, [nodes, fitView])

  useEffect(() => {
    setNodes((nds) =>
      nds.map((node) => ({
        ...node,
        selected: node.id === selectedNodeId,
      })),
    )
  }, [selectedNodeId, setNodes])

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key !== 'Delete' && event.key !== 'Backspace') return
      if (!selectedNodeId) return

      const target = event.target as HTMLElement
      if (
        target.tagName === 'INPUT' ||
        target.tagName === 'TEXTAREA' ||
        target.isContentEditable
      ) {
        return
      }

      event.preventDefault()
      setNodes((nds) => nds.filter((n) => n.id !== selectedNodeId))
      setEdges((eds) =>
        eds.filter(
          (e) => e.source !== selectedNodeId && e.target !== selectedNodeId,
        ),
      )
      setSelectedNodeId(null)
    }

    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [selectedNodeId, setNodes, setEdges, setSelectedNodeId])

  const selectedNode = useMemo(
    () =>
      (nodes.find((n) => n.id === selectedNodeId) as ServiceNode | undefined) ??
      null,
    [nodes, selectedNodeId],
  )

  const updateNodeData = useCallback(
    (partial: Partial<ServiceNodeData>) => {
      if (!selectedNodeId) return
      setNodes((nds) =>
        nds.map((node) =>
          node.id === selectedNodeId
            ? { ...node, data: { ...node.data, ...partial } }
            : node,
        ),
      )
    },
    [selectedNodeId, setNodes],
  )

  const value: GraphContextValue = {
    nodes: nodes as ServiceNode[],
    edges,
    selectedNode,
    updateNodeData,
    onNodesChange,
    onEdgesChange,
    setNodes,
    setEdges,
    isLoading,
    isError,
    error: error as Error | null,
    refetch: () => void refetch(),
    hasApp: Boolean(selectedAppId),
  }

  return (
    <GraphContext.Provider value={value}>{children}</GraphContext.Provider>
  )
}

export function GraphProvider({ children }: { children: ReactNode }) {
  return (
    <ReactFlowProvider>
      <GraphStateProvider>{children}</GraphStateProvider>
    </ReactFlowProvider>
  )
}
