import { useCallback } from 'react'
import {
  ReactFlow,
  Background,
  BackgroundVariant,
  Controls,
  MiniMap,
  type Node,
} from '@xyflow/react'
import { ServiceNode } from './ServiceNode'
import { useGraph } from '@/hooks/useGraph'
import { useAppStore } from '@/store/useAppStore'
import { Skeleton } from '@/components/ui/skeleton'
import { Button } from '@/components/ui/button'

const nodeTypes = { service: ServiceNode }

export function FlowCanvas() {
  const setSelectedNodeId = useAppStore((s) => s.setSelectedNodeId)
  const setMobilePanelOpen = useAppStore((s) => s.setMobilePanelOpen)

  const {
    nodes,
    edges,
    onNodesChange,
    onEdgesChange,
    isLoading,
    isError,
    error,
    refetch,
    hasApp,
  } = useGraph()

  const onNodeClick = useCallback(
    (_: React.MouseEvent, node: Node) => {
      setSelectedNodeId(node.id)
      if (window.innerWidth < 1024) {
        setMobilePanelOpen(true)
      }
    },
    [setSelectedNodeId, setMobilePanelOpen],
  )

  const onPaneClick = useCallback(() => {
    setSelectedNodeId(null)
  }, [setSelectedNodeId])

  if (!hasApp) {
    return (
      <div className="flex h-full items-center justify-center text-sm text-[var(--color-muted-foreground)]">
        Select an app to view its graph
      </div>
    )
  }

  if (isLoading) {
    return (
      <div className="flex h-full flex-col gap-4 p-8">
        <Skeleton className="h-8 w-48" />
        <Skeleton className="h-full w-full" />
      </div>
    )
  }

  if (isError) {
    return (
      <div className="flex h-full flex-col items-center justify-center gap-3">
        <p className="text-sm text-[var(--color-destructive)]">
          {error?.message ?? 'Failed to load graph'}
        </p>
        <Button variant="outline" size="sm" onClick={refetch}>
          Retry
        </Button>
      </div>
    )
  }

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onNodeClick={onNodeClick}
      onPaneClick={onPaneClick}
      nodeTypes={nodeTypes}
      fitView
      deleteKeyCode={null}
      className="bg-[var(--color-background)]"
    >
      <Background variant={BackgroundVariant.Dots} gap={16} size={1} />
      <Controls />
      <MiniMap nodeStrokeWidth={3} className="!bg-white/90" zoomable pannable />
    </ReactFlow>
  )
}
