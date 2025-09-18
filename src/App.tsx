import React, { useState } from 'react';
import Header from './components/Header';
import Home from './pages/Home';
import './styles/globals.css';
import './App.css';

function App() {
  const [currentPage, setCurrentPage] = useState('home');

  const handleNavigate = (page: string) => {
    setCurrentPage(page);
  };

  const renderCurrentPage = () => {
    switch (currentPage) {
      case 'home':
        return <Home />;
      case 'about':
        return <div className="page-placeholder">About Page - Coming Soon</div>;
      case 'projects':
        return <div className="page-placeholder">Projects Page - Coming Soon</div>;
      case 'contact':
        return <div className="page-placeholder">Contact Page - Coming Soon</div>;
      default:
        return <Home />;
    }
  };

  return (
    <div className="App">
      <Header currentPage={currentPage} onNavigate={handleNavigate} />
      <main className="main-content">
        {renderCurrentPage()}
      </main>
    </div>
  );
}

export default App;
