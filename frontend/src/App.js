import React from "react";
import ImageUpload from "./ImageUpload";

function App() {
  return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(120deg, #e0eafc 0%, #cfdef3 100%)",
      padding: 0,
      margin: 0
    }}>
      <ImageUpload />
      <footer style={{
        textAlign: "center",
        marginTop: 40,
        color: "#888",
        fontSize: 14
      }}>
        <span>© {new Date().getFullYear()} MediScan &mdash; AI-powered Chest X-ray Diagnosis</span>
      </footer>
    </div>
  );
}

export default App;
