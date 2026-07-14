import { defineType, defineField } from 'sanity';

export const skillType = defineType({
  name: 'skill',
  title: 'Skill',
  type: 'document',
  fields: [
    defineField({ name: 'order', title: 'Order', type: 'number' }),
    defineField({ name: 'name', title: 'Name', type: 'string' }),
    defineField({ name: 'category', title: 'Category', type: 'string', options: { list: ['frontend', 'backend', 'tools', 'language', 'other'] } }),
    defineField({ name: 'icon', title: 'Icon (Phosphor Icon Name)', type: 'string' }),
    defineField({ name: 'proficiency', title: 'Proficiency (%)', type: 'number' }),
  ],
});
