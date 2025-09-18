import React, { useState } from 'react';
import './Header.css';

interface HeaderProps {
  currentPage: string;
  onNavigate: (page: string) => void;
}

const Header: React.FC<HeaderProps> = ({ currentPage, onNavigate }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const navigationItems = [
    { id: 'home', label: 'Home', labelDe: 'Startseite' },
    { id: 'about', label: 'About', labelDe: 'Über mich' },
    { id: 'projects', label: 'Projects', labelDe: 'Projekte' },
    { id: 'contact', label: 'Contact', labelDe: 'Kontakt' },
  ];

  const handleNavClick = (pageId: string) => {
    onNavigate(pageId);
    setIsMenuOpen(false);
  };

  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          {/* Logo/Name */}
          <div className="logo" onClick={() => handleNavClick('home')}>
            <span className="logo-text">Sebastian Maierhofer</span>
          </div>

          {/* Desktop Navigation */}
          <nav className="desktop-nav">
            {navigationItems.map((item) => (
              <button
                key={item.id}
                className={`nav-item ${currentPage === item.id ? 'active' : ''}`}
                onClick={() => handleNavClick(item.id)}
              >
                {item.label}
              </button>
            ))}
          </nav>

          {/* Mobile Menu Button */}
          <button 
            className={`mobile-menu-btn ${isMenuOpen ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label="Toggle menu"
          >
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <nav className="mobile-nav">
            {navigationItems.map((item) => (
              <button
                key={item.id}
                className={`mobile-nav-item ${currentPage === item.id ? 'active' : ''}`}
                onClick={() => handleNavClick(item.id)}
              >
                {item.label}
              </button>
            ))}
          </nav>
        )}
      </div>
    </header>
  );
};

export default Header;