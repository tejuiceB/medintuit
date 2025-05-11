import React, { useState } from "react";
import axios from "axios";

function ImageUpload() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    setResult(null);
    setError("");
    if (selected) {
      setPreview(URL.createObjectURL(selected));
    } else {
      setPreview(null);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    setError("");
    setResult(null);
    const formData = new FormData();
    formData.append("file", file);
    try {
      const res = await axios.post("http://127.0.0.1:8000/predict", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(res.data);
    } catch (err) {
      setError(err.response?.data?.detail || "Prediction failed.");
    }
    setLoading(false);
  };

  // Helper to render a more detailed explanation
  const renderExplanation = (result) => {
    if (!result) return null;
    return (
      <div style={{ marginTop: 12, fontSize: 15, color: "#1a3a5c" }}>
        <pre style={{
          background: "#f5faff",
          borderRadius: 8,
          padding: "10px 14px",
          whiteSpace: "pre-wrap",
          fontFamily: "inherit"
        }}>
          {result.explanation}
        </pre>
      </div>
    );
  };

  return (
    <div style={{
      maxWidth: 420,
      margin: "40px auto",
      padding: 32,
      background: "#fff",
      borderRadius: 12,
      boxShadow: "0 2px 16px rgba(0,0,0,0.08)",
      fontFamily: "Segoe UI, Arial, sans-serif"
    }}>
      <h2 style={{textAlign: "center", marginBottom: 24, color: "#2b4c7e"}}>MediScan: Chest X-ray Diagnosis</h2>
      <form onSubmit={handleSubmit} style={{display: "flex", flexDirection: "column", gap: 16}}>
        <label style={{fontWeight: 500, color: "#2b4c7e"}}>Select Chest X-ray Image</label>
        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          style={{marginBottom: 8}}
        />
        {preview && (
          <img
            src={preview}
            alt="Preview"
            style={{
              maxWidth: "100%",
              maxHeight: 220,
              margin: "0 auto 12px auto",
              display: "block",
              borderRadius: 8,
              border: "1px solid #e0e0e0"
            }}
          />
        )}
        <button
          type="submit"
          disabled={!file || loading}
          style={{
            background: "#2b4c7e",
            color: "#fff",
            border: "none",
            borderRadius: 6,
            padding: "10px 0",
            fontWeight: 600,
            fontSize: 16,
            cursor: loading ? "not-allowed" : "pointer",
            opacity: !file || loading ? 0.7 : 1
          }}
        >
          {loading ? "Predicting..." : "Predict"}
        </button>
      </form>
      {error && (
        <div style={{color: "#b00020", marginTop: 18, textAlign: "center"}}>
          <strong>Error:</strong> {error}
        </div>
      )}
      {result && (
        <div style={{
          marginTop: 24,
          padding: "16px 0",
          background: "#f5faff",
          borderRadius: 8,
          textAlign: "center",
          color: "#2b4c7e",
          fontSize: 18,
          fontWeight: 500,
          border: "1px solid #d0e6fa"
        }}>
          <div>
            <span>Prediction: </span>
            <span style={{fontWeight: 700, fontSize: 20}}>{result.prediction}</span>
          </div>
          <div style={{marginTop: 8, fontSize: 16}}>
            <span>Confidence: </span>
            <span style={{fontWeight: 600}}>{(result.confidence * 100).toFixed(2)}%</span>
          </div>
          {renderExplanation(result)}
        </div>
      )}
    </div>
  );
}

export default ImageUpload;
