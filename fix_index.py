import os
import re

def fix_index():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\index.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Mini Projects section
    old_mini_projects = """                <div class="w-12 h-12 rounded-2xl flex items-center justify-center mb-6 text-white" style="background-color: {{ project.card_color }};">
                    <i class="ph ph-folder text-2xl"></i>
                </div>
                
                <h3 class="text-2xl font-bold mb-3">{{ project.title }}</h3>
                <p class="text-[var(--color-text-secondary)] mb-6 line-clamp-3">{{ project.description }}</p>
                
                <div class="flex flex-wrap gap-2 mb-8">
                    {% for tech in project.technologies %}
                        <span class="text-xs font-semibold px-3 py-1 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300">
                            {{ tech.name }}
                        </span>
                    {% endfor %}
                </div>
                
                <div class="flex items-center gap-4 mt-auto">
                    {% if project.github_url %}
                    <a href="{{ project.github_url }}" target="_blank" class="text-gray-400 hover:text-black dark:hover:text-white transition-colors">
                        <i class="ph ph-github-logo text-2xl"></i>
                    </a>
                    {% endif %}
                    {% if project.live_url %}
                    <a href="{{ project.live_url }}" target="_blank" class="text-gray-400 hover:text-[var(--color-accent)] transition-colors">
                        <i class="ph ph-arrow-up-right text-2xl"></i>
                    </a>
                    {% endif %}
                </div>"""

    new_mini_projects = """                <div class="flex justify-between items-start mb-6">
                    <h3 class="text-2xl font-display font-bold">{{ project.title }}</h3>
                    {% if project.live_url %}
                    <a href="{{ project.live_url }}" target="_blank" class="flex items-center gap-2 text-sm font-semibold tracking-wider uppercase text-[var(--color-accent)] hover:text-black dark:hover:text-white transition-colors">
                        <span>Open</span>
                        <i class="ph ph-arrow-up-right"></i>
                    </a>
                    {% endif %}
                </div>
                
                <p class="text-[var(--color-text-secondary)] mb-6 line-clamp-3 flex-grow">{{ project.description }}</p>
                
                <div class="flex flex-wrap gap-2 mb-6">
                    {% for tech in project.technologies %}
                        <span class="text-xs font-semibold px-3 py-1 rounded-full bg-black/5 dark:bg-white/10 text-gray-700 dark:text-gray-300 border border-gray-200 dark:border-gray-700">
                            {{ tech.name }}
                        </span>
                    {% endfor %}
                </div>
                
                {% if project.github_url %}
                <div class="pt-4 border-t border-gray-100 dark:border-gray-800 mt-auto">
                    <a href="{{ project.github_url }}" target="_blank" class="text-gray-400 hover:text-black dark:hover:text-white transition-colors flex items-center gap-2 text-sm">
                        <i class="ph ph-github-logo text-lg"></i>
                        <span>Source Code</span>
                    </a>
                </div>
                {% endif %}"""

    if "ph-folder" in content:
        content = content.replace(old_mini_projects, new_mini_projects)
        # Also fix the card border/hover slightly to look more premium
        content = content.replace(
            "class=\"group glass dark:glass rounded-3xl p-8 hover:-translate-y-2 transition-all duration-300 reveal-up border border-gray-200 dark:border-gray-800 hover:border-[var(--color-accent)] dark:hover:border-[var(--color-accent)]\"",
            "class=\"group glass dark:glass rounded-3xl p-8 flex flex-col hover:-translate-y-2 transition-all duration-300 reveal-up border border-white/40 dark:border-white/10 hover:border-[var(--color-accent)] dark:hover:border-[var(--color-accent)] hover:shadow-2xl hover:shadow-[var(--color-accent)]/20\""
        )

    # 2. Update Experience & Education to include Internships and Certifications
    old_exp_edu = """<!-- EXPERIENCE & EDUCATION -->
<section id="experience" class="py-24 bg-gray-100 dark:bg-[#0c0c11]">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-20">
        
        <!-- Experience -->
        <div>
            <h2 class="text-3xl md:text-4xl font-bold mb-12 reveal-up">Work Experience</h2>
            <div class="relative pl-8 md:pl-12">
                <div class="timeline-line"></div>
                
                {% for exp in experience %}
                <div class="relative mb-12 reveal-up" style="transition-delay: 0.{{ forloop.counter }}s;">
                    <div class="timeline-dot"></div>
                    <div class="text-sm font-bold text-[var(--color-accent)] mb-1 tracking-wider uppercase">
                        {{ exp.start_date }} – {{ exp.end_date }}
                    </div>
                    <h3 class="text-xl md:text-2xl font-bold mb-1">{{ exp.role }}</h3>
                    <div class="text-gray-600 dark:text-gray-400 font-medium mb-4">
                        {% if exp.company_url %}
                            <a href="{{ exp.company_url }}" target="_blank" class="hover:text-[var(--color-accent)] underline decoration-dotted underline-offset-4">{{ exp.company }}</a>
                        {% else %}
                            {{ exp.company }}
                        {% endif %}
                    </div>
                    
                    {% if exp.technologies %}
                    <div class="text-sm text-gray-500 mb-4 font-mono bg-white dark:bg-[#15151a] px-3 py-1.5 rounded-lg inline-block border border-gray-200 dark:border-gray-800">
                        {{ exp.technologies }}
                    </div>
                    {% endif %}
                    
                    <p class="text-[var(--color-text-secondary)] mb-4">{{ exp.description }}</p>
                    
                    {% if exp.bullets %}
                    <ul class="space-y-2 text-[var(--color-text-secondary)]">
                        {% for bullet in exp.bullets %}
                        <li class="flex items-start gap-2">
                            <i class="ph-fill ph-caret-right text-[var(--color-accent)] mt-1 text-sm"></i>
                            <span>{{ bullet }}</span>
                        </li>
                        {% endfor %}
                    </ul>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        </div>
        
        <!-- Education -->
        <div>
            <h2 class="text-3xl md:text-4xl font-bold mb-12 reveal-up">Education</h2>
            <div class="relative pl-8 md:pl-12">
                <div class="timeline-line"></div>
                
                {% for edu in education %}
                <div class="relative mb-12 reveal-up" style="transition-delay: 0.{{ forloop.counter }}s;">
                    <div class="timeline-dot"></div>
                    <div class="text-sm font-bold text-[var(--color-accent)] mb-1 tracking-wider uppercase">
                        {{ edu.start_date }} – {{ edu.end_date }}
                    </div>
                    <h3 class="text-xl md:text-2xl font-bold mb-1">{{ edu.degree }}</h3>
                    <div class="text-gray-600 dark:text-gray-400 font-medium mb-3">
                        {{ edu.institution }}
                    </div>
                    
                    {% if edu.grade %}
                    <div class="inline-flex items-center gap-2 bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400 px-3 py-1 rounded-full text-sm font-semibold mb-3">
                        <i class="ph-fill ph-check-circle"></i>
                        {{ edu.grade_label }}: {{ edu.grade }}
                    </div>
                    {% endif %}
                    
                    <p class="text-[var(--color-text-secondary)]">{{ edu.description }}</p>
                </div>
                {% endfor %}
            </div>
        </div>
        
    </div>
</section>"""

    new_exp_edu = """<!-- EXPERIENCE & CREDENTIALS -->
<section id="experience" class="py-24 bg-gray-100 dark:bg-[#0c0c11]">
    <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-20">
        
        <!-- Work & Internships -->
        <div>
            {% if experience %}
            <h2 class="text-3xl md:text-4xl font-bold mb-12 reveal-up">Work Experience</h2>
            <div class="relative pl-8 md:pl-12 mb-16">
                <div class="timeline-line"></div>
                
                {% for exp in experience %}
                <div class="relative mb-12 reveal-up" style="transition-delay: 0.{{ forloop.counter }}s;">
                    <div class="timeline-dot"></div>
                    <div class="text-sm font-bold text-[var(--color-accent)] mb-1 tracking-wider uppercase">
                        {{ exp.start_date }} – {{ exp.end_date }}
                    </div>
                    <h3 class="text-xl md:text-2xl font-bold mb-1">{{ exp.role }}</h3>
                    <div class="text-gray-600 dark:text-gray-400 font-medium mb-4">
                        {% if exp.company_url %}
                            <a href="{{ exp.company_url }}" target="_blank" class="hover:text-[var(--color-accent)] underline decoration-dotted underline-offset-4">{{ exp.company }}</a>
                        {% else %}
                            {{ exp.company }}
                        {% endif %}
                    </div>
                    
                    {% if exp.technologies %}
                    <div class="text-sm text-gray-500 mb-4 font-mono bg-white dark:bg-[#15151a] px-3 py-1.5 rounded-lg inline-block border border-gray-200 dark:border-gray-800">
                        {{ exp.technologies }}
                    </div>
                    {% endif %}
                    
                    <p class="text-[var(--color-text-secondary)] mb-4">{{ exp.description }}</p>
                    
                    {% if exp.bullets %}
                    <ul class="space-y-2 text-[var(--color-text-secondary)] mb-4">
                        {% for bullet in exp.bullets %}
                        <li class="flex items-start gap-2">
                            <i class="ph-fill ph-caret-right text-[var(--color-accent)] mt-1 text-sm"></i>
                            <span>{{ bullet }}</span>
                        </li>
                        {% endfor %}
                    </ul>
                    {% endif %}

                    {% if exp.certificate_file %}
                    <a href="{{ exp.certificate_file.url }}" target="_blank" class="inline-flex items-center gap-2 text-sm font-semibold tracking-wider uppercase border border-[var(--color-accent)] text-[var(--color-accent)] px-4 py-2 rounded-full hover:bg-[var(--color-accent)] hover:text-black transition-colors">
                        <i class="ph ph-file-pdf"></i>
                        <span>View Document</span>
                    </a>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
            {% endif %}

            {% if internships %}
            <h2 class="text-3xl md:text-4xl font-bold mb-12 reveal-up">Internships</h2>
            <div class="relative pl-8 md:pl-12">
                <div class="timeline-line"></div>
                
                {% for exp in internships %}
                <div class="relative mb-12 reveal-up" style="transition-delay: 0.{{ forloop.counter }}s;">
                    <div class="timeline-dot" style="border-color: #6366f1;"></div>
                    <div class="text-sm font-bold text-[#6366f1] mb-1 tracking-wider uppercase">
                        {{ exp.start_date }} – {{ exp.end_date }}
                    </div>
                    <h3 class="text-xl md:text-2xl font-bold mb-1">{{ exp.role }}</h3>
                    <div class="text-gray-600 dark:text-gray-400 font-medium mb-4">
                        {% if exp.company_url %}
                            <a href="{{ exp.company_url }}" target="_blank" class="hover:text-[var(--color-accent)] underline decoration-dotted underline-offset-4">{{ exp.company }}</a>
                        {% else %}
                            {{ exp.company }}
                        {% endif %}
                    </div>
                    
                    <p class="text-[var(--color-text-secondary)] mb-4">{{ exp.description }}</p>
                    
                    {% if exp.certificate_file %}
                    <a href="{{ exp.certificate_file.url }}" target="_blank" class="inline-flex items-center gap-2 text-sm font-semibold tracking-wider uppercase border border-[#6366f1] text-[#6366f1] px-4 py-2 rounded-full hover:bg-[#6366f1] hover:text-white transition-colors">
                        <i class="ph ph-file-pdf"></i>
                        <span>View Certificate</span>
                    </a>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
            {% endif %}
        </div>
        
        <!-- Education & Certifications -->
        <div>
            <h2 class="text-3xl md:text-4xl font-bold mb-12 reveal-up">Education</h2>
            <div class="relative pl-8 md:pl-12 mb-16">
                <div class="timeline-line"></div>
                
                {% for edu in education %}
                <div class="relative mb-12 reveal-up" style="transition-delay: 0.{{ forloop.counter }}s;">
                    <div class="timeline-dot"></div>
                    <div class="text-sm font-bold text-[var(--color-accent)] mb-1 tracking-wider uppercase">
                        {{ edu.start_date }} – {{ edu.end_date }}
                    </div>
                    <h3 class="text-xl md:text-2xl font-bold mb-1">{{ edu.degree }}</h3>
                    <div class="text-gray-600 dark:text-gray-400 font-medium mb-3">
                        {{ edu.institution }}
                    </div>
                    
                    {% if edu.grade %}
                    <div class="inline-flex items-center gap-2 bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400 px-3 py-1 rounded-full text-sm font-semibold mb-3">
                        <i class="ph-fill ph-check-circle"></i>
                        {{ edu.grade_label }}: {{ edu.grade }}
                    </div>
                    {% endif %}
                    
                    <p class="text-[var(--color-text-secondary)]">{{ edu.description }}</p>
                </div>
                {% endfor %}
            </div>

            {% if certifications %}
            <h2 class="text-3xl md:text-4xl font-bold mb-12 reveal-up">Certifications</h2>
            <div class="grid grid-cols-1 gap-6">
                {% for cert in certifications %}
                <div class="glass dark:glass rounded-3xl p-8 border border-white/40 dark:border-white/10 hover:border-[var(--color-accent)] transition-all reveal-up">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="w-12 h-12 rounded-full bg-[var(--color-accent)]/10 text-[var(--color-accent)] flex items-center justify-center">
                            <i class="ph ph-certificate text-2xl"></i>
                        </div>
                        <div>
                            <h3 class="text-xl font-bold">{{ cert.title }}</h3>
                            <p class="text-gray-500">{{ cert.issuer }}</p>
                        </div>
                    </div>
                    <div class="flex gap-4 mt-6">
                        {% if cert.certificate_file %}
                        <a href="{{ cert.certificate_file.url }}" target="_blank" class="flex-1 text-center py-2 rounded-lg bg-black text-white dark:bg-white dark:text-black font-semibold text-sm hover:opacity-90 transition-opacity">
                            View Document
                        </a>
                        {% endif %}
                        {% if cert.credential_url %}
                        <a href="{{ cert.credential_url }}" target="_blank" class="flex-1 text-center py-2 rounded-lg border border-gray-300 dark:border-gray-700 font-semibold text-sm hover:border-[var(--color-accent)] transition-colors">
                            Verify Credential
                        </a>
                        {% endif %}
                    </div>
                </div>
                {% endfor %}
            </div>
            {% endif %}
        </div>
        
    </div>
</section>"""

    if "<!-- EXPERIENCE & EDUCATION -->" in content:
        content = content.replace(old_exp_edu, new_exp_edu)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_index()
