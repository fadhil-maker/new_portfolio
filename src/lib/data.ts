import fs from 'fs';
import path from 'path';

export function getPortfolioData() {
  const filePath = path.join(process.cwd(), 'data.json');
  let fileContents = fs.readFileSync(filePath, 'utf8');
  if (fileContents.charCodeAt(0) === 0xFEFF) {
    fileContents = fileContents.slice(1);
  }
  const data = JSON.parse(fileContents);

  const profile = data.find((item: any) => item.model === 'core.profile')?.fields || {};
  
  const sortItems = (items: any[]) => items.sort((a: any, b: any) => (a.fields.order || 0) - (b.fields.order || 0));
  
  const projects = sortItems(data.filter((item: any) => item.model === 'core.project' && item.fields.is_featured)).map((i: any) => i.fields);
  const miniProjects = sortItems(data.filter((item: any) => item.model === 'core.project' && !item.fields.is_featured)).map((i: any) => i.fields);
  const skills = sortItems(data.filter((item: any) => item.model === 'core.skill')).map((i: any) => i.fields);
  const education = sortItems(data.filter((item: any) => item.model === 'core.education')).map((i: any) => i.fields);
  const experience = sortItems(data.filter((item: any) => item.model === 'core.experience' && !item.fields.is_internship)).map((i: any) => i.fields);
  const internships = sortItems(data.filter((item: any) => item.model === 'core.experience' && item.fields.is_internship)).map((i: any) => i.fields);
  const certifications = sortItems(data.filter((item: any) => item.model === 'core.certification')).map((i: any) => i.fields);

  return { profile, projects, miniProjects, skills, education, experience, internships, certifications };
}
