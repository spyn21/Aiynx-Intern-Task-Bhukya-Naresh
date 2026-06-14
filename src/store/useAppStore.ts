import { create } from 'zustand'
import type { InspectorTab } from '@/types'

interface AppState {
  selectedAppId: string | null
  selectedNodeId: string | null
  isMobilePanelOpen: boolean
  activeInspectorTab: InspectorTab
  simulateApiError: boolean

  setSelectedAppId: (appId: string) => void
  setSelectedNodeId: (nodeId: string | null) => void
  setMobilePanelOpen: (open: boolean) => void
  toggleMobilePanel: () => void
  setActiveInspectorTab: (tab: InspectorTab) => void
  setSimulateApiError: (value: boolean) => void
}

export const useAppStore = create<AppState>((set) => ({
  selectedAppId: null,
  selectedNodeId: null,
  isMobilePanelOpen: false,
  activeInspectorTab: 'config',
  simulateApiError: false,

  setSelectedAppId: (appId) =>
    set({ selectedAppId: appId, selectedNodeId: null }),
  setSelectedNodeId: (nodeId) => set({ selectedNodeId: nodeId }),
  setMobilePanelOpen: (open) => set({ isMobilePanelOpen: open }),
  toggleMobilePanel: () =>
    set((state) => ({ isMobilePanelOpen: !state.isMobilePanelOpen })),
  setActiveInspectorTab: (tab) => set({ activeInspectorTab: tab }),
  setSimulateApiError: (value) => set({ simulateApiError: value }),
}))

export const selectSelectedAppId = (state: AppState) => state.selectedAppId
export const selectSelectedNodeId = (state: AppState) => state.selectedNodeId
export const selectIsMobilePanelOpen = (state: AppState) =>
  state.isMobilePanelOpen
export const selectActiveInspectorTab = (state: AppState) =>
  state.activeInspectorTab
