"""
Translation system for Sebastian Maierhofer Homepage
Support for German, English, and French languages
"""

TRANSLATIONS = {
    'en': {
        # Navigation
        'home': 'Home',
        'about': 'About',
        'projects': 'Projects',
        'contact': 'Contact',

        # Hero Section
        'hero_description': '''I'm Sebastian, having recently completed my Matura and currently doing my civil service. Afterwards, I'll begin studying Technical Physics, where I want to deepen my passion for natural sciences and technology.

        Already during school, I engaged with projects like building a submarine, participating in the CanSat competition, or programming my own websites. Tinkering, developing, and understanding connections is not just a hobby for me, but a passion. Astronomy also fascinates me – looking at the starry sky always opens up new questions and ideas.

        Besides technology, sports play a major role in my life: whether cycling, football, tennis, table tennis, volleyball, skiing, hiking, swimming, or basketball – I enjoy movement and variety in all their facets. I'm constantly looking for new challenges that I approach with curiosity and dedication. On this page, I want to give insight into my projects, interests, and goals – perhaps as inspiration, perhaps simply to get to know me better.''',

        'get_in_touch': 'Get in Touch',
        'view_projects': 'View Projects',

        # Projects Section
        'featured_projects': 'Featured Projects',
        'projects_description': 'A collection of my work spanning web development, engineering, competitions, and creative pursuits.',
        'view_all_projects': 'View All Projects',

        # Stats Section
        'graduated': 'Graduated',
        'major_projects': 'Major Projects',
        'learning': 'Learning',
        'stargazing': 'Stargazing',

        # Footer
        'footer_text': '',

        # Project Data
        'project_wiener_schuelerliga_title': 'Wiener Schülerliga',
        'project_wiener_schuelerliga_desc': 'Student league management system and competition platform.',
        'project_chemieolympiade_title': 'Chemistry Olympiad',
        'project_chemieolympiade_desc': 'Chemistry olympiad participation and achievements.',
        'project_cansat_title': 'CanSat',
        'project_cansat_desc': 'Satellite technology project with atmospheric measurements.',
        'project_triton_title': 'Triton',
        'project_triton_desc': 'Advanced engineering project with innovative solutions.',
        'project_cs50_title': 'CS50 Homepage',
        'project_cs50_desc': 'Harvard CS50 final project - this very website.',
        'project_astrophoto_title': 'Astrophotography',
        'project_astrophoto_desc': 'Deep space imaging and astronomical photography collection.',

        # Categories
        'cat_web_development': 'Web Development',
        'cat_competition': 'Competition',
        'cat_engineering': 'Engineering',
        'cat_photography': 'Photography',

        # Status
        'status_completed': 'Completed',
        'status_achievement': 'Achievement',
        'status_in_progress': 'In Progress',
        'status_current': 'Current',
        'status_ongoing': 'Ongoing',

        # Personal Info
        'personal_subtitle': 'Aspiring Engineer • Problem Solver',
        'personal_description': 'Recent graduate from Schottengymnasium, currently completing Zivildienst before pursuing Technical Physics. Passionate about engineering, programming, and astrophotography.',
        'current_status': 'Civil Service',

        # About Page
        'about_me': 'About Me',
        'about_description': '',
        'hello_sebastian': 'Hello, I\'m Sebastian',
        'current_status_title': 'Current Status',
        'interests_hobbies': 'Interests & Hobbies',
        'interest_astrophotography': 'Astrophotography and stargazing',
        'interest_programming': 'Programming and software development',
        'interest_engineering': 'Engineering projects and problem-solving',
        'interest_physics': 'Physics and scientific research',
        'interest_additional': '[Placeholder for additional hobby]',
        'education_timeline': 'Education',
        'experiences': 'Experiences',
        'competitions_courses': 'Competitions and Courses',
        'competitions_courses_desc': 'Participation in extracurricular competitions such as the CanSat competition (mini-satellite construction), Chemistry Olympiad, and DACH seminar',
        'cern_courses': 'Completed two CERN online courses',
        'vrvis_internship': 'VRVIS Internship',
        'vrvis_internship_desc': 'Programming a robotic dog and developing a computer game',
        'languages_skills': 'Languages and Skills',
        'languages': 'Languages',
        'engagement_skills': 'Skills and Community Engagement',
        'german_native': 'German',
        'english_bilingual': 'English',
        'french_good': 'French',
        'latin_very_good': 'Latin',
        'programming': 'Programming',
        'engagement_hobbies': 'Engagement and Hobbies',
        'astronomy_desc': 'Astronomy: Astrophotography & organization of "Astronomy evenings" (knowledge transfer, image processing and application of technical skills)',
        'class_representative': 'Class representative',
        'sports_reading': 'Football, tennis, cycling, reading',

        # About page hardcoded translations
        'native': 'Native',
        'bilingual': 'Bilingual',
        'b1_b2': 'B1 - B2',
        'academic_level': 'Academic Level (Großes Latinum)',
        'cansat_competition': 'CanSat Competition',
        'cansat_description': 'Design and construction of a miniature satellite with integrated sensors, radio communications, and comprehensive data analysis',
        'chemistry_olympiad': 'Chemistry Olympiad',
        'chemistry_olympiad_description': 'Chemistry competition with theoretical and practical components',
        'dach_seminar': 'DACH Seminar',
        'dach_seminar_description': 'International chemistry seminar for talented students',
        'cern_courses_title': 'CERN Courses',
        'cern_courses_description': 'Online courses in particle physics and accelerator technology',
        'vrvis_internship_title': 'VRVIS Internship',
        'vrvis_internship_description': 'Programming robotic systems and computer game development',
        'astronomy': 'Astronomy',
        'astronomy_description': 'Astrophotography and astronomy evenings (knowledge transfer & image processing)',
        'software_web_development': 'Software & Web Development',
        'projects': 'Projects',
        'projects_description': 'Comprehensive project development and management combining engineering, programming, and design - including building an autonomous submarine from scratch',
        'student_leadership': 'Student leadership role',
        'school': 'School',
        'free_time_activities': 'Free Time Activities',
        'soccer': 'Soccer',
        'tennis': 'Tennis',
        'basketball': 'Basketball',
        'cycling': 'Cycling',
        'swimming': 'Swimming',
        'volleyball': 'Volleyball',
        'table_tennis': 'Table Tennis',
        'reading': 'Reading',
        'cooking': 'Cooking',

        # Education entries
        'technical_physics_studies': 'Technical Physics Studies',
        'civil_service': 'Civil Service',
        'paramedic_training': 'Paramedic Training',
        'schottengymnasium': 'Schottengymnasium',
        'matura': 'Matura',
        'ves': 'VES',
        'elementary_school': 'Elementary School',

        # Wiener Schülerliga Story
        'wiener_story_title': 'From Underdogs to Champions – Our Journey to Winning the Wiener Schülerliga',
        'wiener_story_p1': 'Looking back at our journey, it\'s almost hard to believe how far we\'ve come. When we first started competing in lower secondary school, the results were anything but encouraging. Matches often ended in crushing defeats – scorelines like 1:10 were unfortunately no rarity. We lacked structure, confidence, and, quite honestly, the experience to compete with stronger teams.',
        'wiener_story_p2': 'Everything started to change once we moved into the upper secondary. Bit by bit, our performance improved. Instead of suffering heavy defeats, we began to hold our ground, even managing to win about a third of our games. For the first time, it felt like we belonged on the pitch.',
        'wiener_story_p3': 'Last year marked a historic step for our team: we reached the knock-out stage for the very first time. Even though we lost in the first match, that achievement alone gave us the motivation to keep pushing.',
        'wiener_story_p4': 'This season, we entered with a new mindset. We worked on our passing and tactical awareness, and it paid off. We won every but one match in the group stage, yet every game was close – no easy wins. We were no longer a team to be underestimated.',
        'wiener_story_p5': 'In the knock-out stage, our progress became undeniable. Match after match, we grew more confident. The semi-final, however, was the real test. We faced a dedicated sports school, widely regarded as one of the strongest teams in the competition. For most of the game, it looked as though we wouldn\'t make it. But in the last quarter, everything changed. We turned the game around, and I personally had one of my best performances ever as goalkeeper. With numerous decisive saves, I was honored as man of the match – a memory I will never forget.',
        'wiener_story_p6': 'The final had to be postponed due to the school year ending, which only added to the anticipation. Then, in September, the big day finally arrived. Fueled by determination and belief in ourselves, we gave everything we had – and it was enough. We won the Wiener Schülerliga.',
        'wiener_story_p7': 'From being the team that once lost by double digits, to standing at the very top – this victory is proof of how much can be achieved with perseverance, teamwork, and constant improvement. For us, it wasn\'t just about lifting the trophy. It was about the journey: growing together, learning from defeats, and turning setbacks into motivation.',
        'wiener_story_p8': 'This championship is the proudest chapter in our story so far – and hopefully just the beginning of many more.',

        # Chemistry Olympiad Story
        'chemistry_story_title': 'Participation in the Chemistry Olympiad',
        'chemistry_story_p1': 'Since my fifth year of high school, I have been participating in the Chemistry Olympiad elective course. Early on, I was fascinated not only by the theory but also by the practical work in the laboratory. The Chemistry Olympiad is for me the ideal way to combine both: to deepen theoretical foundations while simultaneously developing my experimental skills.',
        'chemistry_story_p2': 'Each year, in addition to the weekly preparation sessions, there is also the so-called course competition. In this, all participating students from the school compete against each other, and the top three qualify to represent the school at the state competition. Together with two friends, I was able to qualify – a great success for all of us.',
        'chemistry_story_p3': 'The state competition itself is divided into two parts:',
        'chemistry_story_p4': 'In the theoretical part, we had to engage with current questions in chemistry and apply our knowledge to complex problems.',
        'chemistry_story_p5': 'The practical part took place in the laboratory. Here, the task was to determine which substances were contained in unknown samples using various methods – such as "spot testing" (the targeted mixing of small chemical drops). Additionally, a titration was on the program, where precise work and accurate observations were crucial.',
        'chemistry_story_p6': 'Thanks to the dedicated preparation by our teacher, we were able to improve from year to year. Finally, we managed to win the 3rd prize in our last participation – a result that simultaneously set the school record.',
        'chemistry_story_p7': 'These successes show me that perseverance, curiosity, and good teamwork count not only in the laboratory but also lead to success in competition. For me, the Chemistry Olympiad was not just a competition, but above all an opportunity to live my passion for chemistry and to grow beyond myself.',

        # CanSat Project Story
        'cansat_story_title': 'CanSat Competition – Space Journey in Miniature Format',
        'cansat_story_p1': 'The CanSat competition is a project organized by the European Space Agency (ESA) and the Ars Electronica Center. The goal is to develop a satellite the size of a beverage can from the ground up and bring it safely back to Earth after launch using a rocket – including data collection throughout the entire flight.',
        'cansat_story_p2': 'Our team took on this challenge with enthusiasm. While many other groups already had experience in programming and building satellites, we had to work our way through this knowledge step by step. But that\'s exactly what appealed to us: learning everything from scratch and implementing our progress directly in the project.',
        'cansat_story_p3': 'The competition itself began spectacularly. After the rocket launch, our satellite reached its ejection position at about 380 meters altitude and was released by explosive charge. The parachute worked as planned, and we were relieved when the can landed safely on the ground. Thanks to our data recording, we were able to meet all requirements – and even successfully pass technical tests like the so-called "drop tests."',
        'cansat_story_p4': 'The next day we presented our project to a jury and a small audience. Our presentation was enhanced with additional content, so we ultimately achieved a top-5 placement – a great success for us as a team.',
        'cansat_story_p5': 'Looking back, participation was not only an exciting competition, but above all a unique insight into the processes of a real space mission: from design through construction to successful deployment. This was also made possible through the support of our parents as well as sponsors, to whom we would like to express our heartfelt thanks.',
        'cansat_story_p6': 'The CanSat competition showed us how fascinating technology and teamwork can be – and that even a "satellite can" can set great experiences in motion.',

        # TRITON Project Story
        'triton_story_title': 'TRITON – From CanSat to Autonomous Submarine Navigation',
        'triton_story_p1': 'What began as a small satellite project developed step by step into a complex system for autonomous navigation underwater: the TRITON project. Inspired by the experiences from the CanSat competition, we used our knowledge in physics, programming, electronics, and project management to explore a completely new field of application – marine robotics.',
        'triton_story_theory_title': 'From Theory to Practice',
        'triton_story_p2': 'The heart of TRITON is the combination of various sensors that together provide a precise picture of the environment. A BME280 sensor measures temperature, humidity, and air pressure – parameters that are not only relevant for weather and environmental data, but in submarine deployment are also used for depth determination. The system is supplemented by an MPU6050 module, which captures acceleration and rotational movements on all three axes. This allows orientation and movement to be determined even when GPS is not available underwater.',
        'triton_story_programming_title': 'Programming and Data Transmission',
        'triton_story_p3': 'On the software side, TRITON works with a dual architecture: A Raspberry Pi Zero 2 W collects the sensor data, processes it in real time, and transmits it wirelessly. A PC-based mission control system receives, analyzes, and visualizes the data in a web dashboard.',
        'triton_story_p4': 'For communication, we rely on LoRa radio technology, which enables robust data transmission over long distances – crucial when the system works in water. To keep transmission efficient, data is only sent when it changes by predefined threshold values. This relieves the network without losing accuracy.',
        'triton_story_design_title': 'Design and Construction',
        'triton_story_p5': 'Mechanical integration also plays an important role: sensors must be precisely positioned, electronics reliably encapsulated, and the antenna optimally aligned. Parallel to software tests, initial considerations flowed into the CAD-assisted development of a waterproof housing – a crucial step to make the technology actually deployable underwater.',
        'triton_story_project_mgmt_title': 'Project Management and Development Steps',
        'triton_story_p6': 'TRITON didn\'t emerge overnight, but through numerous iterations. Each version – from TRY1 to TRY9 – built on the experiences of the previous one: from the first sensor integration through data logging and error handling to complete web visualization with statistics functions. Old code versions were carefully archived to document the development process transparently and comprehensively.',
        'triton_story_applications_title': 'Application Possibilities',
        'triton_story_p7': 'The application fields for TRITON are diverse: Autonomous navigation of underwater robots without GPS, environmental monitoring in lakes and seas, research in the field of marine ecosystems, support in search and rescue operations.',
        'triton_story_conclusion_title': 'Conclusion',
        'triton_story_p8': 'TRITON shows how you can develop a project from a satellite can to an autonomous submarine system through systematic approach, technical curiosity, and continuous improvement. It combines physics, computer science, electronics, and design into an innovative overall concept – and forms the basis for future developments in the field of marine robotics.',

        # CS50 Project Story
        'cs50_story_title': 'CS50 – Introduction to the World of Computer Science',
        'cs50_story_p1': 'To deepen my knowledge in computer science and programming, I completed the course CS50: Introduction to Computer Science from Harvard University. The course is considered one of the most well-known and comprehensive introductions to computer science.',
        'cs50_story_p2': 'What was particularly exciting for me was the diversity of topics: from the basics of algorithms and data structures through C and Python to web development with HTML, CSS, and JavaScript. Each week new problem sets were presented that required not only technical knowledge, but also logical thinking and perseverance.',
        'cs50_story_p3': 'CS50 showed me how broad and at the same time deep the field of computer science is. Through the practice-oriented assignments, I was able not only to understand the theory, but also to implement real projects – a learning process that was both challenging and incredibly enriching.',

        # Astrophotography Project Story
        'astrophoto_story_title': 'Astrophotography – From First Observations to Automated Telescope System',
        'astrophoto_story_p1': 'About three years ago I bought my first telescope – a beginner version with mount and tracking. The deciding factor was simply the fascination with the night sky, which I had always found incredibly beautiful. With this setup, I could already observe quite a bit visually and also take short exposures of a few seconds. For planetary shots, this was sufficient, but for deep-sky objects like galaxies or nebulae, the equipment quickly reached its limits.',
        'astrophoto_story_p2': 'Since astrophotography increasingly captivated me, I began to deal more intensively with the theoretical side and decided to upgrade my equipment step by step. First came a smaller telescope with compact camera to improve tracking through so-called guiding. Later followed a precise focuser and finally a cooled astro camera that also enables long exposures.',
        'astrophoto_story_p3': 'Despite these extensions, it became apparent that the mount reached its limits in terms of precision and that computer control still had optimization potential. But by now everything was available to build a fully automated telescope system.',
        'astrophoto_story_p4': 'Today my hobby encompasses the entire spectrum of sky photography: from planetary shots through images of the sun and moon to impressive deep-sky photos – galaxies, nebulae, star clusters, or even large-scale Milky Way landscapes. The journey from a simple beginner telescope to a complex system shows me that astrophotography requires not only technology, but above all passion, patience, and curiosity – and that\'s exactly what makes the appeal of this hobby for me.',

        # Gallery translations
        'view_gallery': 'View Gallery',
        'gallery_title': 'Astrophotography Gallery',
        'gallery_description': 'Explore my collection of astronomical images captured over the years, from planets and the moon to deep-sky objects like galaxies and nebulae.',
        'gallery_coming_soon': 'Gallery Coming Soon',
        'gallery_coming_soon_description': 'I\'m currently preparing my astrophotography collection for display. Please check back soon to see my astronomical images!',
        'back_to_project': 'Back to Project',
        'sample_image_1_title': 'Orion Nebula',
        'sample_image_1_desc': 'The Orion Nebula (M42) captured with long exposure techniques.',
        'sample_image_2_title': 'Saturn',
        'sample_image_2_desc': 'Detailed view of Saturn showing its ring system.',
    },

    'de': {
        # Navigation
        'home': 'Startseite',
        'about': 'Über mich',
        'projects': 'Projekte',
        'contact': 'Kontakt',

        # Hero Section
        'hero_description': '''Ich heiße Sebastian, habe vor Kurzem meine Matura abgeschlossen und leiste derzeit meinen Zivildienst. Im Anschluss beginne ich mein Studium der Technischen Physik, wo ich meine Begeisterung für Naturwissenschaft und Technik vertiefen möchte.

Schon während der Schulzeit habe ich mich mit Projekten wie dem Bau eines U-Boots, der Teilnahme am CanSat-Wettbewerb oder dem Programmieren eigener Websites beschäftigt. Das Tüfteln, Entwickeln und Verstehen von Zusammenhängen ist für mich nicht nur ein Hobby, sondern eine Leidenschaft. Auch die Astronomie fasziniert mich – der Blick in den Sternenhimmel eröffnet immer wieder neue Fragen und Ideen.

Neben der Technik spielt der Sport eine große Rolle in meinem Leben: ob Radfahren, Fußball, Tennis, Tischtennis, Volleyball, Skifahren, Wandern, Schwimmen oder Basketball – ich genieße die Bewegung und die Abwechslung in all ihren Facetten. Ich bin ständig auf der Suche nach neuen Herausforderungen, die ich mit Neugier und Einsatzbereitschaft angehe. Auf dieser Seite möchte ich einen Einblick in meine Projekte, Interessen und Ziele geben – vielleicht als Inspiration, vielleicht einfach nur, um mich besser kennenzulernen.''',

        'get_in_touch': 'Kontakt aufnehmen',
        'view_projects': 'Projekte ansehen',

        # Projects Section
        'featured_projects': 'Ausgewählte Projekte',
        'projects_description': 'Eine Sammlung meiner Arbeiten aus Webentwicklung, Ingenieurswesen, Wettbewerben und kreativen Projekten.',
        'view_all_projects': 'Alle Projekte ansehen',

        # Stats Section
        'graduated': 'Abgeschlossen',
        'major_projects': 'Große Projekte',
        'learning': 'Lernen',
        'stargazing': 'Sterne beobachten',

        # Footer
        'footer_text': '',

        # Project Data
        'project_wiener_schuelerliga_title': 'Wiener Schülerliga',
        'project_wiener_schuelerliga_desc': 'Schülerliga-Verwaltungssystem und Wettbewerbsplattform.',
        'project_chemieolympiade_title': 'Chemieolympiade',
        'project_chemieolympiade_desc': 'Teilnahme und Erfolge bei der Chemieolympiade.',
        'project_cansat_title': 'CanSat',
        'project_cansat_desc': 'Satellitentechnologie-Projekt mit atmosphärischen Messungen.',
        'project_triton_title': 'Triton',
        'project_triton_desc': 'Fortgeschrittenes Ingenieursprojekt mit innovativen Lösungen.',
        'project_cs50_title': 'CS50 Homepage',
        'project_cs50_desc': 'Harvard CS50 Abschlussprojekt - genau diese Website.',
        'project_astrophoto_title': 'Astrophotographie',
        'project_astrophoto_desc': 'Deep Space Bildgebung und astronomische Fotosammlung.',

        # Categories
        'cat_web_development': 'Webentwicklung',
        'cat_competition': 'Wettbewerb',
        'cat_engineering': 'Ingenieurswesen',
        'cat_photography': 'Fotografie',

        # Status
        'status_completed': 'Abgeschlossen',
        'status_achievement': 'Erfolg',
        'status_in_progress': 'In Arbeit',
        'status_current': 'Aktuell',
        'status_ongoing': 'Laufend',

        # Personal Info
        'personal_subtitle': 'Angehender Ingenieur • Problemlöser',
        'personal_description': 'Kürzlich Absolvent des Schottengymnasiums, derzeit Zivildienst vor dem Studium der Technischen Physik. Leidenschaftlich für Ingenieurswesen, Programmierung und Astrophotographie.',
        'current_status': 'Zivildienst',

        # About Page
        'about_me': 'Über mich',
        'about_description': '',
        'hello_sebastian': 'Hallo, ich bin Sebastian',
        'current_status_title': 'Aktueller Status',
        'interests_hobbies': 'Interessen & Hobbies',
        'interest_astrophotography': 'Astrophotographie und Sterne beobachten',
        'interest_programming': 'Programmierung und Softwareentwicklung',
        'interest_engineering': 'Ingenieursprojekte und Problemlösung',
        'interest_physics': 'Physik und wissenschaftliche Forschung',
        'interest_additional': '[Platzhalter für weiteres Hobby]',
        'education_timeline': 'Education',
        'experiences': 'Erfahrungen',
        'competitions_courses': 'Wettbewerbe und Kurse',
        'competitions_courses_desc': 'Teilnahme an außerschulischen Wettbewerben wie am CanSat-Wettbewerb (Mini-Satellitenbau), der Chemie-Olympiade und am DACH-Seminar',
        'cern_courses': 'Absolvierung zweier CERN-Online-Kurse',
        'vrvis_internship': 'Praktikum VRVIS',
        'vrvis_internship_desc': 'Programmieren eines robotischen Hundes und Entwicklung eines Computerspiels',
        'languages_skills': 'Sprachen und Fähigkeiten',
        'languages': 'Sprachen',
        'engagement_skills': 'Fähigkeiten und gesellschaftliches Engagement',
        'german_native': 'Deutsch',
        'english_bilingual': 'Englisch',
        'french_good': 'Französisch',
        'latin_very_good': 'Latein',
        'programming': 'Programmieren',
        'engagement_hobbies': 'Engagement und Hobbies',
        'astronomy_desc': 'Astronomie: Astrofotografie & Organisation von „Astronomie-Abenden" (Wissensvermittlung, Bildverarbeitung und Anwendung technischer Kenntnisse)',
        'class_representative': 'Klassensprecher',
        'sports_reading': 'Fußball, Tennis, Radfahren, Lesen',

        # About page hardcoded translations
        'native': 'Muttersprache',
        'bilingual': 'Zweisprachig',
        'b1_b2': 'B1 - B2',
        'academic_level': 'Akademisches Niveau (Großes Latinum)',
        'cansat_competition': 'CanSat Competition',
        'cansat_description': 'Entwurf und Bau eines Miniatursatelliten mit integrierten Sensoren, Funkverbindungen und umfassender Datenanalyse',
        'chemistry_olympiad': 'Chemieolympiade',
        'chemistry_olympiad_description': 'Chemiewettbewerb mit theoretischen und praktischen Komponenten',
        'dach_seminar': 'DACH Seminar',
        'dach_seminar_description': 'Internationales Chemieseminar für talentierte Schüler',
        'cern_courses_title': 'CERN Kurse',
        'cern_courses_description': 'Online-Kurse in Teilchenphysik und Beschleunigertechnologie',
        'vrvis_internship_title': 'VRVIS Praktikum',
        'vrvis_internship_description': 'Programmierung robotischer Systeme und Computerspielentwicklung',
        'astronomy': 'Astronomie',
        'astronomy_description': 'Astrophotographie und Astronomiеabende (Wissensvermittlung & Bildverarbeitung)',
        'software_web_development': 'Software- & Webentwicklung',
        'projects': 'Projekte',
        'projects_description': 'Umfassende Projektentwicklung und -management, das Ingenieurswesen, Programmierung und Design kombiniert - einschließlich dem Bau eines autonomen U-Boots von Grund auf',
        'student_leadership': 'Schülervertretung',
        'school': 'Schule',
        'free_time_activities': 'Freizeitaktivitäten',
        'soccer': 'Fußball',
        'tennis': 'Tennis',
        'basketball': 'Basketball',
        'cycling': 'Radfahren',
        'swimming': 'Schwimmen',
        'volleyball': 'Volleyball',
        'table_tennis': 'Tischtennis',
        'reading': 'Lesen',
        'cooking': 'Kochen',

        # Education entries
        'technical_physics_studies': 'Technische Physik Studium',
        'civil_service': 'Zivildienst',
        'paramedic_training': 'Sanitäterausbildung',
        'schottengymnasium': 'Schottengymnasium',
        'matura': 'Matura',
        'ves': 'VES',
        'elementary_school': 'Volksschule',

        # Wiener Schülerliga Story
        'wiener_story_title': 'Von Außenseitern zu Meistern – Unser Weg zum Gewinn der Wiener Schülerliga',
        'wiener_story_p1': 'Wenn ich auf unseren Weg zurückblicke, kann ich kaum glauben, wie weit wir gekommen sind. Als wir in der Unterstufe zu spielen begannen, waren die Ergebnisse alles andere als ermutigend. Spiele endeten oft in vernichtenden Niederlagen – Ergebnisse wie 1:10 waren leider keine Seltenheit. Uns fehlten Struktur, Selbstvertrauen und ehrlich gesagt auch die Erfahrung, um mit stärkeren Teams zu konkurrieren.',
        'wiener_story_p2': 'Alles begann sich zu ändern, als wir in die Oberstufe wechselten. Schritt für Schritt verbesserte sich unsere Leistung. Anstatt schwere Niederlagen zu erleiden, begannen wir standzuhalten und gewannen sogar etwa ein Drittel unserer Spiele. Zum ersten Mal hatten wir das Gefühl, auf den Platz zu gehören.',
        'wiener_story_p3': 'Letztes Jahr markierte einen historischen Schritt für unser Team: Wir erreichten zum allerersten Mal die K.O.-Phase. Obwohl wir im ersten Spiel verloren, gab uns diese Leistung allein die Motivation, weiterzumachen.',
        'wiener_story_p4': 'Diese Saison starteten wir mit einer neuen Einstellung. Wir arbeiteten an unserem Passspiel und taktischen Verständnis, und es zahlte sich aus. Wir gewannen bis auf ein Spiel alle Gruppenspiele, doch jedes Spiel war knapp – keine einfachen Siege. Wir waren nicht mehr die Mannschaft, die unterschätzt werden konnte.',
        'wiener_story_p5': 'In der K.O.-Phase wurde unser Fortschritt unbestreitbar. Spiel für Spiel wurden wir selbstbewusster. Das Halbfinale war jedoch die wahre Prüfung. Wir standen einer spezialisierten Sportschule gegenüber, die als eines der stärksten Teams des Turniers galt. Den größten Teil des Spiels sah es so aus, als würden wir es nicht schaffen. Aber im letzten Viertel änderte sich alles. Wir drehten das Spiel, und ich persönlich hatte eine meiner besten Leistungen als Torhüter. Mit zahlreichen entscheidenden Paraden wurde ich als Spieler des Spiels ausgezeichnet – eine Erinnerung, die ich nie vergessen werde.',
        'wiener_story_p6': 'Das Finale musste aufgrund des Schuljahresendes verschoben werden, was die Vorfreude nur noch steigerte. Dann, im September, kam endlich der große Tag. Angetrieben von Entschlossenheit und dem Glauben an uns selbst gaben wir alles – und es reichte. Wir gewannen die Wiener Schülerliga.',
        'wiener_story_p7': 'Von der Mannschaft, die einst zweistellig verlor, bis ganz an die Spitze – dieser Sieg ist der Beweis dafür, was mit Ausdauer, Teamwork und ständiger Verbesserung erreicht werden kann. Für uns ging es nicht nur darum, den Pokal zu heben. Es ging um die Reise: zusammenwachsen, aus Niederlagen lernen und Rückschläge in Motivation verwandeln.',
        'wiener_story_p8': 'Diese Meisterschaft ist das stolzeste Kapitel unserer bisherigen Geschichte – und hoffentlich nur der Anfang von vielen weiteren.',

        # Chemistry Olympiad Story
        'chemistry_story_title': 'Teilnahme an der Chemieolympiade',
        'chemistry_story_p1': 'Seit der 5. Klasse im Gymnasium nehme ich am Freifach Chemieolympiade teil. Schon früh hat mich nicht nur die Theorie, sondern auch das praktische Arbeiten im Labor fasziniert. Die Chemieolympiade ist für mich die ideale Möglichkeit, beides zu verbinden: theoretische Grundlagen zu vertiefen und gleichzeitig meine experimentellen Fähigkeiten weiterzuentwickeln.',
        'chemistry_story_p2': 'Jedes Jahr gibt es neben den wöchentlichen Vorbereitungseinheiten auch den sogenannten Kurswettbewerb. Dabei treten alle teilnehmenden Schüler:innen der Schule gegeneinander an, und die drei besten qualifizieren sich, um die Schule beim Landeswettbewerb zu vertreten. Gemeinsam mit zwei Freunden konnte ich mich dafür qualifizieren – ein großer Erfolg für uns alle.',
        'chemistry_story_p3': 'Der Landeswettbewerb selbst ist in zwei Teile gegliedert:',
        'chemistry_story_p4': 'Im theoretischen Teil mussten wir uns mit aktuellen Fragestellungen der Chemie auseinandersetzen und unser Wissen auf komplexe Probleme anwenden.',
        'chemistry_story_p5': 'Der praktische Teil fand im Labor statt. Hier galt es, durch verschiedene Methoden – wie dem „Tüpfeln" (das gezielte Mischen kleiner Chemikaliendrops) – herauszufinden, welche Substanzen in unbekannten Proben enthalten waren. Außerdem stand eine Titration auf dem Programm, bei der genaues Arbeiten und präzise Beobachtungen entscheidend waren.',
        'chemistry_story_p6': 'Dank der engagierten Vorbereitung durch unseren Lehrer konnten wir uns von Jahr zu Jahr steigern. Schließlich gelang es uns, bei unserer letzten Teilnahme den 3. Preis zu erringen – ein Ergebnis, das gleichzeitig den Schulrekord einstellte.',
        'chemistry_story_p7': 'Diese Erfolge zeigen mir, dass Ausdauer, Neugier und gute Teamarbeit nicht nur im Labor zählen, sondern auch im Wettbewerb zum Ziel führen. Für mich war die Chemieolympiade nicht nur ein Wettbewerb, sondern vor allem eine Möglichkeit, meine Leidenschaft für Chemie zu leben und über mich hinauszuwachsen.',

        # CanSat Project Story
        'cansat_story_title': 'CanSat Wettbewerb - Weltraumreise im Miniformat',
        'cansat_story_p1': 'Der CanSat-Wettbewerb ist ein Projekt, das von der Europäischen Weltraumorganisation (ESA) und dem Ars Electronica Center veranstaltet wird. Ziel ist es, einen Satelliten in der Größe einer Getränkedose von Grund auf zu entwickeln und ihn nach dem Start mithilfe einer Rakete wieder sicher zur Erde zurückzubringen – inklusive Datenerfassung während des gesamten Flugs.',
        'cansat_story_p2': 'Unser Team nahm diese Herausforderung mit Begeisterung an. Während viele andere Gruppen bereits Erfahrung im Programmieren und Bauen von Satelliten hatten, mussten wir uns dieses Wissen Schritt für Schritt erarbeiten. Doch genau darin lag für uns der Reiz: alles von Grund auf zu lernen und unsere Fortschritte direkt im Projekt umzusetzen.',
        'cansat_story_p3': 'Der Wettbewerb selbst begann spektakulär. Nach dem Raketenstart erreichte unser Satellit in etwa 380 Meter Höhe seine Ausstoßposition und wurde per Sprengladung freigesetzt. Der Fallschirm funktionierte wie geplant, und wir waren erleichtert, als die Dose sicher am Boden landete. Dank unserer Datenaufzeichnung konnten wir alle Vorgaben erfüllen – und sogar technische Prüfungen wie die sogenannten „Droptests" erfolgreich bestehen.',
        'cansat_story_p4': 'Am nächsten Tag präsentierten wir unser Projekt vor einer Jury und einem kleinen Publikum. Unsere Präsentation wurde durch zusätzliche Inhalte ergänzt, sodass wir schließlich einen Top-5-Platz erreichten – ein großer Erfolg für uns als Team.',
        'cansat_story_p5': 'Rückblickend war die Teilnahme nicht nur ein spannender Wettbewerb, sondern vor allem ein einmaliger Einblick in die Abläufe einer echten Weltraummission: vom Entwurf über den Bau bis hin zum erfolgreichen Einsatz. Möglich wurde dies auch durch die Unterstützung unserer Eltern sowie Sponsoren, bei denen wir uns herzlich bedanken möchten.',
        'cansat_story_p6': 'Der CanSat-Wettbewerb hat uns gezeigt, wie faszinierend Technik und Teamarbeit sein können – und dass selbst eine „Satellitendose" großartige Erfahrungen ins Rollen bringen kann.',

        # TRITON Project Story
        'triton_story_title': 'TRITON - Vom CanSat zur autonomen U-Boot-Navigation',
        'triton_story_p1': 'Was als kleines Satellitenprojekt begann, entwickelte sich Schritt für Schritt zu einem komplexen System für die autonome Navigation unter Wasser: das Projekt TRITON. Inspiriert durch die Erfahrungen beim CanSat-Wettbewerb haben wir unser Wissen in Physik, Programmierung, Elektronik und Projektmanagement genutzt, um ein völlig neues Einsatzfeld zu erschließen – die Meeresrobotik.',
        'triton_story_theory_title': 'Von der Theorie zur Praxis',
        'triton_story_p2': 'Herzstück von TRITON ist die Kombination verschiedener Sensoren, die gemeinsam ein präzises Bild der Umgebung liefern. Ein BME280-Sensor misst Temperatur, Luftfeuchtigkeit und Luftdruck – Parameter, die nicht nur für Wetter- und Umgebungsdaten relevant sind, sondern im U-Boot-Einsatz auch zur Tiefenbestimmung genutzt werden. Ergänzt wird das System durch ein MPU6050-Modul, das Beschleunigung und Drehbewegungen auf allen drei Achsen erfasst. So lassen sich Orientierung und Bewegung auch dann bestimmen, wenn GPS unter Wasser nicht verfügbar ist.',
        'triton_story_programming_title': 'Programmierung und Datenübertragung',
        'triton_story_p3': 'Auf der Softwareseite arbeitet TRITON mit einer Dual-Architektur: Ein Raspberry Pi Zero 2 W sammelt die Sensordaten, verarbeitet sie in Echtzeit und überträgt sie drahtlos. Ein PC-basiertes Missionskontrollsystem empfängt, analysiert und visualisiert die Daten in einem Web-Dashboard.',
        'triton_story_p4': 'Für die Kommunikation setzen wir auf LoRa-Funktechnologie, die eine robuste Datenübertragung über weite Strecken ermöglicht – entscheidend, wenn das System im Wasser arbeitet. Damit die Übertragung effizient bleibt, werden Daten nur dann gesendet, wenn sie sich um vordefinierte Schwellenwerte verändern. So wird das Netz entlastet, ohne an Genauigkeit einzubüßen.',
        'triton_story_design_title': 'Design und Konstruktion',
        'triton_story_p5': 'Auch die mechanische Integration spielt eine wichtige Rolle: Sensoren müssen exakt positioniert, Elektronik zuverlässig gekapselt und die Antenne optimal ausgerichtet werden. Parallel zu den Softwaretests flossen daher erste Überlegungen in die CAD-gestützte Entwicklung eines wasserdichten Gehäuses ein – ein entscheidender Schritt, um die Technik auch tatsächlich unter Wasser einsatzfähig zu machen.',
        'triton_story_project_mgmt_title': 'Projektmanagement und Entwicklungsschritte',
        'triton_story_p6': 'TRITON entstand nicht über Nacht, sondern in zahlreichen Iterationen. Jede Version – von TRY1 bis TRY9 – baute auf den Erfahrungen der vorherigen auf: von der ersten Sensorintegration über Datenlogging und Fehlerbehandlung bis hin zur vollständigen Webvisualisierung mit Statistikfunktionen. Alte Codeversionen wurden sorgfältig archiviert, um den Entwicklungsprozess transparent und nachvollziehbar zu dokumentieren.',
        'triton_story_applications_title': 'Anwendungsmöglichkeiten',
        'triton_story_p7': 'Die Einsatzfelder für TRITON sind vielfältig: Autonome Navigation von Unterwasserrobotern ohne GPS, Umweltmonitoring in Seen und Meeren, Forschung im Bereich mariner Ökosysteme, Unterstützung bei Such- und Rettungsaktionen.',
        'triton_story_conclusion_title': 'Fazit',
        'triton_story_p8': 'TRITON zeigt, wie man mit systematischem Vorgehen, technischer Neugier und kontinuierlicher Verbesserung ein Projekt von einer Satellitendose zum autonomen U-Boot-System weiterentwickeln kann. Es verbindet Physik, Informatik, Elektronik und Design zu einem innovativen Gesamtkonzept – und bildet die Basis für künftige Entwicklungen im Bereich der maritimen Robotik.',

        # CS50 Project Story
        'cs50_story_title': 'CS50 - Einstieg in die Welt der Informatik',
        'cs50_story_p1': 'Um meine Kenntnisse in Informatik und Programmierung zu vertiefen, habe ich den Kurs CS50: Introduction to Computer Science der Harvard University absolviert. Der Kurs gilt als einer der bekanntesten und umfassendsten Einstiege in die Informatik.',
        'cs50_story_p2': 'Besonders spannend war für mich die Vielfalt der Themen: Von den Grundlagen der Algorithmen und Datenstrukturen über C und Python bis hin zu Webentwicklung mit HTML, CSS und JavaScript. Jede Woche wurden neue Problemstellungen präsentiert, die nicht nur technisches Wissen, sondern auch logisches Denken und Ausdauer erforderten.',
        'cs50_story_p3': 'CS50 hat mir gezeigt, wie breit und gleichzeitig tief das Feld der Informatik ist. Durch die praxisnahen Aufgaben konnte ich nicht nur die Theorie verstehen, sondern auch echte Projekte umsetzen – ein Lernprozess, der sowohl fordernd als auch unglaublich bereichernd war.',

        # Astrophotography Project Story
        'astrophoto_story_title': 'Astrofotografie - Von den ersten Beobachtungen zum automatisierten Teleskopsystem',
        'astrophoto_story_p1': 'Vor rund drei Jahren habe ich mir mein erstes Teleskop gekauft – eine Einsteigerversion mit Montierung und Nachführung. Ausschlaggebend war schlicht die Faszination für den Nachthimmel, den ich schon immer unglaublich schön fand. Mit diesem Setup konnte ich visuell bereits einiges beobachten und auch kurze Aufnahmen von wenigen Sekunden machen. Für Planetenaufnahmen reichte das aus, doch für Deep-Sky-Objekte wie Galaxien oder Nebel war die Ausrüstung schnell am Limit.',
        'astrophoto_story_p2': 'Da mich die Astrofotografie zunehmend fesselte, begann ich mich intensiver mit der theoretischen Seite zu beschäftigen und beschloss, meine Ausrüstung Schritt für Schritt aufzurüsten. Zunächst kam ein kleineres Teleskop mit kompakter Kamera hinzu, um die Nachführung durch sogenanntes Guiding zu verbessern. Später folgten ein präziser Fokussierer und schließlich eine gekühlte Astrokamera, die auch Langzeitbelichtungen ermöglicht.',
        'astrophoto_story_p3': 'Trotz dieser Erweiterungen zeigte sich, dass die Montierung in puncto Genauigkeit an ihre Grenzen stieß und auch die Steuerung per Computer noch Optimierungspotenzial hatte. Doch mittlerweile war alles vorhanden, um ein vollständig automatisiertes Teleskopsystem aufzubauen.',
        'astrophoto_story_p4': 'Heute umfasst mein Hobby das gesamte Spektrum der Himmelsfotografie: von Planetenaufnahmen über Bilder der Sonne und des Mondes bis hin zu beeindruckenden Deep-Sky-Fotos – Galaxien, Nebel, Sternhaufen oder sogar großflächige Milchstraßen-Landschaften. Die Reise von einem einfachen Einsteigerteleskop bis hin zu einem komplexen System zeigt mir, dass Astrofotografie nicht nur Technik, sondern vor allem Leidenschaft, Geduld und Neugier erfordert – und genau das macht den Reiz dieses Hobbys für mich aus.',

        # Gallery translations
        'view_gallery': 'Galerie ansehen',
        'gallery_title': 'Astrofotografie-Galerie',
        'gallery_description': 'Entdecken Sie meine Sammlung astronomischer Bilder, die über die Jahre entstanden sind, von Planeten und dem Mond bis hin zu Deep-Sky-Objekten wie Galaxien und Nebeln.',
        'gallery_coming_soon': 'Galerie folgt bald',
        'gallery_coming_soon_description': 'Ich bereite gerade meine Astrofotografie-Sammlung zur Anzeige vor. Schauen Sie bald wieder vorbei, um meine astronomischen Bilder zu sehen!',
        'back_to_project': 'Zurück zum Projekt',
        'sample_image_1_title': 'Orionnebel',
        'sample_image_1_desc': 'Der Orionnebel (M42) aufgenommen mit Langzeittechnik.',
        'sample_image_2_title': 'Saturn',
        'sample_image_2_desc': 'Detaillierte Aufnahme des Saturn mit seinem Ringsystem.',
    },

    'fr': {
        # Navigation
        'home': 'Accueil',
        'about': 'À propos',
        'projects': 'Projets',
        'contact': 'Contact',

        # Hero Section
        'hero_description': '''Je m'appelle Sebastian, j'ai récemment terminé ma Matura et j'effectue actuellement mon service civil. Ensuite, je commencerai mes études en Physique Technique, où je souhaite approfondir ma passion pour les sciences naturelles et la technologie.

Déjà pendant mes études, je me suis engagé dans des projets comme la construction d'un sous-marin, la participation au concours CanSat ou la programmation de mes propres sites web. Bricoler, développer et comprendre les connexions n'est pas seulement un hobby pour moi, mais une passion. L'astronomie me fascine aussi – regarder le ciel étoilé ouvre toujours de nouvelles questions et idées.

Outre la technologie, le sport joue un rôle majeur dans ma vie : que ce soit le cyclisme, le football, le tennis, le tennis de table, le volley-ball, le ski, la randonnée, la natation ou le basketball – j'apprécie le mouvement et la variété sous toutes leurs facettes. Je suis constamment à la recherche de nouveaux défis que j'aborde avec curiosité et dévouement. Sur cette page, je veux donner un aperçu de mes projets, intérêts et objectifs – peut-être comme inspiration, peut-être simplement pour mieux me connaître.''',

        'get_in_touch': 'Prendre contact',
        'view_projects': 'Voir les projets',

        # Projects Section
        'featured_projects': 'Projets sélectionnés',
        'projects_description': 'Une collection de mes travaux couvrant le développement web, l\'ingénierie, les compétitions et les projets créatifs.',
        'view_all_projects': 'Voir tous les projets',

        # Stats Section
        'graduated': 'Diplômé',
        'major_projects': 'Grands projets',
        'learning': 'Apprentissage',
        'stargazing': 'Observer les étoiles',

        # Footer
        'footer_text': '',

        # Project Data
        'project_wiener_schuelerliga_title': 'Ligue scolaire viennoise',
        'project_wiener_schuelerliga_desc': 'Système de gestion de ligue étudiante et plateforme de compétition.',
        'project_chemieolympiade_title': 'Olympiade de chimie',
        'project_chemieolympiade_desc': 'Participation et réalisations aux olympiades de chimie.',
        'project_cansat_title': 'CanSat',
        'project_cansat_desc': 'Projet de technologie satellitaire avec mesures atmosphériques.',
        'project_triton_title': 'Triton',
        'project_triton_desc': 'Projet d\'ingénierie avancé avec solutions innovantes.',
        'project_cs50_title': 'Page d\'accueil CS50',
        'project_cs50_desc': 'Projet final Harvard CS50 - ce site web même.',
        'project_astrophoto_title': 'Astrophotographie',
        'project_astrophoto_desc': 'Imagerie spatiale profonde et collection de photographie astronomique.',

        # Categories
        'cat_web_development': 'Développement Web',
        'cat_competition': 'Compétition',
        'cat_engineering': 'Ingénierie',
        'cat_photography': 'Photographie',

        # Status
        'status_completed': 'Terminé',
        'status_achievement': 'Réalisation',
        'status_in_progress': 'En cours',
        'status_current': 'Actuel',
        'status_ongoing': 'En cours',

        # Personal Info
        'personal_subtitle': 'Ingénieur aspirant • Résolveur de problèmes',
        'personal_description': 'Récent diplômé du Schottengymnasium, effectuant actuellement le service civil avant d\'étudier la Physique Technique. Passionné par l\'ingénierie, la programmation et l\'astrophotographie.',
        'current_status': 'Service civil',

        # About Page
        'about_me': 'À propos de moi',
        'about_description': '',
        'hello_sebastian': 'Bonjour, je suis Sebastian',
        'current_status_title': 'Statut actuel',
        'interests_hobbies': 'Intérêts & Loisirs',
        'interest_astrophotography': 'Astrophotographie et observation des étoiles',
        'interest_programming': 'Programmation et développement de logiciels',
        'interest_engineering': 'Projets d\'ingénierie et résolution de problèmes',
        'interest_physics': 'Physique et recherche scientifique',
        'interest_additional': '[Placeholder pour loisir supplémentaire]',
        'education_timeline': 'Education',
        'experiences': 'Expériences',
        'competitions_courses': 'Concours et Cours',
        'competitions_courses_desc': 'Participation à des concours extrascolaires comme le concours CanSat (construction de mini-satellites), l\'Olympiade de Chimie et le séminaire DACH',
        'cern_courses': 'Achèvement de deux cours en ligne du CERN',
        'vrvis_internship': 'Stage VRVIS',
        'vrvis_internship_desc': 'Programmation d\'un chien robotique et développement d\'un jeu informatique',
        'languages_skills': 'Langues et Compétences',
        'languages': 'Langues',
        'engagement_skills': 'Compétences et Engagement Communautaire',
        'german_native': 'Allemand',
        'english_bilingual': 'Anglais',
        'french_good': 'Français',
        'latin_very_good': 'Latin',
        'programming': 'Programmation',
        'engagement_hobbies': 'Engagement et Loisirs',
        'astronomy_desc': 'Astronomie : Astrophotographie & organisation de "soirées astronomiques" (transmission de connaissances, traitement d\'images et application de compétences techniques)',
        'class_representative': 'Représentant de classe',
        'sports_reading': 'Football, tennis, cyclisme, lecture',

        # About page hardcoded translations
        'native': 'Langue maternelle',
        'bilingual': 'Bilingue',
        'b1_b2': 'B1 - B2',
        'academic_level': 'Niveau académique (Großes Latinum)',
        'cansat_competition': 'Compétition CanSat',
        'cansat_description': 'Conception et construction d\'un satellite miniature avec capteurs intégrés, communications radio et analyse complète de données',
        'chemistry_olympiad': 'Olympiade de Chimie',
        'chemistry_olympiad_description': 'Compétition de chimie avec composants théoriques et pratiques',
        'dach_seminar': 'Séminaire DACH',
        'dach_seminar_description': 'Séminaire international de chimie pour étudiants talentueux',
        'cern_courses_title': 'Cours CERN',
        'cern_courses_description': 'Cours en ligne en physique des particules et technologie des accélérateurs',
        'vrvis_internship_title': 'Stage VRVIS',
        'vrvis_internship_description': 'Programmation de systèmes robotiques et développement de jeux informatiques',
        'astronomy': 'Astronomie',
        'astronomy_description': 'Astrophotographie et soirées astronomiques (transmission de connaissances et traitement d\'images)',
        'software_web_development': 'Développement Logiciel & Web',
        'projects': 'Projets',
        'projects_description': 'Développement et gestion de projets complets combinant ingénierie, programmation et design - y compris la construction d\'un sous-marin autonome à partir de zéro',
        'student_leadership': 'Rôle de leadership étudiant',
        'school': 'École',
        'free_time_activities': 'Activités de Temps Libre',
        'soccer': 'Football',
        'tennis': 'Tennis',
        'basketball': 'Basketball',
        'cycling': 'Cyclisme',
        'swimming': 'Natation',
        'volleyball': 'Volley-ball',
        'table_tennis': 'Tennis de Table',
        'reading': 'Lecture',
        'cooking': 'Cuisine',

        # Education entries
        'technical_physics_studies': 'Études de Physique Technique',
        'civil_service': 'Service Civil',
        'paramedic_training': 'Formation de Secouriste',
        'schottengymnasium': 'Schottengymnasium',
        'matura': 'Matura',
        'ves': 'VES',
        'elementary_school': 'École Primaire',

        # Wiener Schülerliga Story
        'wiener_story_title': 'D\'Outsiders à Champions – Notre Parcours vers la Victoire de la Ligue Scolaire Viennoise',
        'wiener_story_p1': 'En regardant en arrière sur notre parcours, il est presque difficile de croire jusqu\'où nous sommes arrivés. Quand nous avons commencé à concourir au collège, les résultats étaient tout sauf encourageants. Les matchs se terminaient souvent par des défaites écrasantes – des scores comme 1:10 n\'étaient malheureusement pas rares. Il nous manquait de la structure, de la confiance et, très honnêtement, l\'expérience pour concourir avec des équipes plus fortes.',
        'wiener_story_p2': 'Tout a commencé à changer quand nous sommes passés au lycée. Petit à petit, notre performance s\'est améliorée. Au lieu de subir de lourdes défaites, nous avons commencé à tenir bon, réussissant même à gagner environ un tiers de nos matchs. Pour la première fois, nous avions l\'impression d\'appartenir au terrain.',
        'wiener_story_p3': 'L\'année dernière a marqué une étape historique pour notre équipe : nous avons atteint la phase éliminatoire pour la toute première fois. Même si nous avons perdu au premier match, cette réalisation seule nous a donné la motivation de continuer à pousser.',
        'wiener_story_p4': 'Cette saison, nous sommes entrés avec un nouvel état d\'esprit. Nous avons travaillé sur nos passes et notre conscience tactique, et cela a payé. Nous avons gagné tous les matchs sauf un en phase de groupe, pourtant chaque match était serré – aucune victoire facile. Nous n\'étions plus une équipe à sous-estimer.',
        'wiener_story_p5': 'En phase éliminatoire, notre progrès est devenu indéniable. Match après match, nous avons gagné en confiance. La demi-finale, cependant, était le vrai test. Nous avons fait face à une école de sport dédiée, largement considérée comme l\'une des équipes les plus fortes de la compétition. Pendant la majeure partie du match, il semblait que nous n\'y arriverions pas. Mais dans le dernier quart, tout a changé. Nous avons retourné le match, et j\'ai personnellement eu l\'une de mes meilleures performances en tant que gardien. Avec de nombreux arrêts décisifs, j\'ai été honoré comme homme du match – un souvenir que je n\'oublierai jamais.',
        'wiener_story_p6': 'La finale a dû être reportée en raison de la fin de l\'année scolaire, ce qui n\'a fait qu\'ajouter à l\'anticipation. Puis, en septembre, le grand jour est enfin arrivé. Alimentés par la détermination et la croyance en nous-mêmes, nous avons donné tout ce que nous avions – et c\'était suffisant. Nous avons gagné la Ligue Scolaire Viennoise.',
        'wiener_story_p7': 'D\'être l\'équipe qui perdait autrefois à deux chiffres, à être au sommet – cette victoire est la preuve de ce qui peut être accompli avec la persévérance, le travail d\'équipe et l\'amélioration constante. Pour nous, il ne s\'agissait pas seulement de soulever le trophée. Il s\'agissait du voyage : grandir ensemble, apprendre des défaites, et transformer les revers en motivation.',
        'wiener_story_p8': 'Ce championnat est le chapitre le plus fier de notre histoire jusqu\'à présent – et espérons juste le début de beaucoup d\'autres.',

        # Chemistry Olympiad Story
        'chemistry_story_title': 'Participation à l\'Olympiade de Chimie',
        'chemistry_story_p1': 'Depuis ma cinquième année de lycée, je participe au cours optionnel d\'Olympiade de Chimie. Très tôt, j\'ai été fasciné non seulement par la théorie, mais aussi par le travail pratique en laboratoire. L\'Olympiade de Chimie est pour moi le moyen idéal de combiner les deux : approfondir les bases théoriques tout en développant simultanément mes compétences expérimentales.',
        'chemistry_story_p2': 'Chaque année, en plus des séances de préparation hebdomadaires, il y a aussi ce qu\'on appelle la compétition de cours. Tous les élèves participants de l\'école s\'affrontent, et les trois meilleurs se qualifient pour représenter l\'école au concours régional. Avec deux amis, j\'ai pu me qualifier – un grand succès pour nous tous.',
        'chemistry_story_p3': 'Le concours régional lui-même est divisé en deux parties :',
        'chemistry_story_p4': 'Dans la partie théorique, nous avons dû nous confronter aux questions actuelles de la chimie et appliquer nos connaissances à des problèmes complexes.',
        'chemistry_story_p5': 'La partie pratique s\'est déroulée en laboratoire. Il s\'agissait de déterminer quelles substances étaient contenues dans des échantillons inconnus en utilisant diverses méthodes – comme le "test à la goutte" (le mélange ciblé de petites gouttes de produits chimiques). De plus, une titration était au programme, où un travail précis et des observations exactes étaient cruciaux.',
        'chemistry_story_p6': 'Grâce à la préparation engagée de notre professeur, nous avons pu nous améliorer d\'année en année. Finalement, nous avons réussi à remporter le 3e prix lors de notre dernière participation – un résultat qui établissait simultanément le record de l\'école.',
        'chemistry_story_p7': 'Ces succès me montrent que la persévérance, la curiosité et le bon travail d\'équipe comptent non seulement en laboratoire, mais mènent aussi au succès en compétition. Pour moi, l\'Olympiade de Chimie n\'était pas seulement une compétition, mais surtout une opportunité de vivre ma passion pour la chimie et de me dépasser.',

        # CanSat Project Story
        'cansat_story_title': 'Concours CanSat – Voyage Spatial en Format Miniature',
        'cansat_story_p1': 'Le concours CanSat est un projet organisé par l\'Agence spatiale européenne (ESA) et l\'Ars Electronica Center. L\'objectif est de développer un satellite de la taille d\'une canette de boisson de zéro et de le ramener en sécurité sur Terre après le lancement à l\'aide d\'une fusée – y compris la collecte de données pendant tout le vol.',
        'cansat_story_p2': 'Notre équipe a relevé ce défi avec enthousiasme. Alors que de nombreux autres groupes avaient déjà de l\'expérience en programmation et en construction de satellites, nous avons dû acquérir ces connaissances étape par étape. Mais c\'est exactement ce qui nous attirait : tout apprendre de zéro et mettre nos progrès directement en œuvre dans le projet.',
        'cansat_story_p3': 'Le concours lui-même a commencé de manière spectaculaire. Après le lancement de la fusée, notre satellite a atteint sa position d\'éjection à environ 380 mètres d\'altitude et a été libéré par charge explosive. Le parachute a fonctionné comme prévu, et nous étions soulagés quand la canette a atterri en sécurité au sol. Grâce à notre enregistrement de données, nous avons pu répondre à toutes les exigences – et même réussir des tests techniques comme les soi-disant "tests de chute".',
        'cansat_story_p4': 'Le lendemain, nous avons présenté notre projet à un jury et à un petit public. Notre présentation a été enrichie de contenu supplémentaire, nous permettant finalement d\'atteindre une place dans le top 5 – un grand succès pour nous en tant qu\'équipe.',
        'cansat_story_p5': 'Rétrospectivement, la participation n\'était pas seulement une compétition passionnante, mais surtout un aperçu unique des processus d\'une vraie mission spatiale : de la conception à la construction jusqu\'au déploiement réussi. Cela a également été rendu possible grâce au soutien de nos parents ainsi que des sponsors, que nous aimerions remercier chaleureusement.',
        'cansat_story_p6': 'Le concours CanSat nous a montré à quel point la technologie et le travail d\'équipe peuvent être fascinants – et qu\'même une "canette satellite" peut mettre en mouvement de grandes expériences.',

        # TRITON Project Story
        'triton_story_title': 'TRITON – Du CanSat à la Navigation Autonome de Sous-Marin',
        'triton_story_p1': 'Ce qui a commencé comme un petit projet de satellite s\'est développé étape par étape en un système complexe pour la navigation autonome sous-marine : le projet TRITON. Inspirés par les expériences du concours CanSat, nous avons utilisé nos connaissances en physique, programmation, électronique et gestion de projet pour explorer un domaine d\'application complètement nouveau – la robotique marine.',
        'triton_story_theory_title': 'De la Théorie à la Pratique',
        'triton_story_p2': 'Le cœur de TRITON est la combinaison de divers capteurs qui fournissent ensemble une image précise de l\'environnement. Un capteur BME280 mesure la température, l\'humidité et la pression atmosphérique – des paramètres qui ne sont pas seulement pertinents pour les données météorologiques et environnementales, mais sont également utilisés pour la détermination de la profondeur dans le déploiement de sous-marins. Le système est complété par un module MPU6050, qui capture l\'accélération et les mouvements de rotation sur les trois axes. Cela permet de déterminer l\'orientation et le mouvement même lorsque le GPS n\'est pas disponible sous l\'eau.',
        'triton_story_programming_title': 'Programmation et Transmission de Données',
        'triton_story_p3': 'Du côté logiciel, TRITON fonctionne avec une architecture duale : Un Raspberry Pi Zero 2 W collecte les données des capteurs, les traite en temps réel et les transmet sans fil. Un système de contrôle de mission basé sur PC reçoit, analyse et visualise les données dans un tableau de bord web.',
        'triton_story_p4': 'Pour la communication, nous nous appuyons sur la technologie radio LoRa, qui permet une transmission de données robuste sur de longues distances – cruciale lorsque le système fonctionne dans l\'eau. Pour maintenir la transmission efficace, les données ne sont envoyées que lorsqu\'elles changent de valeurs seuils prédéfinies. Cela soulage le réseau sans perdre en précision.',
        'triton_story_design_title': 'Conception et Construction',
        'triton_story_p5': 'L\'intégration mécanique joue également un rôle important : les capteurs doivent être positionnés avec précision, l\'électronique encapsulée de manière fiable et l\'antenne alignée de manière optimale. Parallèlement aux tests logiciels, les premières considérations ont été intégrées dans le développement assisté par CAO d\'un boîtier étanche – une étape cruciale pour rendre la technologie réellement déployable sous l\'eau.',
        'triton_story_project_mgmt_title': 'Gestion de Projet et Étapes de Développement',
        'triton_story_p6': 'TRITON n\'est pas apparu du jour au lendemain, mais à travers de nombreuses itérations. Chaque version – de TRY1 à TRY9 – s\'est appuyée sur les expériences de la précédente : de la première intégration de capteurs à travers l\'enregistrement de données et la gestion d\'erreurs jusqu\'à la visualisation web complète avec des fonctions statistiques. Les anciennes versions de code ont été soigneusement archivées pour documenter le processus de développement de manière transparente et compréhensible.',
        'triton_story_applications_title': 'Possibilités d\'Application',
        'triton_story_p7': 'Les domaines d\'application pour TRITON sont divers : Navigation autonome de robots sous-marins sans GPS, surveillance environnementale dans les lacs et mers, recherche dans le domaine des écosystèmes marins, soutien dans les opérations de recherche et sauvetage.',
        'triton_story_conclusion_title': 'Conclusion',
        'triton_story_p8': 'TRITON montre comment on peut développer un projet d\'une canette satellite à un système de sous-marin autonome grâce à une approche systématique, une curiosité technique et une amélioration continue. Il combine physique, informatique, électronique et design en un concept global innovant – et forme la base pour les développements futurs dans le domaine de la robotique marine.',

        # CS50 Project Story
        'cs50_story_title': 'CS50 – Introduction au Monde de l\'Informatique',
        'cs50_story_p1': 'Pour approfondir mes connaissances en informatique et programmation, j\'ai suivi le cours CS50: Introduction to Computer Science de l\'Université Harvard. Le cours est considéré comme l\'une des introductions les plus connues et les plus complètes à l\'informatique.',
        'cs50_story_p2': 'Ce qui était particulièrement passionnant pour moi était la diversité des sujets : des bases des algorithmes et structures de données à travers C et Python jusqu\'au développement web avec HTML, CSS et JavaScript. Chaque semaine, de nouveaux ensembles de problèmes étaient présentés qui nécessitaient non seulement des connaissances techniques, mais aussi une pensée logique et de la persévérance.',
        'cs50_story_p3': 'CS50 m\'a montré à quel point le domaine de l\'informatique est large et en même temps profond. Grâce aux assignations orientées pratique, j\'ai pu non seulement comprendre la théorie, mais aussi implémenter de vrais projets – un processus d\'apprentissage qui était à la fois exigeant et incroyablement enrichissant.',

        # Astrophotography Project Story
        'astrophoto_story_title': 'Astrophotographie – Des Premières Observations au Système de Télescope Automatisé',
        'astrophoto_story_p1': 'Il y a environ trois ans, j\'ai acheté mon premier télescope – une version débutant avec monture et suivi. Le facteur décisif était simplement la fascination pour le ciel nocturne, que j\'ai toujours trouvé incroyablement beau. Avec cette configuration, je pouvais déjà observer pas mal de choses visuellement et aussi prendre de courtes expositions de quelques secondes. Pour les photos planétaires, c\'était suffisant, mais pour les objets du ciel profond comme les galaxies ou nébuleuses, l\'équipement atteignait rapidement ses limites.',
        'astrophoto_story_p2': 'Comme l\'astrophotographie me captivait de plus en plus, j\'ai commencé à m\'occuper plus intensément du côté théorique et j\'ai décidé d\'améliorer mon équipement étape par étape. D\'abord est venu un télescope plus petit avec caméra compacte pour améliorer le suivi à travers ce qu\'on appelle le guidage. Plus tard ont suivi un focaliseur précis et finalement une caméra astro refroidie qui permet aussi les longues expositions.',
        'astrophoto_story_p3': 'Malgré ces extensions, il est devenu apparent que la monture atteignait ses limites en termes de précision et que le contrôle par ordinateur avait encore un potentiel d\'optimisation. Mais maintenant tout était disponible pour construire un système de télescope entièrement automatisé.',
        'astrophoto_story_p4': 'Aujourd\'hui mon hobby englobe tout le spectre de la photographie du ciel : des photos planétaires à travers les images du soleil et de la lune jusqu\'aux photos impressionnantes du ciel profond – galaxies, nébuleuses, amas d\'étoiles, ou même des paysages à grande échelle de la Voie lactée. Le voyage d\'un simple télescope débutant jusqu\'à un système complexe me montre que l\'astrophotographie nécessite non seulement de la technologie, mais surtout de la passion, de la patience et de la curiosité – et c\'est exactement ce qui fait l\'attrait de ce hobby pour moi.',

        # Gallery translations
        'view_gallery': 'Voir la Galerie',
        'gallery_title': 'Galerie d\'Astrophotographie',
        'gallery_description': 'Explorez ma collection d\'images astronomiques capturées au fil des années, des planètes et de la lune aux objets du ciel profond comme les galaxies et nébuleuses.',
        'gallery_coming_soon': 'Galerie à Venir',
        'gallery_coming_soon_description': 'Je prépare actuellement ma collection d\'astrophotographie pour l\'affichage. Revenez bientôt pour voir mes images astronomiques !',
        'back_to_project': 'Retour au Projet',
        'sample_image_1_title': 'Nébuleuse d\'Orion',
        'sample_image_1_desc': 'La nébuleuse d\'Orion (M42) capturée avec des techniques de longue exposition.',
        'sample_image_2_title': 'Saturne',
        'sample_image_2_desc': 'Vue détaillée de Saturne montrant son système d\'anneaux.',
    }
}

def get_translation(lang, key, default=None):
    """Get translation for given language and key"""
    return TRANSLATIONS.get(lang, {}).get(key, default or key)

def get_supported_languages():
    """Get list of supported language codes"""
    return list(TRANSLATIONS.keys())