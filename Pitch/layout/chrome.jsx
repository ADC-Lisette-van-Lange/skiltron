/* global React */
const { useState, useEffect } = React;

/* ===== Hash-routing helpers ===== */
function parseHash() {
  return (window.location.hash || '#/').replace(/^#/, '') || '/';
}
function navigate(path) {
  window.location.hash = '#' + path;
  window.scrollTo({ top: 0, behavior: 'instant' });
}
function useRoute() {
  const [route, setRoute] = useState(parseHash());
  useEffect(() => {
    const fn = () => setRoute(parseHash());
    window.addEventListener('hashchange', fn);
    return () => window.removeEventListener('hashchange', fn);
  }, []);
  return route;
}

/* ===== Minimale icons (alleen wat de shell nodig heeft) ===== */
const SunIcon = () => (
  <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2">
    <circle cx="12" cy="12" r="4"/>
    <path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M5.6 18.4 7 17M17 7l1.4-1.4"/>
  </svg>
);
const MoonIcon = () => (
  <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2">
    <path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>
  </svg>
);

/* ===== Logobar ===== */
function Brandbar() {
  return (
    <header className="logobar">
      <img src="./logo.png" alt="Rijksoverheid" className="site-logo" />
    </header>
  );
}

/* ===== Navbar =====
   Voeg hier extra navigatie-items toe als array-objecten:
     { id: '/mijn-pagina', label: 'Mijn pagina' }
   De actieve tab wordt automatisch onderstreept op basis van de huidige route.
*/
function Navbar({ route, theme, setTheme }) {
  const navItems = [
    /* === VOEG HIER TABS TOE === */
    /* Voorbeeld: { id: '/assistent', label: 'Assistent' } */
  ];

  const isActive = (id) =>
    id === '/' ? route === '/' || route === '' : route === id || route.startsWith(id + '/');

  return (
    <nav className="navbar">
      <div className="container nav-inner">
        <div className="nav-links">
          {navItems.map(item => (
            <button
              key={item.id}
              className={'nav-link' + (isActive(item.id) ? ' active' : '')}
              onClick={() => navigate(item.id)}
            >
              {item.label}
            </button>
          ))}
        </div>
        <div className="nav-actions">
          <button
            className="nav-icon-btn"
            onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            title="Thema wisselen"
            aria-label="Thema wisselen"
          >
            {theme === 'dark' ? <SunIcon /> : <MoonIcon />}
          </button>
        </div>
      </div>
    </nav>
  );
}

/* ===== Footer ===== */
function Footer() {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-grid">
          <div>
            <h4>Raamwerk Digitale Assistenten</h4>
            <p style={{ margin: 0, maxWidth: 480 }}>
              Een handreiking voor overheidsorganisaties om digitale assistenten verantwoord,
              veilig en effectief in te zetten. Beheerd door ICTU in samenwerking met
              Digicampus en ADC.
            </p>
          </div>
          <div>
            <h4>Verken</h4>
            <ul>
              <li><a href="#/domeinen">Domeinen</a></li>
              <li><a href="#/practices">Good Practices</a></li>
              <li><a href="#/over">Over dit raamwerk</a></li>
            </ul>
          </div>
          <div>
            <h4>Contact</h4>
            <ul>
              <li><a href="#">placeholder: email</a></li>
              <li><a href="#">placeholder: ICTU</a></li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  );
}

/* ===== Exports ===== */
Object.assign(window, { Brandbar, Navbar, Footer, useRoute, navigate });
