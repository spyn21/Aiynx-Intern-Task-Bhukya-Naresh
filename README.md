# App Graph Builder

A responsive **App Graph Builder** UI built as a frontend intern take-home task. Visualize service dependency graphs with ReactFlow, inspect node configuration, and switch between apps with mocked API data.

## Setup

```bash
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173).

### Scripts

| Script       | Description                          |
| ------------ | ------------------------------------ |
| `npm run dev`      | Start Vite dev server                |
| `npm run build`    | Type-check and production build      |
| `npm run preview`  | Preview production build             |
| `npm run lint`     | Run ESLint                           |
| `npm run typecheck`| Run TypeScript compiler (no emit)    |

## Features

- **Layout**: Top bar, left icon rail, dotted ReactFlow canvas, right panel (apps list + node inspector)
- **Responsive**: Right panel becomes a slide-over drawer on screens below `lg` (1024px), toggled via Zustand
- **ReactFlow**: 3+ nodes per app, drag/select/delete (Delete/Backspace), zoom/pan, fit view on load + Fit button
- **Node Inspector**: Status pill, Config/Runtime tabs, synced slider + numeric input (0–100), editable name/description
- **TanStack Query**: Mock `GET /api/apps` and `GET /api/apps/:appId/graph` with loading, error, and cache
- **Zustand**: `selectedAppId`, `selectedNodeId`, `isMobilePanelOpen`, `activeInspectorTab`
- **MSW**: In-memory mock API with simulated latency (~600–800ms)

## Key Decisions

1. **GraphProvider** — Shared context wraps ReactFlow state so both the canvas and inspector can read/update node data without prop drilling.
2. **MSW over setTimeout wrappers** — Keeps fetch calls realistic and works in dev + preview builds.
3. **Inspector edits persist locally** — Changes update ReactFlow node `data` in memory; they are not sent back to the mock API (graph refetch resets edits).
4. **shadcn-style components** — Radix UI primitives with Tailwind, matching shadcn/ui patterns without the full CLI scaffold.

## Known Limitations

- Inspector edits are lost when switching apps or refetching the graph.
- Left rail navigation is static (non-functional placeholders).
- No persistence layer (localStorage/backend).
- MSW is used for all environments since there is no real backend.

## Tech Stack

- React 19 + Vite 8
- TypeScript (strict)
- @xyflow/react
- TanStack Query
- Zustand
- MSW
- Tailwind CSS v4 + Radix UI (shadcn-style)
