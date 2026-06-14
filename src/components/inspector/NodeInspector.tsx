import { useCallback } from 'react'
import { StatusPill } from './StatusPill'
import { SyncedLoadControl } from './SyncedLoadControl'
import { useGraph } from '@/hooks/useGraph'
import { useAppStore } from '@/store/useAppStore'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Label } from '@/components/ui/label'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import type { InspectorTab } from '@/types'

export function NodeInspector() {
  const { selectedNode, updateNodeData } = useGraph()
  const activeTab = useAppStore((s) => s.activeInspectorTab)
  const setActiveInspectorTab = useAppStore((s) => s.setActiveInspectorTab)

  const handleTabChange = useCallback(
    (value: string) => {
      setActiveInspectorTab(value as InspectorTab)
    },
    [setActiveInspectorTab],
  )

  if (!selectedNode) {
    return (
      <div className="flex flex-1 items-center justify-center p-6 text-center text-sm text-[var(--color-muted-foreground)]">
        Select a node on the canvas to inspect its configuration
      </div>
    )
  }

  const { data } = selectedNode

  return (
    <div className="flex flex-1 flex-col overflow-hidden">
      <div className="border-b border-[var(--color-border)] px-4 py-3">
        <div className="flex items-center justify-between gap-2">
          <h3 className="text-sm font-semibold">Service Node</h3>
          <StatusPill status={data.status} />
        </div>
        <p className="mt-1 text-xs text-[var(--color-muted-foreground)]">
          ID: {selectedNode.id}
        </p>
      </div>

      <Tabs
        value={activeTab}
        onValueChange={handleTabChange}
        className="flex flex-1 flex-col overflow-hidden px-4 py-3"
      >
        <TabsList className="w-full">
          <TabsTrigger value="config" className="flex-1">
            Config
          </TabsTrigger>
          <TabsTrigger value="runtime" className="flex-1">
            Runtime
          </TabsTrigger>
        </TabsList>

        <TabsContent value="config" className="flex-1 space-y-4 overflow-y-auto">
          <div className="space-y-2">
            <Label htmlFor="node-name">Node name</Label>
            <Input
              id="node-name"
              value={data.label}
              onChange={(e) => updateNodeData({ label: e.target.value })}
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="node-description">Description</Label>
            <Textarea
              id="node-description"
              value={data.description ?? ''}
              onChange={(e) => updateNodeData({ description: e.target.value })}
              rows={3}
            />
          </div>

          <SyncedLoadControl
            value={data.loadPercent}
            onChange={(loadPercent) => updateNodeData({ loadPercent })}
          />
        </TabsContent>

        <TabsContent value="runtime" className="flex-1 space-y-4 overflow-y-auto">
          <div className="rounded-md border border-[var(--color-border)] p-3 text-sm">
            <div className="flex justify-between py-1">
              <span className="text-[var(--color-muted-foreground)]">Status</span>
              <StatusPill status={data.status} />
            </div>
            <div className="flex justify-between py-1">
              <span className="text-[var(--color-muted-foreground)]">Load</span>
              <span className="font-medium">{data.loadPercent}%</span>
            </div>
            <div className="flex justify-between py-1">
              <span className="text-[var(--color-muted-foreground)]">Type</span>
              <span className="font-medium">service</span>
            </div>
          </div>

          <SyncedLoadControl
            value={data.loadPercent}
            onChange={(loadPercent) => updateNodeData({ loadPercent })}
          />
        </TabsContent>
      </Tabs>
    </div>
  )
}
