export default function CvDashboard({ data }) {
  if (!data) return null;

  const { summary, analysis, insights, meta } = data;

  return (
    <div style={styles.container}>

      {/* SCORE GLOBAL */}
      <div style={styles.heroCard}>
        <div style={styles.label}>Score global</div>
        <div style={styles.bigScore}>
          {summary.global_score}
          <span style={styles.small}>/100</span>
        </div>
      </div>

      {/* GRID KPI */}
      <div style={styles.grid}>

        <div style={styles.card}>
          <h3>Structure</h3>
          <p>{summary.structure_score}/100</p>
          <p>{analysis.sections_found.join(", ") || "—"}</p>
        </div>

        <div style={styles.card}>
          <h3>Compétences</h3>
          <p>{summary.skills_score}/100</p>
          <div style={styles.tags}>
            {analysis.skills_found.map((s, i) => (
              <span key={i} style={styles.tag}>{s}</span>
            ))}
          </div>
        </div>

        <div style={styles.card}>
          <h3>Action verbs</h3>
          <p>{summary.action_score}/100</p>
          <p>{analysis.action_verbs_found.join(", ") || "—"}</p>
        </div>

      </div>

      {/* INSIGHTS */}
      <div style={styles.insights}>
        <h3>Recommandations</h3>
        <ul>
          {insights.map((i) => (
            <li key={i}>{i}</li>
          ))}
        </ul>
      </div>

      {/* META */}
      <div style={styles.meta}>
        {meta.word_count} mots • {meta.length} caractères
      </div>

    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    gap: 20,
    marginTop: 20,
  },

  heroCard: {
    padding: 24,
    borderRadius: 16,
    background: "#111",
    color: "white",
    textAlign: "center",
  },

  label: {
    opacity: 0.6,
  },

  bigScore: {
    fontSize: 56,
    fontWeight: "bold",
  },

  small: {
    fontSize: 20,
    opacity: 0.6,
    marginLeft: 6,
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: 16,
  },

  card: {
    padding: 16,
    borderRadius: 12,
    background: "#1e1e1e",
    color: "white",
  },

  tags: {
    display: "flex",
    flexWrap: "wrap",
    gap: 6,
    marginTop: 8,
  },

  tag: {
    background: "#333",
    padding: "4px 8px",
    borderRadius: 8,
    fontSize: 12,
  },

  insights: {
    padding: 16,
    borderRadius: 12,
    background: "#0f0f0f",
    color: "white",
  },

  meta: {
    opacity: 0.5,
    fontSize: 12,
    textAlign: "right",
  },
};