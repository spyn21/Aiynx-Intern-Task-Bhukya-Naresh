import { GraphProvider } from '@/components/canvas/GraphProvider'
import { FlowCanvas } from '@/components/canvas/FlowCanvas'
import { TopBarWithFit } from './TopBar'
import { LeftRail } from './LeftRail'
import { RightPanelContent } from './RightPanel'
import { useAppStore } from '@/store/useAppStore'
import { Sheet, SheetContent } from '@/components/ui/sheet'

export function AppLayout() {
  const isMobilePanelOpen = useAppStore((s) => s.isMobilePanelOpen)
  const setMobilePanelOpen = useAppStore((s) => s.setMobilePanelOpen)

  return (
    <GraphProvider>
      <div className="flex h-screen flex-col overflow-hidden">
        <TopBarWithFit />

        <div className="flex min-h-0 flex-1">
          <LeftRail />

          <main className="relative min-w-0 flex-1">
            <FlowCanvas />
          </main>

          <aside className="hidden w-80 shrink-0 border-l border-[var(--color-border)] lg:block">
            <RightPanelContent />
          </aside>
        </div>

        <Sheet open={isMobilePanelOpen} onOpenChange={setMobilePanelOpen}>
          <SheetContent side="right" className="w-full max-w-sm p-0">
            <RightPanelContent />
          </SheetContent>
        </Sheet>
      </div>
    </GraphProvider>
  )
}
