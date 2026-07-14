import { defineType, defineField } from 'sanity';

export const experienceType = defineType({
  name: 'experience',
  title: 'Experience',
  type: 'document',
  fields: [
    defineField({ name: 'order', title: 'Order', type: 'number' }),
    defineField({ name: 'company', title: 'Company', type: 'string' }),
    defineField({ name: 'company_url', title: 'Company URL', type: 'url' }),
    defineField({ name: 'role', title: 'Role', type: 'string' }),
    defineField({ name: 'location', title: 'Location', type: 'string' }),
    defineField({ name: 'start_date', title: 'Start Date', type: 'string' }),
    defineField({ name: 'end_date', title: 'End Date', type: 'string' }),
    defineField({ name: 'description', title: 'Description', type: 'text' }),
    defineField({ name: 'technologies', title: 'Technologies', type: 'string' }),
    defineField({ name: 'bullets', title: 'Bullets', type: 'array', of: [{ type: 'string' }] }),
    defineField({ name: 'is_current', title: 'Is Current', type: 'boolean' }),
    defineField({ name: 'is_internship', title: 'Is Internship', type: 'boolean' }),
    defineField({ name: 'certificate_file', title: 'Certificate File', type: 'file' }),
    defineField({ name: 'company_logo', title: 'Company Logo', type: 'image' }),
  ],
});
