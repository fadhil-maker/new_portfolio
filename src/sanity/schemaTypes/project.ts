import { defineType, defineField } from 'sanity';

export const projectType = defineType({
  name: 'project',
  title: 'Project',
  type: 'document',
  fields: [
    defineField({ name: 'order', title: 'Order', type: 'number' }),
    defineField({ name: 'title', title: 'Title', type: 'string' }),
    defineField({ name: 'slug', title: 'Slug', type: 'string' }),
    defineField({ name: 'description', title: 'Description', type: 'text' }),
    defineField({ name: 'image', title: 'Image', type: 'image' }),
    defineField({ name: 'thumbnail', title: 'Thumbnail', type: 'image' }),
    defineField({ name: 'project_url', title: 'Project URL', type: 'url' }),
    defineField({ name: 'github_url', title: 'GitHub URL', type: 'url' }),
    defineField({ name: 'technologies', title: 'Technologies', type: 'string' }),
    defineField({ name: 'is_featured', title: 'Is Featured', type: 'boolean' }),
    defineField({ name: 'content', title: 'Content', type: 'text' }),
  ],
});
