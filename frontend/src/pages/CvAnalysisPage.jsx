import { useState } from "react";
import CvUpload from "../features/cv-analysis/CvUpload";
import CvDashboard from "../features/cv-analysis/CvDashboard";

export default function CvAnalysisPage() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ padding: 20 }}>
      <h1>Analyse CV</h1>

      <CvUpload onResult={setResult} />

      <CvDashboard data={result} />
    </div>
  );
}