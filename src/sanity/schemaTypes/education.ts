import { defineType, defineField } from 'sanity';

export const educationType = defineType({
  name: 'education',
  title: 'Education',
  type: 'document',
  fields: [
    defineField({ name: 'order', title: 'Order', type: 'number' }),
    defineField({ name: 'institution', title: 'Institution', type: 'string' }),
    defineField({ name: 'degree', title: 'Degree', type: 'string' }),
    defineField({ name: 'field_of_study', title: 'Field of Study', type: 'string' }),
    defineField({ name: 'start_date', title: 'Start Date', type: 'string' }),
    defineField({ name: 'end_date', title: 'End Date', type: 'string' }),
    defineField({ name: 'grade', title: 'Grade', type: 'string' }),
    defineField({ name: 'grade_label', title: 'Grade Label', type: 'string' }),
    defineField({ name: 'honours', title: 'Honours', type: 'string' }),
    defineField({ name: 'description', title: 'Description', type: 'text' }),
    defineField({ name: 'is_current', title: 'Is Current', type: 'boolean' }),
    defineField({ name: 'certificate_file', title: 'Certificate File', type: 'file' }),
  ],
});
