import { useState } from "react";
import { api } from "../../api/client";

export default function CvUpload({ onResult }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const { data } = await api.post(
      "/analyze/cv/pdf",
      formData
    );

    onResult(data);
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
    </div>
  );
}