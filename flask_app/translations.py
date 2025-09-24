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
        'about_description': 'Get to know more about my background, education, and journey.',
        'hello_sebastian': 'Hello, I\'m Sebastian',
        'current_status_title': 'Current Status',
        'interests_hobbies': 'Interests & Hobbies',
        'interest_astrophotography': 'Astrophotography and stargazing',
        'interest_programming': 'Programming and software development',
        'interest_engineering': 'Engineering projects and problem-solving',
        'interest_physics': 'Physics and scientific research',
        'interest_additional': '[Placeholder for additional hobby]',
        'education_timeline': 'Education Timeline',

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
        'about_description': 'Erfahre mehr über meinen Hintergrund, meine Ausbildung und meinen Weg.',
        'hello_sebastian': 'Hallo, ich bin Sebastian',
        'current_status_title': 'Aktueller Status',
        'interests_hobbies': 'Interessen & Hobbies',
        'interest_astrophotography': 'Astrophotographie und Sterne beobachten',
        'interest_programming': 'Programmierung und Softwareentwicklung',
        'interest_engineering': 'Ingenieursprojekte und Problemlösung',
        'interest_physics': 'Physik und wissenschaftliche Forschung',
        'interest_additional': '[Platzhalter für weiteres Hobby]',
        'education_timeline': 'Bildungsweg',

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
        'about_description': 'Apprenez-en plus sur mon parcours, ma formation et mon voyage.',
        'hello_sebastian': 'Bonjour, je suis Sebastian',
        'current_status_title': 'Statut actuel',
        'interests_hobbies': 'Intérêts & Loisirs',
        'interest_astrophotography': 'Astrophotographie et observation des étoiles',
        'interest_programming': 'Programmation et développement de logiciels',
        'interest_engineering': 'Projets d\'ingénierie et résolution de problèmes',
        'interest_physics': 'Physique et recherche scientifique',
        'interest_additional': '[Placeholder pour loisir supplémentaire]',
        'education_timeline': 'Parcours éducatif',

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
    }
}

def get_translation(lang, key, default=None):
    """Get translation for given language and key"""
    return TRANSLATIONS.get(lang, {}).get(key, default or key)

def get_supported_languages():
    """Get list of supported language codes"""
    return list(TRANSLATIONS.keys())