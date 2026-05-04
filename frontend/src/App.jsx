import AppLayout from "./layout/AppLayout";
import CvAnalysisPage from "./pages/CvAnalysisPage";
import PrivacyPage from "./pages/PrivacyPage";

export default function App() {
  const path = globalThis.location.pathname;

  return (
    <AppLayout>
      {path === "/privacy" ? <PrivacyPage /> : <CvAnalysisPage />}
    </AppLayout>
  );
}