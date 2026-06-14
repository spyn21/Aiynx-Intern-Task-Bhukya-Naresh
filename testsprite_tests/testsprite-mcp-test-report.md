# TestSprite AI Testing Report(MCP)

---

## 1️⃣ Document Metadata
- **Project Name:** Assessment (App Graph Builder)
- **Date:** 2026-06-13
- **Prepared by:** TestSprite AI Team

---

## 2️⃣ Requirement Validation Summary

### Requirement: App Selection
- **Description:** Browse mock applications and switch the graph view to the selected app.

#### Test TC001 Load and select an application
- **Test Code:** [TC001_Load_and_select_an_application.py](./TC001_Load_and_select_an_application.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/14fda675-c24d-4e3d-b6ae-690e79300e1b
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Apps list loads via MSW mock API, first app auto-selects, and the dependency graph renders correctly with the selected app highlighted.

---

#### Test TC006 Recover apps list after loading error
- **Test Code:** [TC006_Recover_apps_list_after_loading_error.py](./TC006_Recover_apps_list_after_loading_error.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/586ff5ff-ea15-48fd-84d9-33c2e2f72c53
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Simulated API error mode correctly shows an error state in the apps list; disabling error mode and retrying restores the apps list.

---

#### Test TC011 Switch to another application
- **Test Code:** [TC011_Switch_to_another_application.py](./TC011_Switch_to_another_application.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/88346ebd-70d7-489a-9ad5-cda06aff55df
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Switching between Checkout, Analytics, and Auth apps updates the selection highlight and refreshes the graph for the newly selected app.

---

### Requirement: Graph Canvas
- **Description:** View and interact with the service dependency graph for the selected application.

#### Test TC002 Load a mock app graph
- **Test Code:** [TC002_Load_a_mock_app_graph.py](./TC002_Load_a_mock_app_graph.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/6e6a0b0a-23e0-4949-8296-f992030ce24b
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Selecting a mock app renders the ReactFlow graph with visible service nodes and connecting edges.

---

#### Test TC003 View and interact with the service graph
- **Test Code:** [TC003_View_and_interact_with_the_service_graph.py](./TC003_View_and_interact_with_the_service_graph.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/c7484252-6328-4cf2-a57b-73affe19ec31
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Pan, zoom, and Fit-to-view controls work as expected; the graph remains visible and usable after viewport adjustments.

---

#### Test TC007 Recover graph after loading error
- **Test Code:** [TC007_Recover_graph_after_loading_error.py](./TC007_Recover_graph_after_loading_error.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/9303650b-d88e-4692-aeca-03001e65244b
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Graph error state displays correctly under simulated API failures; retry after disabling error mode successfully reloads the graph.

---

#### Test TC008 Select and clear a service node
- **Test Code:** [TC008_Select_and_clear_a_service_node.py](./TC008_Select_and_clear_a_service_node.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/5b904658-473b-4f8d-b6a2-ce8bc62e208d
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Clicking a service node selects it and opens the inspector; clicking the canvas background clears the selection.

---

#### Test TC010 Use graph controls to inspect the canvas
- **Test Code:** [TC010_Use_graph_controls_to_inspect_the_canvas.py](./TC010_Use_graph_controls_to_inspect_the_canvas.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/cbe02b11-cd27-44c3-bc63-bc13544d2601
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** ReactFlow zoom controls, Fit button, and pan gestures all function correctly on the dotted canvas.

---

#### Test TC019 Switch apps and refresh the graph
- **Test Code:** [TC019_Switch_apps_and_refresh_the_graph.py](./TC019_Switch_apps_and_refresh_the_graph.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/542b413d-4e89-4d46-8956-85bde0fd6bca
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Graph data refreshes correctly when switching between mock applications; node layout and edges match the selected app's mock data.

---

### Requirement: Node Inspector
- **Description:** Inspect a selected service node and edit its configuration and runtime values.

#### Test TC009 Open the node inspector and switch tabs
- **Test Code:** [TC009_Open_the_node_inspector_and_switch_tabs.py](./TC009_Open_the_node_inspector_and_switch_tabs.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/14cbcfc7-6f54-484a-81f5-044c4cd4eecc
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Selecting a node opens the right-panel inspector; Config and Runtime tabs switch correctly and display the appropriate content.

---

#### Test TC012 Edit node details in the inspector
- **Test Code:** [TC012_Edit_node_details_in_the_inspector.py](./TC012_Edit_node_details_in_the_inspector.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/1389e71a-5bab-447a-9c54-96ef4659963d
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Node name and description fields are editable and changes reflect immediately in the inspector UI.

---

#### Test TC013 Open the node inspector from a selected service
- **Test Code:** [TC013_Open_the_node_inspector_from_a_selected_service.py](./TC013_Open_the_node_inspector_from_a_selected_service.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/14482239-a4e0-4a24-9238-cf4daa9d0c1f
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Clicking a service node on the canvas opens the inspector with the correct node ID, status pill, and configuration fields.

---

#### Test TC014 Keep load controls in sync
- **Test Code:** [TC014_Keep_load_controls_in_sync.py](./TC014_Keep_load_controls_in_sync.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/1a3cfcf3-2f05-46f2-af1f-64ae3730c8d4
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** The synced slider and numeric load input stay in sync when adjusted from either control; updated values appear in the inspector.

---

#### Test TC016 Switch inspector tabs for runtime details
- **Test Code:** [TC016_Switch_inspector_tabs_for_runtime_details.py](./TC016_Switch_inspector_tabs_for_runtime_details.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/23e52656-e610-46e5-8388-c825347b4919
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Runtime tab shows status, load percentage, and service type; switching back to Config tab restores editable fields.

---

#### Test TC018 View runtime status and metrics for a node
- **Test Code:** [TC018_View_runtime_status_and_metrics_for_a_node.py](./TC018_View_runtime_status_and_metrics_for_a_node.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/e6e210a1-935a-4296-b9ed-8ed41ecceb4f
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Status pill (healthy/degraded/down) and runtime metrics display correctly on the Runtime tab for selected nodes.

---

#### Test TC020 Reset local inspector edits when switching apps
- **Test Code:** [TC020_Reset_local_inspector_edits_when_switching_apps.py](./TC020_Reset_local_inspector_edits_when_switching_apps.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/9e98b558-7856-4c87-91e1-0daf721c4762
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Local inspector edits are correctly reset when switching away and back to an app, confirming the known in-memory-only persistence behavior works as designed.

---

### Requirement: Simulate API Error
- **Description:** Toggle mock error mode to observe loading and error states for apps and graph data.

#### Test TC004 Recover the applications list after simulated errors
- **Test Code:** [TC004_Recover_the_applications_list_after_simulated_errors.py](./TC004_Recover_the_applications_list_after_simulated_errors.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/c36c78e8-64ba-4e46-b778-cf42ec4836e6
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** The Simulate Error toggle in the top bar correctly triggers apps list failure; disabling it and retrying restores normal loading.

---

#### Test TC005 Recover the graph after simulated errors
- **Test Code:** [TC005_Recover_the_graph_after_simulated_errors.py](./TC005_Recover_the_graph_after_simulated_errors.py)
- **Test Error:** 
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/d2b32713-b498-47ef-a706-de052ac58c7c
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Graph area shows error state when simulated errors are enabled mid-session; recovery works after toggling errors off and retrying.

---

### Requirement: Mobile Panel
- **Description:** Responsive slide-over panel for apps list and node inspector on smaller screens.

#### Test TC015 Open the mobile drawer and inspect a node
- **Test Code:** [TC015_Open_the_mobile_drawer_and_inspect_a_node.py](./TC015_Open_the_mobile_drawer_and_inspect_a_node.py)
- **Test Error:** TEST BLOCKED — The mobile slide-over inspector could not be reached. The UI appears to present the node inspector only as a desktop right-side drawer and no responsive/mobile control was found to open a slide-over panel.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/87756830-7067-4e49-95f8-ae9bdc908154
- **Status:** ⛔ Blocked
- **Severity:** MEDIUM
- **Analysis / Findings:** TestSprite ran at desktop viewport and could not resize to a mobile breakpoint. The mobile panel toggle (`PanelRight` button, visible below `lg`/1024px) was not accessible. Manual verification at viewport widths under 1024px is recommended.

---

#### Test TC017 Auto-open the mobile panel when selecting a node
- **Test Code:** [TC017_Auto_open_the_mobile_panel_when_selecting_a_node.py](./TC017_Auto_open_the_mobile_panel_when_selecting_a_node.py)
- **Test Error:** TEST BLOCKED — No UI control or toggle to change to a mobile/small-screen viewport was present on the page.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/950ffa96-c535-47a8-acaa-98e4f32e519d/46aea708-5e20-4c05-b354-600e156c65a5
- **Status:** ⛔ Blocked
- **Severity:** MEDIUM
- **Analysis / Findings:** Same viewport limitation as TC015. The auto-open behavior (implemented in `FlowCanvas.tsx` when `window.innerWidth < 1024`) requires a mobile viewport to test and could not be exercised by the cloud runner.

---

## 3️⃣ Coverage & Matching Metrics

- **90%** of tests passed (18 passed, 0 failed, 2 blocked out of 20 total)

| Requirement          | Total Tests | ✅ Passed | ❌ Failed | ⛔ Blocked |
|----------------------|-------------|-----------|-----------|------------|
| App Selection          | 3           | 3         | 0         | 0          |
| Graph Canvas           | 6           | 6         | 0         | 0          |
| Node Inspector         | 7           | 7         | 0         | 0          |
| Simulate API Error     | 2           | 2         | 0         | 0          |
| Mobile Panel           | 2           | 0         | 0         | 2          |
| **Total**              | **20**      | **18**    | **0**     | **2**      |

---

## 4️⃣ Key Gaps / Risks

> 90% of tests passed (18/20). No functional failures were detected in desktop testing.

**Risks and gaps identified:**

1. **Mobile/responsive behavior untested** — TC015 and TC017 were blocked because TestSprite could not switch to a mobile viewport. The slide-over panel (`Sheet` component) and auto-open-on-node-select logic need manual verification at widths below 1024px.

2. **Inspector edits are not persisted** — TC020 confirms edits reset when switching apps (by design). This is documented as a known limitation but may surprise users expecting save behavior.

3. **Non-functional UI elements** — Left rail navigation icons and the Share button in the top bar are placeholders with no actions attached; these were not covered by the test plan.

4. **Node deletion disabled** — `deleteKeyCode` is set to `null` in FlowCanvas, so keyboard deletion of nodes is intentionally disabled and untested.

**Recommendations:**

- Manually test mobile panel behavior using browser dev tools at 375px/768px widths.
- Consider adding Playwright viewport configuration to future TestSprite runs for mobile test cases.
- Add explicit `data-testid` attributes on key controls (app list items, Simulate Error button, panel toggle) to improve automated test reliability.

---
