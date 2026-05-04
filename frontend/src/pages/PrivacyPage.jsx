import "./PrivacyPage.css";

export default function PrivacyPage() {
  return (
    <section className="privacy-page">
      <h1>Confidentialité</h1>

      <p className="privacy-page__intro">
        Text Analysis Service analyse les fichiers transmis par l’utilisateur
        afin de générer un retour automatisé sur la structure du CV, les
        compétences détectées et les pistes d’amélioration.
      </p>

      <h3>Données traitées</h3>
      <p>
        Les fichiers PDF peuvent contenir des données personnelles présentes
        dans un CV : identité, coordonnées, expériences, formations,
        compétences et informations professionnelles.
      </p>

      <h3>Conservation</h3>
      <p>
        Dans la version actuelle, les fichiers sont analysés à la demande par
        l’API et ne sont pas conservés par le service.
      </p>

      <h3>Finalité</h3>
      <p>
        Les données sont utilisées uniquement pour produire une analyse du
        document transmis.
      </p>

      <h3>Statut du projet</h3>
      <p>
        Ce projet est en cours de développement. Les mentions légales et la
        politique de confidentialité complète seront précisées avant toute mise
        en ligne publique.
      </p>
    </section>
  );
}
