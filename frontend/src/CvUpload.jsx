import { useState } from "react";
import axios from "axios";

export default function CvUpload() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(
      "http://127.0.0.1:8000/analyze/cv/pdf",
      formData
    );

    setResult(res.data);
  };

  return (
    <div>
      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload}>
        Analyser CV
      </button>

      {result && (
        <pre>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}