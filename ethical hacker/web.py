import React, { useState, useEffect } from 'react';

// --- Static Data Mockup for Portfolio Content ---
const PORTFOLIO_DATA = {
    personal: {
        name: "Stella Mutai",
        title: "Certified Ethical Hacker (CEH) | Cisco Networking Academy",
        bio: "Dedicated cybersecurity professional specializing in penetration testing, vulnerability analysis, and network defense. Leveraging a strong foundation from the Cisco Networking Academy and active participation in CTFs to build highly resilient systems.",
        email: "stellamutai254@gmail.com",
        linkedin: "www.linkedin.com/in/stella-mutai",
        github: "https://github.com/stellamutai",
        // Placeholder for the profile image URL
        photoUrl: "https://placehold.co/300x300/1d4ed8/ffffff?text=Stella+Mutai", 
    },
    resume: [
        { type: "experience", title: "Security Analyst Intern", company: "SecureFuture Solutions", years: "2024 - Present", details: ["Conducted penetration testing on client web applications and internal infrastructure.", "Developed custom scripts for automated vulnerability scanning and reporting.", "Contributed to incident response planning and post-mortem analysis."] },
        { type: "experience", title: "Network Technician", company: "TechConnect Inc.", years: "2022 - 2024", details: ["Managed and maintained Cisco network devices (routers, switches) across three branch offices.", "Implemented hardening procedures based on CIS benchmarks.", "Provided tier 3 support for complex network security issues."] },
        { type: "education", title: "Certified Ethical Hacker (CEH)", institution: "EC-Council", years: "2024", details: ["Focus areas included: scanning networks, enumeration, system hacking, malware threats, sniffing, social engineering, and DoS."] },
        { type: "education", title: "Cisco Networking Academy Certification", institution: "Cisco Networking Academy", years: "2021", details: ["Comprehensive training in network fundamentals, routing, switching, and infrastructure security."] },
    ],
    projects: [
        { id: 1, title: "Custom Web Application Firewall (WAF)", type: "project", summary: "Deployed a high-availability NGINX-based WAF using ModSecurity rulesets to protect a mock e-commerce platform from OWASP Top 10 vulnerabilities.", tech: ["NGINX", "ModSecurity", "Docker", "Linux"], writeup: "### Project: Custom Web Application Firewall (WAF)\n\n**Goal:** Implement a robust defense layer against common web attack vectors.\n\n**Methodology:**\n1.  Set up an NGINX reverse proxy.\n2.  Integrated ModSecurity and utilized the OWASP CRS (Core Rule Set).\n3.  Tuned rules to minimize false positives while maintaining maximum protection.\n\n**Key Outcome:** Achieved a 99% blocking rate against simulated XSS and SQL injection attacks." },
        { id: 2, title: "Active Directory Recon Automation", type: "project", summary: "Python script utilizing LDAP and native tools for automated enumeration of user accounts, groups, and domain trusts in a simulated AD environment.", tech: ["Python", "LDAP", "Kerberos"], writeup: "### Project: Active Directory Recon Automation\n\n**Goal:** Speed up the initial enumeration phase of internal penetration tests.\n\n**Methodology:** The script sequentially queries the LDAP server for user lists, runs domain enumeration checks, and identifies potential misconfigurations. It outputs results in a structured JSON format.\n\n**Key Outcome:** Reduced enumeration time from hours to minutes, allowing pentesters to focus on exploitation." },
    ],
    labs: [
        { id: 101, title: "Buffer Overflow Exploitation (Stack)", type: "lab", summary: "Step-by-step walkthrough of a classic stack buffer overflow on a 32-bit Linux binary to achieve remote code execution (RCE).", category: "Pwn", writeup: "### Lab Writeup: Stack Buffer Overflow\n\n**Target:** 32-bit ELF binary, vulnerable to input exceeding the buffer size.\n\n**Steps:**\n1.  Fuzzing to determine offset (132 bytes).\n2.  Identifying the EIP (Extended Instruction Pointer) overwrite location.\n3.  Locating a JMP ESP instruction or using ROP gadgets.\n4.  Crafting the final payload using a non-standard null-byte free shellcode.\n\n**Result:** Successfully overwrote the return address to execute shellcode and gain a reverse shell." },
        { id: 102, title: "Cross-Site Scripting (XSS) via Stored Payload", type: "lab", summary: "Detailed guide on exploiting a vulnerable web application using a stored XSS payload and bypassing input sanitization techniques.", category: "Web App", writeup: "### Lab Writeup: Stored XSS Bypass\n\n**Target:** Blog application comment section with flawed `strip_tags` sanitization.\n\n**Bypass Technique:** Used polyglot payloads (`<svg/onload=alert(1)>`) that were overlooked by the filter, successfully injecting persistent JavaScript code into the database.\n\n**Risk:** Demonstrated cookie stealing and session hijacking capability." },
    ],
};

// --- Component Helper: Iconography (Inline SVGs) ---
const Icon = ({ name, className }) => {
    switch (name) {
        case 'Menu': return (<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>);
        case 'X': return (<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>);
        case 'Sun': return (<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2"></path><path d="M12 20v2"></path><path d="M5.42 5.42l1.43 1.43"></path><path d="M17.15 17.15l1.43 1.43"></path><path d="M2 12h2"></path><path d="M20 12h2"></path><path d="M5.42 18.58l1.43-1.43"></path><path d="M17.15 6.85l1.43-1.43"></path></svg>);
        case 'Moon': return (<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"></path></svg>);
        case 'Download': return (<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>);
        case 'ArrowLeft': return (<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>);
        case 'Globe': return (<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>);
        case 'Shield': return (<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>);
        case 'Briefcase': return (<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>);
        case 'GraduationCap': return (<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><path d="M21.42 10.97a7.2 7.2 0 0 0-11.75-2.09"></path><path d="M18.84 15.63A7.2 7.2 0 0 0 7.07 19.33"></path><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><path d="M12 3L2 8l10 5 10-5-10-5z"></path></svg>);
        default: return null;
    }
};

// --- Component: Header and Navigation ---
const Header = ({ setView, toggleTheme, isDarkMode, personalData }) => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const navItems = ['Home', 'Resume', 'Projects', 'Labs', 'Contact'];

    const handleNavClick = (view) => {
        setView(view.toLowerCase());
        setIsMenuOpen(false);
    };

    return (
        <header className="fixed top-0 left-0 w-full z-50 bg-white/95 dark:bg-gray-900/95 shadow-lg dark:shadow-gray-800 backdrop-blur-sm transition-colors duration-300" aria-label="Main Navigation">
            <div className="container mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center h-16">
                {/* Logo / Name */}
                <button
                    className="flex items-center space-x-2 text-xl font-bold text-gray-900 dark:text-gray-50 tracking-wider hover:text-indigo-600 dark:hover:text-cyan-400 transition-colors"
                    onClick={() => setView('home')}
                    aria-label="Go to Home"
                >
                    <Icon name="Shield" className="w-6 h-6 text-indigo-600 dark:text-cyan-400" />
                    <span>{personalData.name.split("'")[0]}</span>
                </button>

                {/* Desktop Navigation */}
                <nav className="hidden md:flex space-x-6" aria-label="Desktop Menu">
                    {navItems.map(item => (
                        <a
                            key={item}
                            href={`#${item.toLowerCase()}`}
                            onClick={(e) => { e.preventDefault(); handleNavClick(item); }}
                            className="text-gray-600 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-cyan-400 font-medium transition-colors relative group focus:outline-none focus:ring-2 focus:ring-indigo-500 rounded-md"
                            aria-current={item.toLowerCase() === 'home' ? 'page' : undefined}
                        >
                            {item}
                            <span className="absolute left-0 bottom-0 w-full h-0.5 bg-indigo-600 dark:bg-cyan-400 scale-x-0 group-hover:scale-x-100 transition-transform duration-300"></span>
                        </a>
                    ))}
                </nav>

                {/* Controls: Download & Theme Toggle */}
                <div className="flex items-center space-x-4">
                    <button
                        className="hidden sm:flex items-center px-3 py-1.5 text-sm font-semibold rounded-full bg-indigo-600 text-white shadow-md hover:bg-indigo-700 dark:bg-cyan-600 dark:hover:bg-cyan-700 transition-colors focus:outline-none focus:ring-4 focus:ring-indigo-300 dark:focus:ring-cyan-500/50"
                        onClick={() => alert("Resume Download functionality would be implemented here.")}
                        aria-label="Download Resume (PDF)"
                    >
                        <Icon name="Download" className="w-4 h-4 mr-2" />
                        Download CV
                    </button>

                    <button
                        onClick={toggleTheme}
                        className="p-2 rounded-full text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-400"
                        aria-label={isDarkMode ? "Switch to Light Mode" : "Switch to Dark Mode"}
                    >
                        <Icon name={isDarkMode ? 'Sun' : 'Moon'} className="w-6 h-6" />
                    </button>

                    {/* Mobile Menu Button */}
                    <button
                        className="md:hidden p-2 rounded-full text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:focus:ring-cyan-400"
                        onClick={() => setIsMenuOpen(!isMenuOpen)}
                        aria-expanded={isMenuOpen}
                        aria-controls="mobile-menu"
                        aria-label="Toggle Navigation Menu"
                    >
                        <Icon name={isMenuOpen ? 'X' : 'Menu'} className="w-6 h-6" />
                    </button>
                </div>
            </div>

            {/* Mobile Menu Content */}
            {isMenuOpen && (
                <nav id="mobile-menu" className="md:hidden bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-700">
                    <div className="px-2 pt-2 pb-3 space-y-1">
                        {navItems.map(item => (
                            <button
                                key={`mobile-${item}`}
                                onClick={() => handleNavClick(item)}
                                className="block w-full text-left px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-indigo-50 dark:hover:bg-gray-800 hover:text-indigo-600 dark:hover:text-cyan-400 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500"
                            >
                                {item}
                            </button>
                        ))}
                        <button
                            className="w-full flex justify-center items-center px-3 py-2 text-sm font-semibold rounded-lg bg-indigo-600 text-white shadow-md hover:bg-indigo-700 dark:bg-cyan-600 dark:hover:bg-cyan-700 transition-colors focus:outline-none focus:ring-4 focus:ring-indigo-300 dark:focus:ring-cyan-500/50 mt-2"
                            onClick={() => alert("Resume Download functionality would be implemented here.")}
                        >
                            <Icon name="Download" className="w-4 h-4 mr-2" />
                            Download CV
                        </button>
                    </div>
                </nav>
            )}
        </header>
    );
};

// --- Component: Hero Section (Home) ---
const Hero = ({ personalData, setView }) => (
    <section id="home" className="pt-24 min-h-screen flex items-center bg-gray-50 dark:bg-gray-900 transition-colors duration-300">
        <div className="container mx-auto px-4 py-16 sm:py-24 lg:py-32">
            <div className="max-w-4xl flex flex-col md:flex-row items-center md:items-start space-y-8 md:space-y-0 md:space-x-12">
                {/* Profile Text Content */}
                <div>
                    <p className="text-xl text-indigo-600 dark:text-cyan-400 font-semibold mb-2">Hello, my name is</p>
                    <h1 className="text-5xl sm:text-7xl font-extrabold text-gray-900 dark:text-white leading-tight">
                        {personalData.name}
                    </h1>
                    <h2 className="text-2xl sm:text-4xl font-light text-gray-700 dark:text-gray-300 mt-2 mb-6">
                        {personalData.title}
                    </h2>
                    <p className="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mb-8 leading-relaxed">
                        {personalData.bio}
                    </p>

                    <div className="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-6">
                        <button
                            onClick={() => setView('projects')}
                            className="px-8 py-3 text-lg font-semibold rounded-lg shadow-xl bg-indigo-600 text-white hover:bg-indigo-700 dark:bg-cyan-600 dark:hover:bg-cyan-700 transition-all duration-300 transform hover:-translate-y-0.5 focus:outline-none focus:ring-4 focus:ring-indigo-300 dark:focus:ring-cyan-500/50"
                        >
                            View Projects
                        </button>
                        <button
                            onClick={() => setView('contact')}
                            className="px-8 py-3 text-lg font-semibold rounded-lg border-2 border-indigo-600 dark:border-cyan-400 text-indigo-600 dark:text-cyan-400 hover:bg-indigo-50 dark:hover:bg-gray-800 transition-all duration-300 focus:outline-none focus:ring-4 focus:ring-indigo-300 dark:focus:ring-cyan-500/50"
                        >
                            Get In Touch
                        </button>
                    </div>
                </div>

                {/* Profile Image */}
                <div className="shrink-0 order-first md:order-last">
                    <img
                        src={personalData.photoUrl}
                        alt={`Portrait of ${personalData.name}`}
                        className="w-48 h-48 sm:w-64 sm:h-64 object-cover rounded-full shadow-2xl border-4 border-indigo-300 dark:border-cyan-600 transform hover:scale-105 transition-transform duration-500 ease-in-out"
                        onError={(e) => {
                            e.target.onerror = null; // Prevents infinite loop
                            e.target.src = "https://placehold.co/150x150/1d4ed8/ffffff?text=Photo+Error"; // Fallback text
                        }}
                    />
                </div>
            </div>
        </div>
    </section>
);

// --- Component: Resume Section ---
const ResumeSection = ({ resumeData }) => (
    <section id="resume" className="py-16 bg-white dark:bg-gray-900 transition-colors duration-300 min-h-screen">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <h2 className="text-4xl font-extrabold text-gray-900 dark:text-white mb-12 border-b-4 border-indigo-600 dark:border-cyan-400 inline-block pb-1">
                Professional Resume
            </h2>

            <div className="grid md:grid-cols-2 gap-12">
                {/* Experience Column */}
                <div>
                    <h3 className="text-3xl font-semibold text-gray-800 dark:text-gray-200 mb-6 flex items-center space-x-2">
                        <Icon name="Briefcase" className="w-7 h-7 text-indigo-600 dark:text-cyan-400" />
                        <span>Experience</span>
                    </h3>
                    <div className="space-y-8">
                        {resumeData.filter(item => item.type === 'experience').map((job, index) => (
                            <div key={index} className="relative pl-6 border-l-4 border-indigo-200 dark:border-cyan-700">
                                <div className="absolute w-4 h-4 bg-indigo-600 dark:bg-cyan-400 rounded-full -left-2 top-0 transform -translate-x-1/2"></div>
                                <p className="text-sm font-light text-gray-500 dark:text-gray-400">{job.years}</p>
                                <h4 className="text-xl font-bold text-gray-900 dark:text-white mt-1">{job.title}</h4>
                                <p className="text-lg font-medium text-indigo-600 dark:text-cyan-400 mb-2">{job.company}</p>
                                <ul className="list-disc ml-5 space-y-1 text-gray-700 dark:text-gray-300">
                                    {job.details.map((detail, dIndex) => (
                                        <li key={dIndex}>{detail}</li>
                                    ))}
                                </ul>
                            </div>
                        ))}
                    </div>
                </div>

                {/* Education/Certifications Column */}
                <div>
                    <h3 className="text-3xl font-semibold text-gray-800 dark:text-gray-200 mb-6 flex items-center space-x-2">
                        <Icon name="GraduationCap" className="w-7 h-7 text-indigo-600 dark:text-cyan-400" />
                        <span>Education & Certifications</span>
                    </h3>
                    <div className="space-y-8">
                        {resumeData.filter(item => item.type === 'education').map((edu, index) => (
                            <div key={index} className="relative pl-6 border-l-4 border-indigo-200 dark:border-cyan-700">
                                <div className="absolute w-4 h-4 bg-indigo-600 dark:bg-cyan-400 rounded-full -left-2 top-0 transform -translate-x-1/2"></div>
                                <p className="text-sm font-light text-gray-500 dark:text-gray-400">{edu.years}</p>
                                <h4 className="text-xl font-bold text-gray-900 dark:text-white mt-1">{edu.title}</h4>
                                <p className="text-lg font-medium text-indigo-600 dark:text-cyan-400 mb-2">{edu.institution}</p>
                                <ul className="list-disc ml-5 space-y-1 text-gray-700 dark:text-gray-300">
                                    {edu.details.map((detail, dIndex) => (
                                        <li key={dIndex}>{detail}</li>
                                    ))}
                                </ul>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    </section>
);

// --- Component: Project Card ---
const ProjectCard = ({ project, setView, setSelectedItem }) => (
    <div className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-lg hover:shadow-2xl dark:hover:shadow-gray-700/50 transition-all duration-300 border border-gray-100 dark:border-gray-700 group flex flex-col justify-between">
        <div>
            <h4 className="text-2xl font-bold text-gray-900 dark:text-white mb-2 group-hover:text-indigo-600 dark:group-hover:text-cyan-400 transition-colors">{project.title}</h4>
            <p className="text-gray-600 dark:text-gray-400 mb-4">{project.summary}</p>
            <div className="flex flex-wrap gap-2 mb-4">
                {/* FIXED: Added optional chaining (?) here to prevent 'map' undefined error when 'tech' is missing (as in labs) */}
                {project.tech?.map(t => (
                    <span key={t} className="px-3 py-1 text-xs font-medium bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-full">
                        {t}
                    </span>
                ))}
                {/* Show Category for Lab Challenges */}
                {project.category && (
                    <span className="px-3 py-1 text-xs font-medium bg-indigo-100 dark:bg-cyan-900 text-indigo-700 dark:text-cyan-300 rounded-full">
                        Category: {project.category}
                    </span>
                )}
            </div>
        </div>
        <button
            onClick={() => { setView(project.type === 'project' ? 'project_detail' : 'lab_detail'); setSelectedItem(project); }}
            className="mt-4 w-full py-2 font-semibold text-indigo-600 dark:text-cyan-400 border border-indigo-600 dark:border-cyan-400 rounded-lg hover:bg-indigo-600 hover:text-white dark:hover:bg-cyan-600 dark:hover:text-white transition-all focus:outline-none focus:ring-4 focus:ring-indigo-300 dark:focus:ring-cyan-500/50"
        >
            View Writeup
        </button>
    </div>
);

// --- Component: Projects/Labs Grid (Shared Component) ---
const ContentGrid = ({ title, data, setView, setSelectedItem }) => (
    <section id={title.toLowerCase().replace(' ', '_')} className="py-16 bg-gray-50 dark:bg-gray-900 transition-colors duration-300 min-h-screen">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <h2 className="text-4xl font-extrabold text-gray-900 dark:text-white mb-12 border-b-4 border-indigo-600 dark:border-cyan-400 inline-block pb-1">
                {title}
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {data.map(item => (
                    <ProjectCard key={item.id} project={item} setView={setView} setSelectedItem={setSelectedItem} />
                ))}
            </div>
        </div>
    </section>
);

// --- Component: Detail View (For Projects and Labs) ---
const DetailView = ({ item, setView, isDarkMode }) => {
    if (!item) {
        // Fallback if accessed directly without an item
        return (
            <div className="py-16 pt-24 min-h-screen flex flex-col justify-center items-center bg-white dark:bg-gray-900">
                <p className="text-gray-600 dark:text-gray-400 text-xl">Item not found.</p>
                <button
                    onClick={() => setView('projects')}
                    className="mt-4 px-6 py-2 font-semibold rounded-lg bg-indigo-600 text-white hover:bg-indigo-700 transition-colors"
                >
                    Go back
                </button>
            </div>
        );
    }

    // FIXED: Refactored markdown rendering to prevent invalid HTML structure (like p inside h3)
    // which caused the "Objects are not valid as a React child" error.
    const renderMarkdown = (text) => {
        let html = text;
        // 1. Headings (H3)
        html = html.replace(/### (.*)\n/g, '<h3 class="text-2xl font-bold text-gray-900 dark:text-white mt-8 mb-3">$1</h3>');
        // 2. Bold text
        html = html.replace(/\*\*([^*]+)\*\*/g, '<strong class="font-semibold text-indigo-600 dark:text-cyan-400">$1</strong>');
        // 3. Convert double newlines to styled div separators (acts as paragraphs)
        html = html.replace(/\n\n/g, '</div><div class="mb-4 text-gray-700 dark:text-gray-300 leading-relaxed">');
        // 4. Convert single newlines to line breaks
        html = html.replace(/\n/g, '<br/>');

        // Wrap the whole content in a styled div container for the base paragraph style
        html = `<div class="text-gray-700 dark:text-gray-300 leading-relaxed">${html}</div>`;

        return { __html: html };
    };

    return (
        <section className="py-16 pt-24 min-h-screen bg-white dark:bg-gray-900 transition-colors duration-300">
            <div className="container mx-auto px-4 sm:px-6 lg:px-8 max-w-4xl">
                <button
                    onClick={() => setView(item.type === 'project' ? 'projects' : 'labs')}
                    className="flex items-center text-indigo-600 dark:text-cyan-400 hover:text-indigo-700 dark:hover:text-cyan-500 transition-colors font-medium mb-8 focus:outline-none focus:ring-2 focus:ring-indigo-500 rounded-md"
                    aria-label="Back to List"
                >
                    <Icon name="ArrowLeft" className="w-5 h-5 mr-2" />
                    Back to {item.type === 'project' ? 'Projects' : 'Lab Challenges'}
                </button>

                <div className="p-8 rounded-xl shadow-2xl bg-gray-50 dark:bg-gray-800 border border-indigo-100 dark:border-cyan-900">
                    <span className="text-sm font-semibold uppercase tracking-wider px-3 py-1 rounded-full bg-indigo-100 text-indigo-700 dark:bg-cyan-900 dark:text-cyan-300">
                        {item.type === 'project' ? 'Project Writeup' : 'CTF/Lab Challenge'}
                    </span>
                    <h1 className="text-4xl font-extrabold text-gray-900 dark:text-white mt-4 mb-4">
                        {item.title}
                    </h1>
                    <p className="text-xl text-gray-600 dark:text-gray-400 italic mb-6">{item.summary}</p>

                    <div className="flex flex-wrap gap-3 mb-8">
                        {item.tech && item.tech.map(t => (
                            <span key={t} className="px-3 py-1 text-sm font-medium bg-indigo-50 dark:bg-cyan-900 text-indigo-700 dark:text-cyan-300 rounded-full">
                                {t}
                            </span>
                        ))}
                         {item.category && (
                            <span className="px-3 py-1 text-sm font-medium bg-indigo-50 dark:bg-cyan-900 text-indigo-700 dark:text-cyan-300 rounded-full">
                                Category: {item.category}
                            </span>
                        )}
                    </div>

                    <div className="writeup-content pt-4" dangerouslySetInnerHTML={renderMarkdown(item.writeup)}>
                        {/* Content rendered from markdown goes here */}
                    </div>
                </div>
            </div>
        </section>
    );
};

// --- Component: Contact Form ---
const ContactForm = ({ personalData }) => {
    const handleSubmit = (e) => {
        e.preventDefault();
        const form = e.target;
        // In a real app, this would send data to a serverless function (e.g., Firebase Cloud Function)
        alert(`Form submitted! In a real application, this data would be sent to a backend service. \n\nName: ${form.name.value}\nEmail: ${form.email.value}\nMessage: ${form.message.value}`);
        form.reset();
    };

    return (
        <section id="contact" className="py-16 bg-white dark:bg-gray-900 transition-colors duration-300 min-h-screen flex items-center">
            <div className="container mx-auto px-4 sm:px-6 lg:px-8 max-w-4xl">
                <h2 className="text-4xl font-extrabold text-gray-900 dark:text-white mb-12 border-b-4 border-indigo-600 dark:border-cyan-400 inline-block pb-1">
                    Get In Touch
                </h2>

                <div className="grid md:grid-cols-2 gap-12">
                    <div>
                        <p className="text-lg text-gray-600 dark:text-gray-400 mb-6">
                            I am currently open to collaboration and new opportunities in penetration testing and security architecture. Feel free to connect via LinkedIn or send a direct message below.
                        </p>

                        <div className="space-y-4">
                            <div className="flex items-center space-x-3">
                                <Icon name="Sun" className="w-6 h-6 text-indigo-600 dark:text-cyan-400" />
                                <a href={`mailto:${personalData.email}`} className="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-cyan-400 transition-colors">{personalData.email}</a>
                            </div>
                            <div className="flex items-center space-x-3">
                                <Icon name="Globe" className="w-6 h-6 text-indigo-600 dark:text-cyan-400" />
                                <a href={personalData.linkedin} target="_blank" rel="noopener noreferrer" className="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-cyan-400 transition-colors">LinkedIn Profile</a>
                            </div>
                            <div className="flex items-center space-x-3">
                                <Icon name="Globe" className="w-6 h-6 text-indigo-600 dark:text-cyan-400" />
                                <a href={personalData.github} target="_blank" rel="noopener noreferrer" className="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-cyan-400 transition-colors">GitHub Repositories</a>
                            </div>
                        </div>
                    </div>

                    {/* Contact Form */}
                    <form onSubmit={handleSubmit} className="p-6 bg-gray-50 dark:bg-gray-800 rounded-xl shadow-lg border border-gray-200 dark:border-gray-700 space-y-4" aria-label="Contact Form">
                        <div>
                            <label htmlFor="name" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Name</label>
                            <input type="text" id="name" name="name" required className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-indigo-500 focus:border-indigo-500 dark:focus:ring-cyan-400 dark:focus:border-cyan-400" />
                        </div>
                        <div>
                            <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Email</label>
                            <input type="email" id="email" name="email" required className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-indigo-500 focus:border-indigo-500 dark:focus:ring-cyan-400 dark:focus:border-cyan-400" />
                        </div>
                        <div>
                            <label htmlFor="message" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Message</label>
                            <textarea id="message" name="message" rows="4" required className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-indigo-500 focus:border-indigo-500 dark:focus:ring-cyan-400 dark:focus:border-cyan-400"></textarea>
                        </div>
                        <button type="submit" className="w-full py-2.5 font-semibold rounded-lg bg-indigo-600 text-white hover:bg-indigo-700 dark:bg-cyan-600 dark:hover:bg-cyan-700 transition-colors focus:outline-none focus:ring-4 focus:ring-indigo-300 dark:focus:ring-cyan-500/50">
                            Send Message
                        </button>
                    </form>
                </div>
            </div>
        </section>
    );
};

// --- Component: Footer ---
const Footer = ({ personalData }) => (
    <footer className="bg-gray-800 dark:bg-gray-950 py-6">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 text-center text-gray-400 dark:text-gray-500 text-sm">
            <p>&copy; {new Date().getFullYear()} {personalData.name.split("'")[0]} Khan. All rights reserved.</p>
            <p className="mt-1">Built with React & Tailwind CSS.</p>
        </div>
    </footer>
);


// --- Main App Component ---
export default function App() {
    // State for client-side routing and selected detail item
    const [view, setView] = useState('home'); // 'home', 'resume', 'projects', 'labs', 'contact', 'project_detail', 'lab_detail'
    const [selectedItem, setSelectedItem] = useState(null);

    // State for dark mode
    const [isDarkMode, setIsDarkMode] = useState(() => {
        // Initialize state from localStorage or default to user preference
        const storedTheme = localStorage.getItem('theme');
        if (storedTheme) {
            return storedTheme === 'dark';
        }
        return window.matchMedia('(prefers-color-scheme: dark)').matches;
    });

    // Theme persistence effect
    useEffect(() => {
        const root = window.document.documentElement;
        if (isDarkMode) {
            root.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        } else {
            root.classList.remove('dark');
            localStorage.setItem('theme', 'light');
        }
    }, [isDarkMode]);

    const toggleTheme = () => setIsDarkMode(prev => !prev);

    // Central rendering logic (Router substitute)
    const renderContent = () => {
        switch (view) {
            case 'resume':
                return <ResumeSection resumeData={PORTFOLIO_DATA.resume} />;
            case 'projects':
                return <ContentGrid title="Security Projects" data={PORTFOLIO_DATA.projects} setView={setView} setSelectedItem={setSelectedItem} />;
            case 'labs':
                return <ContentGrid title="CTF/Lab Challenges" data={PORTFOLIO_DATA.labs} setView={setView} setSelectedItem={setSelectedItem} />;
            case 'contact':
                return <ContactForm personalData={PORTFOLIO_DATA.personal} />;
            case 'project_detail':
            case 'lab_detail':
                return <DetailView item={selectedItem} setView={setView} isDarkMode={isDarkMode} />;
            case 'home':
            default:
                return <Hero personalData={PORTFOLIO_DATA.personal} setView={setView} />;
        }
    };

    return (
        <div className="min-h-screen font-sans antialiased text-gray-900 dark:text-gray-50 transition-colors duration-300" style={{ fontFamily: 'Inter, sans-serif' }}>
            {/* Tailwind uses 'dark:' prefix, so the class must be on the root element (handled in useEffect) */}

            <style>
                {/* Fallback for Inter font, and basic global styles */}
                {`
                    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');
                    html { scroll-behavior: smooth; }
                    /* General styling for markdown content in DetailView */
                    .writeup-content h3 {
                        margin-bottom: 0.75rem;
                        margin-top: 2rem;
                    }
                `}
            </style>

            <Header
                setView={setView}
                toggleTheme={toggleTheme}
                isDarkMode={isDarkMode}
                personalData={PORTFOLIO_DATA.personal}
            />

            <main className="pt-16">
                {renderContent()}
            </main>

            <Footer personalData={PORTFOLIO_DATA.personal} />
        </div>
    );
}