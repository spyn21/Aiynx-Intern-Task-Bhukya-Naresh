import { AppSelector } from '@/components/apps/AppSelector'
import { NodeInspector } from '@/components/inspector/NodeInspector'
import { Separator } from '@/components/ui/separator'

export function RightPanelContent() {
  return (
    <div className="flex h-full flex-col overflow-hidden bg-white">
      <AppSelector />
      <Separator />
      <div className="flex min-h-0 flex-1 flex-col">
        <div className="border-b border-[var(--color-border)] px-4 py-2">
          <h2 className="text-xs font-semibold uppercase tracking-wide text-[var(--color-muted-foreground)]">
            Node Inspector
          </h2>
        </div>
        <NodeInspector />
      </div>
    </div>
  )
}
