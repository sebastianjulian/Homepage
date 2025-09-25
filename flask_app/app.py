"""
Sebastian Maierhofer Homepage - Flask Application
Professional homepage with space-themed design
"""

from flask import Flask, render_template, request, jsonify, session
import os
from datetime import datetime
from translations import get_translation, get_supported_languages, TRANSLATIONS

# Initialize Flask application
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['DEBUG'] = os.environ.get('FLASK_ENV') == 'development'

# Language configuration
DEFAULT_LANGUAGE = 'en'  # Default to English

# Category definitions
CATEGORIES = {
    'content': ['Sports', 'Competition', 'Chemistry', 'Engineering', 'Physics', 'Programming', 'Project Management', 'Event Management', 'CAD', 'Astrophotography', 'Data Processing'],
    'status': ['Achievement', 'Education', 'Project', 'Hobby']
}

def get_current_language():
    """Get current language from session or default"""
    return session.get('language', DEFAULT_LANGUAGE)

def set_language(lang_code):
    """Set language in session"""
    if lang_code in get_supported_languages():
        session['language'] = lang_code
        return True
    return False

# Project data - same structure as React version
PROJECTS_DATA = [
    {
        'id': 'wiener-schuelerliga',
        'title': 'Wiener Schülerliga',
        'description': 'Our journey from crushing defeats with scorelines like 1:10 to ultimately winning the championship. A story of growth, structure, and determination that transformed underdogs into champions.',
        'categories': ['Sports', 'Competition'],
        'status': 'Achievement',
        'tech': ['Event Management', 'Organization', 'Sports'],
        'github_url': None,
        'demo_url': None
    },
    {
        'id': 'chemieolympiade',
        'title': 'Chemieolympiade',
        'description': 'Participation in the Chemistry Olympiad since fifth year of high school, combining theoretical knowledge with hands-on laboratory work to develop both understanding and experimental skills.',
        'categories': ['Chemistry', 'Competition'],
        'status': 'Achievement',
        'tech': ['Chemistry', 'Problem Solving'],
        'github_url': None,
        'demo_url': None
    },
    {
        'id': 'cansat',
        'title': 'CanSat',
        'description': 'European Space Agency (ESA) project to develop a satellite the size of a beverage can, launch it with a rocket, and safely return it to Earth while collecting atmospheric data.',
        'categories': ['Engineering', 'Competition', 'Physics'],
        'status': 'Achievement',
        'tech': ['Raspberry Pi', 'Sensors', 'Data Analysis'],
        'github_url': 'https://github.com/sebastianjulian/cansat',
        'demo_url': None
    },
    {
        'id': 'triton',
        'title': 'TRITON',
        'description': 'Complex system for autonomous navigation underwater that evolved from our CanSat project. Using physics, programming, electronics, and project management to explore marine robotics.',
        'categories': ['Engineering', 'Programming', 'Project Management', 'CAD', 'Physics'],
        'status': 'Project',
        'tech': ['CAD', 'Simulation', 'Programming'],
        'github_url': 'https://github.com/sebastianjulian/triton',
        'demo_url': None
    },
    {
        'id': 'cs50-homepage',
        'title': 'CS50 Homepage',
        'description': 'Completed Harvard University\'s comprehensive CS50: Introduction to Computer Science course, one of the most well-known introductions to computer science. This website serves as the final project.',
        'categories': ['Programming'],
        'status': 'Education',
        'tech': ['Flask', 'Python', 'HTML5', 'CSS3'],
        'github_url': 'https://github.com/sebastianjulian/Homepage',
        'demo_url': None
    },
    {
        'id': 'astrophotography',
        'title': 'Astrophotography',
        'description': 'Three-year journey from a beginner telescope setup to an automated system, capturing deep-sky objects like galaxies and nebulae that were initially beyond reach of basic equipment.',
        'categories': ['Astrophotography', 'Event Management', 'Data Processing'],
        'status': 'Hobby',
        'tech': ['Telescope', 'Image Processing', 'Stacking', 'Event Management'],
        'github_url': None,
        'demo_url': None
    }
]

# Personal information
PERSONAL_INFO = {
    'name': 'Sebastian Maierhofer',
    'title': '',
    'subtitle': 'Aspiring Engineer • Problem Solver',
    'description': 'Recent graduate from Schottengymnasium, currently completing Zivildienst before pursuing Technical Physics. Passionate about engineering, programming, and astrophotography.',
    'email': 'sebastian@maierhofers.net',
    'instagram': 'sebi_maierhofer',
    'github': 'sebastianjulian',
    'education': [
        {
            'institution_key': 'technical_physics_studies',
            'degree_key': '',
            'year': '2026+',
            'status': 'planned'
        },
        {
            'institution_key': 'civil_service',
            'degree_key': 'paramedic_training',
            'year': '2025-2026',
            'status': 'ongoing'
        },
        {
            'institution_key': 'schottengymnasium',
            'degree_key': 'matura',
            'year': '2025',
            'status': 'completed'
        },
        {
            'institution_key': 'ves',
            'degree_key': 'elementary_school',
            'year': '2017',
            'status': 'completed'
        }
    ],
    'current_status': 'Zivildienst (Civil Service)',
    'graduation_year': 2025
}

def get_navigation(lang):
    """Get navigation items with proper translations"""
    return [
        {'id': 'home', 'label': get_translation(lang, 'home')},
        {'id': 'about', 'label': get_translation(lang, 'about')},
        {'id': 'projects', 'label': get_translation(lang, 'projects')},
        {'id': 'contact', 'label': get_translation(lang, 'contact')},
    ]

@app.route('/')
def home():
    """Homepage route - displays hero section and project grid"""
    current_lang = get_current_language()
    return render_template('home.html',
                         projects=PROJECTS_DATA,
                         personal_info=PERSONAL_INFO,
                         navigation=get_navigation(current_lang),
                         current_page='home')

@app.route('/about')
def about():
    """About page route - personal background and timeline"""
    current_lang = get_current_language()
    return render_template('about.html',
                         personal_info=PERSONAL_INFO,
                         navigation=get_navigation(current_lang),
                         current_page='about')

@app.route('/projects')
def projects():
    """Projects page route - detailed project showcase"""
    current_lang = get_current_language()
    return render_template('projects.html',
                         projects=PROJECTS_DATA,
                         personal_info=PERSONAL_INFO,
                         navigation=get_navigation(current_lang),
                         current_page='projects')

@app.route('/projects/<project_id>')
def project_detail(project_id):
    """Individual project detail page"""
    project = next((p for p in PROJECTS_DATA if p['id'] == project_id), None)
    if not project:
        return render_template('404.html'), 404

    current_lang = get_current_language()
    return render_template('project_detail.html',
                         project=project,
                         personal_info=PERSONAL_INFO,
                         navigation=get_navigation(current_lang),
                         current_page='projects')

@app.route('/projects/astrophotography/gallery')
def astrophotography_gallery():
    """Astrophotography gallery page"""
    current_lang = get_current_language()

    # Sample astrophotography images data
    # In a real implementation, this would come from a database or file system scan
    images = [
        {
            'filename': 'sample1.jpg',
            'title': get_translation('sample_image_1_title', current_lang),
            'description': get_translation('sample_image_1_desc', current_lang),
            'date': '2024-01-15',
            'equipment': 'Telescope + Canon EOS',
            'exposure': '120s'
        },
        {
            'filename': 'sample2.jpg',
            'title': get_translation('sample_image_2_title', current_lang),
            'description': get_translation('sample_image_2_desc', current_lang),
            'date': '2024-02-20',
            'equipment': 'Refractor 80mm',
            'exposure': '300s'
        }
    ]

    # Filter out images that don't exist
    import os
    existing_images = []
    for image in images:
        image_path = os.path.join(app.static_folder, 'images', 'astrophotography', image['filename'])
        if os.path.exists(image_path):
            existing_images.append(image)

    return render_template('astrophotography_gallery.html',
                         images=existing_images,
                         personal_info=PERSONAL_INFO,
                         navigation=get_navigation(current_lang),
                         current_page='projects')

@app.route('/contact')
def contact():
    """Contact page route - contact information and form"""
    current_lang = get_current_language()
    return render_template('contact.html',
                         personal_info=PERSONAL_INFO,
                         navigation=get_navigation(current_lang),
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
    current_lang = get_current_language()
    return render_template('404.html',
                         personal_info=PERSONAL_INFO,
                         navigation=get_navigation(current_lang)), 404

@app.errorhandler(500)
def server_error(error):
    """500 error handler"""
    current_lang = get_current_language()
    return render_template('500.html',
                         personal_info=PERSONAL_INFO,
                         navigation=get_navigation(current_lang)), 500

# Template filters for additional functionality
@app.template_filter('status_class')
def status_class(status):
    """Convert status to CSS class name"""
    return status.lower().replace(' ', '-')

@app.template_filter('year_current')
def year_current():
    """Get current year for copyright"""
    return datetime.now().year

# Language switching route
@app.route('/set_language/<lang_code>')
def set_language_route(lang_code):
    """Route to set language"""
    if set_language(lang_code):
        # Redirect back to the referring page or home
        return jsonify({'success': True, 'language': lang_code})
    return jsonify({'success': False, 'error': 'Invalid language code'}), 400

# Context processor to make common data available to all templates
@app.context_processor
def inject_common_data():
    """Inject commonly used data into all templates"""
    current_lang = get_current_language()
    return {
        'current_year': datetime.now().year,
        'site_title': 'Sebastian Maierhofer',
        'current_language': current_lang,
        'supported_languages': get_supported_languages(),
        'get_translation': lambda key, default=None: get_translation(current_lang, key, default),
        'translations': TRANSLATIONS.get(current_lang, {})
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