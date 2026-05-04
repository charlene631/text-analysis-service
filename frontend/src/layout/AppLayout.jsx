import "./AppLayout.css";

export default function AppLayout({ children }) {
  return (
    <div className="app-layout">
      <header className="app-layout__header">
        <div className="app-layout__container app-layout__header-inner">
          <div>
            <p className="app-layout__eyebrow">Open source CV analyzer</p>
            <h1 className="app-layout__brand">Text Analysis Service</h1>
          </div>
        </div>
      </header>

      <main className="app-layout__container app-layout__main">
        {children}
      </main>

      <footer className="app-layout__footer">
        <div className="app-layout__container app-layout__footer-inner">
          <div>
            <strong>Text Analysis Service</strong>
            <p>
              © 2026 Charlène Gausset. Projet open source d’analyse de CV. Les fichiers sont traités à
              la demande et ne sont pas conservés dans la version actuelle.
            </p>
          </div>

          <div className="app-layout__footer-links">
            <a href="/privacy">Confidentialité</a>
            <span>Mentions légales à venir</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
