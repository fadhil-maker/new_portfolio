import { defineType, defineField } from 'sanity';

export const profileType = defineType({
  name: 'profile',
  title: 'Profile',
  type: 'document',
  fields: [
    defineField({ name: 'order', title: 'Order', type: 'number' }),
    defineField({ name: 'full_name', title: 'Full Name', type: 'string' }),
    defineField({ name: 'title', title: 'Title', type: 'string' }),
    defineField({ name: 'subtitle', title: 'Subtitle', type: 'string' }),
    defineField({ name: 'tagline', title: 'Tagline', type: 'text' }),
    defineField({ name: 'bio', title: 'Bio', type: 'text' }),
    defineField({ name: 'email', title: 'Email', type: 'string' }),
    defineField({ name: 'phone', title: 'Phone', type: 'string' }),
    defineField({ name: 'location', title: 'Location', type: 'string' }),
    defineField({ name: 'github_url', title: 'GitHub URL', type: 'url' }),
    defineField({ name: 'linkedin_url', title: 'LinkedIn URL', type: 'url' }),
    defineField({ name: 'instagram_url', title: 'Instagram URL', type: 'url' }),
    defineField({ name: 'portfolio_url', title: 'Portfolio URL', type: 'url' }),
    defineField({ name: 'profile_image', title: 'Profile Image', type: 'image' }),
    defineField({ name: 'image_blend_amount', title: 'Image Blend Amount', type: 'number' }),
    defineField({ name: 'resume_file', title: 'Resume File', type: 'file' }),
  ],
});
