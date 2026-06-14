import { useReactFlow } from '@xyflow/react'
import { useQueryClient } from '@tanstack/react-query'
import { useAppStore } from '@/store/useAppStore'
import { setSimulateError } from '@/mocks/handlers'
import { Button } from '@/components/ui/button'
import {
  Maximize2,
  PanelRight,
  Share2,
  Workflow,
  AlertTriangle,
} from 'lucide-react'
import { cn } from '@/lib/utils'

interface TopBarProps {
  onFitView?: () => void
}

export function TopBar({ onFitView }: TopBarProps) {
  const queryClient = useQueryClient()
  const toggleMobilePanel = useAppStore((s) => s.toggleMobilePanel)
  const simulateApiError = useAppStore((s) => s.simulateApiError)
  const setSimulateApiError = useAppStore((s) => s.setSimulateApiError)

  const handleToggleError = () => {
    const next = !simulateApiError
    setSimulateApiError(next)
    setSimulateError(next)
    void queryClient.invalidateQueries()
  }

  return (
    <header className="flex h-14 shrink-0 items-center justify-between border-b border-[var(--color-border)] bg-white px-4">
      <div className="flex items-center gap-3">
        <div className="flex h-8 w-8 items-center justify-center rounded-md bg-[var(--color-primary)] text-white">
          <Workflow className="h-4 w-4" />
        </div>
        <div>
          <h1 className="text-sm font-semibold leading-none">App Graph Builder</h1>
          <p className="text-xs text-[var(--color-muted-foreground)]">
            Visualize service dependencies
          </p>
        </div>
      </div>

      <div className="flex items-center gap-2">
        <Button
          variant="outline"
          size="sm"
          className={cn(
            'hidden sm:inline-flex',
            simulateApiError && 'border-amber-500 text-amber-700',
          )}
          onClick={handleToggleError}
        >
          <AlertTriangle className="h-3.5 w-3.5" />
          {simulateApiError ? 'Errors On' : 'Simulate Error'}
        </Button>

        <Button variant="outline" size="sm" className="hidden sm:inline-flex">
          <Share2 className="h-3.5 w-3.5" />
          Share
        </Button>

        {onFitView && (
          <Button variant="outline" size="sm" onClick={onFitView}>
            <Maximize2 className="h-3.5 w-3.5" />
            <span className="hidden sm:inline">Fit</span>
          </Button>
        )}

        <Button
          variant="outline"
          size="icon"
          className="lg:hidden"
          onClick={toggleMobilePanel}
          aria-label="Toggle panel"
        >
          <PanelRight className="h-4 w-4" />
        </Button>
      </div>
    </header>
  )
}

export function TopBarWithFit() {
  const { fitView } = useReactFlow()

  return (
    <TopBar
      onFitView={() => {
        fitView({ padding: 0.2 })
      }}
    />
  )
}
