import Image from 'next/image';
import { getPortfolioData } from '@/lib/data';import { ArrowDown } from "@phosphor-icons/react/dist/ssr/ArrowDown";
import { ArrowUpRight } from "@phosphor-icons/react/dist/ssr/ArrowUpRight";
import { Bank } from "@phosphor-icons/react/dist/ssr/Bank";
import { Briefcase } from "@phosphor-icons/react/dist/ssr/Briefcase";
import { CheckCircle } from "@phosphor-icons/react/dist/ssr/CheckCircle";
import { Code } from "@phosphor-icons/react/dist/ssr/Code";
import { DownloadSimple } from "@phosphor-icons/react/dist/ssr/DownloadSimple";
import { EnvelopeSimple } from "@phosphor-icons/react/dist/ssr/EnvelopeSimple";
import { GithubLogo } from "@phosphor-icons/react/dist/ssr/GithubLogo";
import { GraduationCap } from "@phosphor-icons/react/dist/ssr/GraduationCap";
import { Image as ImageIcon } from "@phosphor-icons/react/dist/ssr/Image";
import { InstagramLogo } from "@phosphor-icons/react/dist/ssr/InstagramLogo";
import { Layout } from "@phosphor-icons/react/dist/ssr/Layout";
import { LinkedinLogo } from "@phosphor-icons/react/dist/ssr/LinkedinLogo";
import { Medal } from "@phosphor-icons/react/dist/ssr/Medal";
import { SealCheck } from "@phosphor-icons/react/dist/ssr/SealCheck";
import { User } from "@phosphor-icons/react/dist/ssr/User";


function getMediaUrl(path: string) {
  if (!path) return '';
  if (path.startsWith('http')) return path;
  return `/media/${path}`;
}

export default async function Home() {
  const data = await getPortfolioData();
  const { profile, projects, miniProjects, skills, education, experience, internships, certifications } = data;

  return (
    <main className="flex-grow">
      {/* HERO SECTION */}
      <section id="hero" className="relative min-h-screen flex items-center justify-center pt-20 overflow-hidden">
        <div className="absolute inset-0 z-0 opacity-20 dark:opacity-40" style={{ backgroundImage: 'radial-gradient(circle at center, var(--color-surface-elevated) 0%, var(--color-surface) 100%)' }}></div>
        
        <div className="premium-glow top-[10%] left-[20%] dark:opacity-25"></div>
        <div className="premium-glow bottom-[10%] right-[10%] dark:opacity-20" style={{ background: 'radial-gradient(circle, #a855f7 0%, transparent 70%)' }}></div>
        
        <div className="relative z-10 max-w-7xl mx-auto px-6 w-full flex flex-col items-center text-center">
          <h1 className="text-5xl md:text-6xl lg:text-8xl font-bold tracking-tight text-shadow reveal-up active max-w-5xl leading-tight">
            {profile.tagline ? profile.tagline : (
              <>
                In a world of digital noise, <br />
                <span className="text-gradient-premium">clarity</span> is a story worth telling.
              </>
            )}
          </h1>
          <div className="mt-12 animate-bounce reveal-up active" style={{ transitionDelay: '0.4s' }}>
            <a href="#about" aria-label="Scroll down to About section" className="text-gray-600 dark:text-gray-300 hover:text-[var(--color-accent)] transition-colors">
              <ArrowDown className="text-3xl" />
            </a>
          </div>
        </div>
      </section>

      {/* ABOUT SECTION */}
      <section id="about" className="py-24 relative z-10">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div className="reveal-up active">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 bg-[var(--color-accent)]/10 rounded-full mb-6">
                <User className="text-[var(--color-accent)]" />
                <span className="text-sm text-[var(--color-accent)] font-bold tracking-wide uppercase">About Me</span>
              </div>
              <h2 className="text-4xl md:text-5xl font-bold leading-tight mb-4">
                Building the Future with <br />
                <span className="text-[var(--color-accent)]">{profile.title || "FULL STACK"} {profile.subtitle || "DEVELOPER"}</span>
              </h2>
              
              <div className="prose dark:prose-invert prose-lg max-w-none text-[var(--color-text-secondary)] mb-10 space-y-6 leading-relaxed whitespace-pre-wrap">
                {profile.bio}
              </div>
              
              <div className="flex items-center gap-6">
                {profile.resume_file && (
                  <a href={getMediaUrl(profile.resume_file)} download className="btn-circle-expand border border-gray-300 dark:border-gray-700 hover:border-transparent dark:hover:border-transparent hover:text-black hover:bg-[var(--color-accent)]">
                    <DownloadSimple className="text-xl" />
                    <span>Download Resume</span>
                  </a>
                )}
                
                <div className="flex items-center justify-center lg:justify-start gap-4">
                  {profile.github_url && (
                    <a href={profile.github_url} target="_blank" aria-label="GitHub Profile" className="p-3 rounded-full border border-gray-300 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">
                      <GithubLogo className="text-xl" />
                    </a>
                  )}
                  {profile.linkedin_url && (
                    <a href={profile.linkedin_url} target="_blank" aria-label="LinkedIn Profile" className="p-3 rounded-full border border-gray-300 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">
                      <LinkedinLogo className="text-xl" />
                    </a>
                  )}
                  {profile.instagram_url && (
                    <a href={profile.instagram_url} target="_blank" aria-label="Instagram Profile" className="p-3 rounded-full border border-gray-300 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">
                      <InstagramLogo className="text-xl" />
                    </a>
                  )}
                </div>
              </div>
            </div>
            
            <div className="reveal-up active" style={{ transitionDelay: '0.2s' }}>
              <div className="aspect-[4/5] rounded-3xl overflow-hidden bg-white/10 dark:bg-black/60 backdrop-blur-2xl p-4 rotate-3 hover:rotate-0 transition-transform duration-500">
                {profile.profile_image ? (
                  <div className="w-full h-full rounded-2xl relative">
                    <Image 
                      src={getMediaUrl(profile.profile_image)} 
                      alt={profile.full_name} 
                      fill
                      priority
                      fetchPriority="high"
                      sizes="(max-width: 768px) 100vw, 50vw"
                      className="object-cover rounded-2xl filter grayscale hover:grayscale-0 transition-transform duration-500" 
                    />
                    <div className="absolute inset-0 rounded-2xl pointer-events-none" style={{ background: `linear-gradient(to top, #050505 0%, rgba(5,5,5,0.7) calc(${profile.image_blend_amount || 45}% / 2), transparent ${profile.image_blend_amount || 45}%)` }}></div>
                  </div>
                ) : (
                  <div className="w-full h-full bg-gray-200 dark:bg-gray-800 rounded-2xl flex items-center justify-center">
                    <User className="text-6xl text-gray-600 dark:text-gray-300" />
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* SKILLS MARQUEE */}
      <section id="skills" className="py-24 overflow-hidden bg-gray-100 dark:bg-[#1a1a1a]">
        <div className="max-w-7xl mx-auto px-6 flex flex-col gap-6 reveal-up active overflow-visible">
          <div className="relative w-full overflow-x-hidden fade-edges pause-on-hover mb-4 md:mb-8 order-1">
            <div className="animate-marquee whitespace-nowrap flex items-center gap-12 py-4 px-4">
              {[...skills, ...skills, ...skills, ...skills].map((skill: any, idx) => (
                <div key={idx} className="flex items-center gap-3 text-3xl font-bold text-gray-600 dark:text-gray-300 hover:text-black dark:hover:text-white transition-colors cursor-default">
                  {skill.icon_svg ? (
                    <div className="w-10 h-10" dangerouslySetInnerHTML={{ __html: skill.icon_svg }}></div>
                  ) : (
                    <Code className="text-4xl text-[var(--color-accent)]" />
                  )}
                  {skill.name}
                </div>
              ))}
            </div>
          </div>
          
          <div className="flex items-center gap-4 pl-2 md:pl-8 mt-4 md:mt-8 order-2">
            <h3 className="shrink-0 text-3xl md:text-5xl font-bold tracking-tight text-gray-800 dark:text-gray-200">
              My Dev Stack
            </h3>
            <div className="shrink-0 w-20 h-20 md:w-28 md:h-28 text-gray-700 dark:text-gray-400 dark:text-gray-600 dark:text-gray-300 transform -translate-y-4 md:-translate-y-8 flex items-center justify-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 154 141" className="w-full h-full">
                <path fill="currentColor" d="m2.956 132.708-1.373-.603-1.206 2.747 1.374.603.603-1.374zM141.561.364a1.5 1.5 0 0 0-2.068.475l-7.163 11.443a1.5 1.5 0 1 0 2.543 1.592l6.367-10.172 10.172 6.368a1.5 1.5 0 1 0 1.591-2.543zM48.628 93.412l-1.167.943zm77.38-4.319-.929-1.177zM78.86 97.731l-1.335-.684zM60.145 61.38l-.212-1.485zM2.354 134.081l-.603 1.374q1.41.618 2.804 1.156l.54-1.399.54-1.399a66 66 0 0 1-2.679-1.105zm8.355 2.993-.4 1.446q3.008.83 5.932 1.3l.239-1.481.238-1.481a52 52 0 0 1-5.609-1.229zm11.648 1.856-.059 1.499q3.105.12 6.096-.146l-.131-1.494-.132-1.494a45 45 0 0 1-5.715.136zm11.745-1.036.322 1.465a49 49 0 0 0 5.86-1.682l-.503-1.413-.503-1.413a46 46 0 0 1-5.498 1.578zm11.118-3.937.665 1.345a57 57 0 0 0 5.288-2.983l-.805-1.266-.805-1.266a53 53 0 0 1-5.007 2.825zm9.974-6.317.923 1.182a70 70 0 0 0 4.594-3.923l-1.022-1.098-1.021-1.099a67 67 0 0 1-4.397 3.756zm8.663-8.032 1.103 1.016a87 87 0 0 0 3.918-4.564l-1.17-.938-1.171-.938a83 83 0 0 1-3.783 4.407zm7.396-9.217 1.228.862a103 103 0 0 0 3.302-5.009l-1.276-.789-1.276-.789a100 100 0 0 1-3.205 4.863zm6.225-10.047 1.317.719a114 114 0 0 0 1.4-2.649l-1.335-.683-1.335-.684q-.663 1.297-1.363 2.578zm1.382-2.613 1.335.683a71 71 0 0 0 1.499-3.105l-1.367-.618-1.367-.617a68 68 0 0 1-1.435 2.973zm3.866-9.33 1.435.437c.745-2.445 1.213-4.729 1.43-6.857L84.1 81.83l-1.493-.153c-.195 1.912-.62 4.004-1.316 6.287zm1.12-13.269 1.47-.296c-.52-2.58-1.503-4.815-2.834-6.715l-1.229.86-1.228.86c1.09 1.557 1.91 3.406 2.35 5.588zm-7.48-10.707.788-1.276c-2.047-1.266-4.31-2.16-6.629-2.73l-.358 1.456-.36 1.456c2.058.507 4.024 1.29 5.77 2.37zm-12.87-3.302-.02-1.5a28 28 0 0 0-3.543.272l.212 1.485.212 1.485a25 25 0 0 1 3.158-.242zm-3.351.257-.212-1.485a21 21 0 0 0-3.582.827l.465 1.426.466 1.426a18 18 0 0 1 3.075-.71zm-9.246 4.086-.98-1.136c-1.905 1.644-3.412 3.625-4.533 5.795l1.332.688 1.333.689c.96-1.857 2.236-3.527 3.828-4.9zM44.646 77.29l-1.483-.224a24.1 24.1 0 0 0 .008 7.258l1.482-.228 1.483-.228a21.1 21.1 0 0 1-.007-6.353zm2.11 13.272-1.326.7a19 19 0 0 0 2.03 3.093l1.168-.943 1.167-.942a16 16 0 0 1-1.712-2.609zm1.872 2.85-1.167.943c.639.79 1.45 1.55 2.393 2.27l.91-1.191.911-1.192c-.802-.613-1.426-1.21-1.88-1.772zm7.254 4.998-.625 1.364a49 49 0 0 0 5.707 2.168l.449-1.432.449-1.43a46 46 0 0 1-5.355-2.033zM67.141 102l-.31 1.468c1.9.402 3.894.739 5.964 1l.188-1.488.187-1.488a70 70 0 0 1-5.72-.959zm11.746 1.49-.072 1.499c1.968.094 3.984.116 6.037.057l-.043-1.5-.043-1.499a76 76 0 0 1-5.808-.055zm11.83-.341.158 1.492a76 76 0 0 0 5.977-.875l-.276-1.474-.277-1.475a73 73 0 0 1-5.741.84zm11.628-2.184.397 1.446a71 71 0 0 0 5.759-1.843l-.519-1.408-.518-1.407a68 68 0 0 1-5.515 1.765zm11.097-4.092.64 1.357a67 67 0 0 0 5.354-2.829l-.76-1.293-.76-1.293a64 64 0 0 1-5.115 2.702zm10.198-5.996.875 1.219a66 66 0 0 0 2.423-1.826l-.93-1.177-.929-1.177a63 63 0 0 1-2.314 1.743zm2.368-1.784.93 1.177a37 37 0 0 0 2.294-1.967l-1.021-1.098-1.022-1.099a35 35 0 0 1-2.11 1.81zm6.125-6.146 1.176.93a44 44 0 0 0 3.385-4.947l-1.291-.763-1.292-.764a41 41 0 0 1-3.155 4.613zm5.915-9.934 1.371.61a61 61 0 0 0 2.137-5.542l-1.424-.473-1.423-.473a58 58 0 0 1-2.031 5.27zm3.68-10.98 1.457.355c.464-1.904.86-3.834 1.194-5.775l-1.479-.254-1.478-.255a83 83 0 0 1-1.152 5.573zm1.984-11.415 1.49.168c.22-1.955.385-3.91.505-5.852l-1.498-.092-1.497-.092c-.116 1.896-.278 3.8-.491 5.7zm.721-11.57 1.5.025c.034-1.98.025-3.935-.018-5.85l-1.499.034-1.5.033c.042 1.878.051 3.793.018 5.732zm-.252-11.593 1.497-.087c-.117-2.019-.267-3.97-.437-5.835l-1.494.136-1.494.136c.168 1.835.315 3.754.43 5.737zm-1.053-11.553 1.489-.184a187 187 0 0 0-.804-5.781l-1.482.23-1.482.23c.263 1.696.534 3.606.79 5.688zM141.347 4.47l1.474-.283c-.177-.92-.325-1.638-.429-2.128q-.078-.368-.121-.561l-.032-.146-.009-.038-.002-.01-.001-.004v-.001l-1.462.336-1.462.336v.002l.002.007.007.032.03.134q.04.18.116.535c.1.472.244 1.172.416 2.072z"></path>
              </svg>
            </div>
          </div>
        </div>
      </section>

      {/* SELECTED WORKS */}
      <section id="works" className="py-32 relative">
        <div className="max-w-7xl mx-auto px-6 mb-20 reveal-up active">
          <h2 className="text-4xl md:text-6xl font-bold">Selected Works</h2>
        </div>
        <div className="max-w-7xl mx-auto px-6 flex flex-col gap-12 pb-32">
          {projects.map((project: any, i: number) => (
            <div key={i} className="lg:sticky transition-transform duration-500 reveal-up active" style={{ top: `calc(10vh + ${i * 40}px)`, zIndex: i + 1, ...(project.card_color ? { '--color-accent': project.card_color } as React.CSSProperties : {}) }}>
              <div className="bg-white/10 dark:bg-black/60 backdrop-blur-2xl rounded-[2.5rem] md:rounded-[3.5rem] p-8 md:p-12 border border-white/40 dark:border-white/10 shadow-2xl hover:shadow-[var(--color-accent)]/20 hover:border-[var(--color-accent)] transition-all duration-500 flex flex-col lg:flex-row gap-10 md:gap-16">
                <div className="flex-1 flex flex-col justify-center order-2 lg:order-1">
                  <div className="mb-6">
                    <span className="text-[var(--color-accent)] font-bold tracking-widest uppercase text-sm mb-2 block">Project {project.number}</span>
                    <h3 className="text-4xl md:text-5xl font-extrabold tracking-tight mb-2">{project.title}</h3>
                    {project.subtitle && <p className="text-xl font-bold opacity-80">{project.subtitle}</p>}
                  </div>
                  <p className="text-base md:text-lg opacity-80 mb-8 leading-relaxed whitespace-pre-wrap">{project.description}</p>
                  
                  {project.technologies && project.technologies.length > 0 && (
                    <div className="flex flex-wrap gap-2 mb-10">
                      {project.technologies.map((tech: any, tIdx: number) => (
                        <span key={tIdx} className="px-4 py-1.5 rounded-full border border-black/10 dark:border-white/10 bg-black/5 dark:bg-white/5 font-bold text-xs md:text-sm shadow-sm backdrop-blur-md">
                          {tech.name}
                        </span>
                      ))}
                    </div>
                  )}
                  
                  <div className="flex flex-wrap gap-4 mt-auto">
                    {project.github_url && (
                      <a href={project.github_url} target="_blank" className="flex items-center gap-2 px-6 py-3 rounded-full border-2 border-black dark:border-white font-bold text-sm hover:bg-black hover:text-white dark:hover:bg-white dark:hover:text-black transition-colors">
                        <GithubLogo className="text-lg" />
                        Github
                      </a>
                    )}
                    {project.live_url && (
                      <a href={project.live_url} target="_blank" className="flex items-center gap-2 px-6 py-3 rounded-full bg-black text-white dark:bg-white dark:text-black font-bold text-sm hover:scale-105 transition-transform shadow-lg shadow-black/20 dark:shadow-white/20">
                        Live Demo
                        <ArrowUpRight className="text-lg" />
                      </a>
                    )}
                  </div>
                </div>
                
                <div className="flex-1 order-1 lg:order-2">
                  <div className="w-full rounded-2xl md:rounded-[2rem] overflow-hidden shadow-2xl relative border-2 border-white/20 dark:border-white/5 group aspect-[4/3] md:aspect-square lg:aspect-[4/3]">
                    {project.image ? (
                      <Image 
                        src={getMediaUrl(project.image)} 
                        alt={project.title}
                        fill
                        loading="lazy"
                        sizes="(max-width: 768px) 100vw, 50vw"
                        className="object-cover object-center transition-transform duration-700 group-hover:scale-105" 
                      />
                    ) : (
                      <div className="w-full h-full flex flex-col items-center justify-center p-8 text-center text-white bg-[#1a1a1a]">
                        <Layout className="text-6xl opacity-50 mb-4" />
                        <span className="font-display font-bold text-2xl tracking-widest uppercase opacity-80">{project.title}</span>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* EXPERIENCE SECTION */}
      <section id="experience" className="py-24 relative overflow-hidden">
        <div className="max-w-4xl mx-auto px-6">
          <div className="text-center mb-16 reveal-up active">
            <div className="inline-flex items-center gap-2 px-4 py-1.5 bg-[var(--color-accent)]/10 rounded-full mb-4">
              <Briefcase className="text-[var(--color-accent)] text-lg" />
              <span className="text-sm text-[var(--color-accent)] font-bold tracking-wide uppercase">Experience</span>
            </div>
            <h2 className="text-4xl md:text-5xl font-bold mb-4">Work Experience</h2>
          </div>
          
          <div className="space-y-6 ml-6 md:ml-8 border-l-2 border-gray-200 dark:border-gray-800 pl-8 md:pl-10">
            {experience.map((exp: any, i: number) => (
              <div key={i} className="relative mb-8 reveal-up active bg-white/10 dark:bg-black/60 backdrop-blur-2xl p-6 md:p-8 rounded-3xl border border-white/10 hover:border-[var(--color-accent)] transition-colors group">
                 <div className="absolute w-4 h-4 rounded-full border-4 border-white dark:border-[var(--color-surface)] bg-[var(--color-accent)] -left-[calc(2rem+9px)] md:-left-[calc(2.5rem+9px)] top-8 group-hover:scale-125 transition-transform duration-300 shadow-[0_0_15px_var(--color-accent)]"></div>
                 <div className="text-sm font-bold text-[var(--color-accent)] mb-2 tracking-wider uppercase">{exp.start_date} – {exp.end_date}</div>
                 <h3 className="text-2xl font-bold mb-1">{exp.role}</h3>
                 <p className="text-[var(--color-text-secondary)] font-semibold text-lg mb-4">{exp.company}</p>
                 <p className="text-[var(--color-text-secondary)] leading-relaxed mb-6 whitespace-pre-wrap">{exp.description}</p>
                 {exp.technologies && exp.technologies.length > 0 && (
                   <div className="flex flex-wrap gap-2 mb-6">
                     {exp.technologies.map((tech: string, tIdx: number) => (
                       <span key={tIdx} className="text-xs font-semibold px-3 py-1 rounded-full bg-black/5 dark:bg-white/10 text-gray-700 dark:text-gray-300 border border-gray-200 dark:border-gray-700">
                         {tech}
                       </span>
                     ))}
                   </div>
                 )}
                 {exp.bullets && exp.bullets.length > 0 && (
                   <ul className="space-y-2 mb-6">
                     {exp.bullets.map((b: string, idx: number) => (
                       <li key={idx} className="flex items-start gap-3">
                         <CheckCircle className="text-[var(--color-accent)] mt-1" weight="fill" />
                         <span className="text-[var(--color-text-secondary)]">{b}</span>
                       </li>
                     ))}
                   </ul>
                 )}
              </div>
            ))}
          </div>

          {internships.length > 0 && (
            <>
              <div className="text-center mt-16 mb-12 reveal-up active">
                  <h3 className="text-3xl font-bold mb-2">Internships</h3>
              </div>
              <div className="space-y-6 ml-6 md:ml-8 border-l-2 border-gray-200 dark:border-gray-800 pl-8 md:pl-10">
                {internships.map((exp: any, i: number) => (
                  <div key={i} className="relative mb-8 reveal-up active bg-white/10 dark:bg-black/60 backdrop-blur-2xl p-6 md:p-8 rounded-3xl border border-white/10 hover:border-[var(--color-accent)] transition-colors group">
                     <div className="absolute w-4 h-4 rounded-full border-4 border-white dark:border-[var(--color-surface)] bg-[var(--color-accent)] -left-[calc(2rem+9px)] md:-left-[calc(2.5rem+9px)] top-8 group-hover:scale-125 transition-transform duration-300 shadow-[0_0_15px_var(--color-accent)]"></div>
                     <div className="text-sm font-bold text-[var(--color-accent)] mb-2 tracking-wider uppercase">{exp.start_date} – {exp.end_date}</div>
                     <h3 className="text-2xl font-bold mb-1">{exp.role}</h3>
                     <p className="text-[var(--color-text-secondary)] font-semibold text-lg mb-4">{exp.company}</p>
                     <p className="text-[var(--color-text-secondary)] leading-relaxed mb-6 whitespace-pre-wrap">{exp.description}</p>
                     {exp.technologies && exp.technologies.length > 0 && (
                       <div className="flex flex-wrap gap-2 mb-6">
                         {exp.technologies.map((tech: string, tIdx: number) => (
                           <span key={tIdx} className="text-xs font-semibold px-3 py-1 rounded-full bg-black/5 dark:bg-white/10 text-gray-700 dark:text-gray-300 border border-gray-200 dark:border-gray-700">
                             {tech}
                           </span>
                         ))}
                       </div>
                     )}
                  </div>
                ))}
              </div>
            </>
          )}
        </div>
      </section>

      {/* MINI PROJECTS */}
      {miniProjects.length > 0 && (
        <section id="mini-projects" className="py-16 pb-32">
          <div className="max-w-7xl mx-auto px-6 mb-12 reveal-up active">
            <h2 className="text-3xl md:text-4xl font-bold flex items-center gap-4">
                Mini Projects <span className="text-gray-600 dark:text-gray-300 text-lg font-normal">/ experiments</span>
            </h2>
          </div>
          <div className="max-w-7xl mx-auto px-6">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {miniProjects.map((project: any, i: number) => (
                <div key={i} className="group bg-white/10 dark:bg-black/60 backdrop-blur-2xl rounded-3xl p-8 flex flex-col hover:-translate-y-2 transition-transform duration-300 reveal-up active border border-white/40 dark:border-white/10 hover:border-[var(--color-accent)] hover:shadow-2xl hover:shadow-[var(--color-accent)]/20" style={project.card_color ? { '--color-accent': project.card_color } as React.CSSProperties : {}}>
                  <div className="flex justify-between items-start mb-6">
                    <h3 className="text-2xl font-display font-bold">{project.title}</h3>
                    {project.live_url && (
                      <a href={project.live_url} className="flex items-center gap-2 text-sm font-semibold tracking-wider uppercase text-[var(--color-accent)] hover:text-black dark:hover:text-white transition-colors">
                        <span>Open</span>
                        <ArrowUpRight />
                      </a>
                    )}
                  </div>
                  <p className="text-[var(--color-text-secondary)] mb-6 line-clamp-3 flex-grow whitespace-pre-wrap">{project.description}</p>
                  <div className="flex flex-wrap gap-2 mb-6">
                    {project.technologies && project.technologies.map((tech: any, tIdx: number) => (
                      <span key={tIdx} className="text-xs font-semibold px-3 py-1 rounded-full bg-black/5 dark:bg-white/10 text-gray-700 dark:text-gray-300 border border-gray-200 dark:border-gray-700">
                        {tech.name}
                      </span>
                    ))}
                  </div>
                  {project.github_url && (
                    <div className="pt-4 border-t border-gray-100 dark:border-gray-800 mt-auto">
                      <a href={project.github_url} target="_blank" aria-label="GitHub Repository" className="text-gray-600 dark:text-gray-300 hover:text-black dark:hover:text-white transition-colors flex items-center gap-2 text-sm">
                        <GithubLogo className="text-xl" />
                        <span>Source Code</span>
                      </a>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* EDUCATION */}
      <section id="education" className="py-24 relative overflow-hidden">
        <div className="max-w-4xl mx-auto px-6">
          <div className="text-center mb-16 reveal-up active">
            <div className="inline-flex items-center gap-2 px-4 py-1.5 bg-[var(--color-accent)]/10 rounded-full mb-4">
              <GraduationCap className="text-[var(--color-accent)] text-lg" />
              <span className="text-sm text-[var(--color-accent)] font-bold tracking-wide uppercase">Education</span>
            </div>
            <h2 className="text-4xl md:text-5xl font-bold mb-4">Academic Background</h2>
          </div>
          <div className="space-y-6">
            {education.map((edu: any, i: number) => (
              <div key={i} className="reveal-up active p-6 md:p-8 bg-white/10 dark:bg-black/60 backdrop-blur-2xl rounded-2xl border border-white/20 dark:border-white/10 hover:border-[var(--color-accent)] transition-transform group">
                <div className="flex flex-col md:flex-row items-start gap-6">
                  <div className="p-4 bg-[var(--color-accent)]/10 rounded-xl shrink-0 group-hover:bg-[var(--color-accent)] group-hover:text-black dark:group-hover:text-white text-[var(--color-accent)] transition-colors">
                    <Bank className="text-3xl" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-2xl font-bold mb-1">{edu.degree}</h3>
                    <p className="text-[var(--color-accent)] font-bold text-lg mb-2">{edu.institution}</p>
                    <p className="text-gray-700 dark:text-gray-400 text-sm mb-4 font-mono">{edu.start_date} – {edu.end_date}</p>
                    {edu.grade && (
                      <div className="inline-flex items-center gap-2 px-4 py-2 bg-black/5 dark:bg-white/5 rounded-lg border border-black/10 dark:border-white/10 mb-4">
                        <Medal className="text-[var(--color-accent)]" weight="fill" />
                        <span className="text-sm text-[var(--color-text-secondary)]">{edu.grade_label}: <strong className="text-black dark:text-white">{edu.grade}</strong></span>
                      </div>
                    )}
                    {edu.description && <p className="text-[var(--color-text-secondary)] leading-relaxed whitespace-pre-wrap">{edu.description}</p>}
                  </div>
                </div>
              </div>
            ))}
          </div>
          
          {certifications.length > 0 && (
            <>
              <div className="text-center mt-16 mb-12 reveal-up active">
                  <h3 className="text-3xl font-bold mb-2">Certifications</h3>
              </div>
              <div className="space-y-6">
                {certifications.map((cert: any, i: number) => (
                  <div key={i} className="reveal-up active p-6 md:p-8 bg-white/10 dark:bg-black/60 backdrop-blur-2xl rounded-2xl border border-white/20 dark:border-white/10 hover:border-[var(--color-accent)] transition-transform group">
                    <div className="flex flex-col md:flex-row items-start gap-6">
                      <div className="p-4 bg-[var(--color-accent)]/10 rounded-xl shrink-0 group-hover:bg-[var(--color-accent)] group-hover:text-black dark:group-hover:text-white text-[var(--color-accent)] transition-colors">
                        <SealCheck className="text-3xl" />
                      </div>
                      <div className="flex-1">
                        <h3 className="text-2xl font-bold mb-1">{cert.title}</h3>
                        <p className="text-[var(--color-accent)] font-bold text-lg mb-2">{cert.issuer}</p>
                        <p className="text-gray-700 dark:text-gray-400 text-sm mb-4 font-mono">
                            Issued: {cert.issue_date}
                            {cert.expiry_date && ` – Expires: ${cert.expiry_date}`}
                        </p>
                        {cert.credential_id && <p className="text-sm text-[var(--color-text-secondary)] mb-4 font-mono opacity-80">Credential ID: {cert.credential_id}</p>}
                        <div className="flex flex-wrap items-center gap-4 mt-4">
                          {cert.credential_url && (
                            <a href={cert.credential_url} target="_blank" className="inline-flex w-fit whitespace-nowrap items-center justify-center gap-2 px-6 py-3 rounded-full bg-black text-white dark:bg-white dark:text-black font-bold text-sm hover:scale-105 transition-transform shadow-lg shadow-black/20 dark:shadow-white/20">
                              <span>Show Credential</span>
                              <ArrowUpRight weight="bold" />
                            </a>
                          )}
                          {cert.certificate_file && (
                            <a href={getMediaUrl(cert.certificate_file)} target="_blank" className="inline-flex w-fit whitespace-nowrap items-center justify-center gap-2 px-6 py-3 rounded-full bg-black text-white dark:bg-white dark:text-black font-bold text-sm hover:scale-105 transition-transform shadow-lg shadow-black/20 dark:shadow-white/20">
                              <ImageIcon className="text-lg" />
                              View Certificate
                            </a>
                          )}
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </>
          )}
        </div>
      </section>

      {/* CONTACT SECTION */}
      <section id="contact" className="py-32 md:py-48 relative overflow-hidden bg-white dark:bg-[#050505]">
        <div className="absolute inset-0 z-0 opacity-[0.03] dark:opacity-[0.02]" style={{ backgroundImage: 'radial-gradient(circle at center, black 1px, transparent 1px)', backgroundSize: '40px 40px' }}></div>
        <div className="max-w-7xl mx-auto px-6 text-center relative z-10 reveal-up active">
          <p className="text-sm md:text-base text-gray-700 dark:text-gray-400 mb-8 font-medium uppercase tracking-[0.3em]">Got a project in mind?</p>
          <h2 className="text-6xl md:text-[8rem] font-display font-black leading-none mb-16 tracking-tighter hover:text-[var(--color-accent)] transition-colors duration-500 cursor-default">
            Let's Talk.
          </h2>
          <div className="flex flex-col md:flex-row items-center justify-center gap-8 md:gap-16 max-w-4xl mx-auto border-t border-gray-200 dark:border-white/10 pt-16">
            {profile.email && (
              <a href={`https://mail.google.com/mail/?view=cm&fs=1&to=${profile.email}`} target="_blank" className="group relative flex flex-col items-center gap-2 hover:-translate-y-2 transition-transform duration-300">
                <div className="w-16 h-16 rounded-full bg-gray-100 dark:bg-white/5 flex items-center justify-center group-hover:bg-[var(--color-accent)] group-hover:text-black transition-colors duration-300 mb-2">
                  <EnvelopeSimple className="text-2xl" />
                </div>
                <span className="text-xl font-bold">Email Me</span>
                <span className="text-sm text-gray-700 dark:text-gray-400">{profile.email}</span>
              </a>
            )}
            {profile.linkedin_url && (
              <a href={profile.linkedin_url} target="_blank" className="group relative flex flex-col items-center gap-2 hover:-translate-y-2 transition-transform duration-300">
                <div className="w-16 h-16 rounded-full bg-gray-100 dark:bg-white/5 flex items-center justify-center group-hover:bg-[var(--color-accent)] group-hover:text-black transition-colors duration-300 mb-2">
                  <LinkedinLogo className="text-2xl" />
                </div>
                <span className="text-xl font-bold">LinkedIn</span>
                <span className="text-sm text-gray-700 dark:text-gray-400">Connect with me</span>
              </a>
            )}
            {profile.instagram_url && (
              <a href={profile.instagram_url} target="_blank" className="group relative flex flex-col items-center gap-2 hover:-translate-y-2 transition-transform duration-300">
                <div className="w-16 h-16 rounded-full bg-gray-100 dark:bg-white/5 flex items-center justify-center group-hover:bg-[var(--color-accent)] group-hover:text-black transition-colors duration-300 mb-2">
                  <InstagramLogo className="text-2xl" />
                </div>
                <span className="text-xl font-bold">Instagram</span>
                <span className="text-sm text-gray-700 dark:text-gray-400">Follow me</span>
              </a>
            )}
            {profile.github_url && (
              <a href={profile.github_url} target="_blank" className="group relative flex flex-col items-center gap-2 hover:-translate-y-2 transition-transform duration-300">
                <div className="w-16 h-16 rounded-full bg-gray-100 dark:bg-white/5 flex items-center justify-center group-hover:bg-[var(--color-accent)] group-hover:text-black transition-colors duration-300 mb-2">
                  <GithubLogo className="text-2xl" />
                </div>
                <span className="text-xl font-bold">GitHub</span>
                <span className="text-sm text-gray-700 dark:text-gray-400">View my code</span>
              </a>
            )}
          </div>
        </div>
      </section>
    </main>
  );
}
