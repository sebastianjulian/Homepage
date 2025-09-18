import React from 'react';
import './Home.css';

const Home: React.FC = () => {
  const projects = [
    {
      id: 'wiener-schuelerliga',
      title: 'Wiener Schülerliga',
      description: 'Student league management system and competition platform.',
      category: 'Web Development',
      tech: ['React', 'Node.js', 'MongoDB'],
      status: 'Completed'
    },
    {
      id: 'chemieolympiade',
      title: 'Chemieolympiade',
      description: 'Chemistry olympiad participation and achievements.',
      category: 'Competition',
      tech: ['Chemistry', 'Problem Solving'],
      status: 'Achievement'
    },
    {
      id: 'cansat',
      title: 'CanSat',
      description: 'Satellite technology project with atmospheric measurements.',
      category: 'Engineering',
      tech: ['Arduino', 'Sensors', 'Data Analysis'],
      status: 'Completed'
    },
    {
      id: 'triton',
      title: 'Triton',
      description: 'Advanced engineering project with innovative solutions.',
      category: 'Engineering',
      tech: ['CAD', 'Simulation', 'Prototyping'],
      status: 'In Progress'
    },
    {
      id: 'cs50-homepage',
      title: 'CS50 Homepage',
      description: 'Harvard CS50 final project - this very website.',
      category: 'Web Development',
      tech: ['React', 'TypeScript', 'CSS3'],
      status: 'Current'
    },
    {
      id: 'astrophotography',
      title: 'Astrophotography',
      description: 'Deep space imaging and astronomical photography collection.',
      category: 'Photography',
      tech: ['Telescope', 'Image Processing', 'Stacking'],
      status: 'Ongoing'
    }
  ];

  const handleProjectClick = (projectId: string) => {
    // Navigate to project detail or projects page
    console.log(`Navigate to project: ${projectId}`);
  };

  const handleContactClick = () => {
    // Navigate to contact page
    console.log('Navigate to contact');
  };

  return (
    <div className="home">
      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-content">
            <div className="hero-text">
              <h1 className="hero-title fade-in">Sebastian Maierhofer</h1>
              <div className="hero-subtitle fade-in">
                <span className="subtitle-highlight">Technical Physics Student</span>
                <span className="subtitle-separator">•</span>
                <span className="subtitle-text">Aspiring Engineer</span>
                <span className="subtitle-separator">•</span>
                <span className="subtitle-text">Problem Solver</span>
              </div>
              <p className="hero-description fade-in">
                Recent graduate from Schottengymnasium, currently completing Zivildienst 
                before pursuing Technical Physics. Passionate about engineering, programming, 
                and astrophotography.
              </p>
              <div className="hero-actions fade-in">
                <button className="btn btn-primary" onClick={handleContactClick}>
                  Get in Touch
                </button>
                <a 
                  href="#projects" 
                  className="btn btn-secondary"
                  onClick={(e) => {
                    e.preventDefault();
                    document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth' });
                  }}
                >
                  View Projects
                </a>
              </div>
            </div>
            <div className="hero-image">
              <div className="image-placeholder">
                <div className="image-content">
                  <svg width="200" height="200" viewBox="0 0 200 200" className="profile-svg">
                    <defs>
                      <linearGradient id="profileGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stopColor="var(--accent-primary)" />
                        <stop offset="100%" stopColor="var(--accent-secondary)" />
                      </linearGradient>
                    </defs>
                    <circle cx="100" cy="100" r="90" fill="url(#profileGradient)" opacity="0.2" />
                    <circle cx="100" cy="100" r="70" fill="none" stroke="url(#profileGradient)" strokeWidth="2" />
                    <text x="100" y="110" textAnchor="middle" fill="var(--text-primary)" fontSize="16" fontWeight="500">
                      Professional
                    </text>
                    <text x="100" y="130" textAnchor="middle" fill="var(--text-secondary)" fontSize="14">
                      Photo Here
                    </text>
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="hero-background"></div>
      </section>

      {/* Projects Grid Section */}
      <section id="projects" className="projects-section section">
        <div className="container">
          <div className="section-header text-center">
            <h2 className="section-title">Featured Projects</h2>
            <p className="section-description">
              A collection of my work spanning web development, engineering, competitions, and creative pursuits.
            </p>
          </div>
          
          <div className="projects-grid grid grid-3">
            {projects.map((project, index) => (
              <div 
                key={project.id} 
                className={`project-card card fade-in`}
                style={{ animationDelay: `${index * 0.1}s` }}
                onClick={() => handleProjectClick(project.id)}
              >
                <div className="project-header">
                  <div className="project-status">
                    <span className={`status-badge status-${project.status.toLowerCase().replace(' ', '-')}`}>
                      {project.status}
                    </span>
                  </div>
                  <div className="project-category">{project.category}</div>
                </div>
                
                <h3 className="project-title">{project.title}</h3>
                <p className="project-description">{project.description}</p>
                
                <div className="project-tech">
                  {project.tech.map((tech) => (
                    <span key={tech} className="tech-tag">{tech}</span>
                  ))}
                </div>
                
                <div className="project-arrow">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clipRule="evenodd" />
                  </svg>
                </div>
              </div>
            ))}
          </div>
          
          <div className="projects-footer text-center">
            <button className="btn btn-secondary">
              View All Projects
            </button>
          </div>
        </div>
      </section>

      {/* Quick Stats Section */}
      <section className="stats-section section">
        <div className="container">
          <div className="stats-grid grid grid-4">
            <div className="stat-item text-center fade-in">
              <div className="stat-number">2025</div>
              <div className="stat-label">Graduated</div>
            </div>
            <div className="stat-item text-center fade-in">
              <div className="stat-number">6</div>
              <div className="stat-label">Major Projects</div>
            </div>
            <div className="stat-item text-center fade-in">
              <div className="stat-number">∞</div>
              <div className="stat-label">Learning</div>
            </div>
            <div className="stat-item text-center fade-in">
              <div className="stat-number">🌌</div>
              <div className="stat-label">Stargazing</div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;