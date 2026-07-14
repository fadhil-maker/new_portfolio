import { client } from '@/sanity/lib/client';
import { groq } from 'next-sanity';

export async function getPortfolioData() {
  const query = groq`{
    "profile": *[_type == "profile"][0] {
      ...,
      "profile_image": profile_image.asset->url,
      "resume_file": resume_file.asset->url
    },
    "projects": *[_type == "project" && is_featured == true] | order(order asc) {
      ...,
      "image": image.asset->url
    },
    "miniProjects": *[_type == "project" && is_featured != true] | order(order asc) {
      ...,
      "image": image.asset->url
    },
    "skills": *[_type == "skill"] | order(order asc),
    "education": *[_type == "education"] | order(order asc),
    "experience": *[_type == "experience" && is_internship != true] | order(order asc) {
      ...,
      "technologies": technologies
    },
    "internships": *[_type == "experience" && is_internship == true] | order(order asc) {
      ...,
      "technologies": technologies
    },
    "certifications": *[_type == "certification"] | order(order asc) {
      ...,
      "certificate_file": certificate_file.asset->url
    }
  }`;

  const data = await client.fetch(query, {}, { next: { revalidate: 60 } });
  return data;
}
