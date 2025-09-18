# Sebastian Maierhofer Homepage - Technical Project Plan

## 📋 Project Specifications

### **Client Requirements**
- **Name**: Sebastian Maierhofer
- **Education**: VES (elementary) → Schottengymnasium (graduated 2025) → Gap year (Zivildienst) → Technical Physics studies
- **Contact**: sebastian@maierhofers.net, Instagram: @sebi_maierhofer
- **Design Preference**: Modern space-themed dark colors, interactive elements, not too much white space

### **Technical Architecture**

#### **Framework Decision**
- **Primary**: React (for interactive components and state management)
- **Secondary**: Vanilla JavaScript (for custom animations and DOM manipulation)
- **Minimal**: Next.js features (only if specifically needed for performance)
- **Reasoning**: Balance of modern React capabilities with direct control over animations

#### **Project Structure**
```
src/
├── components/           # Reusable UI components
│   ├── common/          # Header, Footer, Navigation, Layout
│   ├── ui/              # Buttons, Cards, Modals, Forms
│   └── features/        # Gallery, Timeline, ContactForm
├── pages/               # Main page components
│   ├── Home/            # Hero + Portfolio grid hybrid
│   ├── About/           # Education timeline, hobbies
│   ├── Projects/        # Project showcases with GitHub links
│   └── Contact/         # Email/Instagram integration
├── assets/              # Static files
│   ├── images/          # Photos, project screenshots
│   ├── documents/       # PDF resume, downloadables
│   └── data/            # Project data, translations
├── styles/              # CSS organization
│   ├── globals.css      # Global styles, CSS variables
│   ├── themes.css       # Dark/light mode definitions
│   └── components/      # Component-specific styles
├── utils/               # Helper functions
│   ├── translations.js  # German/English language data
│   ├── analytics.js     # Visitor tracking
│   └── imageUtils.js    # Gallery functionality
└── hooks/               # Custom React hooks
    ├── useTheme.js      # Dark/light mode management
    ├── useLanguage.js   # Language switching
    └── useAnalytics.js  # Analytics tracking
```

## 🎨 Design System

### **Color Scheme - Space Theme**
```css
:root {
  /* Dark Mode (Primary) */
  --bg-primary: #0a0a0f;        /* Deep space black */
  --bg-secondary: #1a1a2e;      /* Dark blue-purple */
  --bg-tertiary: #16213e;       /* Deeper blue */
  --accent-primary: #e94560;    /* Cosmic red */
  --accent-secondary: #f39c12;  /* Star yellow */
  --text-primary: #eee;         /* Light text */
  --text-secondary: #bbb;       /* Muted text */
  
  /* Light Mode (Secondary) */
  --bg-primary-light: #f8f9fa;
  --bg-secondary-light: #e9ecef;
  --text-primary-light: #212529;
}
```

### **Typography**
- **Headers**: Modern sans-serif (Inter, Roboto, or system fonts)
- **Body**: Readable sans-serif with good spacing
- **Code**: Monospace for technical content

### **Interactive Elements**
- Smooth hover transitions (0.3s ease)
- Subtle animations on scroll
- Loading animations between pages
- Image gallery lightbox effects
- Parallax elements for depth

## 📱 Page Specifications

### **1. Home Page**
**Layout**: Hero + Portfolio Grid Hybrid
- **Hero Section**: 
  - Professional photo (provided by Sebastian)
  - Name with elegant typography
  - Brief tagline about studies/interests
  - Animated background (subtle space particles)
- **Portfolio Preview**: 
  - Grid of project cards with hover effects
  - Quick navigation to main sections
  - Contact CTA buttons

### **2. About Me Page**
**Components**:
- **Education Timeline**: Interactive timeline showing VES → Schottengymnasium → gap year → Technical Physics
- **Skills Section**: Progress bars or skill cards
- **Hobbies**: Placeholder section for additional hobby (reusable component)
- **Achievements**: Awards, competitions, recognitions
- **Personal Philosophy**: What drives Sebastian professionally

### **3. Projects Page**
**Project Sections** (each with consistent structure):
1. **Wiener Schülerliga**: Brief description, images, GitHub link
2. **Chemieolympiade**: Competition details, achievements, documentation
3. **CanSat**: Technical project overview, team collaboration, results
4. **Triton**: Project specifics, technical implementation, links
5. **CS50/Homepage**: Meta-project about this website, code links
6. **Astrophotography**: Special gallery section with downloadable images

**Features per project**:
- Brief text description
- Image gallery/screenshots
- External links (GitHub, documentation, live demos)
- Technologies used
- Project timeline/duration

### **4. Contact Page**
**Integration**:
- **Email**: sebastian@maierhofers.net (mailto: link opens email client)
- **Instagram**: @sebi_maierhofer (direct link to profile)
- **Contact Form**: Optional backup contact method
- **Download Resume**: PDF download button

## 🔧 Technical Features Implementation

### **1. Astrophotography Gallery**
**Requirements**:
- Image filtering by category/date/equipment
- Lightbox enlargement on click
- Downloadable high-resolution versions
- EXIF data display (camera settings, location, date)
- Responsive grid layout

**Technical Implementation**:
```javascript
// Gallery component structure
const AstroGallery = () => {
  const [filter, setFilter] = useState('all');
  const [lightbox, setLightbox] = useState(null);
  
  // Filter images by category
  // Lightbox modal for enlargement
  // Download functionality for high-res images
}
```

### **2. Multi-language Support**
**Languages**: German (primary), English (secondary)
**Implementation**:
- JSON files for translation strings
- React context for language state
- URL-based language detection (/de/, /en/)
- Language switcher in header

### **3. Dark/Light Mode Toggle**
**Implementation**:
- CSS custom properties for theming
- localStorage persistence
- System preference detection
- Smooth transitions between modes

### **4. PDF Resume Download**
**Features**:
- Pre-generated PDF stored in assets
- Download tracking via analytics
- Print-friendly web version
- Multiple language versions if needed

### **5. Search Functionality**
**Scope**: Search across all content (projects, about, etc.)
**Implementation**:
- Client-side search using Fuse.js or custom implementation
- Search bar in header
- Results highlighting
- Keyboard shortcuts (Ctrl+K)

### **6. Analytics Integration**
**Tracking**:
- Page views
- Download counts
- Contact form submissions
- Gallery interactions
**Privacy**: GDPR compliant, minimal data collection

## 🚀 Performance & SEO

### **Optimization Targets**
- **Loading**: < 3 seconds initial load
- **Mobile**: Fully responsive, touch-friendly
- **SEO**: Proper meta tags, structured data, sitemap
- **Accessibility**: WCAG 2.1 AA compliance

### **Image Optimization**
- WebP format with fallbacks
- Lazy loading for gallery images
- Multiple sizes for responsive images
- Compression for web delivery

### **Code Optimization**
- Component code splitting
- CSS minimization
- JavaScript bundling optimization
- Service worker for caching (optional)

## 🧪 Testing Strategy

### **Functional Testing**
- All navigation links work
- Contact forms submit correctly
- Downloads function properly
- Language switching works
- Theme toggling works

### **Cross-Platform Testing**
- **Desktop**: Chrome, Firefox, Safari, Edge
- **Mobile**: iOS Safari, Android Chrome
- **Tablets**: iPad, Android tablets
- **Screen Readers**: Basic accessibility testing

### **Performance Testing**
- Lighthouse scores > 90
- Mobile performance testing
- Image loading optimization
- Bundle size analysis

## 📦 Deployment Preparation

### **Build Process**
- React production build (`npm run build`)
- Asset optimization
- Environment variable configuration
- Error boundary implementation

### **Server Requirements**
- Static file hosting capability
- HTTPS support
- Gzip compression
- Cache headers for static assets

### **Future Deployment Options**
- Home server (as mentioned by Sebastian)
- GitHub Pages (fallback)
- Netlify/Vercel (alternatives)

## 📝 Development Phases

### **Phase 1: Foundation** (Current)
- [x] Documentation setup (CLAUDE.md, README.md, PROJECT_PLAN.md)
- [ ] React project initialization
- [ ] Basic project structure
- [ ] Initial testing setup

### **Phase 2: Core Development**
- [ ] Design system implementation
- [ ] Basic page layouts
- [ ] Navigation and routing
- [ ] Theme system setup

### **Phase 3: Feature Implementation**
- [ ] Individual page development
- [ ] Gallery functionality
- [ ] Contact integration
- [ ] Language switching

### **Phase 4: Advanced Features**
- [ ] Search functionality
- [ ] Analytics integration
- [ ] Performance optimization
- [ ] Accessibility enhancements

### **Phase 5: Polish & Deploy**
- [ ] Cross-browser testing
- [ ] Mobile optimization
- [ ] Final content integration
- [ ] Deployment preparation

## 🔄 Maintenance & Updates

### **Easy Expandability Requirements**
- **New Projects**: Simple addition process via data files
- **Content Updates**: Markdown or JSON-based content management
- **Image Gallery**: Folder-based image organization
- **Translations**: Structured language files

### **Documentation Requirements**
- Component documentation for future maintenance
- Content update procedures
- Deployment instructions
- Troubleshooting guide

---

**Document Status**: ✅ COMPLETED  
**Created**: September 18, 2025  
**Last Updated**: September 18, 2025  
**Next Review**: After Phase 1 completion