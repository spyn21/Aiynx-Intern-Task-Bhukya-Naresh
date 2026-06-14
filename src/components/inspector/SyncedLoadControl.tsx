import { useCallback } from 'react'
import { Label } from '@/components/ui/label'
import { Input } from '@/components/ui/input'
import { Slider } from '@/components/ui/slider'

interface SyncedLoadControlProps {
  value: number
  onChange: (value: number) => void
}

function clamp(value: number): number {
  return Math.min(100, Math.max(0, value))
}

export function SyncedLoadControl({ value, onChange }: SyncedLoadControlProps) {
  const handleSliderChange = useCallback(
    (values: number[]) => {
      onChange(clamp(values[0] ?? 0))
    },
    [onChange],
  )

  const handleInputChange = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      const parsed = Number.parseInt(event.target.value, 10)
      if (Number.isNaN(parsed)) {
        onChange(0)
        return
      }
      onChange(clamp(parsed))
    },
    [onChange],
  )

  return (
    <div className="space-y-3">
      <Label htmlFor="load-percent">Load (%)</Label>
      <div className="flex items-center gap-4">
        <Slider
          value={[value]}
          onValueChange={handleSliderChange}
          max={100}
          step={1}
          className="flex-1"
        />
        <Input
          id="load-percent"
          type="number"
          min={0}
          max={100}
          value={value}
          onChange={handleInputChange}
          className="w-20"
        />
      </div>
    </div>
  )
}
