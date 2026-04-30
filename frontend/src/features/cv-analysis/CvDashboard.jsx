import "./CvDashboard.css";

export default function CvDashboard({ data }) {
  if (!data) return null;

  const { summary, analysis, insights, meta } = data;
  const skillsByCategory = analysis.skills_by_category || {};

  const metrics = [
    {
      label: "Structure",
      score: summary.structure_score,
      detail: analysis.sections_found.join(", ") || "Aucune section détectée",
    },
    {
      label: "Compétences",
      score: summary.skills_score,
      detail: `${analysis.skills_found.length} compétence(s) détectée(s)`,
    },
    {
      label: "Verbes d'action",
      score: summary.action_score,
      detail: analysis.action_verbs_found.join(", ") || "Aucun verbe détecté",
    },
  ];

  return (
    <section className="cv-dashboard">
      <div className="cv-dashboard__summary">
        <div>
          <p className="cv-dashboard__eyebrow">Résultat d'analyse</p>
          <h2 className="cv-dashboard__title">Score global du CV</h2>
        </div>

        <div className="cv-dashboard__score-block">
          <span className="cv-dashboard__score">{summary.global_score}</span>
          <span className="cv-dashboard__score-max">/100</span>
        </div>
      </div>

      <div className="cv-dashboard__grid">
        {metrics.map((metric) => (
          <article key={metric.label} className="cv-dashboard__card">
            <div className="cv-dashboard__card-header">
              <h3 className="cv-dashboard__card-title">{metric.label}</h3>
              <span className="cv-dashboard__card-score">
                {metric.score}/100
              </span>
            </div>

            <div className="cv-dashboard__progress-track">
              <div
                className="cv-dashboard__progress-bar"
                style={{ width: `${Math.min(metric.score, 100)}%` }}
              />
            </div>

            <p className="cv-dashboard__card-detail">{metric.detail}</p>
          </article>
        ))}
      </div>

      <div className="cv-dashboard__panel">
        <h3 className="cv-dashboard__panel-title">Compétences détectées</h3>

        {Object.keys(skillsByCategory).length > 0 ? (
          <div className="cv-dashboard__skill-groups">
            {Object.entries(skillsByCategory).map(([category, skills]) => (
              <div key={category} className="cv-dashboard__skill-group">
                <h4 className="cv-dashboard__skill-category">{category}</h4>

                {skills.length > 0 ? (
                  <div className="cv-dashboard__tags">
                    {skills.map((skill) => (
                      <span key={skill} className="cv-dashboard__tag">
                        {skill}
                      </span>
                    ))}
                  </div>
                ) : (
                  <p className="cv-dashboard__empty-text">Aucune compétence.</p>
                )}
              </div>
            ))}
          </div>
        ) : (
          <p className="cv-dashboard__empty-text">
            Aucune compétence détectée.
          </p>
        )}
      </div>

      <div className="cv-dashboard__panel">
        <h3 className="cv-dashboard__panel-title">Recommandations</h3>

        <ul className="cv-dashboard__insight-list">
          {insights.map((insight) => (
            <li key={insight} className="cv-dashboard__insight-item">
              {insight}
            </li>
          ))}
        </ul>
      </div>

      <div className="cv-dashboard__meta">
        {meta.word_count} mots · {meta.length} caractères
      </div>
    </section>
  );
}
