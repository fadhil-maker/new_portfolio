import { defineType, defineField } from 'sanity';

export const certificationType = defineType({
  name: 'certification',
  title: 'Certification',
  type: 'document',
  fields: [
    defineField({ name: 'order', title: 'Order', type: 'number' }),
    defineField({ name: 'name', title: 'Name', type: 'string' }),
    defineField({ name: 'issuer', title: 'Issuer', type: 'string' }),
    defineField({ name: 'issue_date', title: 'Issue Date', type: 'string' }),
    defineField({ name: 'credential_url', title: 'Credential URL', type: 'url' }),
    defineField({ name: 'certificate_file', title: 'Certificate File', type: 'file' }),
  ],
});
