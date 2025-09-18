"""
Sebastian Maierhofer Homepage - Flask Application
Professional homepage with space-themed design
"""

from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['DEBUG'] = os.environ.get('FLASK_ENV') == 'development'

# Project data - same structure as React version
PROJECTS_DATA = [
    {
        'id': 'wiener-schuelerliga',
        'title': 'Wiener Schülerliga',
        'description': 'Student league management system and competition platform.',
        'category': 'Web Development',
        'tech': ['React', 'Node.js', 'MongoDB'],
        'status': 'Completed',
        'github_url': 'https://github.com/sebastianjulian/wiener-schuelerliga',
        'demo_url': None
    },
    {
        'id': 'chemieolympiade',
        'title': 'Chemieolympiade',
        'description': 'Chemistry olympiad participation and achievements.',
        'category': 'Competition',
        'tech': ['Chemistry', 'Problem Solving'],
        'status': 'Achievement',
        'github_url': None,
        'demo_url': None
    },
    {
        'id': 'cansat',
        'title': 'CanSat',
        'description': 'Satellite technology project with atmospheric measurements.',
        'category': 'Engineering',
        'tech': ['Arduino', 'Sensors', 'Data Analysis'],
        'status': 'Completed',
        'github_url': 'https://github.com/sebastianjulian/cansat',
        'demo_url': None
    },
    {
        'id': 'triton',
        'title': 'Triton',
        'description': 'Advanced engineering project with innovative solutions.',
        'category': 'Engineering',
        'tech': ['CAD', 'Simulation', 'Prototyping'],
        'status': 'In Progress',
        'github_url': 'https://github.com/sebastianjulian/triton',
        'demo_url': None
    },
    {
        'id': 'cs50-homepage',
        'title': 'CS50 Homepage',
        'description': 'Harvard CS50 final project - this very website.',
        'category': 'Web Development',
        'tech': ['Flask', 'Python', 'HTML5', 'CSS3'],
        'status': 'Current',
        'github_url': 'https://github.com/sebastianjulian/Homepage',
        'demo_url': None
    },
    {
        'id': 'astrophotography',
        'title': 'Astrophotography',
        'description': 'Deep space imaging and astronomical photography collection.',
        'category': 'Photography',
        'tech': ['Telescope', 'Image Processing', 'Stacking'],
        'status': 'Ongoing',
        'github_url': 'https://github.com/sebastianjulian/astrophotography',
        'demo_url': None
    }
]

# Personal information
PERSONAL_INFO = {
    'name': 'Sebastian Maierhofer',
    'title': 'Technical Physics Student',
    'subtitle': 'Aspiring Engineer • Problem Solver',
    'description': 'Recent graduate from Schottengymnasium, currently completing Zivildienst before pursuing Technical Physics. Passionate about engineering, programming, and astrophotography.',
    'email': 'sebastian@maierhofers.net',
    'instagram': 'sebi_maierhofer',
    'github': 'sebastianjulian',
    'education': [
        {
            'institution': 'Schottengymnasium',
            'degree': 'Matura (High School Diploma)',
            'year': '2025',
            'status': 'completed'
        },
        {
            'institution': 'VES (Volksschule)',
            'degree': 'Elementary Education', 
            'year': '2017',
            'status': 'completed'
        },
        {
            'institution': 'Technical Physics Studies',
            'degree': 'Bachelor of Science (planned)',
            'year': '2026+',
            'status': 'planned'
        }
    ],
    'current_status': 'Zivildienst (Civil Service)',
    'graduation_year': 2025
}

# Navigation items
NAVIGATION = [
    {'id': 'home', 'label': 'Home', 'label_de': 'Startseite'},
    {'id': 'about', 'label': 'About', 'label_de': 'Über mich'},
    {'id': 'projects', 'label': 'Projects', 'label_de': 'Projekte'},
    {'id': 'contact', 'label': 'Contact', 'label_de': 'Kontakt'},
]

@app.route('/')
def home():
    """Homepage route - displays hero section and project grid"""
    return render_template('home.html', 
                         projects=PROJECTS_DATA,
                         personal_info=PERSONAL_INFO,
                         navigation=NAVIGATION,
                         current_page='home')

@app.route('/about')
def about():
    """About page route - personal background and timeline"""
    return render_template('about.html',
                         personal_info=PERSONAL_INFO,
                         navigation=NAVIGATION,
                         current_page='about')

@app.route('/projects')
def projects():
    """Projects page route - detailed project showcase"""
    return render_template('projects.html',
                         projects=PROJECTS_DATA,
                         personal_info=PERSONAL_INFO,
                         navigation=NAVIGATION,
                         current_page='projects')

@app.route('/projects/<project_id>')
def project_detail(project_id):
    """Individual project detail page"""
    project = next((p for p in PROJECTS_DATA if p['id'] == project_id), None)
    if not project:
        return render_template('404.html'), 404
    
    return render_template('project_detail.html',
                         project=project,
                         personal_info=PERSONAL_INFO,
                         navigation=NAVIGATION,
                         current_page='projects')

@app.route('/contact')
def contact():
    """Contact page route - contact information and form"""
    return render_template('contact.html',
                         personal_info=PERSONAL_INFO,
                         navigation=NAVIGATION,
                         current_page='contact')

@app.route('/api/projects')
def api_projects():
    """API endpoint for projects data (for potential future AJAX calls)"""
    return jsonify(PROJECTS_DATA)

@app.route('/api/contact', methods=['POST'])
def api_contact():
    """API endpoint for contact form submission"""
    data = request.get_json()
    
    # Basic validation
    required_fields = ['name', 'email', 'message']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # In a real application, you would save this to a database or send an email
    # For now, just return success
    return jsonify({
        'success': True,
        'message': 'Thank you for your message! I will get back to you soon.'
    })

@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template('404.html',
                         personal_info=PERSONAL_INFO,
                         navigation=NAVIGATION), 404

@app.errorhandler(500)
def server_error(error):
    """500 error handler"""
    return render_template('500.html',
                         personal_info=PERSONAL_INFO,
                         navigation=NAVIGATION), 500

# Template filters for additional functionality
@app.template_filter('status_class')
def status_class(status):
    """Convert status to CSS class name"""
    return status.lower().replace(' ', '-')

@app.template_filter('year_current')
def year_current():
    """Get current year for copyright"""
    return datetime.now().year

# Context processor to make common data available to all templates
@app.context_processor
def inject_common_data():
    """Inject commonly used data into all templates"""
    return {
        'current_year': datetime.now().year,
        'site_title': 'Sebastian Maierhofer - Technical Physics Student & Engineer'
    }

if __name__ == '__main__':
    # Create necessary directories if they don't exist
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    # Run the application
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=app.config['DEBUG']
    )