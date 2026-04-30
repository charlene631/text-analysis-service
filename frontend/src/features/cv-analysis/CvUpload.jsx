import { useState } from "react";
import { api } from "../../api/client";
import "./CvUpload.css";

export default function CvUpload({ onResult }) {
  const [file, setFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];

    setFile(selectedFile);
    setError("");
  };

  const handleUpload = async () => {
    if (!file || isLoading) return;

    setIsLoading(true);
    setError("");

    try {
      const formData = new FormData();
      formData.append("file", file);

      const { data } = await api.post("/analyze/cv/pdf", formData);

      onResult(data);
    } catch (err) {
      const message =
        err.response?.data?.detail ||
        "Une erreur est survenue pendant l'analyse du CV.";

      setError(message);
      onResult(null);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <section className="cv-upload">
      <div>
        <h2 className="cv-upload__title">Importer un CV</h2>
        <p className="cv-upload__description">
          Sélectionnez un fichier PDF pour générer une analyse structurée.
        </p>
      </div>

      <label className="cv-upload__file-input">
        <input
          type="file"
          accept="application/pdf"
          onChange={handleFileChange}
          className="cv-upload__hidden-input"
        />
        <span>{file ? file.name : "Choisir un fichier PDF"}</span>
      </label>

      {error && <p className="cv-upload__error">{error}</p>}

      <button
        type="button"
        onClick={handleUpload}
        disabled={!file || isLoading}
        className="cv-upload__button"
      >
        {isLoading ? "Analyse en cours..." : "Analyser le CV"}
      </button>
    </section>
  );
}
